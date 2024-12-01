import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_importance(model, feature_names):
    importance = pd.DataFrame({'Feature': feature_names, 'Importance': model.feature_importances_})
    importance = importance.sort_values(by='Importance', ascending=False)
    sns.barplot(x='Importance', y='Feature', data=importance)
    plt.title("Feature Importance")
    plt.show()

def plot_roc_auc(model, X_test, y_test):
    from sklearn.metrics import roc_auc_score
    roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    print(f"ROC-AUC: {roc_auc}")
