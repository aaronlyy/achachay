# AGENTS.md — Arbeitsregeln und Fallstricke für dieses Projekt

Notizen für KI-Agenten, die an *Achachay* arbeiten. Entstanden aus konkreten Fehlern, nicht aus
Theorie. Wer hier reinschaut, spart sich die Stunde, die uns das gekostet hat.

Projektplan: `docs/PLAN.md`

---

## 1. Die wichtigste Regel

**Wenn der Nutzer sagt „das funktioniert bei mir", dann funktioniert es. Der Fehler liegt beim
Messwerkzeug, nicht beim Nutzer.**

Was passiert ist: Ich habe über MCP die Property `Mappings` am `IMC_Gameplay` gelesen, ein leeres
Array bekommen und daraus geschlossen, dass Enhanced Input im Projekt nicht konfiguriert ist. Der
Nutzer hat **dreimal** widersprochen — „movement geht", „ich kann mit WASD laufen und mit Controller
auch", „hier ist alles schon voll". Ich habe stattdessen immer neue Erklärungen gebaut, warum meine
Messung stimmt und seine Beobachtung täuscht (SpectatorPawn, Level Blueprints, stale UI).

Am Ende hat ein Screenshot es aufgeklärt: Die echten Daten liegen unter `DefaultKeyMappings`, nicht
unter `Mappings`. Am Asset existiert zusätzlich ein totes, leeres `Mappings`-Array, das der Editor
gar nicht anzeigt. Ich habe also die ganze Zeit die falsche Property gelesen — **und beschrieben**.

Konsequenzen für die Arbeitsweise:

- Beim ersten Widerspruch **die eigene Messung anzweifeln**, nicht die Beobachtung des Nutzers.
- Property-Namen gegen das prüfen, was der Editor anzeigt — nicht gegen die eigene Erwartung.
- Bei Widersprüchen zwischen Werkzeug und Nutzer: **die Datei selbst** befragen. Ein Binärdump der
  `.uasset` mit `re.findall(rb'[ -~]{3,}', data)` zeigt Schlüsselnamen, Key-Namen und Asset-Pfade und
  hätte die Frage in zwei Minuten beantwortet.
- **Niemals fremde Assets schreiben, um eine Hypothese zu testen.** Ich habe acht Mappings in das
  IMC geschrieben und wieder gelöscht, bevor ich sicher wusste, was dort steht. Dass nichts kaputt
  ging, war Glück, nicht Sorgfalt.

---

## 2. Projektfakten, die überraschen können

- **Git LFS ist aktiv** für `*.uasset`, `*.umap`, Texturen, Audio, FBX. `git show HEAD:<asset>`
  liefert einen 130-Byte-Pointer, keinen Asset-Inhalt. Größenvergleiche über `git cat-file -s` sind
  wertlos; die echte Größe steht im Pointer-Text (`size <bytes>`).
- **Unreal serialisiert beim Speichern neu.** Ein Asset kann in `git status` als `M` auftauchen,
  obwohl sich inhaltlich nichts geändert hat. Nicht als Beweis für eine Änderung werten.
- **CommonUI ist NICHT aktiviert.** In `Config/DefaultGame.ini` stehen zwar
  `[/Script/CommonUI.CommonUISettings]`-Einträge, aber das Plugin fehlt in `achachay.uproject`. Die
  Einträge sind wirkungslose Template-Reste. (Aktive Plugins: ModelingToolsEditorMode,
  ModelContextProtocol, Terminal, EditorToolset.)
- **`Config/DefaultInput.ini` enthält keine Bindings**, nur `AxisConfig` (Deadzones, Sensitivity).
  Alle Bindings laufen über Enhanced Input.
