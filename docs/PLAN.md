# Achachay — Produktionsplan

**Vertical Slice · Abgabe 25.09.2026 · UE 5.8 · Blueprint-only**

Top-Down-Wave-Shooter mit Extraktions-Loop und permanenter Progression. Du überlebst draußen so
lange du kannst, nimmst das Geld mit rein, kaufst dich stärker, gehst wieder raus. Die Wellen
starten bei jedem Rausgehen wieder bei 1 — weiter kommst du nur, weil *du* stärker geworden bist.

Du hast dabei genau eine Waffe. Sie frisst jedes Kaliber, das es gibt. **Munition ist unbegrenzt** —
was Geld kostet, ist das *Freischalten* eines Kalibers, und zwar einmalig. Danach gehört es dir.
Die Kostenseite eines starken Kalibers ist nicht sein Preis, sondern sein Magazin: .50 BMG hat drei
Schuss und lädt drei Sekunden nach.

---

## Der Loop

```
                      ┌──────────── AUSRÜSTEN ────────────┐
                      │                                   ▼
  MENÜ ──einmalig──▶ SAFEHOUSE                        OUTSIDE
  Gegner im Hinter-   Kaliber · Werkbank ·            Welle 1 → Boss
  grund               Verbrauchsgüter                     │
                      ▲                                   │
                      └──── RÜCKWEG IN 15 S · GELD ───────┘
```

Das Menü ist ein einmaliger Einstieg. Der eigentliche Kreis läuft zwischen Safehouse und Outside —
und die einzige interessante Entscheidung im Spiel ist, wann du ihn schließt.

---

## Takt eines Runs

| | |
|---|---|
| **15 s** | Zeit, das Safehouse zu erreichen |
| **~90 m** | Extraktionsreichweite bei 600 uu/s |
| **10** | Wellen bis zum Boss |
| **4–5** | Runs, bis Welle 10 fällt |

Wenn der letzte Gegner einer Welle fällt, hast du 15 Sekunden, um es zurück ins Safehouse zu
schaffen. Schaffst du es nicht, beginnt die nächste Welle — die Entscheidung fällt also nicht per
Knopfdruck, sondern mit den Füßen.

Es gibt **keinen Timer und keine Obergrenze**: Eine Welle ist zu Ende, wenn der letzte Gegner
stirbt — sonst nie. Damit ist die Länge eines Runs nichts Festgelegtes, sondern ein Ergebnis. Je
stärker du bist, desto schneller ist eine Welle vorbei, und dein Fortschritt steht direkt auf der
Uhr. Genau deshalb darf keine Welle über einen Timer enden: dann wäre die Uhr immer gleich, egal
wie stark du bist, und das Upgrade fühlte sich nach nichts an.

Die neun Rückweg-Fenster eines vollen Runs summieren sich auf über zwei Minuten Stehzeit, wenn du
sie jedes Mal aussitzt — deshalb sollte man sie vorzeitig schließen können.

**Drei Folgen ergeben sich daraus von allein:**

- Deine **Position** auf der Karte wird Teil der Entscheidung — wer am hinteren Ende kämpft, kommt
  gar nicht mehr raus.
- Das **Speed-Upgrade** verlängert nicht nur die Beweglichkeit im Kampf, sondern buchstäblich die
  Extraktionsreichweite.
- Spieler werden von selbst darauf kommen, den letzten Gegner einer Welle in Türnähe zu locken,
  bevor sie ihn erledigen.

Damit wird die Größe des Outside-Areals zum Balancing-Parameter, gemessen in Sekunden statt Metern:
Bei rund 600 uu/s sind 15 Sekunden etwa **90 Meter** Luftlinie. Die entfernteste Kampfzone sollte
spürbar darunter liegen.

---

## Loadout

Keine Slots, kein Inventar. Du hast **eine Waffe**, und ein Knopf wechselt durch die Kaliber, die du
freigeschaltet hast. Heilung und Granate liegen auf zwei eigenen Tasten.

**Munition ist unbegrenzt.** Ein Kaliber schaltest du einmal frei, danach kannst du es immer
benutzen. 6mm ist von Anfang an da und kostet nichts.

Was die Kaliber unterscheidet, ist nicht der Preis pro Schuss, sondern der **Takt**: Magazingröße,
Feuerrate und Nachladezeit. 6mm hält vierzig Schuss und lädt in gut einer Sekunde; .50 BMG hält drei
und braucht über drei Sekunden. Das starke Kaliber zwingt dich damit zum Zielen, ohne dass eine
Währung im Weg steht.

Zwei Regeln, die den Wechsel angenehm machen:

- Der Wechsel geht nur durch **freigeschaltete** Kaliber. Am Anfang ist der Kreis genau ein Eintrag
  lang und wächst mit jedem Kauf.
- Das HUD zeigt **alle freigeschalteten Kaliber**, das aktive ist hervorgehoben.

Belegung: **Q** an Tastatur/Maus, **rechte Schultertaste** am Gamepad. Beides ist ein einzelner
Tastendruck, der einen Schritt weiterschaltet — bewusst identisch auf beiden Geräten. (Geändert am
15.09.; vorher war Mausrad vorgesehen. Das Mausrad ist eine Achse, `IA_SwitchCaliber` aber eine
Boolean-Action — die Belegung war ohnehin ein Mismatch.)

### Stationen im Safehouse

- **Waffenbank** — eine Station pro Kaliber. Hingehen, interagieren, **einmalig freischalten**.
  Danach ist die Station erledigt. Kein Shop-Bildschirm: Wer bezahlen kann, kauft.
- **Werkbank** — die drei permanenten Upgrades: Speed, Armor, Health.
- **Vorratsregal** — Heilung und Granaten, einzeln gekauft.

### Preise (Startvorschlag)

Bei etwa 1 Dollar pro Kill und 150–250 Dollar aus einem gut gelaufenen Run. Alle Kaliberpreise sind
**einmalig**.

| Kaliber | Preis | Magazin | Reload | Charakter |
|---|---|---|---|---|
| 6mm | **frei** | 40 | 1,2 s | Dauerfeuer, kaum Schaden — der Boden |
| 9mm | 60 | 30 | 1,4 s | Arbeitspferd |
| .45 ACP | 120 | 20 | 1,6 s | Langsamer, härter |
| 7.62×39 (AK) | 200 | 30 | 2,0 s | Dauerfeuer mit Wumms |
| .44 Magnum | 300 | 6 | 2,4 s | Wenige Schuss, hoher Einzelschaden |
| .50 BMG | 500 | 3 | 3,2 s | Durchschlägt eine Reihe |
| Heilung | 60 | | | pro Stück |
| Granate | 80 | | | pro Stück |

.50 BMG kostet mehrere gute Runs. Du musst dich bewusst dafür entscheiden und einmal auf alles
andere verzichten — aber wenn du es hast, hast du es für immer.

**Freischaltungen und Upgrades bleiben beim Tod erhalten.** Verloren gehen nur das Run-Geld und die
Verbrauchsgüter.

> In der Top-Down-Ansicht siehst du die Patrone nie. Was der Spieler im Kampf unterscheidet, ist das
> **Projektil**: Tracer-Größe, Farbe, Einschlag. Dort gehört das visuelle Budget hin.

## Festgelegt

| | |
|---|---|
| **Waffe** | Genau eine, für immer. Sie verschießt jedes Kaliber. |
| **Kaliberwechsel** | Ein Knopf wechselt durch die freigeschalteten Kaliber. Keine Slots. |
| **Munition** | **Unbegrenzt.** Ein Kaliber wird einmalig freigeschaltet, danach dauerhaft nutzbar. 6mm ist von Anfang an da. |
| **Magazin** | Magazin und Nachladen sind der alleinige Taktgeber und die eigentliche Kostenseite eines starken Kalibers. |
| **Upgrades** | Genau drei: Speed, Armor, Health. Dauerhaft. |
| **Stamina** | Dashes kosten Stamina, die sich nachlädt. Ersetzt den festen Cooldown. |
| **Verbrauchsgüter** | Heilung und Granate, einzeln gekauft. Bei Benutzung weg — und beim Tod ebenfalls. |
| **Geld** | Kauft genau vier Dinge: Kaliber-Freischaltungen, Granaten, Heilung und die drei Upgrades. Sonst nichts. |
| **Tod** | Run-Geld und Verbrauchsgüter sind weg. Freischaltungen und Upgrades bleiben. |
| **Extraktion** | Nach jeder Welle 15 Sekunden zurück ins Safehouse. |
| **Wellenende** | Wenn der letzte Gegner stirbt. Kein Timer, keine Obergrenze. |
| **Wellentakt** | Nach oben wachsen Menge und Härte der Gegner. |
| **Boss** | Am Ende der zehnten Welle. Erstmal schlicht: sehr viel HP. |
| **Eingabe** | Maus/Tastatur **und** Gamepad, beide vollwertig. |
| **Character-Anpassung** | Raus. |
| **Netzwerk** | Keine Replikation. |
| **Level** | Handgebaut, keine prozedurale Generierung. |

