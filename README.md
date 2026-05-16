# Crop Dataset Merger

A professional Python tool to merge and standardize agricultural datasets for Crop Recommendation Systems. This project focuses on data engineering, ensuring consistency between different data sources.

## Project Structure

```text
.
├── main.py              # Application entry point
├── src/                 # Source code package
│   ├── config.py        # Centralized configurations & mappings
│   └── data_pipeline.py # Core logic for merging and cleaning
├── data/                # Data storage (CSV files)
├── requirements.txt     # Python dependencies
└── .gitignore           # Git ignore rules
```

## Features

- **Column Standardization**: Maps various naming conventions (e.g., 'Nitrogen' to 'n') into a unified schema.
- **Label Normalization**: Synchronizes crop names (e.g., 'Mung Bean' and 'mungbean' become identical).
- **Automated Cleaning**: Handles duplicate records and provides median imputation for missing values.
- **Production-Ready**: Modular structure built for scalability and maintainability.

## Dataset Sources

This project consolidates data from the following Kaggle repositories:
- **Source 1**: [Crop Recommendation Dataset (Jitesh Sharma)](https://www.kaggle.com/datasets/jiteshsharma45/crop-recommendation)
- **Source 2**: [Crop Recommendation Dataset (Nishchal Chandel)](https://www.kaggle.com/datasets/nishchalchandel/crop-recommendation)

## Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Setup Environment
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Merging Process
Place your source CSV files in the `data/` directory and run:
```bash
python main.py
```
The standardized dataset will be saved as `output/merged_crop_data.csv`.

## Data Schema
The final merged dataset follows this schema:
- `n, p, k`: Nutrient content (Nitrogen, Phosphorous, Potassium)
- `temperature, humidity, ph, rainfall`: Environmental factors
- `label`: Standardized crop name (lowercase, no spaces)
