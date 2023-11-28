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
#  <b>Klassifizierer für Lucky 7</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 08 Klassifizierer für Lucky 7.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_170_lucky7_classifiers.py -->

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import pickle

import matplotlib.pyplot as plt  # noqa
import numpy as np  # noqa

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

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
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Drucken von Konfusionsmatrizen

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
# ## Klassifikation mit Linearem Modell

# %% tags=["keep"]
sgd_clf = SGDClassifier()

# %% tags=["keep"]
sgd_clf.fit(x_train, lucky7_train)

# %% tags=["keep"]
sgd_pred = sgd_clf.predict(x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_test, sgd_pred))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_train, sgd_clf.predict(x_train)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(sgd_clf, x_train, x_test, lucky7_train, lucky7_test)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Klassifikation mit Entscheidungsbäumen

# %%

# %%

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(8, 4), dpi=200)
fig.tight_layout()
plot_tree(dt_clf, ax=ax)
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_test, dt_pred))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_train, dt_clf.predict(x_train)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(dt_clf, x_train, x_test, lucky7_train, lucky7_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(
    dt_clf, x_train, x_test, lucky7_train, lucky7_test, normalize="true"
)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_test, dt_pred2))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_train, dt_clf2.predict(x_train)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(dt_clf2, x_train, x_test, lucky7_train, lucky7_test)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Klassifikation mit Random Forests

# %%

# %%

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_test, rf_pred))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_train, rf_clf.predict(x_train)))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plot_confusion_matrices(rf_clf, x_train, x_test, lucky7_train, lucky7_test)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Vorsicht bei unbalancierten Datensätzen!
#
# Die beiden Klassen in unserem Datensatz sind unterschiedlich groß.
# Das führt dazu, dass wir bei der Beurteilung unserer Qualitätsmaße vorsichtig sein
# müssen.

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Klassifizierer für Fashion-MNIST
#
# - Trainieren und evaluieren Sie folgende Klassifizierer für Sneaker
#   für den Fashion-MNIST Datensatz:
#   - `sklearn.linear_model.RidgeClassifier`
#   - `sklearn.tree.DecisionTreeClassifier`
#   - `sklearn.neighbors.KNeighborsClassifier`
#   - `sklearn.ensemble.RandomForestClassifier`
#   - `sklearn.ensemble.HistGradientBoostingClassifier`

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import pickle

import matplotlib.pyplot as plt  # noqa
import numpy as np  # noqa

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
config = EnvConfig()
# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
with open(config.processed_fashion_mnist_pkl_path, "rb") as file:
    fashion_mnist_data = pickle.load(file)

# %% tags=["keep"]
x_train = fashion_mnist_data["x_train"]
x_test = fashion_mnist_data["x_test"]
y_train = fashion_mnist_data["y_train"]
y_test = fashion_mnist_data["y_test"]
# %% tags=["keep"]
sneaker_train = y_train == 7
sneaker_test = y_test == 7

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%