### Bleibt zum Austesten

**Trägt das Magazin als alleinige Kostenseite?** Ohne Munitionspreis muss der Takt die Arbeit machen:
Drei Schuss und 3,2 Sekunden Reload müssen sich teurer anfühlen als vierzig Schuss 6mm. Prüfstein:
Wenn .50 BMG nach der Freischaltung einfach immer die beste Wahl ist, sind Magazin und Reloadzeit zu
milde — dann müssen die Zahlen härter, nicht ein Preis zurück ins Spiel.

**Bleibt nach den Freischaltungen genug zu kaufen?** Einmalige Preise heißen: Irgendwann ist alles
freigeschaltet und Geld verliert seinen Zweck. Upgrades und Verbrauchsgüter müssen die Senke danach
tragen. Prüfstein: Wenn nach vier Runs alles gekauft ist und Geld sich sinnlos anfühlt, brauchen die
Upgrade-Stufen mehr Tiefe.

## Umpriorisiert am 15.09.

Die Munitionsökonomie hat zwei Tage gefressen, während **Gegner, Map und HUD noch gar nicht
existieren** — der Vertical Slice hängt an denen, nicht an der Wirtschaft. Deshalb:

- **Munition ist unbegrenzt**, Kaliber werden einmalig freigeschaltet. Das nimmt Vorrat, Packungen,
  Preis-pro-Schuss und den Rückfall auf 6mm komplett aus dem Weg.
- Geld kauft nur noch **vier Dinge**: Kaliber-Freischaltungen, Granaten, Heilung, und die drei
  Upgrades (Speed, Armor, Health).
- Als Nächstes stehen **19–22** an: Health-Komponente, Schaden am Ziel, `BP_EnemyBase`, `L_Outside`
  als Graybox. Erst danach wieder Safehouse-Stationen.

**Graphen aufgeräumt (15.09.).** `Fire` ist jetzt neun Zeilen und ruft `CanFire`, `GetMagazineRounds`
und `SpawnShot` auf, statt alles selbst zu tun.

Dabei kam heraus, warum die Graphen so unlesbar geworden waren: `write_graph_dsl` **ersetzt einen
Graphen nicht**, es verdrahtet nur die neue Kette und lässt die alten Nodes als Leichen liegen.
`Fire` hatte nach mehreren Umschreibungen über **200 Nodes** bei neun Zeilen sichtbarer Logik,
darunter fünf `SpawnActorFromClass` und mehrere For-Loop-Macros aus alten Fassungen. Der Read-back
zeigt nur die erreichbare Kette, deshalb fiel es lange nicht auf.

**Konsequenz für die Zukunft:** Eine Funktion nicht wiederholt überschreiben, sondern bei
grundlegenden Änderungen löschen, neu anlegen und einmal schreiben. Nach dem Löschen muss einmal
kompiliert werden, sonst bleibt der Name reserviert und Unreal hängt ein `_0` an.

**Zweite DSL-Falle: `(return (impure-call))` führt den Aufruf nicht aus.** `BP_Weapon.GetMagazineRounds`
gab immer 0 zurück. Der Return-Node bekam seinen Exec-Eingang direkt vom Function Entry, während der
Aufruf von `GI.GetMagazineRounds` nur mit seinem *Datenpin* am Return hing. Eine impure Funktion, die
nie ausgeführt wird, liefert ihren Defaultwert — also 0.

Symptome: Die Waffe schoss nicht und lud sofort nach, obwohl das Magazin laut HUD voll war. Ein
Fehler, zwei Symptome — `Fire` und `StartReload` lasen beide über dieselbe kaputte Funktion.

**Regel:** Einen impure-Aufruf (alles mit Exec-Pins, also auch jede eigene Blueprint-Funktion mit
Rückgabewert) immer erst mit `(bind x ...)` als Anweisung setzen und dann `(return x)`. Nie direkt in
`(return ...)` oder in eine `if`-Bedingung schachteln. Pure Ausdrücke (Map-Lookup, Array-Contains,
Variablen-Getter, Mathe) sind davon nicht betroffen.

**Gegengeprüft:** `CanFire`, `GI.IsCaliberUnlocked`, `GI.GetMagazineRounds` und `GetCaliberById` geben
nur pure Ausdrücke zurück; `InitWeapon` hängt korrekt am Aufruf. Es war die einzige Stelle.

## Bestand (Stand 15.09.2026)

| Asset | Zustand | Anmerkung |
|---|---|---|
| `BP_PlayerCharacter` | **Läuft** | Bewegung, Zielen mit Maus und Gamepad, Geräteerkennung, Dash mit Stamina, Interaktion, Stats aus der GI |
| ↳ Funktionen | | `GetAimLocation`, `ApplyAimRotation`, `UpdateActiveInputDevice`, `UpdateGamepadAim`, `UpdateMouseDelta`, `MarkAimInput`, `RegenerateStamina`, `SpendDashStamina`, `StartDash`, `StoreEssentialVariables`, `UpdateFocus`, `TryInteract`, `ApplyPlayerStats` |
| `GI_Achachay` | **Steht** | Geld (`Money`/`RunMoney`), Upgrade-Level, `CurrentCaliberId`, `MagazineAmmo` (Map String→Int), Verbrauchsgüter, `GetPlayerStats`, Geräteerkennung. `UnlockedCalibers` kommt beim Umbau dazu. EventGraph leer. |
| `E_InputDevice` | Vorhanden | `KeyboardMouse`, `Gamepad` |
| `IMC_Gameplay` | Vorhanden | 9 Mappings: Move (WASD + Stick), Dash (Space, Schulter, Stick-Klick), Aim (rechter Stick) |
| Input Actions | **Vollständig** | `IA_Move`, `IA_Dash`, `IA_Aim`, `IA_Fire`, `IA_Reload`, `IA_Interact`, `IA_SwitchCaliber`, `IA_UseHeal`, `IA_UseGrenade`. `Pressed`-Trigger fehlen noch. |
| `L_Menu` / `L_Outside` / `L_Safehouse` | Rohbau | Licht, Himmel, Boden, PlayerStart. Keine Geometrie, kein NavMesh. |
| `GM_*` | Verdrahtet | Pawn- und Controller-Klassen korrekt, Graphs leer |
| `BP_RecordPlayer` | Fertig | Zufallstrack; Instanz in L_Menu hat nur `loop_menu1` |
| Musik (7 Loops) | 6 ungenutzt | |
| Data Assets | **Steht** | `CaliberData`, dazu alle sechs Kaliber von 6mm bis .50 BMG. `ProjectileSpeed` und `ProjectileSize` am 14.09. ergänzt (Startwerte, ungetunt); `ProjectileColor` ist gefüllt, wird aber erst ab Schritt 39 benutzt. `PackPrice`/`RoundsPerPack` werden durch **`UnlockPrice`** ersetzt, `Unlimited` entfällt. |
| `BPI_Interactable` + `BP_TestInteractable` | Fertig | Fokus über `UpdateFocus`, Auslösen über `IA_Interact` |
| `ItemData`, `UpgradeData`, `WaveData` | Nichts | Gerüste aus Schritt 13 noch offen |
| Widgets | Nichts | |
| `BP_Weapon` | **Läuft** | `ActiveCaliber`, `Fire(AimDir)` mit Feuerratensperre, Streuung und `ProjectilesPerShot`. Wird vom Character gespawnt und angehängt (`EquipWeapon`). Seit 15.09. Magazin und Nachladen: `MagazineAmmo` (Map CaliberId→Schuss), `IsReloading`, `AllCalibers`, `GI`; `InitWeapon` auf BeginPlay, `SeedMagazine`, `StartReload`/`CommitReload`/`FinishReload`, `FallbackToDefaultCaliber`, `GetCaliberById`, `SetActiveCaliberById`. |
| `BP_Projectile` | **Läuft** | Parent `StaticMeshActor`, Mobility `Movable`, Tick-Bewegung, 3 s Lebensdauer. Kein Treffer, kein Schaden — das ist Schritt 20. |
| Gegner, Wellen | Nichts | Der Rest des Kerns — hier geht es weiter |

**Handverdrahtung:** Die beiden offenen Verbindungen zur GameInstance sind erledigt. Was noch offen
ist, steht in `AGENTS.md` §4b — und ist per Toolset baubar, nicht mehr Handarbeit.

**Getrimmte Werte.** Movement: MaxWalkSpeed 800 (Basis, aus `GetPlayerStats`), GroundFriction 12,
BrakingFriction 12 mit Faktor 2. Dash: Distanz 650, Restgeschwindigkeit 1200, Kosten 34 von 100
Stamina, Regen 25/s nach 0,5 s Verzögerung, Mindestpause 0,25 s.

