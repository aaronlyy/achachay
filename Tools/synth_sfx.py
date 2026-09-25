import math, random, struct, wave, os, sys

SR = 44100
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
random.seed(7)


def n(sec):
    return int(sec * SR)


def noise(sec):
    return [random.uniform(-1, 1) for _ in range(n(sec))]


def lowpass(x, cutoff):
    # cutoff may be a float or a function of t (seconds)
    y, prev = [], 0.0
    for i, s in enumerate(x):
        c = cutoff(i / SR) if callable(cutoff) else cutoff
        a = 1 - math.exp(-2 * math.pi * c / SR)
        prev += a * (s - prev)
        y.append(prev)
    return y


def highpass(x, cutoff):
    lp = lowpass(x, cutoff)
    return [a - b for a, b in zip(x, lp)]


def env(x, attack, decay_tau):
    return [s * min(1.0, (i / SR) / attack if attack > 0 else 1.0) * math.exp(-(i / SR) / decay_tau)
            for i, s in enumerate(x)]


def tone(sec, f0, f1=None, shape="sine"):
    f1 = f0 if f1 is None else f1
    out, ph = [], 0.0
    total = n(sec)
    for i in range(total):
        f = f0 * (f1 / f0) ** (i / total)
        ph += 2 * math.pi * f / SR
        if shape == "sine":
            out.append(math.sin(ph))
        elif shape == "square":
            out.append(1.0 if math.sin(ph) >= 0 else -1.0)
        elif shape == "saw":
            out.append(((ph / (2 * math.pi)) % 1.0) * 2 - 1)
    return out


def mix(*parts):
    L = max(n(offset) + len(p) for p, _, offset in parts)
    out = [0.0] * L
    for p, gain, offset in parts:
        o = n(offset)
        for i, s in enumerate(p):
            out[o + i] += s * gain
    return out


def echo(x, delay, fb, taps=4):
    d = n(delay)
    out = x + [0.0] * d * taps
    for k in range(1, taps + 1):
        g = fb ** k
        for i, s in enumerate(x):
            out[i + d * k] += s * g
    return out


def fade_out(x, sec):
    f = n(sec)
    L = len(x)
    return [s * (min(1.0, (L - i) / f)) for i, s in enumerate(x)]


def write(name, x, peak=0.89):
    x = fade_out(x, 0.01)
    m = max(abs(s) for s in x) or 1
    x = [s / m * peak for s in x]
    with wave.open(os.path.join(OUT, name + ".wav"), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(b"".join(struct.pack("<h", int(s * 32767)) for s in x))
    print(name, round(len(x) / SR, 2), "s")


# Schuss leicht: knackiger Rauschimpuls + kurzer Tiefton
write("SFX_Shot_Light", mix(
    (env(lowpass(noise(0.18), lambda t: 6000 * math.exp(-t * 25) + 400), 0.001, 0.035), 1.0, 0),
    (env(tone(0.12, 180, 70), 0.001, 0.03), 0.8, 0),
    (env(highpass(noise(0.01), 3000), 0.0005, 0.003), 0.5, 0),
))

# Schuss schwer: längerer, tieferer Knall mit Nachhall
write("SFX_Shot_Heavy", echo(mix(
    (env(lowpass(noise(0.5), lambda t: 3500 * math.exp(-t * 10) + 200), 0.001, 0.09), 1.0, 0),
    (env(tone(0.4, 110, 40), 0.001, 0.09), 1.0, 0),
    (env(highpass(noise(0.015), 2500), 0.0005, 0.004), 0.6, 0),
), 0.09, 0.25, 3))

# Treffer: kurzer, trockener Klick mit Ton
write("SFX_Hit", mix(
    (env(highpass(noise(0.06), 1500), 0.0005, 0.012), 0.8, 0),
    (env(tone(0.07, 900, 500), 0.0005, 0.018), 0.7, 0),
))

# Gegnertod: fallender Rechteckton + Rauschen
write("SFX_EnemyDeath", mix(
    (env(lowpass(tone(0.3, 420, 70, "square"), 2500), 0.002, 0.1), 0.6, 0),
    (env(lowpass(noise(0.3), 1800), 0.001, 0.07), 0.8, 0),
))

# Spieler getroffen: dumpfer Schlag
write("SFX_PlayerHurt", mix(
    (env(lowpass(tone(0.22, 200, 110, "saw"), 900), 0.003, 0.07), 0.9, 0),
    (env(lowpass(noise(0.2), 1200), 0.001, 0.04), 0.6, 0),
))

# Tür: Riegelklick, dann dumpfer Schlag
write("SFX_Door", mix(
    (env(highpass(noise(0.03), 2500), 0.0005, 0.006), 0.7, 0),
    (env(tone(0.03, 1400), 0.0005, 0.006), 0.4, 0),
    (env(lowpass(noise(0.4), 350), 0.004, 0.09), 1.0, 0.12),
    (env(tone(0.4, 75, 55), 0.004, 0.1), 0.8, 0.12),
))

# Kauf: Münzen-Ding in zwei Tönen
write("SFX_Buy", mix(
    (env(mix((tone(0.5, 988), 1, 0), (tone(0.5, 1976), 0.3, 0)), 0.002, 0.12), 0.8, 0),
    (env(mix((tone(0.7, 1319), 1, 0), (tone(0.7, 2638), 0.3, 0)), 0.002, 0.2), 0.9, 0.08),
))

# Abgelehnt: zwei tiefe Brummer
write("SFX_Denied", mix(
    (env(lowpass(tone(0.12, 140, 140, "square"), 1500), 0.002, 0.08), 0.8, 0),
    (env(lowpass(tone(0.16, 110, 110, "square"), 1500), 0.002, 0.1), 0.8, 0.14),
))

# Nachladen: Magazin raus, Magazin rein
write("SFX_Reload", mix(
    (env(highpass(noise(0.05), 1800), 0.0005, 0.01), 0.7, 0),
    (env(tone(0.04, 700), 0.0005, 0.01), 0.4, 0),
    (env(highpass(noise(0.07), 1200), 0.0005, 0.015), 1.0, 0.3),
    (env(tone(0.06, 520, 380), 0.0005, 0.02), 0.6, 0.3),
))

# Wellenstart: tiefe Trommel mit Hall, darunter ein Horn-artiger Ton
write("SFX_WaveStart", echo(mix(
    (env(tone(0.8, 90, 45), 0.002, 0.25), 1.0, 0),
    (env(lowpass(noise(0.5), 500), 0.002, 0.08), 0.7, 0),
    (env(lowpass(tone(1.2, 110, 110, "saw"), 600), 0.15, 0.5), 0.35, 0.05),
), 0.18, 0.35, 4))

# Explosion: langes, tiefes Rauschen und Grollen
write("SFX_Explosion", mix(
    (env(lowpass(noise(1.4), lambda t: 2500 * math.exp(-t * 4) + 120), 0.002, 0.35), 1.0, 0),
    (env(tone(1.2, 60, 30), 0.002, 0.3), 0.9, 0),
    (env(highpass(noise(0.03), 2000), 0.0005, 0.008), 0.5, 0),
))

# Tod: schwerer, dunkler Schlag mit langem Ausklang
write("SFX_Death", echo(mix(
    (env(tone(3.0, 55), 0.005, 0.9), 1.0, 0),
    (env(tone(3.0, 55.7), 0.005, 0.9), 0.8, 0),
    (env(tone(3.0, 82.4), 0.01, 0.7), 0.4, 0),
    (env(lowpass(noise(1.0), 300), 0.002, 0.15), 0.8, 0),
), 0.25, 0.3, 4))
