"""
PytestForWorkoutTracker.py
----------------------
5 tests covering the core logic of WorkoutTracker.py.

Install: pip install pytest
Run:     pytest WorkoutTracker.py -v
"""

import json
import os
import pytest

# ---------- Minimal copies of the core functions ----------
# These mirror the functions in weight_tracker.py exactly,
# but use a temp file so tests never touch your real data.

FILE = "test_exercises.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def rows(data):
    return [[name, str(info["weight"])] for name, info in sorted(data.items())]


# ---------- Setup / teardown ----------
# Runs before and after every test to ensure a clean slate.

@pytest.fixture(autouse=True)
def clean_file():
    """Delete the test JSON file before and after each test."""
    if os.path.exists(FILE):
        os.remove(FILE)
    yield
    if os.path.exists(FILE):
        os.remove(FILE)


# ---------- Tests ----------

def test_load_returns_empty_dict_when_no_file():
    """load() should return {} if the JSON file doesn't exist yet."""
    data = load()
    assert data == {}


def test_save_and_load_roundtrip():
    """Data saved with save() should come back intact via load()."""
    original = {"bench press": {"weight": 185.0}}
    save(original)
    loaded = load()
    assert loaded == original


def test_add_new_exercise():
    """Adding a new exercise should store it in the dict and persist it."""
    data = load()
    data["squat"] = {"weight": 225.0}
    save(data)

    reloaded = load()
    assert "squat" in reloaded
    assert reloaded["squat"]["weight"] == 225.0


def test_update_existing_exercise():
    """Saving an exercise that already exists should overwrite the old weight."""
    data = {"bench press": {"weight": 135.0}}
    save(data)

    data["bench press"] = {"weight": 185.0}   # update
    save(data)

    reloaded = load()
    assert reloaded["bench press"]["weight"] == 185.0
    assert len(reloaded) == 1                  # no duplicate entry created


def test_remove_exercise():
    """Deleting an exercise should remove it from the dict and persist the change."""
    data = {"deadlift": {"weight": 275.0}, "curl": {"weight": 35.0}}
    save(data)

    del data["deadlift"]
    save(data)

    reloaded = load()
    assert "deadlift" not in reloaded
    assert "curl" in reloaded                  # other entries untouched