- Der Spieler-Character nutzt einen **StaticMesh** (`characterMesh`), kein Skeletal Mesh.
- **SaveGame: am 14.09. gestrichen, am 23.09. zurückgeholt.** `SG_Achachay`, `SaveProgress` und
  `LoadProgress` existierten am 14.09. und wurden auf Wunsch des Nutzers entfernt (Schritt 12).
  **Am 23.09. hat der Nutzer ausdrücklich danach gefragt** — es steht als B1 im Fahrplan. Bis es
  gebaut ist, lebt der Zustand ausschließlich in `GI_Achachay` und ist nach einem Neustart weg.

---

## 3. Fallstricke der Unreal-MCP-Toolsets

### Properties

| Falle | Realität |
|---|---|
| `InputMappingContext.Mappings` | **Totes Legacy-Array, immer leer.** Echte Daten: `DefaultKeyMappings` |
| Komponenten in `list_variables` | Tauchen dort **nicht** auf. `list_properties` benutzen |
| Komponenten am CDO lesen | `CharacterMovement` → liefert refPath `…Default__X_C:CharMoveComp`. SCS-Komponenten wie `springArm`, `camera` liefern `"None"` und sind so nicht adressierbar |
| Unbekannte Property | Wirft einen Fehler — ein leeres Ergebnis bedeutet also „wirklich leer", nicht „falscher Name". Trotzdem kann eine *andere*, gleichnamige Property existieren |
| Arrays via `set_properties` | Größe **und** Inhalt gleichzeitig ändern wird abgelehnt („insertion points are ambiguous"). Elemente einzeln anhängen, bestehende unverändert mitschicken |
| Instanced Subobjects (Input-Modifier) | `{"instance": "/Script/…"}` meldet `true`, schreibt aber `None`. **Geht nicht** — vom Nutzer im Editor setzen lassen |

### Blueprint-Graphen

- **`write_graph_dsl` hängt an, ersetzt nicht.** Existiert schon ein ReturnNode oder ein
  Event-Node desselben Typs, schlägt der Schreibvorgang fehl („does not exist"). Vorher die
  betroffenen Nodes per `delete_node` entfernen.
- **Schlägt der Schreibvorgang mittendrin fehl, bleiben Teil-Nodes im Graph liegen.** Danach
  aufräumen, sonst sammeln sich Waisen.
- **`read_graph_dsl` gibt Node-IDs aus, die es beim Schreiben nicht gibt.** Gelesen wird z. B.
  `Math|Vector|vector*vector`, schreiben kann man das nicht. Für Arithmetik die generischen
  Operatoren `(+ - * /)` nutzen — die lösen korrekt auf.
- **`read_graph_dsl` ist keine verlässliche Bestandsaufnahme.** Drei belegte Verzerrungen:
  Ein Pure-Node, der **in einer Schleife** benutzt wird, wird in der Ausgabe **vor** die Schleife
  gehoben — als würde er nur einmal ausgewertet. Im Graph hängt er korrekt im Schleifenkörper.
  Dazu die beiden älteren:
  Bodies von **Enhanced-Input-Events** werden gar nicht gerendert — die Ausgabe zeigt nur
  `(event EnhancedInputActionIA_Interact (…))` und schluckt alles, was daran hängt. Und ein
  **einzelner Break-Node**, dessen Ausgänge mehrfach benutzt werden, erscheint als mehrfach
  wiederholter Inline-Aufruf, als gäbe es ihn mehrmals. **Wer Nodes zählen oder „ist da nichts?"
  beantworten will, nimmt `find_nodes` + `get_node_infos`, nicht die DSL-Ausgabe.** (Kostete am
  14.09. beinahe die falsche Meldung „Interact ist nicht verdrahtet".)
- **Cast-Type-Ids behalten den Unterstrich.** `Utilities|Casting|CastToGI_Achachay` funktioniert
  genau so — die Unterstrich-Regel weiter unten gilt für Struct-/Interface-Nodes, nicht für Casts.
- **Type-IDs mit Klammern brechen den DSL-Parser — aber nicht `create_node`.** In einem
  `write_graph_dsl`-Skript lässt sich `Widget|SetText(Text)` oder `Math|Integer|Clamp(Integer)`
  nicht *benennen*, die Klammern beenden die S-Expression. **`create_node` nimmt exakt dieselben
  IDs anstandslos** (am 23.09. mit `Widget|SetText(Text)` und `Utilities|Text|ToText(String)`
  geprüft). Dazu kommt: Viele Klammer-Nodes landen im Graphen, **ohne dass sie jemand benennt** —
  der DSL setzt Konvertierungen wie `ToFloat(Integer)` oder `ToString(Integer)` selbst ein.
  **Konsequenz für die Wortwahl:** Eine Funktion mit Klammer-Nodes ist *nicht* „nicht neu
  schreibbar". Sie ist neu baubar als DSL-Rumpf plus ein paar `create_node`/`connect_pins` für die
  Klammer-Nodes. Nur ist das mehr Arbeit und mehr Risiko, als den bestehenden Graphen zu ergänzen —
  das ist eine Abwägung, keine Grenze. (Am 23.09. hat der Nutzer zu Recht widersprochen: Die
  fraglichen Graphen stammen selbst aus einer früheren Toolset-Sitzung.)
- **`find_node_types` findet nichts bei Filtern mit Sonderzeichen** wie `*` oder `+`. Nach dem
  Klarnamen filtern und clientseitig nachfiltern.
- **Löschen eines ReturnNode löscht den Output-Parameter mit.** Danach `add_function_param` erneut
  aufrufen und den Wert per `connect_pins` anschließen.
- `add_variable` und `add_function_param` können **keine Enums**. Unterstützt: `bool, int, float,
  byte, name, string, text, Vector, Rotator, Transform, Vector2D, LinearColor`. Enum-Variablen muss
  der Nutzer anlegen.
- **Cross-Blueprint-Nodes gehen doch — der Type-Id muss nur stimmen.** (Korrigiert am 14.09.,
  die frühere Notiz hier war falsch und hat Handarbeit erzwungen, die nicht nötig war.)
  Die Form ist `Class|<BlueprintnameOhneUnterstriche>|<Name>`, für Funktionen **und** Variablen:

  | Ziel | Type-Id |
  |---|---|
  | Funktion auf `GI_Achachay` | `Class|GIAchachay|GetPlayerStats` |
  | Variable setzen auf `GI_Achachay` | `Class|GIAchachay|SetMoney` |
  | Variable lesen auf `GI_Achachay` | `Class|GIAchachay|GetMoney` |

  Das funktioniert per `create_node` **und** per `write_graph_dsl`. Der Zielpin heißt `self` und
  steht als **letztes** positionales Argument: `(Class|GIAchachay|SetMoney <wert> <ziel>)`.

  Was **nicht** geht: der Name, den `find_node_types` unter `context_pins` ausgibt. Dort erscheint
  die Fremdvariable als `Variables|Default|SetMoney` — damit schlägt `create_node` mit
  „does not exist" fehl, auch mit `declaring_class`. Genau diese Fehlmeldung hat zur falschen
  Schlussfolgerung geführt. **Bei „does not exist" erst die `Class|…`-Form probieren, bevor man
  etwas für unmöglich erklärt.**
- **Lazy Registrierung gilt auch hier:** solange kein Graph das fremde Blueprint referenziert,
  liefert `find_node_types` dafür eine leere Liste. Einen Cast-Node anlegen, dann erneut suchen.
- **Enum-Literale fallen still auf Index 0 zurück**, wenn der Name nicht auflöst. `"Gamepad"` wurde
  kommentarlos als `NewEnumerator0` geschrieben, ohne Fehler. Beim Schreiben **immer** die internen
  Namen `NewEnumerator0`, `NewEnumerator1`, … verwenden und das Ergebnis per `read_graph_dsl`
  gegenprüfen. Exec-Pins von `SwitchonE_<Enum>` heißen ebenfalls `NewEnumerator<N>`.
- **Funktionen mit Rückgabewert:** Steht `(return …)` im DSL und existiert bereits ein ReturnNode
  (den `add_function_param` anlegt), bricht der Schreibvorgang ab. Entweder ohne Rückgabewert bauen
  und die Verzweigung beim Aufrufer lassen, oder: Body ohne `return` schreiben, dann
  `add_function_param`, dann `connect_pins` von Hand.
- **Type-Ids verschlucken Unterstriche.** `S_PlayerStats` → `Utilities|Struct|MakeSPlayerStats`,
  `ZZTest_interface` → `ZZTestInterface`. Wer nach dem Asset-Namen mit Unterstrich sucht, findet
  nichts und hält es fälschlich für unmöglich.
- **Node-Registrierung ist träge.** Make-/Break-/SetMembers-Nodes eines eigenen Structs tauchen erst
  auf, wenn der Struct irgendwo in einem Graph benutzt wird. Eine leere `find_node_types`-Antwort
  heißt **nicht** „gibt es nicht“ — erst Namensform prüfen, dann eine Referenz anlegen, dann erneut
  suchen.
- **`add_struct_function_param`** legt Parameter beliebiger UStruct-Typen an, auch eigener —
  `add_function_param` kann das nicht. Bei einem Struct-Rückgabewert liegen die Felder danach als
  einzelne Pins am Return-Node; ein Make-Node wird gar nicht gebraucht.
- **`ProgrammaticToolset` lohnt sich ab drei Aufrufen.** `execute_tool_script` bündelt beliebige
  Toolset-Aufrufe in einem Roundtrip. Einmalig `get_execution_environment` lesen. Vorsicht: die
  Parameternamen dort sind die echten — `add_function_param` will **`param_type`**, nicht
  `type_name` (anders als `add_variable`).
- **`find_node_types` ist unvollständig, kein Beweis.** Eine Funktion auf einem fremden Blueprint
  (`Class|BPWeapon|Fire`) taucht dort teils gar nicht auf, lässt sich per `write_graph_dsl` aber
  anstandslos anlegen. Nicht listen heißt nicht „gibt es nicht" — die `Class|…`-Form einfach
  ausprobieren.
- **Engine-Enums lösen über den Klarnamen auf.** `"SnapToTarget"`, `"KeepWorld"`, `"NoCollision"`,
  `"AlwaysSpawn"` werden korrekt geschrieben. Die `NewEnumerator<N>`-Regel weiter unten gilt nur für
  **eigene** Enums. Trotzdem gegenprüfen, der Rückfall auf Index 0 ist still.
- **Klammer-Type-Ids braucht man meist gar nicht.** `Math|Conversions|ToString(Integer)` bricht den
  Parser — aber der DSL setzt Konvertierungen von selbst ein. Den Integer direkt an den String-Pin
  hängen, fertig. Gleiches gilt für Int→Float.
- **Viele Engine-Nodes haben `self` als erstes positionales Argument.** `Transformation|SetActorScale3D`
  nimmt `(self, NewScale3D)`, nicht `(NewScale3D)`. Bei „Could not connect pin … The pins may be
  incompatible types" erst `get_node_type_pins` lesen und dann mit **benannten** Pins schreiben
  (`:self self :NewScale3D …`) — das ist ohnehin die robustere Schreibweise.
- **Komponenten zur Laufzeit gehen doch.** `AddComponent|Movement|AddProjectileMovementComponent`
  und Geschwister existieren als Graph-Nodes. Die Einschränkung weiter unten betrifft nur den
  **Konstruktionsbaum** (SCS) im Editor, nicht das Anhängen im laufenden Spiel.
- **Enhanced-Input-Events** heißen `Input|EnhancedActionEvents|EnhancedInputActionIA_<Name>` und
  lassen sich nur per `create_node` anlegen, nicht über die `(event …)`-Form des DSL. Danach
  `Triggered` und `ActionValue` von Hand verbinden.
- Nach dem Schreiben liegen alle Nodes auf Position `0,0` übereinander. Der Nutzer muss im Graph
  einmal aufräumen — das vorher ansagen, sonst wirkt es wie ein Fehler.

- **`(return …)` legt den Output-Parameter NICHT an.** Existiert kein ReturnNode, bricht der
  Schreibvorgang genau dort **still** ab — kein Fehler, der Rest des Bodys fehlt einfach. Und
  `add_function_param` **vor** dem DSL-Schreiben nützt nichts, der Schreibvorgang entfernt den
  ReturnNode wieder. Funktionierende Reihenfolge (22.09., `GetSpawnTransform`):
  1. Alte Nodes löschen, 2. Body **ohne** `(return)` schreiben und das Ergebnis per `bind` an einen
  Node hängen, 3. `add_function_param`, 4. `connect_pins` von Hand: Entry `then` →
  ReturnNode `execute`, Wert-Pin → Return-Pin.
- **Ein stiller Abbruch ist die Normalform des Fehlschlags.** Nach *jedem* `write_graph_dsl` mit
  `find_nodes` + `get_node_infos` prüfen, ob die letzten Statements wirklich Nodes wurden. Bekannte
  Auslöser: `(return …)` ohne Parameter (s. o.) und `(select …)` über **Vektoren**.
- **`select` kann keine Vektoren** — dafür `Math|Vector|SelectVector` (positional: A, B, bPickA).
  Über Floats und Ints funktioniert `select` und wird zu `Utilities|Select`.
- **`(* vektor float)` wird zu `vector*vector`** und rechnet damit Unsinn. Es gibt keinen
  schreibbaren `vector*float`-Node. Ausweg: den Skalar in den Vektor ziehen
  (`MakeVector :X rad :Y 0 :Z 0`, dann `RotateVector`) oder komponentenweise multiplizieren.
- **Pure Nodes werden pro Verwendung neu ausgewertet — auch wenn sie gebunden sind.** `bind` teilt
  den *Node*, nicht den *Wert*. `(bind w (+ (GetCurrentWave) 1))`, dann `SetCurrentWave w` und
  später nochmal `w` → das zweite `w` rechnet mit dem bereits erhöhten Wert. Bei allem, was einen
  Zustand ändert: **erst setzen, dann die Variable zurücklesen.** (Kostete am 22.09. eine Welle
  Versatz in der Tabellenzeile.)
- **Pure Nodes mit mehreren Ausgängen sind eine Falle, wenn Zufall im Input steckt.**
  `(bind (proj ok) (ProjectPointtoNavigation …))` sieht aus wie ein Aufruf mit zwei Ergebnissen —
  tatsächlich wird der Node pro gelesenem Pin **erneut** ausgewertet. Hängt am Input ein
  `RandomFloatInRange`, prüft man am Ende einen anderen Wert, als man benutzt. Ergebnis erst in
  Member-Variablen schreiben (Setter sind impure, werten einmal aus), danach nur noch die
  Variablen lesen.
- **Eine Funktion leeren, auf die jemand zugreift, bricht den nächsten Schreibvorgang.** Mit dem
  ReturnNode verschwindet der Output-Parameter, der Aufrufer zeigt ins Leere, und jedes
  `write_graph_dsl` scheitert am Compile — auch das, mit dem man die Funktion gerade reparieren
  will. Reihenfolge: **erst den Aufrufer leeren**, dann die Funktion neu bauen, dann den Aufrufer
  neu schreiben.
- **Neu angelegte Variablen sind nicht Instance Editable.** Im Level sind sie am Actor damit weder
  sicht- noch einstellbar, und `set_properties` auf die Instanz scheitert mit „could not be set".
  Für alles, was getunt werden soll: `set_variable_instance_editable`.
- **`Class|X|Fn`: `self` steht bei Funktionen als erstes Argument, bei Variablen-Settern als
  letztes.** Verlässlich ist nur die benannte Form: `(Class|BPEnemyBase|ApplyWaveProfile :self E …)`.
- **`get_node_type_pins` legt zum Messen echte Nodes im angegebenen Graphen an** und räumt sie
  danach wieder weg. Die in der Antwort genannten `refPath`s zeigen deshalb auf Nodes, die es nicht
  mehr gibt — nicht als Ziel für `connect_pins` benutzen.
- **`Utilities|Array|Get(acopy)` ist wegen der Klammern nicht schreibbar.** Für den Zugriff auf ein
  Element ohne Index reicht `Utilities|Array|RandomArrayItem`; wo der Index zählt, lieber über
  `Utilities|Array|Length` + `select` rechnen als den Get-Node zu erzwingen.

- **Ein fehlgeschlagener Blueprint-Compile blockiert den ganzen Editor.** Unreal kompiliert vor
  jedem PIE-Start die geänderten Blueprints; schlägt das fehl, kommt ein **modaler Dialog**
  („… failed to compile. Play anyway?"). Solange der offen ist, antwortet **kein** MCP-Aufruf mehr,
  und jeder Call läuft in den Timeout. **Wenn ein Aufruf länger als zwei Minuten hängt:** nicht
  weiter am Editor rütteln, sondern per Bash `Saved/Logs/achachay.log` lesen — die Datei liegt
  außerhalb des Editors und verrät die Ursache sofort (`Blueprint failed to compile: <Name>`).
  Auflösen kann den Dialog nur der Nutzer.
- **Nach jeder Signaturänderung die Aufrufer selbst kompilieren.** Wird an einer Funktion mit
  Rückgabewert geschraubt (Return-Knoten neu, Parameter neu), stehen die aufrufenden Blueprints
  bis zu ihrem nächsten Compile auf einem veralteten Pin. `compile_blueprint` auf die Aufrufer
  räumt das auf — sonst macht es PIE, und zwar mit dem Dialog von oben.
- **`add_event` mit einem Namen, der kein Override trifft, legt still ein Custom Event an**, das
  nie feuert. Der interne Name ist oft ein anderer als im Editor sichtbar: Die GameInstance zeigt
  „Event Init", intern heißt es **`ReceiveInit`**. Nach `add_event` am `type_id` prüfen:
  `AddEvent|EventInit` ist der Override, `AddEvent|Custom|Init` ist es nicht.
- **Engine-Events, die einen `Parent:`-Aufruf brauchen, besser gar nicht überschreiben.** Den
  Parent-Knoten kann das Toolset nicht anlegen (`find_node_types` kennt ihn nicht), und ein
  `Event Init` ohne `Parent: Init` überspringt die Subsystem-Initialisierung der GameInstance.
  Ausweg: eine eigene `EnsureLoaded`-Funktion mit Merker-Bool, gerufen vom ersten Verbraucher.

### Assets

- **DataTables sind per Toolset voll bedienbar** — `create`, `add_rows`, `set_rows`, `get_rows`,
  `get_schema`. Und zwar **auch mit einem selbstgebauten Struct als Row-Struct**, obwohl
  `search_row_structs` nur native `FTableRowBase`-Abkömmlinge auflistet und eigene Structs
  verschweigt. Die leere Liste ist kein Beweis — `create` mit dem Struct-Pfad einfach aufrufen.
  Die Spaltennamen in `set_rows`/`get_rows` sind die Feldnamen in **camelCase** (`runnerCount`).
- **`AssetTools` kann keine Assets erzeugen** — nur `duplicate`, `move`, `delete`, `create_folder`.
  Neues Asset gleichen Typs: ein bestehendes duplizieren und die Properties umsetzen (hat für
  `IA_Dash` → `IA_Aim` mit `ValueType: Axis2D` funktioniert).
- Enums, Structs, Widgets und Input Actions „from scratch" gehen nicht. **Vom Nutzer anlegen lassen**
- **`BlueprintTools.create` kann keine Blueprint Interfaces.** Mit `asset_type`
  `/Script/CoreUObject.Interface` entsteht ein **normales** Blueprint (`BlueprintType: BPTYPE_Normal`)
  mit UInterface als Elternklasse. Es kompiliert, nimmt Funktionen an und liefert sogar
  `Class|<Name>|<Fn>`-Nodes — taucht im Editor aber **nicht** im Interface-Picker auf. Vom Nutzer
  anlegen lassen. Prüfbar über `get_asset_tags` → `BlueprintType`.
- **Ein Interface einem Blueprint zuzuweisen geht gar nicht.** Kein Werkzeug dafür, und die
  Blueprint-Asset-Properties sind über `refPath` nicht erreichbar — der Pfad löst auf die generierte
  Klasse auf. Immer vom Nutzer setzen lassen.
- **Komponenten kann man dem Konstruktionsbaum eines Blueprints nicht hinzufügen.** Workaround: eine
  Elternklasse wählen, die die gewünschte Komponente mitbringt — `StaticMeshActor` statt `Actor`,
  wenn ein sichtbares Mesh gebraucht wird. (Zur Laufzeit geht es sehr wohl, siehe oben.)
- **Vorsicht bei `StaticMeshActor` als Elternklasse: Mobility steht auf `Static`.** Damit ignoriert
  der Actor jedes `SetActorLocation` im Spiel — lautlos, ohne Fehler. Am CDO
  (`…Default__X_C:StaticMeshComponent0`) auf `Movable` setzen. Hat bei `BP_Projectile` zugeschlagen.
- **`PrimitiveTools` hilft hier nicht.** Es hängt Mesh-Primitive an **Actors im Level**, nicht an
  Blueprint-Klassen, und kennt ohnehin nur Würfel, Kugel, Zylinder, Kegel.

### Programmatic Toolset

- Erlaubte Module: nur `math, copy, time, datetime, re, json`. Kein `collections`.
- `_StrictDict.get()` akzeptiert **keinen** Default-Wert — immer `d["key"]` mit vorheriger Prüfung.
- **Ein Fehler bricht das ganze Skript ab.** Steht der Schreibvorgang am Ende, wird nichts
  persistiert. Bei mehrstufigen Änderungen jeden Schritt einzeln absichern oder Zwischenstände
  zurückgeben.
- `find_nodes` braucht zwingend `title` (leerer String für „alle").

---

## 4. Verifizierter Stand des Inputs

Damit niemand nochmal die falsche Schlussfolgerung zieht — das hier **funktioniert** und ist korrekt
konfiguriert:

`IMC_Gameplay` → `DefaultKeyMappings`, 9 Einträge:

| Action | Key | Modifier |
|---|---|---|
| IA_Dash | Gamepad Left Shoulder | — |
| IA_Dash | Gamepad Left Thumbstick Button | — |
| IA_Dash | Space Bar | — |
| IA_Move | Gamepad Left Thumbstick 2D-Axis | 2 |
| IA_Move | W | — |
| IA_Move | A | 2 (Swizzle, Negate) |
| IA_Move | S | 1 (Negate) |
| IA_Move | D | 1 (Swizzle YXZ) |
| IA_Aim | Gamepad Right Thumbstick 2D-Axis | — |

Bewegung, Dash und Gamepad laufen im Spiel. `IA_Move` und `IA_Dash` werden **nicht** in
`PC_Outside`/`PC_Safehouse` behandelt — die dortigen Event-Nodes sind leer. Wo die Verdrahtung
tatsächlich sitzt, ist über MCP nicht einsehbar (vermutlich Level Blueprint). **Das ist kein Fehler
und muss nicht „repariert" werden.**

---

## 4b. Handverdrahtungen (Stand 14.09.2026)

Diese drei Verbindungen fehlen, weil sie auf ein fremdes Blueprint zielen und daher nicht per
Toolset erzeugt werden können. Sie sind **kein Versehen** — nicht „aufräumen", sondern vom Nutzer
setzen lassen.

**Erledigt (Stand 14.09.).** Die ersten beiden Zeilen sind verdrahtet — der Character cached die
GI in `StoreEssentialVariables` und ruft `SetDeviceKeyboardMouse` darüber auf. Die dritte ist
weiterhin offen, aber **nicht mehr Handarbeit**: mit der korrigierten `Class|…`-Form (§3) lässt sie
sich per Toolset bauen. Spätestens bei Schritt 31 (Levelwechsel) erledigen.

| Wo | Was | Stand |
|---|---|---|
| `BP_PlayerCharacter.UpdateActiveInputDevice`, hinter dem Branch | `Get Game Instance` → `Cast to GI_Achachay` → `SetDeviceKeyboardMouse` | ✔ erledigt |
| `BP_PlayerCharacter.UpdateGamepadAim`, hinter dem Branch | dasselbe mit `SetDeviceGamepad` | ✔ erledigt |
| `BP_PlayerCharacter` auf `BeginPlay` | `Get ActiveInputDevice` → Switch → `Set UsingGamepad` | offen, per Toolset baubar |

Vertrag zwischen den beiden Speicherorten: **Der Character schreibt, die UI liest.** `UsingGamepad`
am Character ist ein lokaler Cache für die Zielrichtung pro Frame; `ActiveInputDevice` in der
GameInstance ist der Datensatz für UI und Levelwechsel. Die GI wird nie zurück in den Bool gelesen —
mit Ausnahme der einen zurückgestellten BeginPlay-Initialisierung oben.

---

## 4c. Merkposten für Phase 1

**Die Waffe muss entlang der Control Rotation feuern, nicht entlang `GetActorForwardVector`.**
Am Character steht `bUseControllerRotationYaw = false` und am CharacterMovement
`bUseControllerDesiredRotation = true` mit `RotationRate.Yaw = 1080`. Der Körper dreht sich also
bewusst mit Verzögerung nach, während die Control Rotation sofort auf dem Ziel steht. Wer aus der
Actor-Vorwärtsrichtung schießt, trifft bei schnellen Mausbewegungen sichtbar daneben.

---

## 5. Konventionen

- Alles unter `Content/Achachay/`, gegliedert in `Core`, `Player`, `Levels`, `Art`, `RecordPlayer`.
- Präfixe: `BP_`, `GM_`, `PC_`, `GI_`, `IA_`, `IMC_`, `L_`, `SM_`, `M_`, `E_`, `S_`, `SG_`.
- Sprache im Dialog mit dem Nutzer: **Deutsch**.
- Der EventGraph bleibt schlank — Logik gehört in Funktionen.
- Zustand, der einen Levelwechsel überlebt, gehört in `GI_Achachay`; nicht in den GameState (der
  stirbt beim Wechsel) und nicht in den PlayerController (dreimal vorhanden).
- Kein Replication-Code. Single Player.
- **`docs/PLAN.md` ist die einzige Quelle für den Plan.** Es gibt ein älteres Artifact mit demselben
  Inhalt — das ist bewusst stillgelegt und wird **nicht** mehr nachgezogen. Nicht "hilfsbereit"
  synchronisieren.

---

## 6. Vor jeder Änderung an fremden Assets

1. Lesen und den gelesenen Zustand **dem Nutzer zeigen**, bevor geschrieben wird.
2. Bei Unstimmigkeit zwischen Messung und Nutzeraussage: **nicht schreiben**, sondern klären.
3. Schreibende Änderungen an Assets, die der Nutzer selbst gebaut hat, vorher ankündigen.
4. Blueprint-Graphen des Nutzers nicht per `delete_node` leeren, ohne den Inhalt vorher gesichert
   oder abgestimmt zu haben.
