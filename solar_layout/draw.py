"""DXF drawing. Milestone 1: draw the site boundary as a closed rectangle on its own layer.""" """COMPLETE"""
"""Milestone 2: read parameters from params.csv + error handling"""

import ezdxf
import csv

from .params import validate_parameters

def draw_site(width_m, height_m, path):
    doc = ezdxf.new("R2010")
    doc.header["$INSUNITS"] = 6  # 6 indicates meters as the drawing units
    doc.layers.add("SITE_BOUNDARY", color=1)

    msp = doc.modelspace()
    corners = [
        (0, 0),
        (width_m, 0),
        (width_m, height_m),
        (0, height_m),
    ]
    msp.add_lwpolyline(corners, close=True, dxfattribs={"layer": "SITE_BOUNDARY"})
    doc.saveas(path)



if __name__ == "__main__":
    try:
        with open("params.csv", newline="") as params_file:
            params = next(csv.DictReader(params_file), None)
            if params is None:
                raise ValueError("Parameter file must contain a data row")
        width_m, height_m = validate_parameters(params)
        draw_site(width_m, height_m, "output/site.dxf")
    except (OSError, ValueError) as error:
        print(f"Error: {error}")
   