**Beschleunigung ist an die Geschwindigkeit gekoppelt (14.09.).** `MaxAcceleration` und
`BrakingDecelerationWalking` sind keine festen Zahlen mehr, sondern werden in `ApplyPlayerStats` als
`MoveSpeed × AccelerationFactor` gesetzt (`AccelerationFactor` = 20 am Character). Vorher standen
beide fest auf 8192 — bei `SpeedLevel` 20 und damit 2000 uu/s brauchte der Charakter 0,24 s bis auf
Tempo statt 0,10 s wie bei der Basis. **Das Speed-Upgrade machte die Figur träger, je stärker sie
wurde.** Über den Faktor bleibt die Zeit bis Vollgas jetzt konstant bei ~0,05 s, unabhängig vom
Upgrade-Level. Der Faktor ist der Regler für „wie direkt fühlt sich ein Richtungswechsel an";
`GroundFriction` ist der zweite.

## Zeitplan bis 25.09.

17 Tage, zwei Wochenenden. Die Rechnung geht auf, aber **ohne echten Puffer**. Die beiden
Gate-Termine sind die eigentlichen Fristen.

| Tag | Schritte | Ziel des Tages |
|---|---|---|
| Mi 09.09. | 1–4 | Der Charakter zielt auf den Cursor, Kamera bleibt ruhig |
| Do 10.09. | 5–8 | Gamepad-Zielen, Geräteerkennung, Dash mit Cooldown, alle Input Actions |
| Fr 11.09. | 9–12 | Stat-Struct, GameInstance, Charakter liest Werte (12 gestrichen) |
| Sa 12.09. | 13–16 | Data Assets, Interaktion — und die Waffe schießt zum ersten Mal |
| So 13.09. | 17–20 | Magazin und Nachladen, Kaliberwechsel, Health, Schaden am Ziel |
| Mo 14.09. | 21 | Gegner läuft auf dich zu und schlägt zu |
| Di 15.09. | 22 | L_Outside als Graybox mit NavMesh, Rückweg unter 15 s geprüft |
| **Mi 16.09.** | **23–25** | **Gate 1** — drei Wellen, HUD, Tod. Macht der Fight Spaß? |
| Do 17.09. | — | Reiner Tuning-Tag aus Gate 1. Keine neuen Funktionen. |
| ~~Fr 18.09.~~ | ~~26–28~~ | **am 16.09. vorgezogen** — Geld, Rückweg-Fenster, Tür, dazu Gegnertypen aus 36 |
| Sa 19.09. | 29–32 | Sofort-weiter, Tod-Regel, Levelwechsel mit Zustand, Run-Summary |
| **So 20.09.** | **33–35** | **Gate 2** — Waffenbank, Werkbank, Ausgang. Der Loop läuft rund. |
| Mo 21.09. | 36–38 | Echtes Pathfinding, Wellen aus `WaveData`, volle Kaliber-Leiter (Gegnertypen ✔) |
| Di 22.09. | 39–42 | Projektil-Looks, Durchschlag, Heilung und Granate, Armor |
| Mi 23.09. | 43–44 | Boss und Balancing der Wellenkurve |
| Do 24.09. | 45–48 | Menü-Level, Bett, Musik-States, Pause- und Tod-Screen |
| Fr 25.09. | 49–50 | Trefferfeedback, Art-Pass, Build. **Keine neuen Funktionen mehr.** |

### Die vier Tage, an denen es kippt

**Sa 12. und So 13.09.** tragen je vier Schritte, darunter der komplette Waffenkern — Projektile,
Magazin, Kaliberwechsel. Dichtester Block des Plans, liegt bewusst aufs Wochenende.

**Mo 14. und Di 15.09.** sind Gegner-KI und NavMesh. Beides sieht nach wenig aus und frisst
erfahrungsgemäß einen ganzen Abend an Kleinigkeiten: NavMesh das nicht baut, `MoveTo` das nichts
tut, Kollisionseinstellungen. Deshalb steht dort nur je ein Schritt pro Tag.

### Streichliste, falls du am 20.09. hinterherhinkst

In dieser Reihenfolge streichen:

1. **Art-Pass** (Schritt 50) — Graybox ist ein legitimer Zustand für einen Vertical Slice.
2. **Aufwachen im Bett** (Schritt 46) — reine Inszenierung.
3. **Gegner im Menü-Hintergrund** (Schritt 45) — statisches Menü tut es auch.
4. **Durchschlag** (Schritt 40) — .50 BMG funktioniert auch ohne.
5. **Kaliber-Leiter von sieben auf vier** — 6mm, 5.56, 12 Gauge, .50 BMG.
6. **Granate** (Teil von Schritt 41) — nur Heilung, keine Wurfwaffe.
7. **Gegnertypen von drei auf zwei** — Rusher und Tank, der Schütze ist der aufwendigste.

> **Nie streichen:** der geschlossene Loop, die Tod-Regel, das Rückweg-Fenster, zwei Kaliber mit
> spürbarem Unterschied, der Boss. Ohne diese fünf zeigt der Slice nicht, was das Spiel ist.

---

# Baureihenfolge

Jeder Schritt ist eine abgeschlossene Einheit mit einer Probe am Ende. Erst wenn die Probe
durchgeht, kommt der nächste.

## Phase 0 — Fundament · bis Sa 12.09.

Am Ende läuft und zielt der Charakter mit beiden Eingabegeräten, dasht mit Stamina und zieht seine
Werte aus der GameInstance, die einen Neustart übersteht.

> **Phase 0 abgeschlossen (14.09.).** Schritte 1–14 stehen; Schritt 12 (SaveGame) ist gestrichen.
> Darüber hinaus gebaut: Stamina statt Dash-Cooldown, Rückdrehen in Laufrichtung bei längerem
> Nicht-Zielen, Mausbewegungs-Erkennung über die Cursorposition, weiches Körper-Nachdrehen über
> `bUseControllerDesiredRotation`.
>
> Schritt 11 galt als „Cross-Blueprint, also Handarbeit". Das war ein Irrtum über die MCP-Toolsets,
> kein Engine-Limit — siehe `AGENTS.md` §3. Er ist jetzt per Toolset gebaut.
>
> **Offen aus Phase 0:** nur noch die `Pressed`-Trigger an den Input Actions.

### 1. SpringArm auf Top-Down stellen

- `BP_PlayerCharacter` → Komponente `springArm`
- Relative Rotation: Pitch `-60`, Yaw `0`, Roll `0`
- Target Arm Length: `1200` als Startwert
- Use Pawn Control Rotation: **aus**
- Inherit Pitch / Yaw / Roll: **alle drei aus** — das ist der entscheidende Punkt
- Do Collision Test: **aus**, sonst springt die Kamera an Wänden
- An der Komponente `camera` ebenfalls Use Pawn Control Rotation aus

**Probe:** Play drücken. Die Kamera schaut schräg von oben. Wenn du den Charakter drehst, bleibt die
Kamera stehen.

### 2. Bewegung prüfen — nur bauen, falls sie fehlt

- Play in `L_Outside`, WASD testen
- Falls nichts passiert: `IA_Move`-Event → `AddMovementInput`, zweimal
- X-Achse auf Weltvektor `(1,0,0)`, Y-Achse auf `(0,1,0)`
- Bewusst weltrelativ, nicht kamerarelativ

**Probe:** WASD bewegt in feste Weltrichtungen, unabhängig davon, wohin der Charakter schaut.

### 3. Zielpunkt aus der Mausposition

- Neue Funktion `GetAimLocation` in `BP_PlayerCharacter`, Rückgabe Vector
- `Get Player Controller` → `Deproject Mouse Position To World` liefert Ursprung und Richtung
- `Line Plane Intersection` gegen eine waagerechte Ebene auf Höhe `GetActorLocation.Z`
- Der Schnittpunkt ist der Zielpunkt auf Spielerhöhe

**Probe:** PrintString des Rückgabewerts auf Tick. Die Zahlen folgen dem Cursor, die Z-Komponente
bleibt konstant.

### 4. Charakter zum Zielpunkt drehen

- Auf Event Tick: `Find Look at Rotation` von `GetActorLocation` zu `GetAimLocation`
- Nur den Yaw übernehmen, Pitch und Roll auf 0
- `SetControlRotation` am PlayerController — nicht `SetActorRotation`
- `bUseControllerRotationYaw` steht am Character bereits auf true, dadurch folgt der Körper

**Probe:** Der Charakter schaut immer zum Cursor. Die Kamera bleibt dabei völlig ruhig — tut sie das
nicht, stimmt Schritt 1 nicht.

### 5. Zielen mit dem rechten Stick

