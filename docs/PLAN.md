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
- **Werkbank** — die permanenten Upgrades: Speed, Armor, Health, Damage, Stamina, Reload.
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
| **Upgrades** | Sechs: Speed, Armor, Health, Damage, Stamina, Reload. Dauerhaft. (Am 16.09. von drei erweitert.) |
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
- Geld kauft nur noch **vier Dinge**: Kaliber-Freischaltungen, Granaten, Heilung, und die
  Upgrades (am 16.09. von drei auf sechs erweitert).
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
| Sa 19.09. | 29, 32 | Sofort-weiter, Run-Summary (30 und 31 am 16.09. miterledigt) |
| **So 20.09.** | **Gate 2** | **33–35 am 16.09. gebaut** — jetzt nur noch prüfen: Der Loop läuft rund. |
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

## Fahrplan ab 23.09. — neu geschnitten

Am 23.09. kam eine Wunschliste dazu (Boss, Menü, SFX, FX, Screenshake, Low-HP-Screen, Tank,
Achievements, Savegame, Meshes, Animationen, Post Processing). Die **Abgabe bleibt der 25.09.** —
das sind zwei Bautage plus den Freitag. Deshalb zwei Phasen: was den Slice trägt, und was danach
kommt.

Maßstab für Phase A ist die „Nie streichen"-Liste: geschlossener Loop ✔, Tod-Regel ✔,
Rückwegfenster ✔, zwei spürbar verschiedene Kaliber ✔ — **es fehlt allein der Boss.**

### Phase A — bis zur Abgabe

| Tag | Was | Warum genau das |
|---|---|---|
| **Mi 23.09.** | **1. Wellenbonus** (unten) · **2. Wellenende bei 10 + Boss** | Ohne Ende hat der Slice kein Ziel, und der Boss ist der letzte Punkt der Nie-streichen-Liste |
| | 3. HUD-Blöcke anschließen | wartet auf die sechs TextBlocks — siehe Schritt 24a |
| **Do 24.09.** | 4. **Trefferfeedback**: FX + SFX für Schuss und Treffer, Screenshake | Der größte Unterschied zwischen „Graybox" und „Spiel" pro investierter Stunde |
| | 5. **Roter Screen bei wenig HP** | Gehört zum selben Paket: Der Slice hat bisher keine Rückmeldung, dass es eng wird |
| | 6. **Menü + Tod-Screen** | Ein Vertical Slice, der mit einem Levelstart beginnt, wirkt unfertig, egal wie gut der Kampf ist |
| **Fr 25.09.** | 7. Balancing-Pass, 8. Build | **Keine neuen Funktionen.** Steht so schon im alten Zeitplan und gilt weiter |

**Wenn Mittwoch kippt**, fällt in dieser Reihenfolge: Menü-Hintergrund → Tod-Screen → Screenshake.
Boss und Wellenende fallen nie.

### 1. Wellenbonus ✔ (23.09.)

Der Extraktionsbonus steht auf `Welle × BonusPerWave` mit `BonusPerWave` = 10, Welle 10 zahlt also
**100 $** — bei rund 1600 $ Kill-Einnahmen allein aus Welle 10. Der Rückweg lohnt sich damit nie.
Neu: **`Bonus = Welle² × 10`**.

| Welle | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bonus neu | 10 | 40 | 90 | 160 | 250 | 360 | 490 | 640 | 810 | **1000** |
| Kills dieser Welle | 10 | 27 | 59 | 123 | 208 | 338 | 515 | 754 | 1100 | 1596 |

Damit liegt der Bonus ab Welle 4 zwischen 60 % und 100 % dessen, was eine ganze Welle an Kills
bringt — genau der Punkt, an dem „noch eine Welle oder raus?" eine echte Frage wird. Quadratisch
statt linear, weil ein linearer Bonus entweder früh zu fett ist (Welle 1 = 100 $ für nichts) oder
spät wieder bedeutungslos.

**Gebaut am 23.09.** Neue Funktion `BP_SafehouseDoor.BonusForWave(Wave) → Bonus` mit
`Welle × Welle × BonusPerWave`; `DoExtract` und `GetPrompt` rufen sie statt selbst zu multiplizieren.
`BonusPerWave` (10) bleibt der Regler und ist jetzt **Instance Editable**.

**Warum eine eigene Funktion statt zwei Zeilen Rechnung:** Beide Graphen enthalten Nodes mit
**Klammern im Type-Id** — `Game|OpenLevel(byName)` und `Utilities|String|ToString(Integer)`. Die
brechen den DSL-Parser, ein Neuschreiben der Funktionen war damit ausgeschlossen. Also die Rechnung
einmal per DSL in eine neue Funktion, und in den beiden alten Graphen nur den Aufruf per
`create_node` in die Exec-Kette gehängt und die alten Multiplikations-Nodes entfernt.

Ein voller Zehn-Wellen-Run bringt damit **5730 $** gegen **9080 $** Gesamtsenke — gut 1,6 volle
Runs, um alles zu kaufen. Das passt zu „Welle 10 fällt im vierten bis fünften Run".

### 2. Boss ✔ teilweise (23.09.)

**`BP_EnemyBoss`**, Kind von `BP_EnemyBase`, wird vom Director gespawnt, sobald die Zeile
`IsBossWave` gesetzt hat — zusätzlich zur normalen Welle, über dieselbe Ring-Spawnlogik.

| Wert | Basis | auf Welle 10 |
|---|---|---|
| `BaseHealth` | 1200, `HealthScaleMul` 0,5 | **2040 HP** |
| `MoveSpeed` | 260, `SpeedScaleMul` 0,3, Deckel 420 | **287 uu/s** — gut ein Drittel des Spielers |
| `AttackDamage` / `AttackCooldown` | 25 / **0,9 s** (war 1,6) | **27,8 Schaden pro Sekunde** statt 15,6 |
| `ShotSpeed` | **1300** (war 800) | Flugzeit auf volle Reichweite: 1,15 s statt 1,9 s |
| `ShotSize` | **1,5** | Actor-Skalierung *und* Trefferradius (75 statt 17,5) |
| `KillReward` | 40 | 480 $ bei `RewardMul` 12 |
| `BodyScale` | 2,4 | unübersehbar |

**`ShotSize` ist neu an `BP_EnemyBase`** (Default 0,35 für alle anderen). `FireShot` hatte die
Projektilgröße als Literal `0.35` im Graph; jetzt liest es die Variable. `BP_Projectile.Setup`
skaliert damit Actor **und** `TraceRadius` (`Size × 50`) — ein Wert, zwei Wirkungen.

