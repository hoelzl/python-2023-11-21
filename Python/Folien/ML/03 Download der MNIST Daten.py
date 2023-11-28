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
#  <b>Download der MNIST Daten</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Download der MNIST Daten.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_130_download_mnist.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Download der MNIST Daten
#
# Da der Download der MNIST Daten von OpenML relativ lange dauert, speichern wir
# eine lokale Version der Daten.
#
# Die `EnvConfig`-Klasse hilft uns dabei, die Verzeichnisse, in denen wir Daten
# speichern, zwischen verschiedenen Notebooks konsistent zu halten.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
config = EnvConfig()

# %% tags=["keep"]
print(f"Scikit-learn Cache Path:   {config.sklearn_cache_dir_path}")
print(f"Path to MNIST pickle file: {config.mnist_pkl_path}")

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Herunterladen der Daten
#
# [Scikit-learn](https://scikit-learn.org/stable/index.html) ist eine Open-Source
# Bibliothek, die viele traditionelle Algorithmen für maschinelles Lernen implementiert.
#
# Außerdem stellt sie viele Hilfsmittel zur Verarbeitung von Daten, Modell-Auswahl,
# Modell-Evaluierung, usw. bereit.
#
# In diesem Notebook verwenden wir einen der Beispiel-Datensätze, die scikit-learn
# anbietet. Der MNIST-Datensatz ist das typische "Hello, world!" Beispiel für
# Algorithmen zum maschinellen Lernen.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sklearn.datasets import fetch_openml

# %%
print("Loading MNIST data...", flush=True, end="")
mnist = fetch_openml(
    "mnist_784",
    version=1,
    data_home=config.sklearn_cache_dir_path.as_posix(),
    cache=True,
    parser="auto",
)
print("done.", flush=True)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Schreiben der Daten

# %% tags=["keep"]
config.mnist_pkl_path.parent.mkdir(exist_ok=True, parents=True)

# %%
import pickle

# %%
with open(config.mnist_pkl_path, "wb") as file:
    print(f"Writing MNIST data to {config.mnist_pkl_path}.")
    pickle.dump(mnist, file)

# %%
assert config.mnist_pkl_path.exists()

# %% tags=["keep"]
print("Downloaded and saved MNIST data.")

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Download der Fashion-MNIST Daten
#
# [Fashion-MNIST](https://www.openml.org/search?type=data&sort=runs&id=40996)
# ist ein Datensatz, der im gleichen Format wie MNIST ist, aber Bilder
# von verschiedenen Kleidungsstücken enthält.
#
# - Laden Sie den Fashion-MNIST Datensatz von der OpenML Website herunter:<br>
#   `fetch_openml(data_id=40996)` oder<br>
#   `fetch_openml("Fashion-MNIST", version=1)`
# - Schreiben Sie die Daten in eine Pickle-Datei
#
# *Hinweis:* Die `EnvConfig`-Klasse enthält dafür ein Attribut `fashion_mnist_pkl_path`.


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
import pickle

from sklearn.datasets import fetch_openml

# %% tags=["keep"]
config = EnvConfig()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print(f"Path to Fashion-MNIST pickle file: {config.fashion_mnist_pkl_path}")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
fashion_mnist = fetch_openml(
    data_id=40996,
    data_home=config.sklearn_cache_dir_path.as_posix(),
    cache=True,
    parser="auto",
)

# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
# print("Loading Fashion-MNIST data (by name)...", flush=True, end="")
# fashion_mnist_by_name = fetch_openml(
#     "Fashion-MNIST",
#     version=1,
#     data_home=config.sklearn_cache_dir_path.as_posix(),
#     cache=True,
# )
# print("done.", flush=True)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
config.fashion_mnist_pkl_path.parent.mkdir(exist_ok=True, parents=True)

# %%
with open(config.fashion_mnist_pkl_path, "wb") as file:
    print(f"Writing Fashion-MNIST data to {config.fashion_mnist_pkl_path}.")
    pickle.dump(fashion_mnist, file)

# %%
assert config.fashion_mnist_pkl_path.exists()

# %%
print("Done.")