- Neue Input Action `IA_Aim`, Typ Axis2D
- In `IMC_Gameplay` auf den rechten Stick mappen
- Bei Stick-Auslenkung über der Deadzone: Richtung in Yaw umrechnen, als Control Rotation setzen
- Unterhalb der Deadzone die letzte Richtung halten, nicht zurückspringen

**Probe:** Der rechte Stick dreht den Charakter. Loslassen behält die Richtung bei.

### 6. Erkennen, welches Gerät gerade benutzt wird

- Boolean `bUsingGamepad` im PlayerController
- Umschalten, sobald ein Gamepad-Input oder eine Mausbewegung kommt
- Schritt 4 und 5 laufen jetzt exklusiv: je nach Flag entweder Cursor oder Stick

**Probe:** Maus bewegen, dann Stick, dann wieder Maus. Der Charakter springt nicht und folgt immer
dem zuletzt benutzten Gerät.

### 7. Dash: Stamina statt Cooldown ✔

- `DashReady` wird jeden Frame **abgeleitet**: genug Stamina **und** Mindestpause vorbei
- `SpendDashStamina` zieht beim Dash ab und merkt sich den Zeitpunkt
- `RegenerateStamina` lädt im Tick nach, begrenzt auf `MaxStamina`
- Das alte `Set DashReady = true` am Schleifenende ist entfernt — es gab den Dash sofort wieder frei

**Probe:** Dreimal hintereinander dashen geht, beim vierten Mal nicht mehr.

### 8. Restliche Input Actions anlegen

- `IA_Fire`, `IA_Reload`, `IA_Interact`, `IA_SwitchCaliber`, `IA_UseHeal`, `IA_UseGrenade`
- `IA_SwitchCaliber` ist ein **Durchwechseln**, keine Slot-Wahl — Q und rechte Schultertaste
- Alle in `IMC_Gameplay` mappen, jeweils für Tastatur/Maus **und** Gamepad
- Noch keine Logik dahinter, nur je ein PrintString

**Probe:** Jede Taste und jeder Button gibt seinen Text aus — auf beiden Geräten.

### 9. Struct für die Spielerwerte

- Neues Struct `S_PlayerStats`: `MaxHealth`, `MoveSpeed`, `ArmorReduction`, `MaxStamina`, `StaminaRegen`
- Nur Werte, die von Upgrades verändert werden

**Probe:** Struct kompiliert und ist als Variablentyp auswählbar.

### 10. GI_Achachay mit Zustand füllen

- Geld: `Money` (dauerhaft) und `RunMoney` (nur im Run)
- Upgrade-Level: `SpeedLevel`, `ArmorLevel`, `HealthLevel`
- **Munitionsvorrat je Kaliber** als Map `CaliberData → Anzahl Schuss`
- `CurrentCaliber` als aktives Kaliber — keine Slots
- Verbrauchsgüter: `HealCount`, `GrenadeCount`
- Funktion `GetPlayerStats`: rechnet die drei Level in ein `S_PlayerStats` um, Formel `Basis + Level × Schritt`
- `ActiveInputDevice` und die beiden Setter stehen bereits

**Probe:** `GetPlayerStats` liefert bei Level 0 die Basiswerte und bei Level 3 höhere.

### 11. Charakter zieht seine Werte aus der GameInstance

- Auf BeginPlay: `Get Game Instance` → Cast auf `GI_Achachay` → `GetPlayerStats`
- `MaxWalkSpeed` am CharacterMovement setzen, `DashCooldown` setzen, Health auf MaxHealth

**Probe:** `SpeedLevel` in der GameInstance hochsetzen, Play drücken — der Charakter ist spürbar
schneller.

### 12. ~~SaveGame~~ — **gestrichen (14.09.)**

Ersatzlos entfernt: `SG_Achachay`, `SaveProgress`, `LoadProgress` und die Aufrufe. Die Schrittnummer
bleibt stehen, damit die Verweise im Zeitplan weiter passen.

**Begründung:** Der Slice braucht keinen SaveGame. Die GameInstance überlebt Levelwechsel und Tod —
mehr verlangt der Loop nicht. Persistenz über einen Neustart hinaus ist kein Teil dessen, was der
Slice zeigen soll, und steht entsprechend auch nicht auf der „Nie streichen"-Liste.

Der eigentliche Auslöser war aber praktischer Natur: `LoadProgress` hing an `Event Init` und
überschrieb dort die Class Defaults, sobald irgendein Save existierte — auch ein leeres. Beim
Entwickeln, wo ständig an Werten gedreht wird, macht das jede Probe wertlos. Am 14.09. hat genau
das die Proben zu Schritt 11 und 12 verfälscht: Ein `SpeedLevel` oder `Money`, das in den Class
Defaults gesetzt wurde, war bei `BeginPlay` längst wieder auf 0.

**Falls es je zurückkommt:** Das erste und einzige Save enthielt null Properties. Entweder waren
beim Speichern alle Werte identisch mit den Defaults (dann ist alles in Ordnung — Unreal überspringt
solche Properties), oder den Variablen fehlte das **SaveGame**-Flag (dann speichert
`SaveGameToSlot` grundsätzlich nichts). Das ist nie geklärt worden.

### 13. Data Assets anlegen

- `CaliberData` als PrimaryDataAsset: Anzeigename, Schaden, Magazingröße, Feuerrate, Reloadzeit,
  Streuung, Projektile pro Schuss, Durchschlag, Projektil-Look, Mesh — dazu **`UnlockPrice`**
  (einmalig; 0 für 6mm)
- `ItemData`, `UpgradeData`, `WaveData` als Gerüste
- Zwei Test-Kaliber anlegen, die sich maximal unterscheiden: **6mm** (40er-Magazin) und **.50 BMG** (3er-Magazin)

**Probe:** Beide Kaliber-Assets liegen im Content Browser und lassen sich öffnen.

### 14. Interaktions-System

- Blueprint Interface `BPI_Interactable` mit `GetPrompt` und `Interact`
- Im Charakter: Sphere-Overlap oder kurzer Trace nach vorn, nächstes gültiges Ziel merken
- `IA_Interact` ruft `Interact` am gemerkten Ziel auf
- Bewusst gerätunabhängig — kein Klicken, damit Maus und Gamepad denselben Weg gehen

**Probe:** Ein Testwürfel mit dem Interface gibt beim Hingehen und Drücken einen PrintString aus.

---

## Phase 1 — Der Fight steht · bis Mi 16.09.

Am Ende ist `L_Outside` spielbar: Waffe, Gegner, drei Wellen, HUD.

### 15. BP_Weapon, gespeist aus dem Kaliber

- Eine Waffe, an den Charakter gehängt
- Variable `ActiveCaliber` vom Typ `CaliberData`
- Sämtliches Verhalten wird daraus gelesen, nichts hart eingetragen

**Probe:** Kaliber im Editor tauschen ändert die ausgelesenen Werte.

### 16. Schießen und Projektil

- `BP_Projectile` mit ProjectileMovement, Farbe und Größe aus dem Kaliber
- `IA_Fire` spawnt in Blickrichtung, Feuerrate begrenzt per Timer
- Streuung und Projektilanzahl aus dem Kaliber anwenden

**Probe:** 6mm feuert schnell und schwach, .50 BMG langsam und dick — der Unterschied ist ohne HUD
sichtbar.

### 17. Magazin und Nachladen ✔ (15.09., am 15.09. vereinfacht)

- Magazinstand pro Kaliber als Map `CaliberId→Schuss` in der **GameInstance**
- Größe und Nachladezeit aus dem Kaliber
- Leeres Magazin oder `IA_Reload` startet das Nachladen
- Nachladen füllt auf **voll** auf — es gibt keinen Vorrat, von dem etwas abgezogen wird

**Probe:** .50 BMG dreimal schießen, danach lädt es gut drei Sekunden und ist wieder bei 3.

**Vereinfacht am 15.09.** Ursprünglich lief das über einen getrennten Vorrat (`AmmoReserve`), der
packungsweise gekauft wurde. Damit hingen drei Dinge zusammen, die einzeln schon schwer genug sind:
Magazin, Vorrat und Geld. Gestrichen sind deshalb `AmmoReserve`, `GetReserveRounds`, `AddToReserve`,
`TakeFromReserve`, der automatische Rückfall auf 6mm und der Testvorrat in den GI-Defaults.

Der Magazinstand liegt in der GameInstance, **nicht auf `BP_Weapon`** — die Waffe wird bei jedem
Levelwechsel neu gespawnt, die GI überlebt. Als es auf der Waffe lag, ging bei jedem Wechsel das
volle Magazin verloren und wurde erneut aus dem Vorrat nachgefüllt; pro Levelwechsel verschwanden so
bis zu `MagazineSize` Schuss.

### 18. Kaliber durchwechseln ✔ (15.09., am 15.09. vereinfacht)

