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
#  <b>Glückszahl 7 mit MNIST (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Glückszahl 7 mit MNIST (Teil 1).py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_140_lucky7.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Glückszahl 7 mit MNIST

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
import pickle

import matplotlib.pyplot as plt
import numpy as np

# %% tags=["keep"]
config = EnvConfig()

# %% tags=["keep"]
with open(config.processed_mnist_pkl_path, "rb") as mnist_file:
    mnist_data = pickle.load(mnist_file)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
x_train = mnist_data["x_train"]
x_test = mnist_data["x_test"]
y_train = mnist_data["y_train"]
y_test = mnist_data["y_test"]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
lucky7_train = y_train == 7
lucky7_test = y_test == 7

# %%
lucky7_test[:3], y_test[:3]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
plt.imshow(x_test[0].reshape(28, 28), cmap="binary")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
fig, axes = plt.subplots(10, 10)
for idx, ax in enumerate(np.array(axes).ravel()):
    ax.imshow(x_test[idx].reshape(28, 28), cmap="binary")
    ax.set_xticks([], [])
    ax.set_yticks([], [])
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sklearn.linear_model import SGDClassifier  # noqa: E402

# %%
sgd_clf = SGDClassifier(random_state=42)

# %%
sgd_clf.fit(x_train, lucky7_train)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
sgd_clf.predict([x_test[0]])

# %%
sgd_clf.predict(x_test[:3])

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
lucky7_predict = sgd_clf.predict(x_test)

# %%
correct_predictions = lucky7_predict == lucky7_test

# %%
correct_predictions[:10]

# %%
np.sum(correct_predictions)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Linearer Klassifizierer für Fashion-MNIST
#
# - Trainieren Sie einen SGD Klassifizierer für den Fashion-MNIST Datensatz.
# - Bestimmen Sie, wie viele Sneaker (Kategorie 7) Sie damit richtig klassifizieren
#   können.


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
# %%
sneaker_train = y_train == 7
sneaker_test = y_test == 7

# %%
sneaker_test[:10], y_test[:10]

# %%
plt.imshow(x_test[0].reshape(28, 28), cmap="binary")
plt.show()

# %%
np.argmin(sneaker_test == False)  # noqa

# %%
plt.imshow(x_test[9].reshape(28, 28), cmap="binary")
plt.show()

# %%
from sklearn.linear_model import SGDClassifier  # noqa: E402

# %%
sgd_clf = SGDClassifier(random_state=42)

# %%
sgd_clf.fit(x_train, sneaker_train)

# %%
sgd_clf.predict([x_test[0]])

# %%
sgd_clf.predict([x_test[9]])

# %%
sgd_clf.predict(x_test[:10])

# %%
sneaker_predict = sgd_clf.predict(x_test)

# %%
correct_predictions = sneaker_predict == sneaker_test

# %%
correct_predictions[:10]

# %%
np.sum(correct_predictions)
