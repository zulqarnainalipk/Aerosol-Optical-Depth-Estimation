from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_model(X_train, y_train, params=None):
    if params is None:
        params = {
            'iterations': 100,
            'learning_rate': 0.1,
            'depth': 6,
            'loss_function': 'Logloss',
            'eval_metric': 'Accuracy',
            'random_seed': 42,
            'verbose': 0
        }
    model = CatBoostClassifier(**params)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    return accuracy, precision, recall, f1


