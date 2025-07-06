import pandas as pd
from catboost_aod.data_processing import load_data, preprocess_data, split_data
from catboost_aod.model_training import train_model, evaluate_model

def main():
    # Load data
    df = load_data('/home/ubuntu/catboost_aod_project/data/raw/catboost-depps-aod.csv') # Assuming the data will be placed here

    # Preprocess data
    df_processed = preprocess_data(df)

    # Define features (X) and target (y)
    X = df_processed.drop('target_column', axis=1) # Replace 'target_column' with your actual target column name
    y = df_processed['target_column'] # Replace 'target_column' with your actual target column name

    # Split data
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    accuracy, precision, recall, f1 = evaluate_model(model, X_test, y_test)
    print(f'Accuracy: {accuracy:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')

if __name__ == '__main__':
    main()


