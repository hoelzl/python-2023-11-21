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

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

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

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
