# ⚡ Select-Schalter

## `Abtau-Optimierung`

Die HPSU entnimmt während des Abtauvorgangs warmes Wasser aus dem Tank, öffnet aber standardmäßig das DHW-Mischer-Ventil nur, während das BPV-Ventil (Heizkreis) geschlossen bleibt.
Dies führt dazu, dass ein Teil des Warmwassers unnötigerweise in den Fußboden gedrückt wird, was einen Temperaturverlust von bis zu $3\, \text{K}$ pro Zyklus im WW-Tank verursacht.

Die Abtau-Optimierung steuert dem entgegen:
1. Der ESP schaltet die HPSU temporär in den Sommer-Modus.
2. Dadurch wird das BPV-Ventil auf $100\%$ geöffnet.
3. Dies blockiert effektiv den Fluss des warmen Wassers in den Heizkreislauf.

Ergebnis: Der Wärmeverlust des Warmwasserspeichers reduziert sich auf ca. $1{,}5\, \text{K}$ pro Abtauvorgang.

## `Raumthermostat`
Dieser Schalter dient zur temporären Deaktivierung des Heizbetriebs (Kompressor-Sperre) über die HPSU-Steuerung.

- Primärzweck: Steuerung per Home Assistant-Automatisierung.
- Ablauf:
    1. Wird die Innentemperatur (gemessen durch externe Smart-Sensoren, z.B. Zigbee) zu hoch, löst Home Assistant den Schalter aus (`Ein`). Die HPSU stoppt den Kompressor.
    2. Sinkt die Innentemperatur wieder, setzt Home Assistant den Schalter zurück (`Aus`), und die HPSU nimmt den Heizbetrieb wieder auf.
- **Voraussetzung**: Erfordert die Anbindung von smarten Raumtemperatursensoren an Home Assistant.


<br>
<br>
<br>

# ⚡Taster

## `Warmwasser bereiten`

Dieser virtuelle Taster dient dazu, die Warmwasserbereitung der HPSU kurzfristig und zuverlässig per externer Steuerung auszulösen.
- Funktion: Bei Betätigung wird die WW-Soll-Temperatur temporär auf $70\, \text{°C}$ gesetzt und unmittelbar danach automatisch auf ihren ursprünglichen Sollwert zurückgestellt.
- Wirkung: Diese kurzzeitige Änderung der Solltemperatur zwingt die HPSU zuverlässig in den Betriebsmodus WW-Bereiten.
- Vorteil gegenüber `1x Warmwasser`:
    - Die Methode hat sich als zuverlässiger erwiesen.
    - Da es sich um einen Taster handelt, ist kein separates Kommando zur Rückstellung des Zustandes erforderlich. 
- Anwendungsfall: Ideal für die bedarfsgerechte Warmwasser-Anforderung über eine Home Assistant-Automatisierung.