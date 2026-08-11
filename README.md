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

## API Endpoints

The frontend should expect the following backend endpoints:

### Workouts

- `GET /workouts` - Fetch all workouts
- `GET /workouts/<int:id>` - Fetch a single workout
- `POST /workouts` - Create a new workout
- `DELETE /workouts/<int:id>` - Delete a workout
- `POST workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` - Add an exercise to a workout, including reps/sets/duration

### Exercises

- `GET /exercises` - Fetch all exercises
- `GET /exercises/<int:id>` - Fetch a single exercise
- `POST /exercises` - Create a new exercise
- `DELETE /exercises/<int:id>` - Delete an exercise

## Project structure

```
.
├── README.md                       # Project documentation
├── app.py                          # Application entry point
├── Dockerfile                      # Backend container config
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (local)
├── app/                            # Application package
│   ├── __init__.py                 # Application factory (create_app)
│   ├── config.py                   # App configuration
│   ├── extensions.py               # Flask extensions
│   ├── api/                        # API Blueprints & Modular Routes
│   │   ├── workouts/               # Workouts (routes, service, repository)
│   │   └── exercises/              # Exercises (routes, service, repository)
│   ├── models/                     # Domain data models
│   └── utils/                      # Helper utilities
```
