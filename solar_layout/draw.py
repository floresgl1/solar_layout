"""DXF drawing. Milestone 1: draw the site boundary as a closed rectangle on its own layer."""

import ezdxf


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
    draw_site(100, 60, "output/site.dxf")