- `IA_SwitchCaliber` schaltet auf das nächste **freigeschaltete** Kaliber
- 6mm ist immer freigeschaltet
- Magazinstand pro Kaliber getrennt gemerkt

**Probe:** Mit zwei freigeschalteten Kalibern durchwechseln, jeweils mit eigenem Magazin.

`IA_SwitchCaliber` hat einen **`Pressed`-Trigger**. Ohne den feuert `Triggered` jeden Frame und Q
rast beim Halten durch alle Kaliber.

### 19. Health-Komponente ✔ (15.09.)

- Eine Komponente für Spieler und Gegner gleichermaßen
- Aktuelle und maximale Health, `ApplyDamage`, Tod-Event
- `ArmorReduction` schon einbauen, auch wenn sie noch 0 ist

**Probe:** Testweise Schaden zufügen senkt den Wert und löst bei 0 das Tod-Event aus.

**Gebaut am 15.09.** `BPC_Health` (ActorComponent) unter `Core/`: `MaxHealth`, `CurrentHealth`,
`ArmorReduction`, dazu `ApplyDamage(Amount)`, `InitHealth(NewMax, NewArmor)`, `IsAlive()` und der
Event Dispatcher `OnDeath`. Der Schaden wird um `ArmorReduction` gemindert, aber **nie unter 1** —
sonst würde hohe Armor einen Gegner unverwundbar machen statt nur zäh. `BeginPlay` füllt
`CurrentHealth` auf `MaxHealth`, wenn es noch 0 ist.

### 20. Projektil verursacht Schaden ✔ (15.09.)

- Treffer auf einen Actor mit Health-Komponente wendet den Kaliberschaden an
- Projektil zerstört sich, außer bei Durchschlag — der kommt erst in Phase 3

**Probe:** Ein Testwürfel mit Health verschwindet nach der richtigen Trefferzahl.

**Gebaut am 15.09.** `BP_Projectile` bewegt sich nicht mehr blind per `SetActorLocation`, sondern über
`MoveStep(DeltaSeconds)`: ein **Sphere-Trace von der alten zur neuen Position** mit `TraceRadius`
(= `ProjectileSize × 50`). Kein Treffer → Position setzen; Treffer → `HandleHit`. Ein reines Overlap
hätte bei diesen Geschwindigkeiten durch dünne Gegner durchtunneln können.

`HandleHit` sucht am getroffenen Actor eine `BPC_Health` und ruft deren `ApplyDamage` mit dem
Kaliberschaden. Danach zerstört sich das Projektil — auch bei Treffern ohne Health, also an Wänden.
Durchschlag (`Penetration`) ist noch nicht ausgewertet, das ist Phase 3.

Der Owner (der Spieler) steht in `ActorsToIgnore`, damit man sich nicht selbst trifft.

**Durchschlag vorgezogen (16.09., eigentlich Schritt 40).** Ich hatte für später plädiert, weil die
Wellen noch keine Gegnerreihen liefern — im Spiel stellte sich heraus, dass sie es doch tun: Alle
Gegner laufen direkt auf den Spieler zu und bilden dadurch von selbst eine Kolonne.

`BP_Projectile` hat jetzt `IgnoredActors`. Beim Spawn kommt der Owner hinein, bei jedem Treffer der
getroffene Gegner. Die Liste geht als `ActorsToIgnore` in den Trace — dadurch wird derselbe Gegner
nicht im nächsten Frame erneut getroffen, was `.50 BMG` sonst fünfmal auf ein Ziel statt einmal auf
fünf Ziele feuern ließe.

`Penetration` aus dem Kaliber ist das verbleibende Budget und wird pro Treffer um 1 gesenkt; bei
unter 0 zerstört sich das Projektil. 6mm (0) trifft damit genau einen Gegner, `.50 BMG` (5) sechs.

**Wände stoppen immer**, unabhängig vom Restbudget: Ein Treffer ohne `BPC_Health` zerstört das
Projektil. Sonst würde Durchschlag die Deckung entwerten, statt Gegnerreihen zu belohnen.

****Testziel:** `BP_TestTarget` unter `Enemies/` — Würfel-Mesh, `BPC_Health` mit 100 HP, `OnDeath`
zerstört den Actor. Vorstufe zu `BP_EnemyBase` (Schritt 21).

**Projektilwerte am 15.09. auf sichtbare Größen getunt** (vorher 7000–13000 uu/s bei Größe 0,1–0,3 —
das Projektil sprang pro Frame um ein Vielfaches seiner eigenen Länge und war praktisch unsichtbar):
6mm 2200/0,25 · 9mm 2400/0,30 · .45 ACP 2200/0,35 · 7.62 2800/0,35 · .44 Mag 2600/0,45 ·
.50 BMG 3500/0,60.

**Ziellaser (15.09.).** `BP_PlayerCharacter.DrawAimLaser` am Tick zeichnet eine Linie vom Mündungspunkt
entlang derselben Richtung, die `Fire` bekommt — sie lügt also nicht. Länge über `AimLaserLength`
(1500). Nutzt `DrawDebugLine`, **rendert damit nur in Editor- und Development-Builds**; für ein echtes
Spielelement später Mesh oder Niagara-Beam. Hindernisse ignoriert er noch — sobald es Wände gibt,
kann er auf denselben Trace wie das Projektil gesetzt werden.

### 21. BP_EnemyBase ✔ (15.09., läuft — aber ohne Pathfinding)

- Character mit Health-Komponente
- Eigener AIController, auf Tick oder im Intervall `MoveTo` auf den Spieler
- Nahkampfangriff bei Kontakt mit Cooldown
- Kein Behavior Tree

**Probe:** Der Gegner findet den Spieler durch die Graybox und schlägt zu.

**Gebaut am 15.09.** `BP_EnemyBase` (Character) unter `Enemies/`: `BPC_Health` (60 HP), Würfel-Mesh,
`AutoPossessAI = PlacedInWorldOrSpawned`. `BeginPlay` setzt `MaxWalkSpeed` aus `MoveSpeed` (320) und
merkt sich den Spieler als `Target`. `UpdateAI` am Tick: außerhalb `AttackRange` (150) →
`SimpleMoveToActor`, innerhalb → `TryAttack` mit `AttackCooldown` (1 s) und `AttackDamage` (10).
`OnDeath` zerstört den Actor.

Die Distanz wird **2D** gemessen (`Distance2D`), damit ein Höhenunterschied zwischen Kapselmitte und
Spieler den Angriff nicht blockiert.

**`SimpleMoveToActor` funktioniert nicht — durch direkte Bewegung ersetzt (15.09.).** Der Gegner
bewegte sich keinen Zentimeter. Gemessen statt vermutet: Tick lief, `AIController` besaß den Pawn,
`Target` zeigte auf den Spieler, `MaxWalkSpeed` war 320, die Distanz wurde korrekt berechnet, und
`LastMoveRequestTime` zeigte, dass der Aufruf tatsächlich jede Viertelsekunde stattfand — die
Geschwindigkeit blieb trotzdem 0.

Ausgeschlossen wurden dabei: fehlendes NavMesh (nach Editor-Neustart ist das Navigations-Log leer),
Aufruf jeden Frame (auf 0,25 s gedrosselt), blockierende Kollision am Körper-Mesh (auf `NoCollision`)
und Navigationsrelevanz des Mesh (`bCanEverAffectNavigation = false`).

`UpdateAI` nutzt jetzt **`AddMovementInput`** in Richtung Ziel, flach in der XY-Ebene. Verifiziert per
PIE: Gegner startet bei (1800, 1800), erreicht (70, 93), Spieler-Health fällt von 100 auf 0.

**Preis dieser Lösung:** Die Gegner laufen **nicht um Deckungen herum**, sondern dagegen. Im offenen
Areal fällt das kaum auf, bei den fünf Cover-Blöcken schon. Das NavMesh liegt fertig im Level und
wird momentan nicht benutzt — bei Schritt 36 (Gegnertypen) sollte entweder `AI MoveTo` (latent, mit
Fehlerausgang) probiert oder die Ursache weiter eingegrenzt werden.

**Spieler hat jetzt auch Health (Nachtrag zu 19).** `BPC_Health` am `BP_PlayerCharacter`, gefüllt über
`InitHealthFromStats` aus `MaxHealth`/`ArmorReduction` der `PlayerStats` — direkt nach
`ApplyPlayerStats` im BeginPlay.

### 22. L_Outside als Graybox ✔ (15.09.)

- Grundfläche, ein paar Deckungen, eine klar erkennbare Safehouse-Tür
- NavMeshBoundsVolume über das gesamte begehbare Areal
- Entfernteste Kampfzone so setzen, dass der Rückweg zur Tür unter 15 Sekunden bleibt — bei
  600 uu/s sind das etwa 90 Meter, also spürbar darunter bleiben

