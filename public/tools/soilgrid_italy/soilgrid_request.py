# =========================
# SoilGrids via WCS 1.0.0 → Italia EPSG:3035
# Props: clay, silt, sand | All depths
# Richiede: OWSLib + pyproj
# =========================

# %%capture
!pip -q install owslib pyproj tqdm

from owslib.wcs import WebCoverageService
from pyproj import Transformer
from pathlib import Path
from tqdm.auto import tqdm
import os, shutil

# ---- Config ----
PROPS = ["clay", "silt", "sand"]
DEPTHS = ["0-5cm","5-15cm","15-30cm","30-60cm","60-100cm","100-200cm"]
STAT = "mean"

# BBOX Italia in WGS84 (lon_min, lat_min, lon_max, lat_max)
BBOX_ITALY_4326 = (6.75, 36.62, 18.48, 47.12)

# Output
OUT_DIR = "/content/Downloads/SoilGrids_IT_3035"
ZIP_PATH = "/content/Downloads/SoilGrids_IT_3035.zip"
OVERWRITE = False

# ---- Utils ----
def bbox_4326_to_3035(bbox):
    """Proietta bbox da EPSG:4326 a EPSG:3035 e restituisce (minx,miny,maxx,maxy)."""
    lon_min, lat_min, lon_max, lat_max = bbox
    tf = Transformer.from_crs(4326, 3035, always_xy=True)
    xs, ys = [], []
    for x,y in [(lon_min,lat_min),(lon_min,lat_max),(lon_max,lat_min),(lon_max,lat_max)]:
        X, Y = tf.transform(x, y)
        xs.append(X); ys.append(Y)
    return (min(xs), min(ys), max(xs), max(ys))

def wcs_url(prop):
    return f"https://maps.isric.org/mapserv?map=/map/{prop}.map"

# Prepara bbox in EPSG:3035 (metri)
bbox_3035 = bbox_4326_to_3035(BBOX_ITALY_4326)

Path(OUT_DIR).mkdir(parents=True, exist_ok=True)

# Loop proprietà × profondità
for prop in PROPS:
    prop_dir = Path(OUT_DIR) / prop
    prop_dir.mkdir(exist_ok=True)

    # Istanzia WCS 1.0.0 per la proprietà
    wcs = WebCoverageService(wcs_url(prop), version="1.0.0")  # stabile con SoilGrids

    for d in DEPTHS:
        cov_id = f"{prop}_{d}_{STAT}"
        out_tif = prop_dir / f"{cov_id}_IT_EPSG3035.tif"
        if out_tif.exists() and not OVERWRITE:
            print(f"✔ Già presente: {out_tif}")
            continue

        print(f"↓ Scarico {cov_id} → {out_tif}")
        # Richiesta GetCoverage (WCS 1.0.0): crs urn EPSG:3035, bbox in metri, risoluzione 250 m
        resp = wcs.getCoverage(
            identifier=cov_id,
            crs="urn:ogc:def:crs:EPSG::3035",
            bbox=bbox_3035,
            resx=250,               # SoilGrids risoluzione nativa ~250 m
            resy=250,
            format="GEOTIFF_INT16"  # formato standard per questi layer
        )
        with open(out_tif, "wb") as f:
            # stream to file con barra di avanzamento
            data = resp.read()
            for i in tqdm(range(0, len(data), 2**20), unit="B", unit_scale=True, desc=out_tif.name):
                f.write(data[i:i+2**20])

print("✅ Download completato:", OUT_DIR)

# Zippa e scarica
if os.path.exists(ZIP_PATH):
    os.remove(ZIP_PATH)
shutil.make_archive(ZIP_PATH[:-4], "zip", OUT_DIR)
print("📦 ZIP pronto:", ZIP_PATH)

try:
    from google.colab import files
    files.download(ZIP_PATH)
    print("⬇️ Avviato download dello ZIP sul tuo computer.")
except Exception:
    print(f"Recupera manualmente lo ZIP qui: {ZIP_PATH}")