**Nachgeschärft am 23.09.** Auf Zuruf („der Boss muss härter werden"): `AttackCooldown` 1,6 → 0,9
und `ShotSpeed` 800 → 1300. Der Schadensausstoß steigt damit von 15,6 auf **27,8 pro Sekunde**, und
das Ausweichfenster auf voller Reichweite schrumpft von 1,9 s auf 1,15 s. Der Radius bleibt bei 75
(`ShotSize` 1,5) — ausweichen kostet weiterhin nur einen Schritt zur Seite, aber man muss ihn jetzt
früher machen. HP bleiben bei 1200 (2040 auf Welle 10); das ist der nächste Regler, falls er zu
schnell fällt.

**Noch offen — das Wellenende.**
**Per PIE geprüft** (Welle 1 testweise als Boss-Welle): ein `BP_EnemyBoss` neben zwei Läufern,
1200 HP, Tempo 268 (260 plus Jitter), `ShotSize` 1,5, `ShotSpeed` 800. Danach zurückgestellt;
`Wave10` bleibt die Boss-Zeile.

### 3. Wellenende: Boss tot = durchgespielt ✔ (23.09.)

Fällt der letzte Gegner einer Welle, die `IsBossWave` trägt, endet der Run — er läuft nicht weiter:

- `BP_WaveDirector.RunOver` wird gesetzt, `ExtractionOpen` bleibt **dauerhaft** offen
- **kein `WindowEndTime`, kein `StartWave`-Timer** — das 10-Sekunden-Fenster entfällt, man kann
  sich beliebig Zeit lassen
- `ForceNextWave` (die X-Taste) ist gesperrt, solange `RunOver` steht — sonst hätte ein
  Tastendruck Welle 11 geholt, die mangels eigener Zeile wieder `Wave10` benutzt und damit einen
  zweiten Boss gebracht
- `GI_Achachay.GameCleared` wird gesetzt und überlebt den Levelwechsel

Im Safehouse ist damit alles wie sonst: Das Run-Geld ist beim Durchgehen gebucht, Werkbank und
Waffenbänke funktionieren weiter. Das Spiel ist durch, der Laden bleibt offen.

**Im HUD** zeigt `t_Location` statt Ort und Koordinaten `*** BOSS BESIEGT - DURCHGESPIELT ***`,
sobald `GameCleared` steht — in beiden Leveln. Ein eigener Vollbild-Endscreen bräuchte ein neues
Widget, und Widgets kann das Toolset nicht anlegen (siehe 24a).

**Per PIE geprüft:** Der *normale* Wellenwechsel überlebt den Umbau — Welle 1 testweise auf null
Gegner gesetzt, nach dem Fenster stand `CurrentWave` auf 2 mit 9 gespawnten Gegnern,
`ExtractionOpen` wieder false, `RunOver` false. Der Boss-Zweig selbst ist **nicht** per PIE
geprüft: Dafür müsste der Boss sterben, und in einer Simulate-Runde greift ihn niemand an.

### 4. Erfolgs-Flags: die Datenebene ✔ (23.09.)

Vier Flags in `GI_Achachay`, alle überleben Tod und Levelwechsel:

| Flag | Bedingung | Wo gesetzt |
|---|---|---|
| `GameCleared` | Boss-Welle geräumt | `CheckWaveOver` → `NoteGameCleared` |
| `WaveUnder30` | irgendeine Welle in unter 30 s geräumt | `CheckWaveOver` → `NoteWaveCleared` |
| `WaveUnder10` | dasselbe unter 10 s | dito |
| `NoHitClear` | durchgespielt **ohne einen Treffer im Run** | `NoteGameCleared`, wenn `RunDamage` 0 ist |

Dazu zwei Messwerte, die es vorher nicht gab:

**Wellendauer.** `BP_WaveDirector.WaveStartTime` wird in `StartWave` gesetzt, `CheckWaveOver`
reicht `Jetzt − WaveStartTime` an `NoteWaveCleared`. Nebenbei fällt `BestWaveTime` ab — die
schnellste je geräumte Welle, brauchbar für eine Bestenliste im Safehouse.

**Schaden im Run.** `RunDamage` zählt Treffer auf den Spieler und wird in `ResetRunClock`
genullt — das läuft bei `BP_WaveDirector.BeginPlay`, also bei jedem Rausgehen. Ein Run ohne
Treffer ist damit genau ein Run, keine Sitzung.

**Wie der Schaden erkannt wird, ohne den Spieler anzufassen:** `BPC_Health` sitzt auf Spieler
*und* Gegnern, `ApplyDamage` darf also nicht pauschal zählen. Die neue Funktion
`NotePlayerDamage` castet den **Besitzer der Komponente** auf `BP_PlayerCharacter` — schlägt der
Cast fehl, war es ein Gegner und es passiert nichts. Kein Flag am Spieler, keine Änderung an
`BP_PlayerCharacter`.

Ein Umweg war nötig: Eine Flag-Variable an der Komponente wäre einfacher gewesen, aber
**SCS-Komponenten sind am CDO nicht adressierbar** (`…Default__BP_PlayerCharacter_C:Health` ist
kein gültiger Objektpfad), der Wert hätte sich also nicht setzen lassen.

**Per PIE geprüft:** Welle 1 testweise auf null Gegner — nach 1,07 s standen `WaveUnder30` und
`WaveUnder10` auf true, `BestWaveTime` auf 1,07, `RunDamage` auf 0. Danach zurückgestellt.

**Noch offen:** Die Pokale im Safehouse (ein Podest pro Flag, Platzhalter-Mesh, sichtbar sobald das
Flag steht) und der Umbau des Safehouse-Grundrisses.

### 5. Pokalraum ✔ (23.09.)

Pro Flag ein Podest im Safehouse. Podest steht immer da, der Pokal erscheint, sobald das Flag
steht — das leere Podest ist der Hinweis, dass es dort etwas zu holen gibt.

- **`BP_Trophy`**, Elternklasse `StaticMeshActor` (Mobility **Movable**, siehe Fallstrick unten),
  Variable `FlagId` als String, Instance Editable. `BeginPlay` fragt die GI und versteckt sich per
  `SetActorHiddenInGame`, wenn das Flag false ist.
- **`GI_Achachay.GetFlag(FlagId) → bool`** — Namensschalter wie `RaiseUpgradeLevel`, damit die
  Instanz im Level nur einen String setzen muss: `GameCleared`, `WaveUnder30`, `WaveUnder10`,
  `NoHitClear`.
- **Podeste** als einfache Würfel (`StaticMeshActor`, 100er Cube auf 1,2 × 1,2 × 0,8), Platzhalter
  wie der Rest der Graybox. Pokal-Mesh vorerst ein gedrehter Kegel oder Zylinder.
- Vier Stück, später erweiterbar: Jedes neue Flag ist eine Zeile in `GetFlag` plus eine Instanz.

⚠ **`StaticMeshActor` steht per Default auf `Static`** — dann ignoriert der Actor jedes
Verstecken und Bewegen zur Laufzeit, lautlos. Am CDO auf `Movable` gesetzt, sonst wiederholt sich
der Fehler von `BP_Projectile` (siehe `AGENTS.md` §3).

**Gebaut am 23.09.** Vier Podeste (Würfel 120 × 120 × 80) und vier `BP_Trophy` (Kegel) bei
x 900, y 300 / 650 / 1000 / 1350 — im Outliner-Ordner `Trophies`, also dort, wo nach dem Umbau der
Pokalraum liegt. Jede Instanz trägt ihren `FlagId` als String.

**`GI_Achachay.GetFlag(FlagId) → bool`** löst den Namen auf. Zwei Umwege waren nötig:

1. **`==` auf Strings löst nicht auf** (der generische Operator landet beim Zahlenvergleich), und
   `Utilities|String|Equal(String)` trägt Klammern. Stattdessen der **String-Switch**, den der DSL
   als `(switch string …)` direkt kennt.
2. **Die Case-Werte sind keine Pins**, sondern die Node-Eigenschaft `pinNames`; im DSL heißen die
   Ausgänge zwangsweise `Case_0…Case_3`. `pinNames` per `set_properties` auf die Flag-Namen
   umzubiegen funktioniert — **kappt dabei aber alle Case-Verbindungen**, die danach neu gesetzt
   werden müssen. Zugeordnet über den Getter, der am jeweiligen Setter hängt.

Ein Schönheitsfehler bleibt: Die Funktion schreibt über die Hilfsvariable `FlagResult`, weil hinter
einem Switch im DSL kein Statement mehr stehen darf.

**Per PIE geprüft:** Alle Flags false → alle vier Pokale versteckt. `GameCleared` testweise am
CDO auf true → **nur** `Trophy_GameCleared` sichtbar, die anderen drei weiter versteckt. CDO
danach zurückgesetzt.

### 6. Safehouse als Wohnung ✔ (23.09.)

Der Boden ist **8000×8000**, genutzt wird ein Bereich von rund **2800×2800**. Alles steht frei im
Raum, es gibt keine einzige Wand. Vorschlag, analog zum Umbau von `L_Outside`:

**Grundfläche auf 3000×3000**, Wände auf ±1500, dazu ein **Gang in der Mitte** (x −250…250, in
Nord-Süd-Richtung) mit vier Räumen daran:

| Raum | Lage | Inhalt |
|---|---|---|
| **Ausgang** | Nordende des Gangs, (0, 1400) | `ExitDoor` bleibt, wo sie ist; `EntrySpawn` daneben |
| **Shop** | West-Nord, x −1400…−300, y 200…1400 | die sechs Werkbänke |
| **Waffenkammer** | West-Süd, x −1400…−300, y −1400…−200 | die fünf Kaliberbänke |
| **Pokalraum** | Ost-Nord, x 300…1400, y 200…1400 | die vier Podeste |
| **Schlafzimmer** | Ost-Süd, x 300…1400, y −1400…−200 | das Bett |

Damit hat jeder Abschnitt seinen Raum, und der Gang gibt dem Safehouse einen Weg statt einer
Fläche. Türöffnungen bleiben als Lücken in den Wänden — Türen als Actor braucht es hier nicht.

**Gebaut am 23.09.**, mit einer Abweichung: Die Räume reichen jeweils bis zur Mitte
(y 0…1500 bzw. −1500…0), getrennt durch zwei Querwände bei y = 0. Das gibt vier gleich große
Räume statt vier kleiner mit Restfläche.

**Zwölf Wände**, alle 100 dick und 400 hoch, im Outliner-Ordner `Rooms`:

| Wand | Lage |
|---|---|
| `Wall_North/South/East/West` | Außenmauern auf ±1500 |
| `Hall_W_South/Mid/North`, `Hall_E_…` | die beiden Gangwände auf x = ∓250, jeweils dreigeteilt |
| `Split_West`, `Split_East` | Querwände bei y = 0 zwischen Nord- und Südraum |

Die Gangwände waren **absichtlich dreigeteilt**: Zwischen den Segmenten blieb je eine 400 uu
breite Lücke als Türöffnung — eine pro Raum, mittig. Keine Tür-Actors, nur Durchgänge.

**Am 23.09. wieder entfernt — das Safehouse ist jetzt ein Loft.** Auf Zuruf sind alle acht
Innenwände raus (`Hall_*`, `Split_*`), die vier Außenmauern bleiben. Die Zonen tragen sich über
die Einrichtung: Werkbänke im Nordwesten, Kaliberbänke im Südwesten, Podeste im Nordosten, Bett im
Südosten. Der Weg durch die Mitte bleibt als Achse lesbar, nur ohne Wände drumherum — und man
sieht von überall, was es im Safehouse zu holen gibt.

**Einrichtung umgezogen:** die sechs Werkbänke in den Shop (zwei Reihen à drei), die fünf
Kaliberbänke in die Waffenkammer, die vier Podeste standen schon im Pokalraum. Das **Bett** ist
ein Platzhalter-Würfel (220 × 120 × 60) bei (1000, −900). `PlayerStart`, `EntrySpawn`, `ExitDoor`
und der Plattenspieler liegen im Gang.

**Geprüft:** Alle 24 Einrichtungs-Actors liegen im vorgesehenen Raum, keiner außerhalb von ±1440,
Boden misst 3000 × 3000. Dazu ein Screenshot von oben — Räume, Gang und die vier Türöffnungen
sitzen.

**Offen:** Ob das Bett nur Deko ist oder der Einstiegspunkt beim ersten Start wird (Schritt 46,
„Aufwachen im Bett"). Falls ja, gehört der `PlayerStart` ins Schlafzimmer und die Rückkehr aus dem
Run weiterhin an die Tür.

### 7. Was der Nutzer beisteuern muss

Sammelstelle, damit es nicht in den Notizen untergeht. Alles davon kann das Toolset **nicht**
erzeugen:

| Wofür | Was |
|---|---|
| Roter Screen bei wenig HP | Image über den ganzen Canvas in `WBP_HUD`, Name `img_LowHP`, Deckkraft 0, „Is Variable" an |
| SFX Schuss und Treffer | zwei `.wav` unter `Content/Achachay/Art/Audio/` importieren |
| Menü | `WBP_Menu` — Canvas, Titel, Start-Button |
| Tod-Screen | `WBP_DeathScreen` — Canvas, ein paar TextBlocks |
| Endscreen (optional) | `WBP_EndScreen`, falls mehr als die HUD-Zeile gewünscht ist |
| Bett, Pokal-Meshes (optional) | eigene Meshes statt Platzhalter-Primitive |

Die Hüllen reichen — Verdrahtung und Zahlen kommen aus der GI, die dafür nötigen Werte
(`HighestWave`, `TotalKills`, `TotalSeconds`, `RunSeconds`, `Money`, die vier Flags) stehen alle.

### 8. Savegame ✔ (23.09.)

Schritt 12 war am 14.09. auf Wunsch gestrichen und ist am 23.09. auf Wunsch zurückgekommen.

**`SG_Achachay`** (Elternklasse `SaveGame`) hält 17 Felder — alles, was einen Neustart überleben
soll: `Money`, die sechs Upgrade-Level, `CurrentCaliberId` und `UnlockedCalibers`, `HighestWave`,
`TotalKills`, `TotalSeconds`, `BestWaveTime` und die vier Erfolgs-Flags. **Nicht** gespeichert wird
der Run-Zustand (`RunMoney`, `HealCount`, `GrenadeCount`, `MagazineAmmo`, `RunDamage`) — der gehört
zum laufenden Ausflug, nicht zum Fortschritt.

**Gespeichert wird an jeder Stelle, an der sich Bleibendes ändert:** `SpendMoney` (nur bei
erfolgreichem Kauf), `UnlockCaliber`, `BankRunMoney` (Extraktion), `ClearRunState` (Tod),
`NoteWaveCleared` (jede geräumte Welle) und `NoteGameCleared`. Slot heißt `Achachay`, Datei liegt
unter `Saved/SaveGames/Achachay.sav`.

**Geladen wird faul, nicht über `Event Init`.** Erster Anlauf war ein Override von `Event Init` in
der GameInstance — **das war ein Fehler und hat den Editor zweimal blockiert.** Ohne den
`Parent: Init`-Aufruf überspringt so ein Override die Subsystem-Initialisierung, und den
Parent-Knoten kann das Toolset nicht anlegen. Jetzt gibt es `EnsureLoaded()` mit dem Merker
`ProgressLoaded`, gerufen von **`GetPlayerStats`** (die erste Abfrage jedes Characters) und von
**`BP_WaveDirector.BeginPlay`**. Damit ist der Stand geladen, bevor irgendwer ihn liest, und kein
Engine-Event ist angefasst.

**Was den Editor wirklich blockiert hat**, steht als eigene Lektion in `AGENTS.md`: Ein
fehlgeschlagener Blueprint-Compile hält PIE mit einem modalen Dialog an, und dann antwortet kein
MCP-Aufruf mehr. Die Ursache stand im `Saved/Logs/achachay.log`, das sich per Bash auch dann lesen
lässt, wenn der Editor steht.

**Per PIE geprüft, in zwei Läufen:** Lauf A räumt eine leere Testwelle → `Achachay.sav` entsteht
(2413 Bytes, GVAS, Klasse `SG_Achachay_C`). Lauf B startet frisch mit zehn Gegnern, räumt also
nichts — und trotzdem stehen `WaveUnder30`, `WaveUnder10` und `BestWaveTime` **1,0000008** aus
Lauf A. Der Wert kann nur aus der Datei kommen.

### 9. Fehlersuche: Kauf zog Geld ab, ohne zu liefern ✔ (23.09.)

Gemeldet: *„wenn ich ein Kaliber kaufe, geht mein Geld weg, aber ich bekomme das Kaliber nicht."*

**Ursache** war die Pure-Node-Falle in `GI_Achachay.SpendMoney`, eingebaut beim Savegame-Umbau am
selben Tag: Der Rückgabewert `Paid` hing direkt am Vergleich `Geld >= Preis`. Der ist **pure** und
wurde zweimal ausgewertet — einmal für die Verzweigung und ein zweites Mal für den Return,
**nachdem** das Geld abgezogen war. Wer mit 500 $ ein 500-$-Kaliber kauft, bekommt so `0 >= 500`
zurück; `BP_WeaponBench.TryUnlock` sieht `Paid = false` und schaltet nicht frei. Nur wenn nach dem
Kauf noch genug Geld übrig blieb, funktionierte es — deshalb fiel es bei den günstigen Kalibern
nicht auf.

**Behoben** über die Variable `LastSpendOk`: einmal vor dem Abzug gesetzt, der Return liest sie.

**Derselbe Scan fand zwei weitere Stellen** (siehe `AGENTS.md`, „So findet man diese Falle"):

| Funktion | Auswirkung |
|---|---|
| `BP_EnemyBase.ApplyWaveProfile` | `MaxWalkSpeed` wurde aus dem bereits gesetzten `MoveSpeed` **erneut** skaliert und neu gejittert. Auf Welle 10 rannten Gegner dadurch am Deckel (1000) statt bei den geplanten 837 |
| `BP_WaveDirector.SpawnOne` | Der Typwurf wurde zweimal gewürfelt, die zweite Zahl entschied über den Schützen-Zweig — die Mischung wich also von der Tabelle ab |

**Per PIE geprüft:** `MoveSpeed` und `MaxWalkSpeed` stimmen jetzt überein (573–650 bei Basis 620
plus Jitter); vorher liefen sie auseinander. Alle acht betroffenen Blueprints kompilieren sauber.

**Nicht per PIE geprüft:** der Kauf selbst — dafür braucht es eine Interaktion an der Bank.

### 10. Spawnpunkte: Tür statt Kartenmitte, Tod ins Bett ✔ (23.09.)

Zwei Meldungen aus dem Spieltest: *„ich spawne immer noch mitten in der Map, wenn ich aus der Tür
gehe"* und *„wenn ich sterbe, spawne ich nicht im Schlafzimmer."*

**Draußen** stand der `PlayerStart` schlicht bei (0, 0) — mitten in der Arena, weit weg von der
Tür, durch die man gerade gegangen ist. Jetzt auf **(0, −2100)**, direkt vor der Safehouse-Tür
(0, −2400), mit Blick nach Norden ins Areal. Man tritt also aus der Tür und steht davor, statt
unvermittelt in der Mitte.

**Im Safehouse** setzte `PC_Safehouse.PlaceAtEntry` den Spieler nur dann um, wenn er **nicht**
gestorben war — nach einem Tod blieb er auf dem PlayerStart im Gang liegen. Jetzt wählt die
Funktion den Zielpunkt über ein Tag:

| Zustand | Tag | Ort |
|---|---|---|
| lebend zurück (extrahiert) | `EntrySpawn` | (0, 1100), neben der Ausgangstür |
| gestorben | `BedSpawn` | (800, −900), im Schlafzimmer neben dem Bett |

`BedSpawn` ist ein `TargetPoint` mit dem passenden Tag, gebaut wie der vorhandene `EntrySpawn`.
Die Auswahl läuft über ein `select` auf `DiedLastRun` — kein zweiter Codepfad, nur ein anderer Tag.

**Per PIE geprüft:** `DiedLastRun` true → Spieler bei (800, −900); false → (0, 1100); draußen →
(0, −2100) mit Yaw 90.

**Damit ist Schritt 46 zur Hälfte vorweggenommen:** „Aufwachen im Bett" passiert jetzt nach jedem
Tod. Was noch fehlt, ist der Einstieg beim allerersten Start.

### 11. Heilung, Granate, Kisten, Pause, Tracer ✔ (23.09.)

**Heilung.** `BPC_Health.Heal(Amount)` klemmt auf `MaxHealth`. `BP_PlayerCharacter.UseHeal` heilt
**25 % der Maximal-HP** (Variable `HealFraction`, zuerst 50 %, auf Zuruf halbiert), verbraucht eine
Ladung und speichert — aber nur, wenn eine Ladung da ist, der Spieler lebt und er **nicht schon voll**
ist (sonst verschwendet man eine Heilung). Bei 100 HP Grundleben sind das 25 HP, mit Health auf
Stufe 6 (250 HP) 62.

**Granate.** Neuer Actor `BP_Grenade` (Kugel, 30 uu): fliegt in **0,5 s im Bogen** (180 uu hoch)
zum Mauszeiger, zündet nach **1,4 s** und macht **150 Schaden im Radius 450** an jedem
`BP_EnemyBase` — also auch am Boss. Zur Explosion bläht sie sich für 0,15 s auf den Radius auf, damit
man die Wirkfläche sieht. Kills zählen normal (Geld, `TotalKills`), der Spieler selbst nimmt keinen
Schaden. Wurf über `BP_PlayerCharacter.ThrowGrenade`.

**Kisten.** `BP_SupplyBox`, Kind von `BP_InteractStation`, mit `IsGrenade` (statt einer String-ID,
spart den String-Vergleich), `Price` und `MaxCarry`. Zwei Stück neben der Ausgangstür:

| Kiste | Preis | max. |
|---|---|---|
| Heilung | 60 $ | 3 |
| Granate | 80 $ | 3 |

Der Prompt zeigt den Stand: `HEILUNG   1/3   60 $` bzw. `HEILUNG   3/3   voll`.

**Savegame:** `HealCount` und `GrenadeCount` sind jetzt Felder 18 und 19. **Beim Tod verfallen sie
weiterhin** (`ClearRunState`) — das Savegame sorgt nur dafür, dass ein Neustart des Spiels sie
nicht löscht.

**Pause.** Neue Action `IA_Pause` mit `bTriggerWhenPaused`, in `PC_Outside` und `PC_Safehouse` an
`TogglePause` gehängt. **Die Taste fehlt noch** — die Belegung im IMC macht der Nutzer.

**Erster Start im Bett.** `GI_Achachay.WokeUp` (nicht gespeichert): Beim ersten Betreten des
Safehouse **pro Sitzung** geht es an den `BedSpawn`, danach nur noch nach einem Tod. Damit ist
Schritt 46 erledigt.

**Tracer.** Neues Material `M_Tracer` (Unlit, Emission = `Color` × `Glow`, anfangs 6, jetzt 2,5) als Standard am
Projektil, dazu `BP_Projectile.SetLook(Color, Stretch, Thickness)`:

| Wer schießt | Farbe | Form |
|---|---|---|
| Spieler | `ProjectileColor` des Kalibers | **4× gestreckt, halb so dick**, in Flugrichtung gedreht |
| Läufer, Schütze, Rusher | Orange-Rot | rund |
| Boss | Magenta | rund, weiterhin `ShotSize` 1,5 |

Gegnerschüsse bleiben bewusst rund: Spieler- und Gegnerfeuer sind so auf einen Blick unterscheidbar,
und der große Boss-Ball bleibt als Ausweich-Signal lesbar. Farbe pro Gegnertyp über die neue
Variable `ShotColor`.

**Per PIE geprüft:** erster Start → Spieler bei (800, −900). Alle 22 Blueprints kompilieren.
**Nicht geprüft**, weil es Eingaben braucht: Kaufen, Heilen, Werfen, Pausieren, der Tracer-Look.

**Tasten-Konflikt:** `IA_UseHeal` und `IA_NextWave` liegen **beide auf X**. Jedes Heilen würde die
nächste Welle holen. Muss im IMC umgelegt werden.

### 12. Podeste zeigen ihren Pokal ✔ (23.09.)

*„Ich will sehen, was ein Podest für ein Achievement ist, wenn ich davor stehe."* Die Podeste waren
reine Würfel. Jetzt sind es **`BP_TrophyPodium`**, Kind von `BP_InteractStation` — also genau das
Fokus- und Prompt-System der Werkbänke, ohne Änderung am HUD. Davor stehen zeigt:

`POKAL   WELLE UNTER 10 SEKUNDEN   -   noch offen` bzw. `…   -   geschafft`

| Podest | `Label` | `FlagId` |
|---|---|---|
| (900, 300) | BOSS BESIEGT | `GameCleared` |
| (900, 650) | WELLE UNTER 30 SEKUNDEN | `WaveUnder30` |
| (900, 1000) | WELLE UNTER 10 SEKUNDEN | `WaveUnder10` |
| (900, 1350) | DURCHGESPIELT OHNE TREFFER | `NoHitClear` |

Interagieren (E) tut an einem Podest nichts — `OnInteract` der Basis ist leer.

**Ein Fund dabei:** Das Stations-Mesh `DoorMesh` sitzt in `BP_InteractStation` **150 uu über dem
Boden** (Würfel mittig, bei `MeshScale` z 1,0 also von 100 bis 200). **Alle** Stationen schweben
damit — Werkbänke, Waffenbänke, Kisten. Für die Podeste im Construction Script auf 40 gesetzt
(Podest von 0 bis 80, Pokal bei z 115 genau obendrauf). Eine Änderung am Instanz-Komponent hält
nicht: Der Construction Script baut geerbte Komponenten bei jedem Durchlauf neu auf den Klassenwert.

**Geprüft:** alle vier Podeste bei `DoorMesh` z 40, Screenshot von der Seite. **Nicht per PIE
geprüft:** der Prompt selbst — `PlaceAtEntry` setzt den Spieler beim Start immer an Bett oder Tür,
ein Start neben den Podesten lässt sich nicht erzwingen. Der Weg ist aber derselbe wie bei den
Werkbänken.

**Nachtrag Tracer (23.09.): Kugeln waren weiß.** Hauptgrund: `SetLook` hing in `SpawnShot` an
einer toten Kopie der Schussschleife und lief nie (umgehängt, Kopie gelöscht). Dazu: Die Kaliberfarben waren blass
(6 mm und 9 mm fast weiß), und `Glow` 6 hat jede Farbe in der Tonwertkurve zu Weiß ausgebrannt.
Jetzt `Glow` 2,5 und kräftige Farben, eine pro Kaliber — bewusst ohne Rot und Magenta, die gehören
den Gegnern:

| Kaliber | Farbe |
|---|---|
| 6 mm | Gelb (1 / 0,8 / 0) |
| 9 mm | Grün (0,2 / 1 / 0,1) |
| .45 ACP | Cyan (0 / 0,75 / 1) |
| 7,62×39 | Blau (0,1 / 0,3 / 1) |
| .44 Magnum | Orange (1 / 0,45 / 0) |
| .50 BMG | Violett (0,65 / 0,15 / 1) |

### 13. Licht und Stimmung ✔ erster Pass (23.09.)

Auf Zuruf: *„Safehouse gedimmter, warmes angenehmes Licht. Außen dunkel, kalt, windig, Schnee,
leichtes Flackern, Nebel."*

**Draußen — kalte Nacht.**
- Mond statt Sonne: Directional Light **1,0** (war 6), kaltblau (0,55 / 0,65 / 1,0)
- Himmelslicht **0,35**, kaltblau; Volumetric Cloud entfernt
- Nebel dichter (0,06), kalt, **volumetrisch** — sichtbar vor allem als Dunst um die Lampen
- `PostProcess_Night` (unbegrenzt): **feste Belichtung** (EV 0,5 min = max, sonst hellt die
  Auto-Belichtung die Nacht wieder auf), kalter Farbstich, Sättigung 0,85, Vignette 0,6, leichtes Korn
- **Lampen** (`BP_FlickerLight`): eine **warme über der Safehouse-Tür** — die Wärme zeigt den Weg nach
  Hause —, dazu vier kalte Flutlichter am Rand, zwei davon flackern. Die Mitte bleibt bewusst dunkel.

**Drinnen — warm und gedimmt.**
- Mond 0,15, Himmelslicht 0,15, Nebel fast weg (0,01), Wolken entfernt
- Sechs warme Lampen (~2700 K): eine pro Zone, dazu Eingang und Mitte. Bett- und Eingangslampe
  **schimmern leicht wie Kerzenlicht** (Flackern an, aber `DipChance` 0 — keine Aussetzer)
- `PostProcess_Warm`: feste Belichtung, warmer Farbstich, Vignette 0,5

**`BP_FlickerLight`** (Elternklasse `PointLight`): Timer alle 0,08 s, meist 92–100 % Helligkeit,
mit `DipChance` Einbruch auf 15–55 %. `BaseIntensity`, `DipChance`, `FlickerInterval`, `Flickers`
sind pro Instanz einstellbar.

**Gegner-Glow (23.09.)** — damit man sie auf der dunklen Karte sieht:
- Neues Material `M_Enemy` am `Body` von `BP_EnemyBase` (gilt für alle Gegner inkl. Boss):
  dunkelroter Körper (`BodyColor`), Emission = `GlowColor` × (Fresnel × `Glow` 2,0 + `BaseGlow` 0,15)
  — die Kanten leuchten, die Flächen glimmen leicht. Alles Parameter, also per Material Instance
  pro Gegnertyp umfärbbar.
- Neue Komponente `Glow` (PointLight) in `BP_EnemyBase`: rot, 1500 (unitless), Radius 380,
  **ohne Schatten**, 40 cm über dem Boden — wirft einen roten Schein um jeden Gegner. Bei ~70
  Gegnern gleichzeitig sind das ~70 kleine Lichter; ohne Schatten sollte das tragbar sein, falls es
  ruckelt, ist das die erste Stellschraube.

**Was nicht geht bzw. weggelassen wurde:**
- **Schnee und Wind** brauchen ein Partikelsystem (Niagara) — kann das Toolset nicht anlegen.
  Importiert oder angelegt vom Nutzer, wird es platziert und abgestimmt.
- **Sterne als Skybox:** weggelassen. Die Kamera schaut fast senkrecht nach unten, der Himmel ist
  im Spiel nie im Bild.

**Eine Falle beim Setzen:** Lichtfarben erwartet das Toolset als **0…1**, nicht als 0…255. Werte
über 1 wurden verworfen, nicht übernommen — also kein Schaden, aber auch keine Wirkung.

**Geprüft** per Screenshot aus dem laufenden Spiel (drinnen und draußen). Die Editor-Ansicht
taugt dafür nicht: Die **NavMesh-Anzeige** legt sich grün über den Boden (im Viewport mit **P**
umschaltbar, per Toolset nicht). **Vorsicht bei Tests:** PIE läuft gegen den echten Spielstand des
Nutzers — draußen nur kurz testen, sonst stirbt der Spieler und verliert gekaufte Heilungen.

### 14. Dash: Sprint statt Teleport ✔ (23.09.)

Auf Zuruf: *„Mein Dash ist mir zu schnell … nicht teleportieren, sondern eher zum Punkt sprinten."*

Vorher setzte `StartDash` den Spieler per `SetActorLocation` direkt ans Ziel (mit Rückwärts-Suche
nach einem freien Platz). Jetzt:
- `StartDash` legt nur Richtung, Stamina und `DashEndTime` fest und setzt `IsDashing`
- **`UpdateDash(DeltaSeconds)`** (neu, am Ende von `EventTick`): solange `IsDashing`, schiebt es
  den Spieler jeden Frame um `DashDistance / DashDuration × DeltaSeconds` weiter — **mit Sweep**, also
  stoppen Wände und Gegner wie beim Laufen. Die normale Geschwindigkeit wird dabei auf 0 gehalten.
  Am Ende: Austrittsgeschwindigkeit `DashExitSpeed` in Dash-Richtung.
- Werte (am Character einstellbar): `DashDistance` 600 (war 650), **`DashDuration` 0,25 s**
  (→ 2400 u/s), `DashExitSpeed` 1200 wie vorher. Zu schnell → `DashDuration` hoch; zu weit → `DashDistance` runter.
- `DashTarget` wird nicht mehr benutzt.

### 15. Upgrade „Laser" ✔ (23.09.)

Auf Zuruf: *„Upgrade namens Laser, kostet 1000, dann bekommt man immer einen Laser bis zur Maus bzw.
Controller-Aim. Weniger Spread beim Schießen. Soll rot leuchten."*

- **Kauf:** dritte Kiste im Safehouse, `SupplyBox_Laser` bei (450, 650) neben Heilung und Granaten.
  `BP_SupplyBox` hat dafür den neuen Schalter **`IsLaser`**: `TryBuy` kauft dann einmalig
  (`SpendMoney(Price)` → `HasLaser` = true → speichern), `BuildLaserPrompt(Normal)` zeigt
  „LASER - Ziellicht, halbe Streuung   1000 $" bzw. „LASER   installiert". `GetPrompt` läuft
  jetzt `BuildPrompt` → `BuildLaserPrompt` → Rückgabe; bei Heilung/Granate reicht `BuildLaserPrompt`
  den normalen Text durch.
- **Gespeichert:** `HasLaser` in `GI_Achachay` und `SG_Achachay`, in `SaveProgress`/`LoadProgress`
  ergänzt. Alte Spielstände ohne das Feld laden als „kein Laser".
- **Streuung:** `BP_Weapon.SpawnShot` multipliziert den Kaliber-Spread mit **`LaserSpreadMul` 0,5**,
  wenn `HasLaser`.
- **Sichtbarer Laser:** Die alte Debug-Linie (`DrawDebugLine`, im fertigen Spiel unsichtbar) ist
  raus. Neu: Komponente `LaserBeam` am Spieler (Zylinder, `M_Laser` unlit, rot × `Glow` 2,5, keine
  Kollision, kein Schatten). `DrawAimLaser` streckt ihn jeden Frame von 70 cm vor dem Spieler bis
  in Zielrichtung, **immer `AimLaserLength` = 4000 lang** (bis über den Bildschirmrand; Nutzerwunsch
  23.09. — bis zum Mauspunkt sah es komisch aus). Die Maus gibt nur die Richtung vor, mit Gamepad
  die Blickrichtung. Ohne Laser
  unsichtbar. Dicke `LaserThickness` 0,06 (= 6 cm).
- **Noch nicht:** Der Strahl endet nicht an Wänden oder Gegnern, sondern am Zielpunkt.

### Aufräumen vor dem Build (Review, 25.09.)

Workarounds aus dem Abgabe-Pass, die im Editor sauberer gehen. Vor dem Package-Build durchgehen.

| Wo | Jetzt | Sauber |
|---|---|---|
| `BP_EnemyBoss` | `ApplyBossLook` setzt `M_Enemy` + Farben zur Laufzeit, weil das geerbte `Body`-Override das Material verliert und das Toolset Komponenten-Overrides nicht schreiben kann | Im Boss-BP die geerbte `Body`-Komponente wählen und das Material direkt setzen (am besten eine `MI_Boss` von `M_Enemy` mit den Farben). Danach `ApplyBossLook` samt Aufruf löschen |
| `WBP_Settings` | `SyncSliders` liest alle drei Slider **jeden Tick** und ruft `ApplyVolume`. Grund: `Create Event` braucht eine `float`-Signatur, das Toolset legt nur `double` an | Pro Slider im Designer *Events → On Value Changed* (+). Im Event `Set<Master/Music/Sfx>Volume` an der GI + `ApplyVolume`. Danach `SyncSliders` und den Tick-Aufruf löschen |
| `M_Blue` | Heißt noch „Blue", ist aber seit 25.09. der Stations-Look (Stahl + Bernstein-Rand) | Umbenennen in `M_Station` (Rechtsklick → Rename), danach *Fix Up Redirectors* im Ordner |
| `PC_Outside` / `PC_Safehouse` | Beide haben eigene Kopien von `AddMappingContext`, `StoreEssentialVariables`, `ShowHUD`, `TogglePause` und der Einblende. `PC_Outside` ruft sogar `Class|PCSafehouse|ShowHUD` | Gemeinsame Elternklasse `PC_Achachay` (BP von PlayerController), beide per *File → Reparent Blueprint* darauf, die doppelten Funktionen in die Elternklasse. Optional, eher Phase B |

**Per Toolset erledigbar (Scan vom 25.09.):**

| Wo | Befund | Maßnahme |
|---|---|---|
| `BP_PlayerCharacter.DebugOverlay` | 44 Knoten, baut **jeden Frame** einen String und schreibt ihn per PrintString — der Grund für die Log-Flut (Hunderttausende Zeilen) | Aufruf im Tick entfernen, Funktion löschen |
| `PC_Outside.AddMappingContext` | `PrintString "Added"` | Knoten entfernen |
| `BP_PlayerCharacter.EquipWeapon` | `PrintString` im Fehlerzweig | Darf bleiben (wird im Shipping-Build ohnehin entfernt) |
| `BP_EnemyBase.ApplyWaveScaling` | 31 Knoten, seit 22.09. von `ApplyWaveProfile` ersetzt, **nirgends aufgerufen** | Funktion löschen |
| `BP_WaveDirector` | 10 Variablen der alten Formel (`BaseCount`, `CountPerWave`, `NextWaveDelay`, `HealthPerWave`, `SpeedPerWave`, `ShooterStartWave`, `ShooterEvery`, `RusherStartWave`, `RusherEvery`, `RewardMulPerWave`) — **nirgends gelesen** | Variablen löschen |
| `BP_WaveDirector.StartWave` | `GetDataTableRow` wird **27×** ausgewertet (Pure-Node-Neuauswertung, §3 AGENTS.md), größter Graph im Projekt | Zeile einmal in eine `S_WaveRow`-Variable lesen, danach nur noch deren Felder. Spart grob die Hälfte der Knoten |
| `BP_Grenade.Explode` | Abstand zu Hand aus x/y-Differenzen gerechnet (Pure-Kette mit 8× `GetActorLocation`) | `GetHorizontalDistanceTo` — ein Knoten |
| `BP_PlayerCharacter.HandleDeath` | Zweig „Is Not Valid" dupliziert den Timer, die GI ist immer gültig | Zweig entfernen |
| `L_Outside` | `BP_TestTarget` (Übungspuppe vom 15.09.) steht noch im Level | Aus dem Level löschen; Asset und `BP_TestInteractable` danach löschen, wenn nichts mehr darauf zeigt |

**Phase B (zu groß für heute):** `GI_Achachay.GetUpgradeLevel`/`RaiseUpgradeLevel` (48 + 64 Knoten, sechsfache
`if`-Kette über Namen) → eine `Map<Name,int> UpgradeLevels`. Berührt das Savegame, deshalb nicht vor der Abgabe.

### Phase B — nach der Abgabe

Nach Aufwand sortiert, nicht nach Reiz:

| # | Thema | Notiz |
|---|---|---|
| ~~B1~~ | ~~**Savegame**~~ | **Erledigt am 23.09.**, siehe Schritt 8 |
| B2 | **Tank-Gegnertyp** | Kindklasse mit hoher HP, niedrigem Tempo, eigenen Skalierungsfaktoren. Eine Spalte in `DT_Waves` dazu, sonst nichts — das ist der billigste Punkt der Liste |
| B3 | ~~**Run-Stats & Achievements**~~ | **Datenebene am 23.09. erledigt** (Schritt 4). Offen ist nur noch die Anzeige: Pokalraum, Schritt 5 |
| B4 | **Meshes und Map** | Der Punkt mit dem größten sichtbaren Effekt — und der einzige, der die Graybox wirklich ersetzt |
| B5 | **Animationen** | ⚠ **Der Spieler nutzt derzeit ein StaticMesh**, kein Skeletal Mesh (`AGENTS.md` §2). Animationen heißen also: Mesh tauschen, Animation Blueprint bauen, Bewegungslogik nachziehen. Das ist der teuerste Posten der Liste, nicht der dekorativste |
| B6 | **Shader & Post Processing** | Zuletzt, weil es auf allem anderen aufsetzt. Post-Process-Volume, Bloom/Tonemapping, Outline für Gegner |

**Reihenfolge-Argument für B1 zuerst:** Ohne Savegame ist jeder Test ab Welle 5 ein Neuaufbau von
Hand. Alles danach wird billiger, wenn es zuerst kommt.

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
- **Fünf Deckungen** — am 15.09. entfernt (ohne Pathfinding blieben die Gegner daran hängen, womit
  die Deckungen *schlechter* waren als keine), **am 17.09. wieder gesetzt**, nachdem `AI MoveTo`
  läuft. Würfel 6×2×2 bzw. 5×2×2 bei (1200, 900), (−1300, 1400), (−1600, −1200),
  (1500, −1500) und (300, −2200) — Outliner-Ordner `Graybox/Cover`.
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

### 24a. HUD-Ausbau: Run-Infos ✔ (23.09.)

Das HUD soll neben Leben/Geld/Waffe auch den Zustand des Laufs zeigen: **Ort, höchste Welle,
Gesamt-Kills, Gesamtzeit seit Spielstart, Zeit im laufenden Outside-Run und die Upgrade-Stufen.**

**Fertig — die Datenseite in `GI_Achachay`:**

| Neu | Zweck |
|---|---|
| `HighestWave`, `TotalKills` | überleben den Tod, werden nie zurückgesetzt |
| `TotalSeconds`, `RunSeconds`, `LastClockSample` | die beiden Uhren |
| `NoteWave(Wave)` | zieht `HighestWave` nach — gerufen in `StartWave` |
| `NoteKill()` | zählt hoch — gerufen in `BP_EnemyBase.PayoutAndDie` |
| `ResetRunClock()` | nullt `RunSeconds` — gerufen in `BP_WaveDirector.BeginPlay` |
| `UpdateClock(Now, CountRun)` | addiert die vergangene Zeit; **noch nicht gerufen**, das macht das HUD |
| `FormatTime(Seconds) → String` | `mm:ss` |
| `GetUpgradeSummary() → String` | `SPD 3  HP 2  ARM 0  DMG 4  STA 1  RLD 5` |

**Warum die Uhr so gebaut ist.** `GetGameTimeInSeconds` fängt bei jedem `OpenLevel` wieder bei 0 an,
eine Gesamtzeit kann also nicht einfach abgelesen werden. `UpdateClock` addiert stattdessen die
Differenz zum letzten Aufruf und **verwirft Sprünge über 1 Sekunde oder rückwärts** — genau das
passiert beim Levelwechsel. Kostet höchstens ein Aktualisierungsintervall pro Wechsel und braucht
dafür keinen einzigen Hook in den drei Levelwechsel-Pfaden.

`BP_WaveDirector` hat dafür eine gecachte `GI`-Referenz bekommen (in `BeginPlay` gesetzt). Grund:
Ein Cast-Node **beendet den umgebenden Exec-Fluss** — hätte `StartWave` selbst gecastet, wäre die
halbe Funktion in den `then`-Zweig gewandert.

**Die sechs Textblöcke hat der Nutzer angelegt** — `TextBlock` ist kein `ActorComponent`, und ein
Widget-Toolset gibt es nicht, das Toolset kann in `WBP_HUD` also nichts erzeugen (an einer
Wegwerf-Kopie geprüft, nicht am Original): `t_Location`, `t_HighestWave`, `t_Kills`,
`t_TimeTotal`, `t_TimeRun`, `t_Stats`.

**Angeschlossen in drei Funktionen**, weil der Textsetzer nicht per DSL schreibbar ist:

| Funktion | Was |
|---|---|
| `TickClock(GameInst, Dir)` | ruft `GI.UpdateClock`; `Dir` gültig = draußen = die Run-Uhr läuft mit |
| `BuildRunInfoStrings(GameInst, Player)` | baut die sechs Strings in die Hilfsvariablen `TxtLocation` … `TxtStats` |
| `ApplyRunInfoTexts()` | schreibt sie in die Blöcke |

Alle drei hängen hinten an `RefreshHUD`, also im selben Tick-Takt wie der Rest des HUDs.

**Warum die Dreiteilung:** `Widget|SetText(Text)` und `Utilities|Text|ToText(String)` tragen
**Klammern im Type-Id** und brechen damit den DSL-Parser. `create_node` nimmt sie dagegen
anstandslos — die Klammer-Einschränkung gilt nur für den DSL. Also: Strings per DSL bauen
(lesbar, schnell), die zwölf Setz-Nodes per `create_node` + `connect_pins` verdrahten.
`RefreshHUD` selbst wurde **nicht** neu geschrieben, sondern nur hinten erweitert — die Funktion
enthält genau solche Klammer-Nodes, ein Neuschreiben hätte sie zerstört.

**`t_Location` zeigt bewusst beides**, Levelname und Koordinaten (`L_Outside   1240 / -320`), weil
„location" beides heißen kann.

**Per PIE geprüft:** Nach einer Sekunde im Outside-Run stehen `TotalSeconds` **1,00** und
`RunSeconds` **1,00** (beide laufen draußen mit), `HighestWave` 1. Die Uhr tickt also über
`RefreshHUD` → `TickClock` → `UpdateClock`, wie gebaut.

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

**Kill-Reward skaliert mit der Welle (18.09.).** Ein Dollar pro Kill blieb ein Dollar, egal ob
Welle 1 oder Welle 10 — während die Gegner dreimal so viel HP hatten. `BP_EnemyBase` hat dafür
einen `RewardMultiplier` bekommen, den `BP_WaveDirector.SetupEnemy` beim Spawn setzt:

`Multiplikator = 1 + (Welle − 1) × RewardMulPerWave`, mit **`RewardMulPerWave` = 5,5**.

`PayoutAndDie` zahlt `Truncate(KillReward × Multiplikator)`. Die Basiswerte pro Typ bleiben, was
sie waren — Läufer 1, Schütze 3, Rusher 4 — und werden mitskaliert.

| Welle | Mult. | Läufer | Schütze | Rusher | Gegner | Wellen-Ertrag |
|---|---|---|---|---|---|---|
| 1 | 1,0 | 1 | — | — | 3 | 3 |
| 3 | 12,0 | 12 | — | — | 7 | 84 |
| 5 | 23,0 | 23 | 69 | — | 11 | 299 |
| 7 | 34,0 | 34 | 102 | — | 15 | 646 |
| 9 | 45,0 | 45 | 135 | — | 19 | 1125 |
| **10** | **50,5** | **50** | 151 | 202 | 21 | 1505 |

Die 5,5 sind so gewählt, dass ein Läufer auf **Welle 10 genau 50 $** bringt — der Punkt, an dem man
stark genug für den Boss sein soll.

**Per PIE geprüft:** Welle 1 → `RewardMultiplier` 1,0. Welle 10 → 50,5, Zusammensetzung
17 Läufer + 3 Schützen + 1 Rusher.

**Zwei Zahlen, die dadurch nicht mehr zusammenpassen:**

1. **Ein voller Zehn-Wellen-Run bringt rund 5100 $**, die Gesamtsenke liegt bei 7180 $. Wer einmal
   bis Welle 10 kommt, kauft danach fast alles. Der Plan will aber „Welle 10 fällt erst im vierten
   bis fünften Run" — das trägt nur, solange Welle 10 früh **unerreichbar** ist. Sobald das
   Wellenende bei 10 steht (Schritt 37/43), gehört das nachgerechnet.
2. **Der Extraktionsbonus** ist mit `Welle × 10` stehengeblieben: Welle 10 zahlt dafür 100 — also
   zwei Kills. Das entwertet den Rückweg gegenüber „noch einen mitnehmen". `BonusPerWave` sollte
   mitwachsen.

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

### 29. Sofort weitermachen ✓ teilweise (18.09.)

- Eine Taste, die das Fenster vorzeitig beendet und die nächste Welle startet

**Probe:** Restzeit lässt sich überspringen.

**Gebaut am 18.09. — breiter als geplant.** Die Taste beendet nicht nur das Rückwegfenster, sie
startet die nächste Welle **jederzeit**, auch mitten im Kampf. Wellen stapeln sich dann.

`BP_WaveDirector.ForceNextWave` löscht den laufenden `StartWave`-Timer (sonst gäbe es eine
Doppelwelle, wenn man während des Fensters drückt) und ruft `StartWave` direkt. Das setzt
`ExtractionOpen` ohnehin zurück — das Fenster ist damit weg. `PC_Outside.TriggerNextWave` sucht den
Director und ruft die Funktion; gebunden an `IA_NextWave`, Ausgang **`Started`** (feuert genau
einmal pro Druck, unabhängig davon, welcher Trigger in der IMC steht).

**Warum das mehr ist als ein Skip:** Eine Welle dazuzuholen, während die alte noch lebt, ist eine
echte Entscheidung — mehr Geld pro Zeit gegen mehr Gegner gleichzeitig. Das Rückwegfenster
verschwindet dabei, also kostet es auch die Extraktion. Genau die Spannung, die der Plan mit den
„neun Rückweg-Fenstern = zwei Minuten Stehzeit" beschreibt.

**Per PIE geprüft** (über einen temporären Timer statt Tastendruck, weil PIE keine Eingaben
annimmt): Nach `ForceNextWave` stehen **8 Gegner statt 3** — Welle 1 (3) lebt weiter, Welle 2 (5)
kommt dazu. Timer danach entfernt.

**Offen: die Tastenbelegung.** `IA_NextWave` ist angelegt und verdrahtet, aber die Zuordnung zu
einer Taste fehlt — `IMC_Gameplay.Mappings` lässt sich per MCP nicht lesen und damit auch nicht
gefahrlos schreiben (die Eigenschaft liest als leeres Array zurück, obwohl alle Mappings da sind).
Muss von Hand in die IMC.

**Zu bedenken beim Testen:** Ein Druck während des Fensters kostet die Extraktion sofort, ohne
Rückfrage. Falls sich das zu scharf anfühlt, macht ein **Hold-Trigger** (0,4 s) in der IMC daraus
eine bewusste Geste — eine Zeile in derselben Maske, kein Umbau.

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

### 32a. `BP_InteractStation` — gemeinsame Basis der Stationen ✔ (16.09.)

Alle drei Safehouse-Stationen brauchen dasselbe: ein Interface, einen Würfel, eine GameInstance-
Referenz. Statt das dreimal zu bauen, gibt es jetzt eine Basisklasse unter `Core/`.

**Warum als Duplikat entstanden:** Ein Blueprint-Interface lässt sich per MCP **nicht** hinzufügen —
`ImplementedInterfaces` ist über `ObjectTools` nicht schreibbar. `BP_InteractStation` ist deshalb
eine **Kopie von `BP_SafehouseDoor`** (das die Schnittstelle schon hatte), von der die Extraktions-
Logik entfernt wurde. Kinder erben die Schnittstelle mit.

**Wie Kinder ihr Verhalten einhängen:** Die Basis fängt `EventInteract` ab und ruft `OnInteract` —
eine leere Funktion ohne Rückgabewert. Weil sie keine Ausgänge hat, behandelt Unreal sie als
*event-shape function*: Kinder überschreiben sie **nicht als Funktionsgraph**, sondern als
Event-Node (`add_event`, nicht `add_function_graph` — letzteres wird abgewiesen).

Dazu `Label`, `MeshScale`, `GI` und ein `LabelText` (TextRender). `ApplyLook` läuft im
**Konstruktionsskript**, damit Größe und Beschriftung schon im Editor stimmen und nicht erst bei
BeginPlay.

**Grenze, die dabei auffiel:** `SetRelativeLocation`/`SetRelativeRotation` auf eine
SCS-Komponente wirken im Konstruktionsskript **nicht** — bereits platzierte Instanzen haben eigene
serialisierte Transformwerte, die danach wieder gewinnen. `SetRelativeScale3D`, `SetWorldSize` und
`SetText` greifen dagegen. Transform-Änderungen gehören also ans Komponenten-Template **vor** dem
ersten Platzieren.

### 33. Waffenbank — Kaliber freischalten ✔ (16.09.)

- Actor mit `BPI_Interactable`, referenziert ein `CaliberData`
- Interagieren schaltet das Kaliber **einmalig** frei und zieht `UnlockPrice` ab
- Drei Zustände sichtbar: freischaltbar, zu teuer, bereits freigeschaltet
- Die ID landet in `UnlockedCalibers` in der GameInstance

**Probe:** Freischalten zieht Geld ab, das Kaliber taucht im Q-Kreis auf und die Station ist danach
erledigt.

**Gebaut am 16.09.** `BP_WeaponBench` unter `Safehouse/`, Kind von `BP_InteractStation`. Eine
Instanz pro Kaliber, das `Caliber`-Feld zeigt auf das `CaliberData`. `TryUnlock` prüft
`IsCaliberUnlocked`, ruft `GI.SpendMoney(UnlockPrice)` und bei Erfolg `GI.UnlockCaliber`.

`CaliberData` hat dafür ein **`UnlockPrice`** bekommen, gesetzt nach der Preistabelle: 6mm 0,
9mm 60, .45 ACP 120, 7.62×39 200, .44 Magnum 300, .50 BMG 500.

**`UnlockedCalibers` steht wieder auf nur `6mm`** — die Testdaten (6mm, 9mm, .50 BMG) aus Schritt 18
sind raus, jetzt wo man sie regulär kaufen kann.

**Offen:** Die drei sichtbaren Zustände. Momentan passiert bei „zu teuer" und „schon gekauft"
einfach nichts. Gehört zum HUD-Pass.

### 34. Werkbank ✔ (16.09.)

- Interagierbarer Actor für Speed, Armor und Health
- Preis steigt pro Stufe, Level landen in der GameInstance

**Probe:** Ein Upgrade kaufen und den Unterschied draußen sofort spüren.

**Gebaut am 16.09.** `BP_Workbench`, Kind von `BP_InteractStation`, **eine Instanz pro Upgrade**
(`UpgradeId` = `Speed` / `Armor` / `Health`). Das folgt derselben Regel wie die Waffenbank:
kein Shop-Bildschirm, wer bezahlen kann, kauft.

Preis: `BasePrice + Stufe × PriceStep` = **80, 140, 200, 260, 320**, `MaxLevel` 5. Bei rund 1 $ pro
Kill und 150–250 $ aus einem guten Run ist das früh eine Stufe pro Run, später mehrere Runs.

**Von drei auf sechs Upgrades erweitert (16.09.).** Die „Festgelegt"-Zeile sagte *genau drei*; das
gilt nicht mehr. Grund: Nach den Kaliber-Freischaltungen gab es **keine Schadensschraube mehr** —
und genau die braucht man gegen Rusher mit wachsender HP.

| Upgrade | Pro Stufe | Stufe 5 | Wirkt auf |
|---|---|---|---|
| Speed | +60 uu/s | 1100 | `GetPlayerStats` → `ApplyPlayerStats` |
| Health | +25 HP | 225 | `GetPlayerStats` → `InitHealthFromStats` |
| Armor | +6 % | 30 % | `GetPlayerStats` → `BPC_Health.ArmorReduction` |
| **Damage** | +8 % | **+40 %** | `GI.GetDamageMultiplier` in `BP_Weapon.SpawnShot` |
| **Stamina** | +25 max, +5 Regen | 225 / 50 | `GetPlayerStats` |
| **Reload** | −10 % | **−50 %** | `GI.GetReloadMultiplier` in `BP_Weapon.StartReload` |

Sechs Upgrades × 1000 $ voll ausgebaut plus 1180 $ für alle Kaliber = **7180 $** Gesamtsenke.
(Am 22.09. auf 9080 $ gestiegen, siehe Schritt 34a.)

**Reload ist der wacklige Posten.** Der Plan nennt Magazin und Nachladen „der alleinige Taktgeber
und die eigentliche Kostenseite eines starken Kalibers" — ein −50-%-Upgrade weicht genau das auf.
`.50 BMG` fällt damit von 3,2 s auf 1,6 s. Bewusst so entschieden; `GetReloadMultiplier` klemmt bei
0,5 ab, damit es nicht weiter rutschen kann. **Bei Gate 2 zuerst hier hinschauen.**

Die GameInstance hat dafür drei neue Funktionen: `SpendMoney(Amount) → Paid`,
`GetUpgradeLevel(UpgradeId)` und `RaiseUpgradeLevel(UpgradeId)`. Damit liegt die Geldlogik an
**einer** Stelle statt in jeder Station.

**Der Kauf wirkt sofort.** `BP_PlayerCharacter.RefreshStats` holt die Stats neu aus der GI und ruft
`ApplyPlayerStats` + `InitHealthFromStats` — dieselbe Kette wie in `BeginPlay`. Ohne das würde man
den Unterschied erst nach dem nächsten Levelwechsel merken, und genau daran hängt Gate 2.

### 34a. Werkbank bis Stufe 6 ✔ (22.09.)

`MaxLevel` von 5 auf **6** — eine Stufe mehr Luft nach oben, weil die Wellen nach dem Tempo-Pass
deutlich härter sind. Der Preis der letzten Stufe ist `80 + 5 × 60` = **380 $**, ein voll
ausgebautes Upgrade kostet damit **1380 $** statt 1000.

| Upgrade | Pro Stufe | Stufe 5 (alt) | **Stufe 6 (neu)** |
|---|---|---|---|
| Speed | +60 uu/s | 1100 | **1160** |
| Health | +25 HP | 225 | **250** |
| Armor | +6 % | 30 % | **36 %** |
| Damage | +8 % | +40 % | **+48 %** |
| Stamina | +25 max, +5 Regen | 225 / 50 | **250 / 55** |
| Reload | −10 % | −50 % | *bleibt bei 5* |

**Reload steht bewusst weiter auf `MaxLevel` 5.** `GetReloadMultiplier` klemmt bei **0,5** ab, und
Stufe 5 erreicht diese Kappe exakt — eine sechste Stufe würde 380 $ kosten und **nichts** bewirken.
Statt einen Fehlkauf zu verkaufen, zeigt die Station weiter „RELOAD max". Wer Stufe 6 auch hier
will, lockert die Kappe in `GI_Achachay.GetReloadMultiplier` (0,5 → 0,45); das ist genau die
Schraube, vor der Schritt 34 warnt, deshalb nicht ungefragt.

**Gesamtsenke steigt auf 9080 $** (5 × 1380 + 1000 für Reload + 1180 für alle Kaliber, vorher
7180 $). Zusammen mit den höheren Kill-Prämien aus den größeren Wellen gehört beides in einem Zug
nachgerechnet, sobald das Wellenende steht — siehe Schritt 44.

### 35. Ausgangstür im Safehouse ✔ (16.09.)

- Interagierbar, startet einen neuen Run in `L_Outside` bei Welle 1

**Probe:** Der komplette Kreis läuft: raus, kämpfen, rein, kaufen, wieder raus.

**Gebaut am 16.09.** `BP_ExitDoor`, Kind von `BP_InteractStation`, bei (1400, 0). `LeaveSafehouse`
bucht vorsichtshalber `BankRunMoney` (falls noch Run-Geld herumliegt) und lädt `L_Outside`.

**Aufbau des Safehouse (16.09.):** Tür **rechts** bei (0, 1400) — die Kamera steht mit Yaw 0, also
ist +X oben und +Y rechts. Werkbänke in zwei Reihen: Speed / Armor / Health bei x = −1400
(y = −500 / 0 / +500), Damage / Stamina / Reload bei x = −900 (gleiche y). Die fünf
Kaliber-Stationen bei y = −1400 (x = −1000 bis +1000). Abstand 500 uu, damit bei `InteractRange`
250 immer nur eine Station im Fokus ist. Die beiden Test-Würfel aus der Raummitte sind raus.

**Zwei Spawnpunkte, je nach Grund der Rückkehr (16.09.):**

| Ankunft | Wo | Warum |
|---|---|---|
| Extraktion | direkt neben der Tür, (0, 1100) | Du kommst zur Tür herein, nicht in die Raummitte |
| Tod | Raummitte, (0, 0) | Du wachst im Safehouse auf, nicht an der Tür |

Getragen von `GI_Achachay.DiedLastRun`: `ClearRunState` (Tod) setzt es auf **true**,
`BankRunMoney` (Extraktion und Verlassen) auf **false**; Startwert true, damit der allererste
Spielstart in der Mitte beginnt. `PC_Safehouse.PlaceAtEntry` läuft im `BeginPlay` und setzt den
Pawn auf den Actor mit dem Tag `EntrySpawn`, **wenn** nicht gestorben wurde. Sonst bleibt der
PlayerStart in der Mitte stehen.

**Per PIE geprüft:** `DiedLastRun` false → Spieler bei (0, 1100) mit Blick in den Raum;
`DiedLastRun` true → (0, 0).

**Stationsbeschriftung, dritter Anlauf (18.09.).** Erst TextRender über jeder Station, dann der
Name im HUD-Prompt, dann beides raus — und jetzt zeigt der Prompt **was die Interaktion tut, mit
Preis**. Kein Widerspruch zum früheren „einfach nur ein Interact": das galt, als es noch keine
Läden gab. Vor einem Kauf muss man wissen, was er kostet.

Getragen von `BP_InteractStation.GetPrompt() → String`, das jede Kindklasse überschreibt:

| Station | Prompt |
|---|---|
| Werkbank | `SPEED   Stufe 3   200 $` bzw. `SPEED   max` |
| Waffenbank | `.50 BMG  freischalten   500 $` bzw. `.50 BMG   schon frei` |
| Ausgangstür | `Rausgehen  -  neuer Run` |
| Safehouse-Tür (draußen) | `Extrahieren   +120 $` bzw. `Tuer zu  -  Welle laeuft` |

`WBP_HUD.GetPromptText` castet das fokussierte Interactable auf `BP_InteractStation`, sonst auf
`BP_SafehouseDoor`, sonst bleibt es beim nackten „Interact" — alles andere im Spiel behält also den
schlichten Prompt. Die Preise sind aus den `Label`-Werten raus, die stehen jetzt im Prompt.

**Funktionen *mit* Rückgabewert lassen sich als Funktionsgraph überschreiben** (`add_function_graph`
im Kind erzeugt einen Override mit Parent-Call). Nur Funktionen **ohne** Ausgabe sind
„event-shape" und brauchen `add_event` — siehe `OnInteract` unter 32a.

**Dabei erneut in dieselbe Falle getappt:** `GetPrompt` ist impure, und
**`(return (impure-call))` führt den Aufruf nie aus** — der Prompt blieb leer, obwohl Fokus und
Zielobjekt stimmten. Exakt derselbe Fehler wie bei `BP_Weapon.GetMagazineRounds` am 15.09. Erst
`(bind x (call))`, dann `(return x)`. Aufgefallen ist es nur, weil ein temporäres `LogString`
`focus=true  obj=BP_Workbench_C_0` bei leerem Prompt zeigte — die Ursache lag damit nicht am Fokus.

**Per PIE geprüft** (Spieler jeweils an die Station teleportiert): `SPEED   Stufe 3   200 $`,
`.50 BMG  freischalten   500 $`, `9mm  freischalten   60 $`, `Rausgehen  -  neuer Run`.

### 37. Wellen aus `DT_Waves` ✔ (22.09.)

Die Wellen kamen bis hierher aus Formeln im `BP_WaveDirector` (`3 + 2·step` Gegner, Typ-Anteile
über verschachtelte Clamp-Rechnungen). Balancing hieß damit: Blueprint öffnen, Nodes lesen, Zahlen
raten. Jetzt steht **jede Welle als Zeile in einer Tabelle**.

**`S_WaveRow`** (vom Nutzer angelegt, Structs kann das Toolset nicht erzeugen) und
**`DT_Waves`** unter `Waves/`, zehn Zeilen `Wave01`–`Wave10`:

| Spalte | Bedeutung |
|---|---|
| `RunnerCount` / `ShooterCount` / `RusherCount` | Zusammensetzung der Welle |
| `HealthMul` / `SpeedMul` | Faktoren auf die Basiswerte des Typs (1,0 = unverändert) |
| `RewardMul` | Faktor auf `KillReward` des Typs |
| `FirstBurst` | wie viele sofort beim Wellenstart dastehen |
| `TrickleDelay` | Sekunden bis zum nächsten Nachrücker |
| `IsBossWave` | letzte Welle — gesetzt auf `Wave10`, wird erst mit Schritt 43 wirksam |

| Welle | Läufer | Schütze | Rusher | HP× | Tempo× | Geld× | Burst | Takt |
|---|---|---|---|---|---|---|---|---|
| 1 | 10 | — | — | 1,00 | 1,00 | 1,0 | 6 | 1,40 s |
| 3 | 18 | — | — | 1,30 | 1,08 | 2,2 | 8 | 1,15 s |
| 5 | 26 | 5 | — | 1,60 | 1,16 | 4,0 | 10 | 0,95 s |
| 7 | 34 | 7 | 2 | 1,90 | 1,24 | 6,6 | 12 | 0,80 s |
| 10 | 48 | 12 | 9 | 2,40 | 1,35 | 12,0 | 18 | 0,55 s |

(Stand nach dem Tempo-Pass vom 22.09. — die erste Fassung stand bei 8/16/22/28/40.)

**Die Basiswerte pro Typ bleiben in den drei Gegner-Blueprints** (`BaseHealth`, `MoveSpeed`,
`KillReward`, `AttackDamage`, …). Sie in die Tabelle zu ziehen hätte sechs Spalten pro Typ
gekostet; die Class Defaults sind genauso Daten und einen Klick entfernt.

**Nachrücker statt Pulk.** Eine Welle steht nicht mehr auf einen Schlag da: `FirstBurst` Gegner
sofort, der Rest über einen Timer (`SpawnTick`) im Takt von `TrickleDelay`. Damit bleibt der Druck
durchgehend, statt in einer Welle zu kommen und dann abzureißen.

**Wellenende musste nachziehen.** `CheckWaveOver` hat vorher nur gezählt, ob noch Gegner leben —
mit Nachrückern hätte das die Welle beendet, sobald der Burst tot ist. Jetzt gilt zusätzlich
`SpawnsPending <= 0`.

**Neue Funktionen im Director:** `SpawnOne` (würfelt den Typ aus den offenen Restzahlen, spawnt,
ruft `SetupEnemy`), `SpawnTick` (Timer-Takt, löscht sich selbst bei leerem Rest). `SetupEnemy`
reicht nur noch die drei Multiplikatoren der Welle an den Gegner weiter.

**Wellen jenseits der Tabelle** laufen mit der letzten Zeile weiter (`min(Welle, Zeilenzahl)`),
damit nichts bricht, solange das Ende bei Welle 10 noch nicht gebaut ist.

**Dabei in eine Pure-Node-Falle getappt.** `(bind w (+ (GetCurrentWave) 1))` und danach
`SetCurrentWave w` — `w` hängt an einem **pure** Node und wird bei *jeder* Verwendung neu
ausgewertet, also auch nach dem Setzen. Welle 1 zog dadurch die Zeile `Wave02`. Sichtbar wurde es
nur, weil `CurrentWave` 1 war, `CurHealthMul` aber 1,15. **Regel:** erst setzen, dann die Variable
zurücklesen — nicht den Rechenausdruck mehrfach benutzen.

**Per PIE geprüft** (Simulate, 9 s): `CurrentWave` 1, 8 Gegner, `CurHealthMul` 1,0,
`CurRewardMul` 1,0, `CurTrickleDelay` 1,5, `SpawnsPending` 0.

### 37a. Gegner kommen von allen Seiten — und verklumpen nicht mehr ✔ (22.09.)

Drei Dinge machten den Kampf zu einfach, unabhängig von der Gegnerzahl:

**1. Sie kamen immer aus denselben vier Ecken.** `GetSpawnTransform` nahm die Spawnpunkte reihum
(`Index % 4`). Jetzt wird **im Ring um den Spieler** gespawnt: zufälliger Winkel, Radius zwischen
`RingMin` (1200) und `RingMax` (2100), auf das NavMesh projiziert
(`ProjectPointToNavigation`, Extent 800/800/500). Scheitert die Projektion — Spieler in der Ecke —,
fällt es auf einen zufälligen Spawnpunkt zurück. Die vier Punkte stehen weiter im Level, dazu drei
neue (`Spawn_N`, `Spawn_SE`, `Spawn_SW`), sind aber nur noch Rückfallebene.

**2. Sie liefen alle auf denselben Punkt.** `AI MoveTo` zielte auf den **Actor** des Spielers, also
für jeden Gegner auf exakt dieselbe Koordinate. `BP_EnemyBase` bekommt beim Spawn einen
`ApproachOffset` (zufälliger Winkel, 0–260 uu), der Tick zielt auf **Spielerposition + Offset**.
Damit umstellen sie dich, statt sich auf einer Stelle zu stapeln.

**3. Sie standen ineinander.** `bUseRVOAvoidance` ist jetzt auf allen drei Typen an
(`AvoidanceWeight` 0,5, `AvoidanceConsiderationRadius` 450). Dazu **Tempo-Jitter** von ±12 % pro
Gegner in `ApplyWaveProfile` — sie kommen als Kette an, nicht als Wand.

**Gemessen im Simulate-Lauf:** zwölf Gegner verteilt über die Winkel −147°, −111°, −29°, −16°,
−1°, 40°, 55°, 72°, 92°, 105°, 155°, 165° — also rundherum statt in einem Keil.

**Nachtrag am 22.09.: Gegner spawnten auf den Mauerkronen.** Gemeldet als „manche spawnen
außerhalb", gemessen bei (2489, 0, **z 490**) — das ist oben auf der Ostmauer. Recast legt auf den
100 uu breiten Kronen ein begehbares Band an, und die Projektion durfte mit `QueryExtent` Z **500**
so weit nach oben schnappen. Ein Ringpunkt außerhalb der Arena landete damit auf der Mauer, statt
zu scheitern und auf einen Spawnpunkt zurückzufallen. Zwei Änderungen:

1. **`QueryExtent` auf 300/300/100.** Der Kandidat liegt auf Spielerhöhe (z ≈ 92); 100 reicht nach
   unten auf den Boden, aber nicht mehr auf Deckungen (+108) oder Mauern (+308).
2. **Arena-Grenze als eigene Prüfung.** `ArenaHalf` (2350) — liegt der projizierte Punkt außerhalb,
   gilt er als ungültig und es greift der Spawnpunkt-Rückfall. Das hält auch dann, wenn das NavMesh
   irgendwann alte Kacheln außerhalb behält.

**Und der eigentliche Konstruktionsfehler dahinter:** `ProjectPointToNavigation` ist **pure**, also
wurden `ProjectedLocation` und der Erfolgs-Bool bei *jeder* Verwendung neu ausgewertet — mit
`RandomFloatInRange` im Input hieß das: **geprüfter und benutzter Punkt waren nicht derselbe.**
Jetzt wird der Kandidat erst in `SpawnCandidate` geschrieben, das Ergebnis in `SpawnProjected` /
`SpawnValid`, und alles Weitere liest die Variablen. Siehe die Pure-Node-Regel in `AGENTS.md`.

**Per PIE geprüft (Stresstest):** Ring absichtlich auf 2400–3800 gestellt, also fast vollständig
außerhalb der Arena — acht Gegner, alle auf z 90, keiner außerhalb ±2450. Vorher lag bei derselben
Einstellung einer auf der Mauer.

**`RingMin`, `RingMax`, `ArenaHalf`, `ExtractWindow` und `NextWaveDelay` sind jetzt
Instance Editable** — im Level am `WaveDirector` einstellbar, ohne das Blueprint anzufassen.

**`ApplyWaveProfile` ersetzt `ApplyWaveScaling`.** Statt additiver Boni jetzt multiplikativ, und
der Typ-Faktor moduliert den Faktor der Welle: `1 + (Faktor − 1) × HealthScaleMul`. Ein Rusher mit
`HealthScaleMul` 0,45 zieht aus `HealthMul` 2,6 also nur 1,72. `ApplyWaveScaling` bleibt vorerst
im Blueprint liegen, wird aber nicht mehr gerufen — genauso die Director-Variablen `BaseCount`,
`CountPerWave`, `HealthPerWave`, `SpeedPerWave`, `Shooter*`, `Rusher*` und `RewardMulPerWave`.

### 44a. Tempo- und Mengen-Pass ✔ (22.09.)

Erster Spieltest der neuen Wellen, Befund des Nutzers: *„ich kann denen allen ausweichen sehr
einfach"*. Die Zahl dahinter: **Läufer 320 uu/s gegen 800 uu/s Spielerbasis** — 40 %. Wer dich nie
einholt, ist keine Bedrohung, egal wie viele es sind. Das ist derselbe Befund wie am 16.09.
(Schritt 27a), nur hatte der damalige Fix am additiven Wellenbonus gedreht statt an der Basis.

**Basistempo pro Typ angehoben:**

| Typ | Tempo alt | Tempo neu | Deckel alt | Deckel neu | Tempo-Faktor |
|---|---|---|---|---|---|
| Läufer | 320 | **620** | 620 | 1000 | ×1,0 |
| Schütze | 210 | **400** | 340 | 620 | ×0,5 |
| Rusher | 500 | **780** | 1120 | 1500 | ×2,5 |

Damit liegt der Läufer auf Welle 1 bei rund **78 % deines Grundtempos** statt bei 40 % — ausweichen
geht noch, weglaufen nicht mehr. Auf Welle 10 (`SpeedMul` 1,35) sind es **837 uu/s**, mit dem
Jitter von ±12 % also 736–937: schneller als ein ungeupgradeter Spieler. Das **Speed-Upgrade wird
dadurch zum ersten Mal notwendig** statt nur angenehm. Der Rusher erreicht auf Welle 10 rechnerisch
1463 uu/s und läuft damit in seinen neuen Deckel.

`SpeedMul` wächst dafür flacher (1,45 → **1,35** auf Welle 10), weil die Basis den Sprung schon
trägt. `HealthMul` ebenfalls leicht zurück (2,60 → **2,40**) — mehr Gegner, die schneller bei dir
sind, brauchen nicht zusätzlich mehr HP.

**Mengen um rund ein Drittel hoch:** Welle 1 von 8 auf **10**, Welle 5 von 26 auf **31**, Welle 10
von 58 auf **69**. Der Burst steigt mit (5 → 6 auf Welle 1, 16 → 18 auf Welle 10), der Takt wird
enger (1,5 → 1,40 s bzw. 0,6 → 0,55 s).

### 44b. Typen früher, Schütze schärfer ✔ (22.09.)

Zweiter Befund aus demselben Test: Die Wellen spielten sich zu lange gleich, weil Schütze (ab 4)
und Rusher (ab 6) erst spät dazukamen. **Schütze jetzt ab Welle 2, Rusher ab Welle 3** — bei
unveränderten Gesamtmengen, es verschiebt sich nur die Mischung:

| Welle | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Läufer | 10 | 12 | 14 | 18 | 22 | 25 | 28 | 32 | 36 | 42 |
| Schütze | — | 2 | 3 | 5 | 6 | 8 | 10 | 12 | 14 | 17 |
| Rusher | — | — | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 |
| **gesamt** | 10 | 14 | 18 | 25 | 31 | 37 | 43 | 50 | 58 | 69 |

Welle 1 bleibt bewusst sortenrein — eine Welle, um die Steuerung zu greifen, reicht.

**Der Schütze war zu harmlos:** alle 2 s ein Schuss, Projektil mit 1200 uu/s. Auf 1100 uu
Reichweite brauchte das Geschoss fast eine Sekunde — man lief einfach heraus, ohne es zu merken.
Jetzt **`AttackCooldown` 2,0 → 1,4 s** und **`ShotSpeed` 1200 → 1800 uu/s**. Der Rusher bleibt
unangetastet.

Damit steigt der Schadensausstoß eines Schützen von 4,0 auf **5,7 pro Sekunde**. Auf Welle 10
stehen 17 davon — rechnerisch knapp 100 Schaden pro Sekunde, wenn *alle* gleichzeitig freie Bahn
haben. Das ist die Zahl, die die Deckungen im Level ab jetzt rechtfertigt: Projektile kollidieren
mit den Blöcken, Sichtlinie ist also echter Schutz.

**Per PIE geprüft:** Welle 1 testweise auf 4 Läufer / 3 Schützen / 3 Rusher gestellt — es spawnten
exakt 4 / 3 / 3, und ein laufender Schütze trug `AttackCooldown` 1,4 und `ShotSpeed` 1800.
Danach auf 10 / 0 / 0 zurückgesetzt.

**Per PIE geprüft:** Welle 1 spawnt 10 Gegner, `MoveSpeed` der ersten sechs: 585, 668, 580, 619,
659, 685 — also 620 mit dem gewollten Jitter.

**Offen, bewusst:** Der Geldfluss steigt mit den Mengen mit (Welle 10 zahlt jetzt rund 1440 statt
1224). Das gehört mit Schritt 44 nachgerechnet, sobald das Wellenende steht — vorher ist jede
Zahl geraten.

### 22a. Map auf 50×50 m verkleinert ✔ (22.09.)

Das Areal war mit 8000×8000 uu (80×80 m) so groß, dass man jeder Welle einfach davonlaufen konnte —
bei 800 uu/s Basistempo holt einen niemand ein, und die Gegner verteilten sich auf einer Fläche, auf
der nichts gleichzeitig passierte. Jetzt **5000×5000 uu**, also **61 % weniger Fläche**:

- Boden, `NavMeshBoundsVolume` und die vier Mauern auf 5000 gezogen, Mauern auf ±2500
- Deckungen nach innen: (850, 650), (−900, 1000), (−1150, −850), (1050, −1050), (200, −1550)
- Spawnpunkte auf den neuen Rand, dazu `Spawn_N`, `Spawn_SE`, `Spawn_SW` — jetzt sieben
- `BP_SafehouseDoor` an die neue Südmauer auf (0, −2400)

**Rückweg:** Von der entferntesten Ecke zur Tür sind es jetzt rund 3600 uu statt 5700 — bei 800 uu/s
gut 4,5 Sekunden. Das Fenster steht auf 10 s und ist damit großzügig; sobald die Kurve sitzt, ist
`ExtractWindow` der Regler, um den Rückweg wieder zur Entscheidung zu machen.

**Nebenwirkung:** Das NavMesh wird beim ersten PIE neu erzeugt („Recreating dtNavMesh instance …
mismatch in maxTiles"). Der Agent-Fix aus den technischen Schulden sitzt an der Actor-Instanz und
hat das überlebt — die Gegner laufen weiterhin. Beim nächsten Editor-Neustart trotzdem in die
`DefaultEngine.ini` nachziehen.

> ### ⛳ Gate 2 — nach Schritt 35 (So 20.09.)
> **Willst du nach dem Einkauf sofort wieder raus?**
> Der Test, an dem das ganze Spiel hängt. Wenn der Kauf sich nicht spürbar anfühlt, sind die
> Upgrade-Schritte zu klein — lieber wenige große Sprünge als viele Prozentwerte.

---

## Phase 3 — Inhalt und Kurve · bis Mi 23.09.

Erst jetzt lohnt sich Breite — vorher weißt du nicht, wofür du sie baust.

| # | Schritt | |
|---|---|---|
| ~~35a~~ | ~~Echtes Pathfinding nachziehen~~ | **Erledigt am 17.09.** `AI MoveTo` auf dem NavMesh, Deckungen wieder drin. Siehe technische Schulden. |
| 36 | Weitere Gegnertypen | Schütze und Rusher **am 16.09. gebaut**. Tank fehlt — **braucht eine neue Spalte in `S_WaveRow`**, also eine Änderung am Struct durch den Nutzer |
| ~~37~~ | ~~Wellen aus WaveData~~ | **Erledigt am 22.09.** `DT_Waves` mit zehn Zeilen, Nachrücker statt Pulk. Siehe oben. |
| 38 | Volle Kaliber-Leiter | **Bänke stehen alle** (9mm, .45, 7.62, .44, .50 — 6mm ist frei). Offen ist nur das Tuning der Kaliberwerte |
| 39 | Projektil-Looks pro Kaliber | **Tracer und Farbe erledigt am 23.09.** (Schritt 11). Einschlag fehlt noch — gehört zum FX-Pass |
| ~~40~~ | ~~Durchschlag~~ | **Vorgezogen am 16.09.** Siehe Notiz unter Schritt 20. |
| ~~41~~ | ~~Heilung, Granate, Vorratsregal~~ | **Erledigt am 23.09.**, siehe Schritt 11 |
| ~~42~~ | ~~Armor wirksam machen~~ | **War schon erledigt** — `BPC_Health.ApplyDamage` rechnet `Amount × (1 − ArmorReduction)`, Mindestschaden 1 |
| ~~43~~ | ~~Boss~~ | **Erledigt am 23.09.** `BP_EnemyBoss` plus Wellenende, siehe Fahrplan 2 und 3 |
| 44 | Balancing | Kurve so ziehen, dass Welle 10 erst im vierten bis fünften Run fällt. Prüfen, ob sich die teuren Kaliber lohnen. |

---

## Phase 4 — Rahmen und Politur · bis Fr 25.09.

Bewusst zuletzt — nichts davon verändert, ob der Loop trägt.

| # | Schritt | |
|---|---|---|
| 45 | Menü-Level | Gegner laufen im Hintergrund, Start-Button, Musik-Skip |
| ~~46~~ | ~~Aufwachen im Bett~~ | **Erledigt am 23.09.**, siehe Schritt 10 und 11 |
| 47 | Musik-States | Die sechs ungenutzten Loops an Ort und Wellenintensität koppeln |
| 48 | Pause, Optionen, Tod-Screen | Alle mit Gamepad-Navigation über CommonUI |
| 49 | Feedback | Treffer, Mündungsfeuer, Todes-Effekte, SFX |
| 50 | Art-Pass | Safehouse und Outside |

---

## Offene technische Schulden

Dinge, die **funktionieren, aber nicht fertig sind**. Sie stehen hier, damit sie nicht in
Schritt-Notizen untergehen.

### ~~Gegner laufen ohne Pathfinding~~ — erledigt am 17.09.

`BP_EnemyBase` bewegt sich jetzt über **`AI MoveTo`** auf dem NavMesh. Die Deckungen sind wieder
drin, die Gegner laufen darum herum.

**Was wirklich kaputt war:** Nicht der Aufruf, nicht der Controller, nicht das NavMesh. Der
**Agent des `RecastNavMesh` war zu klein**: `AgentHeight` 144 bei einer Gegner-Kapsel von 176
(Radius 34, Halbhöhe 88). Die Navigation fand für den angefragten Agenten keine passenden Nav-Daten
und fiel auf die ebenfalls registrierte **`AbstractNavData`** zurück — und deren `FindPath` ist ein
Stub, der *stillschweigend nichts tut*. Genau das erklärt das Verhalten vom 15.09.:
`SimpleMoveToActor` meldete keinen Fehler und bewegte trotzdem nichts.

**Behoben** durch `AgentRadius` 42 und `AgentHeight` 192 am `RecastNavMesh-Default` in `L_Outside`.

**Wie es gefunden wurde:** `AI MoveTo` statt `SimpleMoveToActor` — der hat einen `OnFail`-Ausgang.
Damit war binnen einer PIE-Runde klar, dass der Aufruf scheitert und nicht etwa ins Leere läuft.
Danach `LogNavigation` auf `VeryVerbose`: dort stand, dass `RecastNavMesh-Default` **und**
`AbstractNavData-Default` beide erfolgreich registriert waren — das war der entscheidende Hinweis.

**Merksatz:** `SimpleMoveToActor` verschweigt Fehler. Für alles, was nicht auf Anhieb läuft,
gehört `AI MoveTo` in den Graphen, bis es steht.

**NavMesh neu backen nach dem Umbau der Arena (23.09.).** Nach dem Verkleinern auf 5000 zeigt der
Editor „NAVMESH NEEDS TO BE REBUILT". Im Spiel stört das nicht — das NavMesh wird beim Start neu
erzeugt („Recreating dtNavMesh instance …" im Log) —, **für den Build muss es aber gebacken sein.**
Das Toolset kann keinen Build anstoßen: **Build → Build Paths** in `L_Outside` von Hand.

**Noch offen, aber unkritisch:** Der Fix sitzt an der Actor-Instanz im Level, nicht in
`DefaultEngine.ini`. Wird das NavMesh je neu erzeugt, ist er weg. Sauberer wäre ein expliziter
`SupportedAgents`-Eintrag in der Config — der braucht aber einen Editor-Neustart und hätte den
gerade funktionierenden Zustand blind verändert. Beim nächsten ohnehin fälligen Neustart nachziehen.

**Bauliche Folge:** `AI MoveTo` ist ein **latenter** Node und darf deshalb nicht in einem
Funktionsgraphen stehen. `UpdateAI` gibt jetzt ein `WantsMove` zurück (und drosselt selbst über
`MoveRequestInterval`), der `AI MoveTo` selbst sitzt im `EventTick` des EventGraphen.

**Per PIE geprüft:** Gegner startet bei (1725, 1948), ist zwei Messungen später bei (642, 771) und
dann bei (96, 115) — er läuft die volle Strecke an Cover_1 (1200, 900) vorbei, ohne hängenzubleiben.

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
