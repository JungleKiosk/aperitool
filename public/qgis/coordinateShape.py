from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsPointXY
import csv

# 1. Get the active layer
layer = iface.activeLayer()
if not layer or not layer.isValid():
    raise Exception("No valid layer selected. Please select a layer in the Layers panel first.")

# 2. Ensure features are selected
selected = layer.selectedFeatures()
if not selected:
    raise Exception("No features selected. Please select at least one feature in the layer.")

# 3. Define the output CSV path
#    NOTE: change the filename each run (e.g. output1.csv, output2.csv) 
#    or you may get a file-in-use error when overwriting.
csv_path = "C:/Users/Minutella Francesco/OneDrive - diagramgroup.it/Desktop/rootsGIS/output_py/output_py_01.csv"

# 4. Open the CSV and write the header row
with open(csv_path, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["feature_id", "vertex_index", "x", "y"])

    # 5. Iterate only over the selected features
    for feat in selected:
        geom = feat.geometry()
        for idx, pt in enumerate(geom.vertices()):
            writer.writerow([feat.id(), idx, pt.x(), pt.y()])

print(f"Coordinates of selected features have been saved to: {csv_path}")
