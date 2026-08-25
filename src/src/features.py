import pandas as pd
import numpy as np

def create_study_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Engineer features from raw student activity data.
    """
    df = df.copy()
    
    # Example features
    df["study_consistency"] = df["study_hours"].rolling(window=7).std().fillna(0)
    df["attempt_rate"] = df["topics_attempted"] / df["topics_total"].replace(0, np.nan)
    df["past_avg_score"] = df.groupby("student_id")["score"].transform("mean")
    
    return df

def create_topic_weakness(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify weak topics based on attempt rate and score.
    """
    df = df.copy()
    df["topic_weakness"] = np.where(
        (df["attempt_rate"] < 0.5) & (df["score"] < df["score"].median()),
        1, 0
    )
    return df
