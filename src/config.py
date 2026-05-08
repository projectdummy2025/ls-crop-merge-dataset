import numpy as np

# --- GLOBAL CONFIG ---
SEED = 42
np.random.seed(SEED)

# File paths
DATA_FILES = [
    'data/Crop_recommendation-1.csv',
    'data/Crop_recommendation-2.csv'
]

# Column standardization map
RENAME_MAP = {
    'N': 'n', 'P': 'p', 'K': 'k',
    'Nitrogen': 'n', 'Phosphorous': 'p', 'Potassium': 'k',
    'Temperature': 'temperature', 'Humidity': 'humidity',
    'PH': 'ph', 'Rainfall': 'rainfall', 'Crop': 'label'
}

COMMON_COLS = ['n', 'p', 'k', 'temperature', 'humidity', 'ph', 'rainfall', 'label']
