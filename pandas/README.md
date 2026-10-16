# Pandas Learning Workspace

A structured workspace for learning Pandas from basics through data cleaning, grouping, merging, and practical creator analytics.

## Folder structure

```text
pandas/
├── data/
│   ├── raw/                         # Original datasets; keep source files here
│   │   ├── creators.csv
│   │   ├── creators.json
│   │   ├── creator.csv
│   │   ├── posts.csv
│   │   ├── frontier-ai-datatset/
│   │   └── sales-dataset/
│   └── processed/                   # Cleaned datasets and generated reports
├── lessons/                         # Small, ordered learning scripts
├── notebooks/                       # Jupyter .ipynb notebooks
├── projects/
│   └── creator_analytics/            # Reusable creator-analysis scripts
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup (Windows)

From this `pandas` directory, open Command Prompt or PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

Then create/open notebooks in `notebooks/`.

## Run a lesson

Run from any working directory; scripts resolve data paths relative to their own files.

```powershell
python lessons/01_series_dataframes.py
python lessons/02_reading_filtering_sorting.py
python lessons/03_data_cleaning.py
python lessons/04_grouping_aggregation.py
python lessons/05_merging_joining_concat.py
python lessons/06_filter_sort_practice.py
python lessons/07_student_analyzer.py
python lessons/08_creator_data_cleaning.py
```

## Run creator analytics projects

```powershell
python projects/creator_analytics/creator_leaderboard.py
python projects/creator_analytics/platform_analytics.py
python projects/creator_analytics/creator_profile_posts.py
```

Generated reports are written to `data/processed/`.

## Important notes

- `data/raw/` contains source datasets; avoid overwriting them.
- `data/processed/` contains generated output files.
- `notebooks/` is for interactive exploration; scripts in `lessons/` are for repeatable practice.
- The folder name `frontier-ai-datatset` is retained as in the source archive to avoid silently renaming a dataset directory.
- Do not commit passwords, API keys, `.env` files, or private datasets to a public repository.
