# CatBoost AOD Project

This repository contains a refactored version of a Jupyter notebook demonstrating the use of CatBoost for Anomaly/Outlier Detection (AOD). The original notebook has been modularized into a well-structured Python project, following best practices for maintainability, testability, and scalability.

## Project Structure

```
catboost_aod_project/
├── data/
│   └── raw/                # Raw data files
├── models/                 # Trained models
├── notebooks/
│   └── catboost-depps-aod.ipynb  # Original Jupyter notebook
├── src/
│   ├── catboost_aod/
│   │   ├── __init__.py
│   │   ├── data_processing.py  # Data loading and preprocessing functions
│   │   └── model_training.py   # Model training and evaluation functions
│   └── main.py             # Main script to run the AOD pipeline
├── tests/                  # Unit and integration tests
├── .gitignore              # Git ignore file
├── README.md               # Project README
├── requirements.txt        # Python dependencies
└── setup.py                # Project installation (optional, for larger projects)
```

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/catboost_aod_project.git
    cd catboost_aod_project
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Place your raw data:**

    Ensure your `catboost-depps-aod.csv` (or similarly named) data file is placed in the `data/raw/` directory.

2.  **Run the AOD pipeline:**

    ```bash
    python src/main.py
    ```

    This script will load the data, preprocess it, train a CatBoost model, and evaluate its performance.

## Contributing

Contributions are welcome! Please see `CONTRIBUTING.md` for details on how to contribute.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

For any questions or feedback, please open an issue in this repository.


