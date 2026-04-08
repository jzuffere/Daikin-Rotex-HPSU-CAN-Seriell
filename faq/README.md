# ❓ FAQ – Häufig gestellte Fragen

## 🔹 Welche Funktionen bietet das Projekt, die von der Rotex-/Daikin-Luftwärmepumpe nicht nativ bereitgestellt werden:

### 1 - Spreizung
Die Spreizung (auch als Delta-Temperatur bezeichnet) ist die Differenz zwischen der Vorlauftemperatur (Tv) und der Rücklauftemperatur (Tr). Sie ist einer der zentralen Leistungsparameter einer Luftwärmepumpe und spielt eine entscheidende Rolle bei der Effizienzanalyse und Fehlerdiagnose. Siehe auch: [Glättung der Spreizung und Thermischen Leistung](#-warum-wird-spreizung-und-thermische-leistung-geglättet)

### 2 - Thermische Leistung
Die thermische Leistung wird aus Vorlauf-, Rücklauftemperatur und Durchfluss berechnet und im Zeitverlauf geglättet. Sie wird unter anderem benötigt, um einen momentanen COP-Wert zu berechnen.

### 3 - Optimierung des Abtauvorgangs
Die HPSU führt je nach Wetterlage (Außentemperatur und Luftfeuchtigkeit) teilweise alle 25 Minuten einen Abtauvorgang durch. Dabei wird für kurze Zeit (5–7 Minuten) Wärme aus dem Warmwasserspeicher (WW-Tank) entnommen und zum Außengerät geleitet, um den gefrorenen Verdampfer zu enteisen.

Idealerweise würde das DHW-Ventil vollständig geöffnet und der Bypass auf 100 % gesetzt, um zu verhindern, dass Warmwasser in den Fußboden gelangt. Allerdings öffnet die HPSU das Ventil nicht vollständig, sodass ein Teil des Warmwassers dennoch in den Fußboden fließt.

![grafik](../images/ha-can-abtau-optimierung2.png)

Das Projekt bietet hierfür die Option `Abtauoptimierung`, die während des Abtauvorgangs automatisch kurzzeitig die Betriebsart auf `Sommer` umstellt. Dadurch fährt das Bypass-Ventil auf 100%, und das Warmwasser gelangt nicht in den Fußboden. Anschließend wird der Betriebsmodus wieder auf Heizen zurückgesetzt. Der Abtauprozess bleibt dabei unverändert, jedoch sinkt der Wärmeverlust im Warmwasserspeicher.

Effekt:

- Ohne Optimierung: ~1,5 K Wärmeverlust
- Mit Optimierung: ~0,7 K Wärmeverlust

### 4 - Erkennung defekter DHW- und Bypass-Ventile
Die Ventile unterliegen einem natürlichen Verschleiß und funktionieren oft bereits nach 2–6 Jahren nicht mehr einwandfrei. Dies kann dazu führen, dass sie nicht mehr vollständig öffnen oder schließen. Die HPSU erkennt solche Probleme nicht, obwohl sie erhebliche Auswirkungen haben können:
- Der Warmwasserspeicher kühlt unerwartet schnell ab.
- Das Haus wird nicht mehr warm.
- Die Temperaturspreizung steigt nicht über 1K.
- uvm.

Das Projekt überwacht daher kontinuierlich folgende Parameter:
- Vorlauftemperatur (Tv)
- Vorlauftemperatur Backup Heater (TvBH)
- Rücklauftemperatur (Tr)
- Position des DHW-Ventils
- Position des Bypass-Ventils
- Durchfluss

Bei erkannten Fehlfunktionen wird ein entsprechender Fehlercode ausgegeben.

#### Erkennung defekter Ventile
Fall 1: DHW-Ventil = 0 % & Bypass-Ventil = 100 %
- Fehlererkennung ist präzise.
- Bei unzureichendem Schließen oder Öffnen entsteht ein messbarer Temperaturunterschied zwischen Tv und TvBH bzw. TvBH und Tr, der als Fehler gemeldet wird.

Fall 2: DHW-Ventil = 100 % & Bypass-Ventil = 0 %
- Fehlererkennung ist schwieriger.
- Während der Warmwasserbereitung oder im Heizmodus wird die Spreizung überprüft.
- Falls sie über 20 Minuten hinweg nicht den erwarteten Wert erreicht, wird ein Fehler gemeldet.

Die erwartete Spreizung wird anhand von `Tv` interpoliert:
| Tv  | Erwartete Spreizung |
| --- | ------------------- |
| 50° | 4.0K |
| 40° | 3.0K |
| 35° | 2.5K |
| 29° | 1.2K |
| 27° | 0.3K |

## 🔹 Warum wird Spreizung und Thermische Leistung geglättet:
Die gemessenen Werte für Vorlauf (Tv) und Rücklauf (Tr) können je nach Gerät sehr sprunghaft und unregelmäßig sein. Dieses "Rauschen" in den Daten erschwert die Analyse und Fehlererkennung.

Durch den Einsatz eines PID-Reglers und eines Tiefpassfilters werden die Daten geglättet. Dies hat folgende Vorteile:
- Reduzierung von Rauschen und Sprüngen: Die Daten werden stabiler und weniger volatil.
- Bessere Lesbarkeit und Verständlichkeit: Geglättete Daten sind einfacher zu interpretieren.
- Zuverlässige Fehlererkennung: Glatte Daten ermöglichen eine präzisere Identifikation von Fehlverhalten der Pumpe.

## 🔹 Warum kann man `Warmwasser-Soll` nur in 5K-Schritten und `Raum-Soll` nur in 1K-Schritten einstellen?

Standardmäßig sind die Auswahllisten auf wenige gebräuchliche Werte begrenzt, um sie übersichtlich zu halten – besonders auf Smartphones wäre eine vollständige Liste unhandlich.

Beide Entities lassen sich auf zwei Arten an eigene Bedürfnisse anpassen:

### Option 1 – Benutzerdefinierte Auswahlliste (`type: select`)

Über `options` können beliebige Werte innerhalb des gültigen Bereichs eingetragen werden.

**`Warmwasser-Soll`** – gültiger Bereich: 35,0 – 70,0 °C (Schrittweite 0,1 °C)
```yaml
    target_hot_water_temperature_1:
      name: T-WW-Soll1
      type: select
      options:
        40: 40 °C
        41: 41 °C
        45.7: 45.7 °C
        55.1: 55.1 °C
```

**`Raum-Soll`** – gültiger Bereich: 5,0 – 40,0 °C (Schrittweite 0,1 °C)
```yaml
    target_room1_temperature:
      name: Raumsoll 1
      type: select
      options:
        18: 18 °C
        20: 20 °C
        21.5: 21.5 °C
        23.3: 23.3 °C
```

### Option 2 – Numerisches Eingabefeld (`type: number`)

Statt einer Auswahlliste kann ein numerisches Eingabefeld verwendet werden. Es prüft automatisch, ob der eingegebene Wert im gültigen Bereich liegt.

```yaml
    target_hot_water_temperature_1:
      name: T-WW-Soll1
      type: number

    target_room1_temperature:
      name: Raumsoll 1
      type: number
```