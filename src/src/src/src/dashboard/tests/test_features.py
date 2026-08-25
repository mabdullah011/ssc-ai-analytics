import pandas as pd
from src.features import create_study_features, create_topic_weakness

def test_create_study_features():
    df = pd.DataFrame({
        "student_id": [1, 1, 1],
        "study_hours": [2, 3, 2.5],
        "topics_attempted": [5, 6, 4],
        "topics_total": [10, 10, 10],
        "score": [70, 75, 72]
    })
    result = create_study_features(df)
    assert "study_consistency" in result.columns
    assert "attempt_rate" in result.columns

def test_create_topic_weakness():
    df = pd.DataFrame({
        "attempt_rate": [0.3, 0.6, 0.4],
        "score": [50, 80, 60]
    })
    result = create_topic_weakness(df)
    assert "topic_weakness" in result.columns
