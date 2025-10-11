# Raster

## Estrazione delle informazioni dei raster

### 1) QGIS (senza codice)

* **EPSG**: tasto destro sul layer → *Proprietà* → *Informazioni* → “CRS” (es. `EPSG:3035`).
* **NoData**: *Proprietà* → *Trasparenza* → “Valori NoData band” (oppure *Informazioni* mostra il NoData se definito).
* **Title/Abstract** (se presenti come metadati): *Proprietà* → *Metadati* → “Titolo”, “Abstract/Descrizione”.

> Nota: molti GeoTIFF **NON** hanno Title/Abstract incorporati; spesso stanno in un file `.xml` di metadati a lato (ISO 19139/INSPIRE). Se non li vedi, probabilmente il raster non li contiene.

---

### 2) Da riga di comando (GDAL)

```bash
# Info complete
gdalinfo your_raster.tif

# Solo EPSG in WKT/EPSG (se riconosciuto)
gdalinfo -json your_raster.tif | jq -r '.coordinateSystem?.wkt'   # (facoltativo, se usi jq)

# Cerca NoData (per band 1)
gdalinfo your_raster.tif | grep -i "NoData"

# Metadati (Title/Abstract se presenti)
gdalinfo your_raster.tif | sed -n '/Metadata:/,/Image Structure Metadata:/p'
```

Cose da cercare nell’output:

* **EPSG**: nel blocco *Coordinate System is:* (o nel JSON).
* **NoData**: in *Band 1* → `NoData Value=...`.
* **Title/Abstract**: nel blocco *Metadata* come `TITLE=...`, `ABSTRACT=...` oppure `TIFFTAG_IMAGEDESCRIPTION`.

---

### 3) Python – rasterio

```python
import rasterio

path = "your_raster.tif"
with rasterio.open(path) as ds:
    epsg = ds.crs.to_epsg()              # -> es. 3035
    nodata = ds.nodata                   # -> es. -9999 o None
    tags = ds.tags()                     # metadati dataset (dominio DEFAULT)
    title = tags.get("TITLE") or tags.get("TIFFTAG_DOCUMENTNAME")
    abstract = tags.get("ABSTRACT") or tags.get("TIFFTAG_IMAGEDESCRIPTION")

print(epsg, nodata, title, abstract)
```

---

### 4) Python – GDAL (bindings ufficiali)

```python
from osgeo import gdal, osr

ds = gdal.Open("your_raster.tif")
band = ds.GetRasterBand(1)
nodata = band.GetNoDataValue()

# EPSG
srs = osr.SpatialReference()
srs.ImportFromWkt(ds.GetProjection())
srs.AutoIdentifyEPSG()
epsg = srs.GetAttrValue("AUTHORITY", 1)   # stringa tipo "3035"

# Metadati
md = ds.GetMetadata()  # dict
title = md.get("TITLE") or md.get("TIFFTAG_DOCUMENTNAME")
abstract = md.get("ABSTRACT") or md.get("TIFFTAG_IMAGEDESCRIPTION")

print(epsg, nodata, title, abstract)
```

---

### Suggerimenti pratici

* Se **EPSG risulta None**: il raster ha un WKT non mappato a un EPSG noto. In QGIS imposta/definisci il CRS corretto (o usa `gdalsrsinfo` per tradurre il WKT), poi salva/copialo con CRS riconosciuto.
* Se **NoData è vuoto**: non è definito a livello di band. Puoi impostarlo con `gdal_edit.py -a_nodata -9999 your_raster.tif`.
* **Title/Abstract mancanti**: aggiungili con:

  ```bash
  gdal_edit.py -mo "TITLE=Mio Raster" -mo "ABSTRACT=Descrizione breve" your_raster.tif
  ```

  (saranno poi visibili in `gdalinfo`/QGIS).

## No Data

Ottima domanda 👍

---

### Cosa significa il valore **NoData** in un raster

Un raster è una griglia di celle (pixel) con valori numerici. Non sempre tutte le celle hanno un dato valido:

* possono esserci aree **fuori dal dominio** (es. un’immagine satellitare quadrata che copre mare e terra, ma tu hai solo dati di temperatura sul mare).
* possono esserci pixel **mascherati** (nuvole, errori di misura, aree senza osservazioni).
* possono esserci **aree non calcolate** (ad esempio in un modello di erosione solo sulle superfici agricole).

Il valore **NoData** è un numero speciale scritto dentro il raster che segnala:

> “questo pixel non rappresenta un valore reale, trattalo come *vuoto*”.

---

### Perché è importante

* **Analisi corrette**: gli algoritmi GIS ignorano i pixel NoData nei calcoli (media, somma, statistiche).
* **Visualizzazione**: i software possono rendere trasparenti i pixel NoData per mostrare solo i dati validi.
* **Operazioni raster**: in un’operazione pixel-per-pixel, se una cella è NoData, il risultato rimane NoData (per non contaminare i dati).

---

### Esempio pratico

Immagina un raster di altimetria (DEM):

* Valori validi = quote in metri (0–2500 m).
* NoData = `-9999`.

#### In QGIS:

* Se non definisci il NoData, i pixel vuoti potrebbero comparire come celle nere con valore `-9999`, falsando le statistiche e la visualizzazione.
* Se imposti NoData = `-9999`, QGIS li renderà trasparenti e le statistiche ignoreranno quei pixel.

---

#### In Python con `rasterio`

```python
import rasterio
import numpy as np

with rasterio.open("dem.tif") as src:
    arr = src.read(1)
    nodata = src.nodata

    # Maschera i valori nodata
    masked = np.ma.masked_equal(arr, nodata)

print("Valore NoData:", nodata)
print("Media DEM (solo valori validi):", masked.mean())
```

Se il raster ha `nodata=-9999`, i pixel con -9999 non entreranno nel calcolo della media.

---


