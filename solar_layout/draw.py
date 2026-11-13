"""DXF drawing. Milestone 1: draw the site boundary as a closed rectangle on its own layer."""

import ezdxf


def draw_site(width_m, height_m, path):
    doc = ezdxf.new("R2010")
    # TODO 1: set the drawing units to meters (look in ezdxf.units)
    # TODO 2: create a layer called SITE_BOUNDARY with a color of your choice
    msp = doc.modelspace()
    # TODO 3: build the four corner points of the rectangle
    # TODO 4: add a closed polyline to msp on the SITE_BOUNDARY layer
    doc.saveas(path)


if __name__ == "__main__":
    draw_site(100, 60, "output/site.dxf")
