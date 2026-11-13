"""DXF drawing. Milestone 1: draw the site boundary as a closed rectangle on its own layer.""" """COMPLETE"""
"""Milestone 2: read parameters from params.csv + error handling"""

import math
import ezdxf
import csv


def validate_parameters(params):
    try:
        width_m = float(params["site_width_m"])
    except KeyError as error:
        raise ValueError("Missing site width column") from error
    except (TypeError, ValueError) as error:
        raise ValueError("Site width must be a number") from error
    try:
        height_m = float(params["site_height_m"])
    except KeyError as error:
        raise ValueError("Missing site height column") from error
    except (TypeError, ValueError) as error:
        raise ValueError("Site height must be a number") from error
    if not all((width_m > 0, height_m > 0, math.isfinite(width_m), math.isfinite(height_m))):
        raise ValueError("Site dimensions must be positive finite numbers")
    return width_m, height_m

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
   
