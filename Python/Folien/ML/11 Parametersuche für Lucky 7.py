# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# <div style="text-align:center; font-size:200%;">
#  <b>Parametersuche für Lucky 7</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 11 Parametersuche für Lucky 7.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_180_lucky7_parameter_search.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Hyperparameter-Tuning durch Suche

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import pickle

import matplotlib.pyplot as plt  # noqa
import numpy as np  # noqa

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from envconfig import EnvConfig

# %% tags=["keep"]
config = EnvConfig()
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
with open(config.processed_mnist_pkl_path, "rb") as file:
    mnist_data = pickle.load(file)

# %% tags=["keep"]
x_train = mnist_data["x_train"]
x_test = mnist_data["x_test"]
y_train = mnist_data["y_train"]
y_test = mnist_data["y_test"]
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
lucky7_train = y_train == 7
lucky7_test = y_test == 7
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import os
from sklearn.metrics import classification_report

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, classification_report


# %% tags=["keep"]
def plot_confusion_matrices(clf, x_train, x_test, y_train, y_test, normalize=None):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16, 9))
    fig.tight_layout()
    fig.suptitle(f"Confusion Matrices (Normalize={normalize})")
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        clf.predict(x_test),
        normalize=normalize,
        ax=ax1,
        colorbar=False,
        values_format=".3f" if normalize else None,
    )
    ax1.set_title("Test Data")
    ConfusionMatrixDisplay.from_predictions(
        y_train,
        clf.predict(x_train),
        normalize=normalize,
        ax=ax2,
        colorbar=False,
        values_format=".3f" if normalize else None,
    )
    ax2.set_title("Training Data")
    plt.show()
# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Systematische Parametersuche mit Grid Search

# %% tags=["keep"]
param_grid_gs = {
    "bootstrap": [False],
    "class_weight": ["balanced"],
    "max_features": [64, 256],
    "max_leaf_nodes": [250, 500],
    "min_samples_leaf": [2, 4, 8],
    "min_samples_split": [12, 16],
    "n_estimators": [100],
}

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.ensemble import RandomForestClassifier

# %% tags=["keep"]
gs_rf = RandomForestClassifier(n_jobs=max(os.cpu_count() // 4, 1))

# %%
from sklearn.model_selection import GridSearchCV

# %%
gs_clf = GridSearchCV(gs_rf, param_grid_gs, cv=3, n_jobs=4, verbose=2)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
GRID_SEARCH_SAMPLES = 12_000

# %%
gs_clf.fit(x_train[:GRID_SEARCH_SAMPLES], lucky7_train[:GRID_SEARCH_SAMPLES])

# %%
gs_pred = gs_clf.predict(x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_test, gs_pred))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(gs_clf, x_train, x_test, lucky7_train, lucky7_test)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
gs_clf.best_params_

# %% tags=["alt"]
{
    "bootstrap": False,
    "class_weight": "balanced",
    "max_features": 64,
    "max_leaf_nodes": 250,
    "min_samples_leaf": 4,
    "min_samples_split": 16,
    "n_estimators": 100,
}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Stochastische Suche mit Randomized Search

# %% tags=["keep"]
param_grid = {
    "bootstrap": [True, False],
    "class_weight": [None, "balanced"],
    "max_features": [64, 256],
    "max_leaf_nodes": [None, 250, 500, 1000],
    "min_samples_leaf": [1, 4, 8, 16],
    "min_samples_split": [2, 4, 8, 12],
    "n_estimators": [50, 100],
}


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def num_parameter_combinations(parameters: dict):
    result = 1
    for values in parameters.values():
        result *= len(values)
    return result


# %% tags=["keep"]
num_parameter_combinations(param_grid)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
rs_rf = RandomForestClassifier(random_state=42, n_jobs=max(os.cpu_count() // 4, 1))

# %%
from sklearn.model_selection import RandomizedSearchCV

# %%
rs_clf = RandomizedSearchCV(
    rs_rf, param_grid, random_state=2022, cv=3, n_iter=24, n_jobs=4, verbose=2
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
RANDOM_SEARCH_SAMPLES = 12_000

# %%
rs_clf.fit(x_train[:RANDOM_SEARCH_SAMPLES], lucky7_train[:RANDOM_SEARCH_SAMPLES])

# %%
rs_pred = rs_clf.predict(x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_test, rs_pred))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(rs_clf, x_train, x_test, lucky7_train, lucky7_test)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
rs_clf.best_params_

# %% tags=["alt"]
{
    "bootstrap": False,
    "class_weight": "balanced",
    "max_features": 64,
    "max_leaf_nodes": 1000,
    "min_samples_leaf": 8,
    "min_samples_split": 2,
    "n_estimators": 50,
}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Vergleich der besten gefundenen Lösungen

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
rs_clf.cv_results_["rank_test_score"]

# %%
rs_ranks = rs_clf.cv_results_["rank_test_score"] - 1
rs_ranks

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
rs_params = rs_clf.cv_results_["params"]
rs_params[0], type(rs_params)

# %%
rs_sorted_params = np.take(rs_params, np.argsort(rs_ranks))
rs_sorted_params[0]

# %%
rs_sorted_params[0] == rs_clf.best_params_

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
import pandas as pd

# %%
rs_df = pd.DataFrame.from_records(rs_sorted_params)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Schrittweise Halbierung des Suchraums

# %% tags=["keep"]
param_grid_hs = {
    "bootstrap": [True, False],
    "class_weight": [None, "balanced"],
    "max_features": [128, 256],
    "max_leaf_nodes": [None, 250, 500],
    "min_samples_leaf": [1, 4],
    "min_samples_split": [2, 8, 16, 32],
    "n_estimators": [100],
}

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.experimental import enable_halving_search_cv  # noqa
from sklearn.model_selection import HalvingGridSearchCV  # noqa

# %% tags=["keep"]
hs_rf = RandomForestClassifier(random_state=42, n_jobs=max(os.cpu_count() // 4, 1))

# %%
hs_clf = HalvingGridSearchCV(
    hs_rf,
    param_grid_hs,
    random_state=2022,
    cv=3,
    n_jobs=4,
    factor=3,
    verbose=1,
)

# %%
hs_clf.fit(x_train, lucky7_train)

# %%
hs_pred = hs_clf.predict(x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_test, hs_pred))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(hs_clf, x_train, x_test, lucky7_train, lucky7_test)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
hs_clf.best_params_

# %% tags=["alt"]
{
    "bootstrap": False,
    "class_weight": "balanced",
    "max_features": 256,
    "max_leaf_nodes": 500,
    "min_samples_leaf": 4,
    "min_samples_split": 8,
    "n_estimators": 100,
}
