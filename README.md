# Uber NYC ETL Pipeline

A data engineering project that extracts, transforms, and loads Uber NYC trip data.

## Tech Stack
- Python
- Pandas
- SQLAlchemy
- SQLite

## Pipeline
1. **Extract** - Downloads 564,516 Uber trip records from FiveThirtyEight
2. **Transform** - Cleans columns, parses timestamps, adds hour/day/month fields
3. **Load** - Stores data into a local SQLite database

## How to Run
```bash
pip install -r requirements.txt
cd src
python main.py
```
