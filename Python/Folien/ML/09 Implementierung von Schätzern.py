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
#  <b>Implementierung von Schätzern</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 Implementierung von Schätzern.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_172_unlucky_classifier.py -->

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
# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Scikit-Learn Schätzer
#
# Drei der Grundlegenden Konzepte in Scikit-Learn sind **Schätzer** (**Estimators**),
# **Transformer** und **Prediktoren** (**Predictors**).
#
# - Jedes Objekt, das einen Datensatz verwendet, um seine internen Parameter zu
#   bestimmen, ist ein Schätzer.
#   - Schätzer haben eine `fit()`-Methode.
# - Schätzer, die einen Datensatz transformieren können, sind Transformer.
#   - Transformer haben eine `transform()`-Methode (und `fit_transform()`).
# - Schätzer, die eine Vorhersage machen können, sind Prediktoren.
#   - Prediktoren haben eine `predict()`-Methode.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Implementierung von Schätzern
#
# Schätzer erben typischerweise von der `BaseEstimator` Klasse:

# %% tags=["keep"]
from sklearn.base import BaseEstimator


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
class UnluckyClassifier(BaseEstimator):
    def fit(self, _X, _y=None):
        return self

    def predict(self, X):
        result = np.zeros((len(X),), dtype=bool)
        if len(X):
            result[0] = True
        return result


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
unlucky_clf = UnluckyClassifier()

# %%
unlucky_clf.fit(x_train, lucky7_train)

# %%
unlucky_predict = unlucky_clf.predict(x_test)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_test, unlucky_predict))
