from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

def train_random_forest(X_train, y_train):
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    return rf

def train_logistic_regression(X_train, y_train):
    log_reg = LogisticRegression(max_iter=500)
    log_reg.fit(X_train, y_train)
    return log_reg

def train_xgboost(X_train, y_train):
    xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    xgb.fit(X_train, y_train)
    return xgb

def train_lightgbm(X_train, y_train):
    lgbm = LGBMClassifier(n_estimators=100, learning_rate=0.1, max_depth=-1, random_state=42)
    lgbm.fit(X_train, y_train)
    return lgbm

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    return report, roc_auc
