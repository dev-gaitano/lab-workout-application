# Workout API

The API is be responsible for tracking workouts and their associated exercises.
Each workout can include multiple exercises, with sets, reps, or duration attached to each.
Exercises are reusable so a trainer can add the same exercise to various workouts.

## Getting started

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

- API calls are configured to proxy to `http://localhost:5000`
