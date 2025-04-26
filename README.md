# Applied Python Evaluation – Sensor Fusion Simulation

Tento projekt simuluje datový řetězec tvořený třemi zařízeními:
- **f_cam.py** – simulace čelní kamery
- **sensor.py** – simulace referenčního senzoru
- **resim.py** – zpracování dat a sloučení výstupů

## 🧩 Struktura skriptů

### `f_cam.py`
Generuje výstupní CSV soubor `f_cam_out.csv` s následujícími daty:
- `Timestamp`, `FrameID`, `Speed`, `YawRate`, `Signal1`, `Signal2`
- 2000 snímků, rychlost od 60 do ~120 km/h, signály podle zadání

### `sensor.py`
Generuje výstupní CSV `sensor_out.csv` s referenční rychlostí:
- `Timestamp`, `Speed`
- Timestampy po 200 ms s náhodnou odchylkou, rychlost roste od 60 do ~120 km/h

### `resim.py`
Načte oba předchozí CSV soubory a vytvoří `resim_out.csv`, kde:
- `Speed` je průměr mezi aktuální rychlostí z kamery a poslední dostupnou rychlostí ze senzoru (podle času)
- Ostatní sloupce jsou převzaty z kamery

## ▶️ Spuštění

Každý skript se spouští samostatně a přijímá výstupní (nebo vstupní) cestu jako argument:

```bash
python f_cam.py f_cam_out.csv
python sensor.py sensor_out.csv
python resim.py f_cam_out.csv sensor_out.csv resim_out.csv
```
Nebo
```bash
python main.py --f_cam_out ./output/cam.csv --sensor_out ./output/sensor.csv --resim_out ./output/resim.csv


