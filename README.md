# AI-Driven Fitness Coach (Demo)

This repository is a lightweight demo of an AI-driven fitness coach.
It shows how activity logs can be processed to generate daily
workout and meal suggestions. This is a rule-based demo — no ML yet.

## Included files
- `sample_data.json` - mock wearable activity logs
- `data_ingestion.py` - loads and validates activity logs
- `workout_recommender.py` - rule-based workout suggestions
- `meal_recommender.py` - rule-based meal suggestions
- `main.py` - runs the demo
- `requirements.txt` - empty (no external dependencies)

## How to run
```bash
python main.py