**Probe:** Von der entferntesten Ecke zur Tür laufen und die Zeit stoppen. Deutlich unter 15
Sekunden.

**Gebaut am 15.09.** Der vorhandene Boden ist 8000×8000 uu (80×80 m), PlayerStart im Zentrum. Dazu:

- **Vier Begrenzungsmauern** auf ±4000, Höhe 400 — Outliner-Ordner `Graybox/Walls`
- ~~Fünf Deckungen~~ — **am 15.09. wieder entfernt.** Ohne Pathfinding blieben die Gegner daran
  hängen, womit die Deckungen *schlechter* waren als keine: Der Spieler hätte einen sicheren Platz
  gehabt. Kommen zurück, sobald die Schuld aus *Offene technische Schulden* beglichen ist.
- **Türmarke** an der Südmauer bei (0, −3900), blau eingefärbt zum Wiedererkennen. Nur Optik; die
  funktionierende Tür ist Schritt 28.
- **`NavMeshBoundsVolume`** über die volle Fläche (−4000…4000, Z −400…800). `RecastNavMesh-Default`
  ist dadurch automatisch entstanden, AgentRadius 35 / AgentHeight 144.
- Zwei `BP_EnemyBase` und ein `BP_TestTarget` platziert — `Gameplay/Enemies`

**Rechnung zum Rückweg:** Von der entferntesten Ecke zur Tür sind es rund 5700 uu. Bei der
Basis-Bewegung von 800 uu/s sind das etwa **7 Sekunden** — die 15 aus dem Plan sind damit gut
eingehalten, es bleibt sogar Luft, das Areal später zu vergrößern.

### 23. BP_WaveDirector ✔ (15.09.)

- Spawnpunkte als Actors im Level
- Drei Wellen fest verdrahtet, Zusammensetzung noch nicht aus `WaveData`
- Welle endet, wenn der letzte Gegner tot ist — Zähler statt Timer
- Danach Pause, dann nächste Welle

**Probe:** Drei Wellen laufen hintereinander durch. Schneller Töten verkürzt die Welle sichtbar.

**Gebaut am 15.09.** `BP_SpawnPoint` (leerer Actor mit Billboard) und `BP_WaveDirector` unter `Waves/`.
Vier Spawnpunkte an den Arealrändern, Director im Zentrum.

- `BeginPlay` sammelt alle `BP_SpawnPoint` per `GetAllActorsOfClass`, startet Welle 1
- Gegnerzahl: `BaseCount + (Welle-1) × CountPerWave` — aktuell 3 + 2 pro Welle
- Spawnpunkte werden reihum benutzt, mit ±200 uu Streuung, damit Gegner nicht ineinander stehen
- **Wellenende per Timer alle 0,5 s**, nicht per Delegate: `CheckWaveOver` zählt lebende
  `BP_EnemyBase`. Bei 0 → `WaveActive` aus, nach `NextWaveDelay` (3 s) die nächste Welle.

**Warum Polling statt Event:** Ein Delegate pro Gegner an den Director zu binden ist über die
Blueprint-DSL fragil. Alle 0,5 s eine Handvoll Actors zu zählen kostet nichts und hat keine
Bindungsfehler-Klasse. Falls die Gegnerzahl je dreistellig wird, lohnt der Umbau auf Events.

**Verifiziert per PIE:** Welle 1 startet, `CurrentWave` 1, `WaveActive` true, drei Gegner gespawnt,
vier Spawnpunkte gefunden.

**Noch ungetestet:** Der Übergang zur nächsten Welle — dafür müssen erst alle Gegner sterben. Das
geht erst sinnvoll, wenn der Spielertod gebaut ist (Schritt 25), weil sonst der Spieler zuerst fällt.


### 24. Provisorisches HUD ✔ (16.09.)

- Health, Stamina, aktuelle Welle, Geld
- **Alle freigeschalteten Kaliber mit Magazinstand**, das aktive hervorgehoben
- Magazinstand des aktiven Kalibers
- Hässlich ist in Ordnung — es geht um Information, nicht um Gestaltung

**Probe:** Alle Werte aktualisieren sich live, der Wechsel verschiebt die Hervorhebung.

**Gebaut am 16.09.** `WBP_HUD` unter `UI/` mit sechs TextBlocks in einer Vertical Box. `RefreshHUD`
läuft am Widget-Tick und füllt Health, Stamina, Welle, Geld, Magazin und Kaliberleiste. Die
Referenzen auf Spieler, GameInstance und WaveDirector werden einmal im `Construct` geholt, nicht pro
Frame gesucht. Eingeblendet wird in **`PC_Outside`**, nicht im Character — so hängt das HUD am Ort
und erscheint im Safehouse nicht.

**Geld steht als zwei Zahlen da** (`$ 120   RUN + 45`): gesichert und im Run erkämpft. Eine einzelne
Zahl würde den Unterschied verstecken, auf dem das Rückweg-Fenster beruht.

**HP-Leisten über Gegnern (16.09.).** `WBP_EnemyHealth` mit einer ProgressBar, eingehängt als
`WidgetComponent` an `BP_EnemyBase` (`Space: Screen`, `DrawSize` 70×8, 105 uu über der Kapselmitte).
`BindHealthBar` reicht im BeginPlay die Health-Komponente des jeweiligen Gegners durch; der Tick des
Widgets setzt den Prozentwert.

`Space: Screen` statt `World`, damit die Leiste sich zur Kamera dreht und ihre Pixelgröße behält.
Die ProgressBar ist im Canvas auf Füllen verankert — sonst bestimmt ihre feste Slot-Größe die
Darstellung und `DrawSize` bleibt wirkungslos.

**Offen: Zelda-artiger Kreis für Health und Stamina** neben dem Charakter. Braucht ein radiales
Material oder eine Kreistextur — Gestaltungsfrage, gehört zum Art-Pass.

**Werkzeug-Grenze, die dabei klar wurde:** Neue Widgets lassen sich per MCP **nicht** in den
Widget-Tree einfügen. Bestehende dagegen schon — über `WidgetTree.<Name>` und deren Slots sind
Größe, Anker und Eigenschaften änderbar. Arbeitsteilung also: Element von Hand hineinziehen und
benennen, Rest per Werkzeug.

### 25. Spielertod ✔ (16.09.)

- Health auf 0 → Eingabe sperren, kurz warten, Karte neu laden

**Probe:** Sterben führt zuverlässig zum Neustart, ohne hängenzubleiben.

**Gebaut am 16.09.** `BPC_Health.OnDeath` am Spieler ist an `HandleDeath` gebunden: `IsDead`-Flag
setzen (verhindert Mehrfachauslösung), `DisableInput`, `StopMovementImmediately`, dann Timer über
`RestartDelay` (2 s) auf `RestartRun`. Das lädt per `OpenLevel(GetCurrentLevelName(true))` dieselbe
Karte neu — das `true` streift das PIE-Präfix ab, sonst landet man in der Default-Map.

**Tod-Regel gleich mitgebaut (16.09.).** Statt dieselbe Karte neu zu laden führt der Tod **ins
Safehouse** (`OpenLevel("L_Safehouse")`, wie die Debug-Hotkeys im Menü). Davor ruft er
`GI_Achachay.ClearRunState`: `RunMoney`, `HealCount` und `GrenadeCount` auf 0. `Money`,
Upgrade-Level und `UnlockedCalibers` bleiben.

Damit ist ein Teil von **Schritt 30** vorgezogen — der Rest dort (Run-Summary-Anbindung) bleibt offen.

**Kurz aufgekommen und verworfen:** Ob das erkämpfte Geld den Tod überleben soll. Entschieden am
16.09.: **nein.** Sonst verliert das 15-Sekunden-Rückwegfenster seinen Zweck — wenn Sterben nichts
kostet, gibt es keinen Grund zu extrahieren, und Positionswahl, Rückweg und das Speed-Upgrade als
Extraktionsreichweite hängen alle daran.

> ### ⛳ Gate 1 — nach Schritt 25 (Mi 16.09.)
> **Macht der Fight für sich genommen Spaß?**
> Mit Maus **und** Gamepad spielen. Hier wird an Feuerrate, Dash-Cooldown, Gegnertempo und
> Trefferrückmeldung gedreht, bis es sitzt. Wenn es sich hier nicht gut anfühlt, ist alles Folgende
> verschwendete Arbeit.

---

## Phase 2 — Der Loop schließt sich · bis So 20.09.

Ab hier ist es dein Spiel und nicht mehr irgendein Wave-Shooter.

### 26. Geld ✔ teilweise (16.09.)

- Drop pro Kill und Bonus pro überstandener Welle, aufaddiert auf `RunMoney`

**Probe:** Kills erhöhen die Anzeige im HUD.

**Gebaut am 16.09.** `BP_EnemyBase.KillReward` (1) wird beim Tod über `GI.AddRunMoney` auf `RunMoney`
gebucht. Die Auszahlung sitzt in `PayoutAndDie` **vor** dem Zerstören des Actors, sonst geht sie
verloren.

