"""Parameter loading. Milestone 2: read params.csv with the csv module and return the values.

Decide what should happen when a value is missing or negative before writing the code.
"""
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