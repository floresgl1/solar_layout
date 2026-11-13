# solar_layout

A small Python tool that reads site and equipment parameters from a CSV and generates a DXF drawing of solar PV module tables inside a site boundary and setback line. The DXF opens in AutoCAD.

**Status: work in progress.** Nothing is implemented yet. The repo currently holds the project layout and a starting skeleton.

## Planned behavior

1. Read site and equipment parameters from `params.csv`.
2. Draw the site boundary and the setback line, each on its own layer.
3. Place rows of module tables inside the setback line.
4. Report table count, area covered, and ground coverage ratio.

## Layout

```
solar_layout/
├── solar_layout/        package code
│   ├── __init__.py
│   ├── draw.py          DXF drawing (site boundary first)
│   └── params.py        CSV parameter loading
├── tests/               pytest tests for the placement math
├── output/              generated DXF files (not committed)
├── params.csv           sample input
├── requirements.txt
└── README.md
```

## Setup

```
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```
python -m solar_layout.draw
```

## Input: params.csv

| column | meaning |
|---|---|
| site_width_m | site width in meters |
| site_height_m | site height in meters |
| setback_m | distance from each site edge to the buildable area |
| table_width_m | module table width |
| table_height_m | module table height |
| row_pitch_m | distance between the start of one row and the next |
| col_gap_m | gap between tables in a row |

## Roadmap

- [ ] M1: draw a site rectangle on a named layer
- [ ] M2: read parameters from CSV
- [ ] M3: setback line
- [ ] M4: place one row of tables
- [ ] M5: place all rows
- [ ] M6: tests and summary report
- [ ] M7: README with screenshot and limitations