**Offen:** Der **Bonus pro überstandener Welle** fehlt noch — gehört zum WaveDirector, sobald das
Wellenende auch ein Ereignis auslöst (Schritt 27).

### 27. Rückweg-Fenster ✔ (16.09.)

- Nach dem letzten Kill 15 Sekunden Countdown, danach startet die nächste Welle
- Countdown im HUD, dazu ein Wegweiser zur Tür, solange sie außerhalb des Bildes liegt

**Probe:** Countdown läuft sichtbar, die nächste Welle startet exakt bei null.

**Gebaut am 16.09. — mit 10 statt 15 Sekunden.** `CheckWaveOver` setzt bei 0 lebenden Gegnern
`ExtractionOpen` und merkt sich `WindowEndTime`; nach `ExtractWindow` (10 s) läuft `StartWave` und
setzt `ExtractionOpen` wieder zurück. `GetRemainingWindow` liefert die Restzeit geklemmt auf 0,
`T_ExtractTimer` im HUD zeigt sie. Die Tür extrahiert nur, solange das Fenster offen ist, und zahlt
`BonusPerWave` (10) × geschaffte Welle zusätzlich aus.

**15 → 10 Sekunden:** Neun Fenster à 15 s sind über zwei Minuten Stehzeit pro Run (siehe oben). 10 s
reichen für den Rückweg, wenn man beim letzten Kill schon in Türnähe steht — und genau diese
Positionswahl soll das Fenster belohnen.

**Der Wegweiser zur Tür fehlt noch.**

### 27a. Wellenskalierung und Gegnertypen ✔ (16.09.)

Anlass: Welle 12 war ohne ein einziges Upgrade erreichbar. Die Basisgegner (320 uu/s, Deckel bei
620) holen den Spieler (800 uu/s) **nie** ein — es dauerte nur immer länger, gefährlich wurde es nie.
Ein Wave-Shooter, bei dem Zeit die einzige Ressource ist, hat kein Upgrade-Bedürfnis.

**Skalierung pro Welle** (`step` = Welle − 1), im `BP_WaveDirector`:

| Größe | Formel | Welle 1 | Welle 10 | Welle 20 |
|---|---|---|---|---|
| Gegnerzahl | `3 + 2·step` | 3 | 21 | 41 |
| Bonus-HP | `18·step` | 0 | +162 | +342 |
| Bonus-Tempo | `14·step` | 0 | +126 | +266 |

Schaden skaliert **bewusst nicht** — sonst wird der Tod zum Sprung statt zur Kurve.

**Pro Typ skaliert es unterschiedlich.** `BP_EnemyBase` hat dafür `HealthScaleMul` und
`SpeedScaleMul` bekommen; `ApplyWaveScaling` multipliziert die Wellenboni damit. Dazu `BaseHealth`
(statt des Komponenten-Defaults) und `BodyScale`, beide in `BeginPlay` angewandt — so unterscheiden
sich die Typen **nur über Default-Werte** und brauchen keine überschriebenen Funktionen. Das ist
auch die werkzeugfreundlichste Form: Kindklasse anlegen, Zahlen setzen, fertig.

| | Läufer (`BP_EnemyBase`) | Schütze (`BP_EnemyShooter`) | Rusher (`BP_EnemyRusher`) |
|---|---|---|---|
| ab Welle | 1 | **5** | **10** |
| Anzahl | Rest der Welle | `(W−5)/2 + 1`, max ⅓ | `(W−10)/2 + 1`, max ¼ |
| Basis-HP | 60 | 45 | 30 |
| HP-Faktor | ×1,0 | ×0,7 | ×0,45 |
| Basis-Tempo | 320 | 210 | 500 |
| Tempo-Faktor | ×1,0 | ×0,5 | **×2,5** |
| Tempo-Deckel | 620 | 340 | **1120** |
| Reichweite | 150 | **1100** | 150 |
| Schaden | 10 / 1,0 s | 8 / 2,0 s | 14 / 0,8 s |
| Geld | 1 | 3 | 4 |
| Körper | 0,7 × 0,7 × 1,76 | schmal und hoch | klein und gedrungen |

**Der Schütze** bricht die Kite-Strategie: Er muss dich nicht einholen, er trifft dich beim
Weglaufen. Sein Projektil ist mit 1200 uu/s langsam genug zum Ausweichen — Druck, kein Automatismus.

**Der Rusher** bricht den Tempovorteil. Er startet bei 500 und wächst mit ×2,5 am schnellsten:

| Welle | Rusher-Tempo | Spieler (Speed 0) | Anzahl |
|---|---|---|---|
| 10 | 815 | 800 | 1 |
| 15 | 990 | 800 | 3 |
| 20 | 1120 (Deckel) | 800 | 6 |

Ab Welle 10 ist er **schneller als der ungeupgradete Spieler** — genau der Punkt, an dem Upgraden
Pflicht wird. Speed kostet 60 uu/s pro Stufe, holt den Deckel also bei Stufe 5 (1100) fast ein.
Speed allein reicht aber nicht: sechs Rusher à 184 HP sind bei 9mm (96 DPS) elf Sekunden Feuer, in
denen sie 105 DPS austeilen. Es braucht **Schaden oder Health dazu** — was gewollt ist.

**Bleibt es spielbar?** Die Bremsen sind eingebaut: Beide Sondertypen sind auf einen Anteil der
Welle gedeckelt (⅓ und ¼), haben deutlich weniger HP als der Läufer und skalieren ihre HP
schwächer. Der Rusher stirbt auch spät in einer 9mm-Sekunde. Erwartete Wand ohne Upgrades:
**Welle 13–15** statt vorher offen — dort, wo vorher der Leerlauf anfing.

**Kein Eigenbeschuss.** Gegnerprojektile setzen `FromEnemy` und tragen andere Gegner in
`IgnoredActors` ein, statt sie zu treffen — sonst hätte sich eine Welle mit genug Schützen selbst
ausgelöscht. Der Schütze ignoriert von Anfang an sich selbst.

**Per PIE verifiziert (16.09.).** Welle 1 spawnt exakt drei `BP_EnemyBase`, keine Sondertypen. Mit
testweise auf 1 gesetzten Startwellen und `BaseCount` 8: genau 1 Rusher + 1 Schütze + 6 Läufer.
Schützenprojektil geprüft: `FromEnemy` true, Schaden 8, Tempo 1200, eigener Schütze in
`IgnoredActors`; Spieler-HP fällt auf 0, während alle acht Gegner im Dauerbeschuss am Leben bleiben.
Testwerte danach zurückgesetzt.

### 28. Safehouse-Tür als Ausgang ✔ teilweise (16.09.)

- Trigger an der Tür, nur während des Fensters aktiv
- Durchlaufen beendet den Run: `RunMoney` wandert auf `Money`, dann Levelwechsel

**Probe:** Rechtzeitig durch die Tür landet im Safehouse, mit dem Geld auf dem Konto.

**Gebaut am 16.09.** `BP_SafehouseDoor` unter `Safehouse/`, platziert bei (0, −3880) an der Südmauer,
wo vorher nur die Deko-Marke stand. Implementiert `BPI_Interactable`; `EventInteract` ruft
`EnterSafehouse`: `GI.BankRunMoney` bucht `RunMoney` auf `Money`, dann `OpenLevel("L_Safehouse")`.

**Abweichung vom Plan:** Kein Trigger zum Durchlaufen, sondern **Interaktion mit `E`** — das nutzt das
vorhandene `BPI_Interactable` statt einer zweiten Mechanik. Und die Tür ist **immer** aktiv, nicht nur
während des Rückwegfensters; das Fenster gibt es noch nicht (Schritt 27).

**Interact-Prompt im HUD (16.09.).** `T_Interact` zeigt „Interact", solange `HasFocus` am Charakter
wahr ist. Hängt am Interface, gilt also für jedes Interactable ohne Zutun des einzelnen Actors. Das
HUD wird inzwischen in **`PC_Outside` und `PC_Safehouse`** eingeblendet — anfangs nur draußen, was den
Prompt am Safehouse-Würfel verschluckte.

### 29. Sofort weitermachen

- Eine Taste, die das Fenster vorzeitig beendet und die nächste Welle startet

**Probe:** Restzeit lässt sich überspringen.

### 30. Tod-Regel

- Tod draußen: `RunMoney` auf 0, gekaufte Heilung und Granaten weg
- Kaliber und Upgrade-Level bleiben unangetastet
- Danach zurück ins Safehouse, nicht Karte neu laden

**Probe:** Nach dem Tod ist das Run-Geld weg, das gesparte Geld noch da.

### 31. Levelwechsel mit Zustand

