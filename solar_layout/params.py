"""Parameter loading. Milestone 2: read params.csv with the csv module and return the values.

Decide what should happen when a value is missing or negative before writing the code. COMPLETE
"""

""" TO-DO Milestone 3:  draws a second rectangle inside the site boundary on its own layer, offset by setback_m on every edge"""
"""What are the four corner coordinates of the setback rectangle?
What is the width and height of the area inside it?
What condition on the three numbers makes the setback invalid? Think about when that inner rectangle stops existing."""

import math


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