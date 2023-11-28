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
#  <b>Evaluierung von Lucky 7</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 07 Evaluierung von Lucky 7.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_160_lucky7_evaluation.py -->

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
# %% tags=["keep"]
from sklearn.linear_model import SGDClassifier  # noqa: E402

# %% tags=["keep"]
sgd_clf = SGDClassifier(random_state=42)

# %% tags=["keep"]
sgd_clf.fit(x_train, lucky7_train)

# %% tags=["keep"]
lucky7_predict = sgd_clf.predict(x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.metrics import (  # noqa: E402
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Accuracy
#
#  <img src="img/ag/Figure-03-023.png" style="float: right; width: 60%;"/>

# %%
accuracy_score(lucky7_test, lucky7_predict)

# %%
balanced_accuracy_score(lucky7_test, lucky7_predict)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision
#
#  <img src="img/ag/Figure-03-024.png" style="float: right; width: 60%;"/>

# %%
precision_score(lucky7_test, lucky7_predict)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Recall
#
#  <img src="img/ag/Figure-03-026.png" style="float: right; width: 60%;"/>

# %%
recall_score(lucky7_test, lucky7_predict)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## F1-Score
#
#  <img src="img/ag/Figure-03-024.png" style="float: left; width: 40%;"/>
#  <img src="img/ag/Figure-03-026.png" style="float: right; width: 40%;"/>

# %%
f1_score(lucky7_test, lucky7_predict)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Confusion Matrix
#
#  <img src="img/ag/Figure-03-018.png" style="float: right; width: 70%;"/>

# %%
confusion_matrix(lucky7_test, lucky7_predict)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
ConfusionMatrixDisplay.from_predictions(lucky7_test, lucky7_predict)
plt.show()

# %% tags=["alt"]
# Alternative colors:
ConfusionMatrixDisplay.from_predictions(lucky7_test, lucky7_predict, cmap="brg")
plt.show()

# %% tags=["alt"]
# Or:
ConfusionMatrixDisplay.from_predictions(lucky7_test, lucky7_predict, cmap="bwr_r")
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
ConfusionMatrixDisplay.from_predictions(lucky7_test, lucky7_predict, normalize="pred")
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
ConfusionMatrixDisplay.from_predictions(lucky7_test, lucky7_predict, normalize="true")
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
print(classification_report(lucky7_test, lucky7_predict))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Classification Report

# %%
print(classification_report(lucky7_test, lucky7_predict))

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Evaluierung von Fashion-MNIST
#
# - Trainieren Sie einen `SGDClassifier` für Fashion-MNIST, der Sneaker (Kategorie 7)
#   erkennt.
# - Evaluieren Sie seine Performance.

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
# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
sneaker_train = y_train == 7
sneaker_test = y_test == 7

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sklearn.linear_model import SGDClassifier

# %%
sgd_clf = SGDClassifier()

# %%
sgd_clf.fit(x_train, sneaker_train)

# %%
sgd_pred = sgd_clf.predict(x_test)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

# %%
print(classification_report(sneaker_test, sgd_pred))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
ConfusionMatrixDisplay.from_predictions(sneaker_test, sgd_pred, normalize="pred")
plt.show()