- Outside → Safehouse und zurück, alles Relevante über `GI_Achachay`
- Kein Speichern — Schritt 12 ist gestrichen, die GI trägt den Zustand allein

**Probe:** Mehrfach hin- und herwechseln, ohne dass ein Wert verlorengeht.

### 32. Run-Summary

- Beim Ankommen im Safehouse: Wellen geschafft, Kills, verdientes Geld
- Auch nach dem Tod anzeigen, dann mit dem Verlust

**Probe:** Die Zahlen stimmen mit dem gerade Gespielten überein.

### 33. Waffenbank — Kaliber freischalten

- Actor mit `BPI_Interactable`, referenziert ein `CaliberData`
- Interagieren schaltet das Kaliber **einmalig** frei und zieht `UnlockPrice` ab
- Drei Zustände sichtbar: freischaltbar, zu teuer, bereits freigeschaltet
- Die ID landet in `UnlockedCalibers` in der GameInstance

**Probe:** Freischalten zieht Geld ab, das Kaliber taucht im Q-Kreis auf und die Station ist danach
erledigt.

### 34. Werkbank

- Interagierbarer Actor für Speed, Armor und Health
- Preis steigt pro Stufe, Level landen in der GameInstance

**Probe:** Ein Upgrade kaufen und den Unterschied draußen sofort spüren.

### 35. Ausgangstür im Safehouse

- Interagierbar, startet einen neuen Run in `L_Outside` bei Welle 1

**Probe:** Der komplette Kreis läuft: raus, kämpfen, rein, kaufen, wieder raus.

> ### ⛳ Gate 2 — nach Schritt 35 (So 20.09.)
> **Willst du nach dem Einkauf sofort wieder raus?**
> Der Test, an dem das ganze Spiel hängt. Wenn der Kauf sich nicht spürbar anfühlt, sind die
> Upgrade-Schritte zu klein — lieber wenige große Sprünge als viele Prozentwerte.

---

## Phase 3 — Inhalt und Kurve · bis Mi 23.09.

Erst jetzt lohnt sich Breite — vorher weißt du nicht, wofür du sie baust.

| # | Schritt | |
|---|---|---|
| 35a | **Echtes Pathfinding nachziehen** | **Pflicht, keine Option.** `BP_EnemyBase.UpdateAI` bewegt sich aktuell per `AddMovementInput` stur geradeaus und läuft in Deckungen hinein. Muss auf NavMesh-Pathing umgestellt werden, bevor Gegnertypen darauf aufbauen. |
| 36 | Weitere Gegnertypen | Rusher, Schütze, Tank — abgeleitet von `BP_EnemyBase` |
| 37 | Wellen aus WaveData | Zusammensetzung und Menge als Daten, nicht als Nodes. Zehn Wellen, nach oben wachsende Menge und Härte. |
| 38 | Volle Kaliber-Leiter | 6mm bis .50 BMG, je eine Waffenbank im Safehouse |
| 39 | Projektil-Looks pro Kaliber | Tracer, Größe, Farbe, Einschlag — hier entsteht die Lesbarkeit im Kampf |
| ~~40~~ | ~~Durchschlag~~ | **Vorgezogen am 16.09.** Siehe Notiz unter Schritt 20. |
| 41 | Heilung, Granate, Vorratsregal | Eigene Tasten, pro Run gekauft, bei Benutzung und bei Tod weg |
| 42 | Armor wirksam machen | Schadensreduktion in der Health-Komponente scharf schalten |
| 43 | Boss | Am Ende von Welle 10, erstmal schlicht sehr viel HP |
| 44 | Balancing | Kurve so ziehen, dass Welle 10 erst im vierten bis fünften Run fällt. Prüfen, ob sich die teuren Kaliber lohnen. |

---

## Phase 4 — Rahmen und Politur · bis Fr 25.09.

Bewusst zuletzt — nichts davon verändert, ob der Loop trägt.

| # | Schritt | |
|---|---|---|
| 45 | Menü-Level | Gegner laufen im Hintergrund, Start-Button, Musik-Skip |
| 46 | Aufwachen im Bett | Einstieg ins Safehouse beim ersten Start |
| 47 | Musik-States | Die sechs ungenutzten Loops an Ort und Wellenintensität koppeln |
| 48 | Pause, Optionen, Tod-Screen | Alle mit Gamepad-Navigation über CommonUI |
| 49 | Feedback | Treffer, Mündungsfeuer, Todes-Effekte, SFX |
| 50 | Art-Pass | Safehouse und Outside |

---

## Offene technische Schulden

Dinge, die **funktionieren, aber nicht fertig sind**. Sie stehen hier, damit sie nicht in
Schritt-Notizen untergehen.

### Gegner laufen ohne Pathfinding — muss vor der Abgabe echt werden

`BP_EnemyBase.UpdateAI` nutzt `AddMovementInput` in Richtung Spieler. Das ist ein Platzhalter, weil
`SimpleMoveToActor` am 15.09. trotz gebautem NavMesh keinerlei Bewegung erzeugte — Controller,
`Target`, `MaxWalkSpeed` und der tatsächliche Aufruf waren alle nachweislich in Ordnung, die
Geschwindigkeit blieb 0.

**Folge:** Gegner laufen gegen Deckungen statt darum herum. Mit fünf Cover-Blöcken im Areal ist das
sichtbar, und es entwertet die Deckungen als taktisches Element — der Spieler kann sich hinter einen
Block stellen und die Gegner bleiben hängen.

**Was zu tun ist**, in dieser Reihenfolge:

1. `AI MoveTo` (latent, mit `OnFail`-Ausgang) statt `SimpleMoveToActor` — der liefert eine
   Fehlerursache, statt still nichts zu tun
2. Falls das auch scheitert: Projekteinstellungen → Navigation System → `SupportedAgents` prüfen. Die
   Liste war am 15.09. leer.
3. Notfalls eigener AIController mit `MoveToActor` statt der Blueprint-Helper-Bibliothek

**Spätestens vor Schritt 36** erledigen — Gegnertypen wie Rusher oder Schütze bauen auf der Bewegung
auf, und drei Gegnertypen auf kaputtem Pathfinding sind dreimal derselbe Fehler.

## Was den Slice kippen kann

**Das große Kaliber macht die kleinen wertlos.** Kaliber sind deine gesamte Progression *und* deine
einzige taktische Entscheidung im Kampf. Beides gleichzeitig hält nur, wenn ein höheres Kaliber
stärker, aber nicht überall besser ist.

**Gamepad erst am Ende einbauen.** Zwei Eingabegeräte nachträglich zu unterstützen heißt,
Zielsystem, Interaktion und jedes Menü anzufassen. Beide Wege von Anfang an mitbauen und bei jedem
Playtest anfassen.

**Behavior Trees und EQS.** Für „lauf zum Spieler und schlag zu" reicht ein AIController mit
`MoveTo`. BTs zahlen sich erst bei Deckung und Flanken aus. **Aber:** `MoveTo` muss dafür erst einmal
funktionieren — siehe *Offene technische Schulden*.

**Den Boss vor der Wellen-Kurve bauen.** Ein Boss ist nur so gut wie das, was ihn vorbereitet.

---

## Zwei Dinge, die feststehen

**Drei getrennte Maps heißt: jeder Zustand stirbt beim Wechsel.** Geld, Upgrades, freigeschaltete
Kaliber, Munitionsvorrat, Wellenfortschritt — nichts davon überlebt ein `OpenLevel` von allein. Alles,
was den Wechsel überstehen muss, gehört in `GI_Achachay`. Einen **Neustart** übersteht bewusst
nichts — Schritt 12 ist gestrichen. Das ist der Grund, warum Phase 0 vor allem anderen steht.

**UI wird mit reinem UMG gebaut — entschieden am 16.09.** CommonUI wird **nicht** aktiviert. Die
wirkungslosen Template-Reste in `DefaultGame.ini` (Konfiguration ohne Plugin, siehe `AGENTS.md` §2)
sind am 16.09. entfernt worden, damit die Verwirrung nicht ein zweites Mal entsteht.

**Warum nicht CommonUI:** Der Gewinn liegt bei Input-Routing zwischen Gamepad und Maus,
Widget-Stapeln mit Zurück-Verhalten und plattformabhängigen Button-Glyphen. Für ein HUD, das nur
Zahlen anzeigt und keinen Fokus kennt, bringt das nichts. Für die Menüs wäre es real, aber es sind
genau drei Bildschirme (Haupt, Pause, Tod) — bei der Größe kostet das Aufsetzen des Frameworks mehr
Zeit, als es bei der Fokus-Navigation spart. Neun Tage vor Abgabe ist ein neues Framework genau die
Art Arbeit, vor der der Abschnitt *Was den Slice kippen kann* warnt.

Nachrüsten bleibt möglich: CommonUI ersetzt UMG nicht, es baut darauf auf.
