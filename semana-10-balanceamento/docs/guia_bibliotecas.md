# Guia das bibliotecas da semana

| Biblioteca | Para que serve | Funções usadas |
|---|---|---|
| pandas | Ler e resumir os dados | `read_csv`, `value_counts(normalize=True)`, `groupby` |
| scikit-learn: model_selection | Dividir e validar | `train_test_split(stratify=y)`, `StratifiedKFold`, `cross_val_score`, `cross_validate` |
| scikit-learn: metrics | Avaliar classificadores | `confusion_matrix`, `precision_score`, `recall_score`, `f1_score`, `classification_report`, `roc_auc_score`, `average_precision_score`, `precision_recall_curve` |
| scikit-learn: dummy | Modelo-base | `DummyClassifier(strategy='most_frequent')` |
| scikit-learn: linear_model, tree, neighbors | Modelos | `LogisticRegression(class_weight=...)`, `DecisionTreeClassifier`, `KNeighborsClassifier` |
| scikit-learn: utils | Pesos de classe | `compute_class_weight('balanced', ...)` |
| imbalanced-learn (`imblearn`) | Reamostragem | `RandomUnderSampler`, `RandomOverSampler`, `SMOTE`, `SMOTENC`, `fit_resample` |
| imblearn.pipeline | Pipeline com reamostrador | `Pipeline` (importe como `ImbPipeline`) |

Dica: o pacote se instala como `imbalanced-learn` e se importa como `imblearn`.
