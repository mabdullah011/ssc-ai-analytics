import joblib
from pathlib import Path

MODELS_DIR = Path(__file__).parent.parent / "models"

def save_model(model, file_name: str):
    """
    Save trained model to models/ folder.
    """
    MODELS_DIR.mkdir(exist_ok=True)
    file_path = MODELS_DIR / file_name
    joblib.dump(model, file_path)
    print(f"Model saved: {file_path}")

def load_model(file_name: str):
    """
    Load trained model from models/ folder.
    """
    file_path = MODELS_DIR / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"Model not found: {file_path}")
    return joblib.load(file_path)
