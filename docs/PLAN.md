# Achachay — Produktionsplan

**Vertical Slice · Abgabe 25.09.2026 · UE 5.8 · Blueprint-only**

Top-Down-Wave-Shooter mit Extraktions-Loop und permanenter Progression. Du überlebst draußen so
lange du kannst, nimmst das Geld mit rein, kaufst dich stärker, gehst wieder raus. Die Wellen
starten bei jedem Rausgehen wieder bei 1 — weiter kommst du nur, weil *du* stärker geworden bist.

Du hast dabei genau eine Waffe. Sie frisst jedes Kaliber, das es gibt — und **Munition ist die
Währung des Spiels**: 6mm ist gratis und unbegrenzt, alles darüber kaufst du vor jedem Run
packungsweise. Jeder Schuss kostet damit echtes Geld, und jeder Safehouse-Besuch wird zur Frage,
ob du jetzt einkaufst oder auf .50 BMG sparst.

---

## Der Loop

```
                      ┌──────────── AUSRÜSTEN ────────────┐
                      │                                   ▼
  MENÜ ──einmalig──▶ SAFEHOUSE                        OUTSIDE
  Gegner im Hinter-   Kaliber · Werkbank ·            Welle 1 → Boss
  grund               Vorrat                              │
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

Keine Slots, kein Inventar. Du hast **eine Waffe**, und ein Knopf wechselt durch die Kaliber, für die
du Munition dabei hast. Heilung und Granate liegen auf zwei eigenen Tasten.

**6mm ist immer dabei, kostenlos und unbegrenzt.** Es ist der Boden, unter den du nie fallen kannst —
ab höheren Wellen reicht es nur noch, wenn du sauber zielst und dich gut bewegst. Alles darüber
kaufst du vor jedem Run als Munition.

Drei Regeln, die den Wechsel angenehm machen:

- Der Wechsel **überspringt leere Kaliber**. Bei den Preisen trägst du selten mehr als zwei oder drei
  gleichzeitig, der Kreis bleibt also kurz.
- Ist ein Kaliber leergeschossen, fällt die Waffe **automatisch auf 6mm zurück** — kein Klicken ins
  Leere mitten in der Welle.
- Das HUD zeigt **alle mitgeführten Kaliber mit ihrem Vorrat**, das aktive ist hervorgehoben.

Belegung: Mausrad am PC, Steuerkreuz am Gamepad.

### Stationen im Safehouse

- **Munitionskiste** — eine pro Kaliber. Hingehen, interagieren, eine Packung kaufen. Beliebig oft
  wiederholbar. Keine Freischaltung, kein Shop-Bildschirm: Wer bezahlen kann, kauft.
- **Werkbank** — die drei permanenten Upgrades: Speed, Armor, Health.
- **Vorratsregal** — Heilung und Granaten, einzeln gekauft.

### Preise (Startvorschlag)

Bei etwa 1 Dollar pro Kill und 150–250 Dollar aus einem gut gelaufenen Run:

| Kaliber | Packung | Preis | Charakter |
|---|---|---|---|
| 6mm | ∞ | **frei** | Dauerfeuer, kaum Schaden — der Boden |
| 9mm | 50 | 15 | Arbeitspferd, praktisch immer dabei |
| .45 ACP | 50 | 30 | Langsamer, härter |
| 7.62×39 (AK) | 40 | 60 | Dauerfeuer mit Wumms |
| .44 Magnum | 20 | 80 | Wenige Schuss, hoher Einzelschaden |
| .50 BMG | 10 | **250** | Durchschlägt eine Reihe — etwa ein ganzer Run |
| Heilung | 1 | 60 | |
| Granate | 1 | 80 | |

.50 BMG kostet ungefähr einen kompletten erfolgreichen Run. Du musst dich bewusst dafür entscheiden
und einmal auf alles andere verzichten.

**Übrige Munition bleibt beim Extrahieren erhalten und verfällt beim Tod** — dieselbe Regel wie beim
Geld. Sonst wäre Einkaufen Buchhaltung statt Planung.

> In der Top-Down-Ansicht siehst du die Patrone nie — der Kaliber-Mesh wird nur in der Munitionskiste
> gebraucht. Was der Spieler im Kampf unterscheidet, ist das **Projektil**: Tracer-Größe, Farbe,
> Einschlag. Dort gehört das visuelle Budget hin.

## Festgelegt

| | |
|---|---|
| **Waffe** | Genau eine, für immer. Sie verschießt jedes Kaliber. |
| **Kaliberwechsel** | Ein Knopf wechselt durch, leere werden übersprungen. Keine Slots. |
| **Munition** | Wird vor jedem Run als Packung gekauft und verbraucht sich. 6mm ist frei und unbegrenzt. Keine Freischaltung. |
| **Magazin** | Magazin und Nachladen bleiben als Taktgeber — der Vorrat ist davon getrennt. |
| **Upgrades** | Genau drei: Speed, Armor, Health. Dauerhaft. |
| **Stamina** | Dashes kosten Stamina, die sich nachlädt. Ersetzt den festen Cooldown. |
| **Verbrauchsgüter** | Heilung und Granate, einzeln gekauft. Bei Benutzung weg — und beim Tod ebenfalls. |
| **Tod** | Run-Geld, gekaufte Munition und Verbrauchsgüter sind weg. Upgrades bleiben. |
| **Extraktion** | Nach jeder Welle 15 Sekunden zurück ins Safehouse. Übriges bleibt erhalten. |
| **Wellenende** | Wenn der letzte Gegner stirbt. Kein Timer, keine Obergrenze. |
| **Wellentakt** | Nach oben wachsen Menge und Härte der Gegner. |
| **Boss** | Am Ende der zehnten Welle. Erstmal schlicht: sehr viel HP. |
| **Eingabe** | Maus/Tastatur **und** Gamepad, beide vollwertig. |
| **Character-Anpassung** | Raus. |
| **Netzwerk** | Keine Replikation. |
| **Level** | Handgebaut, keine prozedurale Generierung. |

### Bleibt zum Austesten

**Trägt die Ökonomie?** Bei 1 Dollar pro Kill und 15 Dollar für 50 Schuss 9mm zahlst du 30 Cent pro
Kugel — jeder Fehlschuss kostet real Geld. Das ist beabsichtigt und zwingt zum Zielen, kann aber
kippen. Prüfstein: Wenn du nach drei Runs immer noch ausschließlich 6mm schießt, sind die Preise zu
hoch oder das Kopfgeld zu niedrig.

**Ist .50 BMG seinen Preis wert?** 250 Dollar für 10 Schuss lohnen sich nur, wenn der Durchschlag
mehrere Gegner pro Kugel nimmt. Damit erzieht die Ökonomie dich dazu, auf Linien zu warten statt zu
spammen — vorausgesetzt, die Wellen liefern überhaupt Linien. Falls nicht, ist das Kaliber tot.

## Bestand (Stand 14.09.2026)

| Asset | Zustand | Anmerkung |
|---|---|---|
| `BP_PlayerCharacter` | **Läuft** | Bewegung, Zielen mit Maus und Gamepad, Geräteerkennung, Dash mit Stamina, Interaktion, Stats aus der GI |
| ↳ Funktionen | | `GetAimLocation`, `ApplyAimRotation`, `UpdateActiveInputDevice`, `UpdateGamepadAim`, `UpdateMouseDelta`, `MarkAimInput`, `RegenerateStamina`, `SpendDashStamina`, `StartDash`, `StoreEssentialVariables`, `UpdateFocus`, `TryInteract`, `ApplyPlayerStats` |
| `GI_Achachay` | **Steht** | Geld (`Money`/`RunMoney`), Upgrade-Level, `AmmoReserve` (Map String→Int), `CurrentCaliberId`, Verbrauchsgüter, `GetPlayerStats`, Geräteerkennung. EventGraph leer. |
| `E_InputDevice` | Vorhanden | `KeyboardMouse`, `Gamepad` |
| `IMC_Gameplay` | Vorhanden | 9 Mappings: Move (WASD + Stick), Dash (Space, Schulter, Stick-Klick), Aim (rechter Stick) |
| Input Actions | **Vollständig** | `IA_Move`, `IA_Dash`, `IA_Aim`, `IA_Fire`, `IA_Reload`, `IA_Interact`, `IA_SwitchCaliber`, `IA_UseHeal`, `IA_UseGrenade`. `Pressed`-Trigger fehlen noch. |
| `L_Menu` / `L_Outside` / `L_Safehouse` | Rohbau | Licht, Himmel, Boden, PlayerStart. Keine Geometrie, kein NavMesh. |
| `GM_*` | Verdrahtet | Pawn- und Controller-Klassen korrekt, Graphs leer |
| `BP_RecordPlayer` | Fertig | Zufallstrack; Instanz in L_Menu hat nur `loop_menu1` |
| Musik (7 Loops) | 6 ungenutzt | |
| Data Assets | **Steht** | `CaliberData` mit 15 Feldern, dazu alle sechs Kaliber von 6mm bis .50 BMG. `ProjectileSpeed` und `ProjectileSize` am 14.09. ergänzt (Startwerte, ungetunt); `ProjectileColor` ist gefüllt, wird aber erst ab Schritt 39 benutzt. Ein Mesh-Feld für die Munitionskiste fehlt noch (Schritt 33). |
| `BPI_Interactable` + `BP_TestInteractable` | Fertig | Fokus über `UpdateFocus`, Auslösen über `IA_Interact` |
| `ItemData`, `UpgradeData`, `WaveData` | Nichts | Gerüste aus Schritt 13 noch offen |
| Widgets | Nichts | |
| `BP_Weapon` | **Läuft** | `ActiveCaliber`, `Fire(AimDir)` mit Feuerratensperre, Streuung und `ProjectilesPerShot`. Wird vom Character gespawnt und angehängt (`EquipWeapon`). |
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
| So 13.09. | 17–20 | Magazin und Vorrat, Kaliberwechsel, Health, Schaden am Ziel |
| Mo 14.09. | 21 | Gegner läuft auf dich zu und schlägt zu |
| Di 15.09. | 22 | L_Outside als Graybox mit NavMesh, Rückweg unter 15 s geprüft |
| **Mi 16.09.** | **23–25** | **Gate 1** — drei Wellen, HUD, Tod. Macht der Fight Spaß? |
| Do 17.09. | — | Reiner Tuning-Tag aus Gate 1. Keine neuen Funktionen. |
| Fr 18.09. | 26–28 | Geld, Rückweg-Fenster mit Countdown, Safehouse-Tür |
| Sa 19.09. | 29–32 | Sofort-weiter, Tod-Regel, Levelwechsel mit Zustand, Run-Summary |
| **So 20.09.** | **33–35** | **Gate 2** — Munitionskiste, Werkbank, Ausgang. Der Loop läuft rund. |
| Mo 21.09. | 36–38 | Gegnertypen, Wellen aus WaveData, volle Kaliber-Leiter |
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
- `IA_SwitchCaliber` ist ein **Durchwechseln**, keine Slot-Wahl — Mausrad und Steuerkreuz
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
  Streuung, Projektile pro Schuss, Durchschlag, Projektil-Look, Mesh — dazu **`PackPrice`**,
  **`RoundsPerPack`** und **`bUnlimited`** (nur für 6mm)
- `ItemData`, `UpgradeData`, `WaveData` als Gerüste
- Zwei Test-Kaliber anlegen, die sich maximal unterscheiden: **6mm** (unbegrenzt) und **.50 BMG**

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

### 17. Magazin, Nachladen und Vorrat

- Magazinstand als Variable, Größe aus dem Kaliber
- **Vorrat getrennt vom Magazin**: Nachladen zieht aus dem Vorrat in der GameInstance
- Leeres Magazin oder `IA_Reload` startet das Nachladen, Dauer aus dem Kaliber
- 6mm hat `bUnlimited` und zieht keinen Vorrat ab
- Vorrat und Magazin leer → **automatischer Rückfall auf 6mm**

**Probe:** .50 BMG leerschießen wechselt von selbst auf 6mm, ohne dass du klicken musst.

### 18. Kaliber durchwechseln

- `IA_SwitchCaliber` schaltet auf das nächste Kaliber **mit Vorrat**, leere werden übersprungen
- 6mm ist immer in der Liste
- Magazinstand pro Kaliber getrennt merken

**Probe:** Mit zwei Testkalibern durchwechseln, jeweils mit eigenem Magazin.

### 19. Health-Komponente

- Eine Komponente für Spieler und Gegner gleichermaßen
- Aktuelle und maximale Health, `ApplyDamage`, Tod-Event
- `ArmorReduction` schon einbauen, auch wenn sie noch 0 ist

**Probe:** Testweise Schaden zufügen senkt den Wert und löst bei 0 das Tod-Event aus.

### 20. Projektil verursacht Schaden

- Treffer auf einen Actor mit Health-Komponente wendet den Kaliberschaden an
- Projektil zerstört sich, außer bei Durchschlag — der kommt erst in Phase 3

**Probe:** Ein Testwürfel mit Health verschwindet nach der richtigen Trefferzahl.

### 21. BP_EnemyBase

- Character mit Health-Komponente
- Eigener AIController, auf Tick oder im Intervall `MoveTo` auf den Spieler
- Nahkampfangriff bei Kontakt mit Cooldown
- Kein Behavior Tree

**Probe:** Der Gegner findet den Spieler durch die Graybox und schlägt zu.

### 22. L_Outside als Graybox

- Grundfläche, ein paar Deckungen, eine klar erkennbare Safehouse-Tür
- NavMeshBoundsVolume über das gesamte begehbare Areal
- Entfernteste Kampfzone so setzen, dass der Rückweg zur Tür unter 15 Sekunden bleibt — bei
  600 uu/s sind das etwa 90 Meter, also spürbar darunter bleiben

**Probe:** Von der entferntesten Ecke zur Tür laufen und die Zeit stoppen. Deutlich unter 15
Sekunden.

### 23. BP_WaveDirector

- Spawnpunkte als Actors im Level
- Drei Wellen fest verdrahtet, Zusammensetzung noch nicht aus `WaveData`
- Welle endet, wenn der letzte Gegner tot ist — Zähler statt Timer
- Danach Pause, dann nächste Welle

**Probe:** Drei Wellen laufen hintereinander durch. Schneller Töten verkürzt die Welle sichtbar.

### 24. Provisorisches HUD

- Health, Stamina, aktuelle Welle, Geld
- **Alle mitgeführten Kaliber mit Vorrat**, das aktive hervorgehoben
- Magazinstand des aktiven Kalibers
- Hässlich ist in Ordnung — es geht um Information, nicht um Gestaltung

**Probe:** Alle Werte aktualisieren sich live, der Wechsel verschiebt die Hervorhebung.

### 25. Spielertod

- Health auf 0 → Eingabe sperren, kurz warten, Karte neu laden

**Probe:** Sterben führt zuverlässig zum Neustart, ohne hängenzubleiben.

> ### ⛳ Gate 1 — nach Schritt 25 (Mi 16.09.)
> **Macht der Fight für sich genommen Spaß?**
> Mit Maus **und** Gamepad spielen. Hier wird an Feuerrate, Dash-Cooldown, Gegnertempo und
> Trefferrückmeldung gedreht, bis es sitzt. Wenn es sich hier nicht gut anfühlt, ist alles Folgende
> verschwendete Arbeit.

---

## Phase 2 — Der Loop schließt sich · bis So 20.09.

Ab hier ist es dein Spiel und nicht mehr irgendein Wave-Shooter.

### 26. Geld

- Drop pro Kill und Bonus pro überstandener Welle, aufaddiert auf `RunMoney`

**Probe:** Kills erhöhen die Anzeige im HUD.

### 27. Rückweg-Fenster

- Nach dem letzten Kill 15 Sekunden Countdown, danach startet die nächste Welle
- Countdown im HUD, dazu ein Wegweiser zur Tür, solange sie außerhalb des Bildes liegt

**Probe:** Countdown läuft sichtbar, die nächste Welle startet exakt bei null.

### 28. Safehouse-Tür als Ausgang

- Trigger an der Tür, nur während des Fensters aktiv
- Durchlaufen beendet den Run: `RunMoney` wandert auf `Money`, dann Levelwechsel

**Probe:** Rechtzeitig durch die Tür landet im Safehouse, mit dem Geld auf dem Konto.

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

### 33. Munitionskiste

- Actor mit `BPI_Interactable`, referenziert ein `CaliberData`
- Interagieren kauft **eine Packung**, beliebig oft wiederholbar
- Zwei Zustände sichtbar: kaufbar oder zu teuer
- Gekaufte Schuss landen im Vorrat der GameInstance, nicht im Magazin

**Probe:** Kaufen zieht Geld ab, der Vorrat steigt um `RoundsPerPack`.

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
| 36 | Weitere Gegnertypen | Rusher, Schütze, Tank — abgeleitet von `BP_EnemyBase` |
| 37 | Wellen aus WaveData | Zusammensetzung und Menge als Daten, nicht als Nodes. Zehn Wellen, nach oben wachsende Menge und Härte. |
| 38 | Volle Kaliber-Leiter | 6mm bis .50 BMG, je eine Munitionskiste im Safehouse |
| 39 | Projektil-Looks pro Kaliber | Tracer, Größe, Farbe, Einschlag — hier entsteht die Lesbarkeit im Kampf |
| 40 | Durchschlag | Große Kaliber treffen mehrere Gegner in einer Linie |
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

## Was den Slice kippen kann

**Das große Kaliber macht die kleinen wertlos.** Kaliber sind deine gesamte Progression *und* deine
einzige taktische Entscheidung im Kampf. Beides gleichzeitig hält nur, wenn ein höheres Kaliber
stärker, aber nicht überall besser ist.

**Gamepad erst am Ende einbauen.** Zwei Eingabegeräte nachträglich zu unterstützen heißt,
Zielsystem, Interaktion und jedes Menü anzufassen. Beide Wege von Anfang an mitbauen und bei jedem
Playtest anfassen.

**Behavior Trees und EQS.** Für „lauf zum Spieler und schlag zu" reicht ein AIController mit
`MoveTo`. BTs zahlen sich erst bei Deckung und Flanken aus.

**Den Boss vor der Wellen-Kurve bauen.** Ein Boss ist nur so gut wie das, was ihn vorbereitet.

---

## Zwei Dinge, die feststehen

**Drei getrennte Maps heißt: jeder Zustand stirbt beim Wechsel.** Geld, Upgrades, freigeschaltete
Kaliber, Munitionsvorrat, Wellenfortschritt — nichts davon überlebt ein `OpenLevel` von allein. Alles,
was den Wechsel überstehen muss, gehört in `GI_Achachay`. Einen **Neustart** übersteht bewusst
nichts — Schritt 12 ist gestrichen. Das ist der Grund, warum Phase 0 vor allem anderen steht.

**CommonUI ist NICHT aktiviert — hier stand vier Tage lang das Gegenteil.** In `DefaultGame.ini`
liegt zwar eine CommonUI-Konfiguration inklusive Fokus-Regeln, aber das Plugin fehlt in
`achachay.uproject`; die Einträge sind wirkungslose Template-Reste (siehe `AGENTS.md` §2). Wer das
Widget-Kapitel angeht, entscheidet also zuerst: Plugin aktivieren und die geschenkte
Fokus-Navigation mitnehmen, oder mit UMG bauen und die Gamepad-Navigation selbst verdrahten.
