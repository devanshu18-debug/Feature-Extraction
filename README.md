# Anime Title Feature Extraction

A Python and pandas exercise that parses episode counts and a time field from anime titles in the bundled CSV, then inspects scores and titles in the dataset.

## What it does

- Loads `anime.csv` with pandas.
- Extracts text in parentheses from each title and converts the episode count to an integer.
- Extracts a following title substring into a `Time` column.
- Prints selected rows, the first rows of the dataset, the highest-scoring title or titles, and the first five scores.

## Project files

- `feature_extraction/anime.csv` — input dataset.
- `feature_extraction/feature_extraction.py` — parsing and analysis script.

## Run locally

Install Python 3 and the dependencies:

```bash
python -m pip install numpy pandas
```

Run from the `feature_extraction` directory so the relative CSV path resolves:

```bash
cd feature_extraction
python feature_extraction.py
```

## Current limitations

The parser assumes titles contain the expected parenthesized episode count and uses a fixed-length substring for the following field. Titles with different formats may need additional handling. The script currently prints results rather than saving a cleaned dataset.
