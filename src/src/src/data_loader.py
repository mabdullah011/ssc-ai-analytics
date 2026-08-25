import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def load_mock_exam_data(file_name: str = "mock_exam.csv") -> pd.DataFrame:
    """
    Load mock exam dataset from data/ folder.
    Replace with actual data loading logic (Kaggle, Google Drive, API) as needed.
    """
    file_path = DATA_DIR / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")
    return pd.read_csv(file_path)

def load_student_activity(file_name: str = "student_activity.csv") -> pd.DataFrame:
    """
    Load student activity logs (study time, topic attempts, etc.).
    """
    file_path = DATA_DIR / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")
    return pd.read_csv(file_path)
