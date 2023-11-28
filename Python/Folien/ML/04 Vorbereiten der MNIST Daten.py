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
#  <b>Vorbereiten der MNIST Daten</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Vorbereiten der MNIST Daten.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_132_mnist_prep.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Vorbereitungen

# %% tags=["keep"]
try:
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
config = EnvConfig()

# %% tags=["keep"]
import pickle
from textwrap import wrap  # noqa


# %% tags=["keep"]
def print_wrapped(text: str):
    for paragraph in text.split("\n"):
        print("\n".join(wrap(paragraph)))


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Laden der MNIST-Daten

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
with open(config.mnist_pkl_path, "rb") as file:
    mnist = pickle.load(file)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Analysieren der Daten
#
# Der Wert in `mnist` ist ein scikit-learn `Bunch`. Das ist ein Typ, der ähnlich zu
# einem Dictionary ist, aber Einträge können mit den beiden (äquivalenten)
# Syntax-Varianten `bunch["key"]` und `bunch.key` gelesen und geschrieben werden.

# %%
type(mnist)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.utils import Bunch

# %%
my_bunch = Bunch()

# %%
my_bunch["my_key"] = 123

# %%
my_bunch["my_key"]

# %%
my_bunch.keys()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
my_bunch.my_key

# %%
my_bunch.my_key = 234

# %%
my_bunch.my_key

# %%
my_bunch["my_key"]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
mnist.keys()

# %%
print_wrapped(mnist["DESCR"])

# %%
mnist.details

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Analysieren von `data` und `target`

# %%
type(mnist.data)

# %%
mnist.data.shape

# %%
type(mnist.target)

# %%
mnist.target.shape

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Verwenden der geläufigen Variablennamen

# %%
X, y = mnist.data, mnist.target  # noqa

# %%
type(X)

# %%
type(y)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Umwandeln in Numpy Arrays

# %%
X = X.to_numpy()
y = y.to_numpy()

# %%
type(X)

# %%
type(y)

# %%
X.shape

# %%
y.shape

# %%
X.dtype

# %%
y.dtype

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Analysieren des Wertebereichs

# %%
np.min(X)

# %%
np.max(X)

# %%
np.min(y)

# %%
np.max(y)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Analysieren einzelner Einträge

# %%
first_number = X[0]
second_number = X[1]

# %%
type(first_number)

# %%
first_number.shape

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Umwandeln in Bilder

# %%
first_number_image = first_number.reshape(28, 28)
second_number_image = second_number.reshape(28, 28)

# %%
first_number_image.shape

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Anzeigen der Bilder

# %%
plt.imshow(first_number_image, cmap="binary")
plt.show()

# %%
plt.imshow(second_number_image, cmap="binary")
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
fig, axes = plt.subplots(10, 10)
for idx, ax in enumerate(np.array(axes).ravel()):
    ax.imshow(X[idx].reshape(28, 28), cmap="binary")
    ax.set_xticks([], [])
    ax.set_yticks([], [])
plt.show()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Umwandeln der Klassen in Zahlen

# %%
y[:2]

# %%
y = y.astype(np.int32)

# %%
y[:2]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Die Zahl 7

# %%
first_index_of_7 = np.where(y == 7)[0][0]
first_index_of_7

# %%
plt.imshow(X[first_index_of_7].reshape(28, 28), cmap="binary")
plt.show()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Aufspalten in Trainings- und Test-Set

# %%
x_train, x_test = X[:60_000], X[60_000:]

# %%
y_train, y_test = y[:60_000], y[60_000:]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Exportieren der Daten

# %%
processed_mnist_data = {
    "x_train": x_train,
    "x_test": x_test,
    "y_train": y_train,
    "y_test": y_test,
}

# %%
with open(config.processed_mnist_pkl_path, "wb") as mnist_file:
    pickle.dump(processed_mnist_data, mnist_file)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Exkurs: Vergleich von Listen und Numpy Arrays

# %%
[1, 2, 3] == [1, 3, 3]  # noqa: B015

# %%
np.array([1, 2, 3]) == np.array([1, 3, 3])  # noqa: B015

# %%
(np.array([1, 2, 3]) == np.array([1, 3, 3])).all()

# %%
(np.array([1, 2, 3]) == np.array([1, 2, 3])).all()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Sanity Checks

# %%
with open(config.processed_mnist_pkl_path, "rb") as mnist_file:
    loaded_mnist_data = pickle.load(mnist_file)

# %%
assert (loaded_mnist_data["x_test"] == x_test).all()  # noqa
assert (loaded_mnist_data["x_train"] == x_train).all()  # noqa
assert (loaded_mnist_data["y_test"] == y_test).all()  # noqa
assert (loaded_mnist_data["y_train"] == y_train).all()  # noqa

# %%
print("\nPrepared MNIST data!")

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Workshop: Vorbereiten der Fashion-MNIST Daten
#
# Bereiten Sie die Fashion-MNIST Daten für Machine-Learning Algorithmen vor:
#
# - Laden Sie die in einem vorhergehenden Workshop gespeicherte Pickle-Datei.
# - Analysieren Sie das Format der wichtigsten Attribute.
# - Konvertieren Sie die beiden Attribute in Numpy Arrays und speichern Sie die
#   Resultate in Variablen `X` und `y`.
# - Lassen Sie sich Bilder der ersten Einträge in `X` anzeigen.
# - Konvertieren Sie die Werte in `y` in `int`-Werte.
# - Teilen Sie die Daten in Trainings- und Test-Daten auf.
# - Speichern Sie die bearbeiteten Daten.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
try:  # noqa
    from python_courses.envconfig import EnvConfig
except ModuleNotFoundError:
    from envconfig import EnvConfig  # noqa

# %% tags=["keep"]
from textwrap import wrap

# %% tags=["keep"]
config = EnvConfig()


# %% tags=["keep"]
def print_wrapped(text: str):
    for paragraph in text.split("\n"):
        print("\n".join(wrap(paragraph)))


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Laden Sie die in einem vorhergehenden Workshop gespeicherte Pickle-Datei.


# %%
import pickle

# %%
with open(config.fashion_mnist_pkl_path, "rb") as file:
    fashion_mnist = pickle.load(file)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Analysieren Sie den Typ und die Keys des geladenen Objekts
# - Analysieren Sie das Format der `data`- und `target`-Attribute.
# - Lassen Sie sich die Beschreibung im `DESCR`-Attribut anzeigen.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
type(fashion_mnist)

# %%
fashion_mnist.keys()

# %%
type(fashion_mnist.data)

# %%
fashion_mnist.data.shape

# %%
type(fashion_mnist.target)

# %%
fashion_mnist.target.shape

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
print_wrapped(fashion_mnist.DESCR)  # noqa

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Konvertieren Sie die beiden Attribute in Numpy Arrays und speichern Sie die
#   Resultate in Variablen `X` und `y`.
# - Analysieren Sie dir Form der erhaltenen Arrays und die Wertebereiche der Elemente.


# %%
X, y = fashion_mnist.data, fashion_mnist.target

# %%
type(X)

# %%
type(y)

# %%
X = X.to_numpy()
y = y.to_numpy()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
type(X)

# %%
type(y)

# %%
X.shape

# %%
y.shape

# %%
X.dtype

# %%
y.dtype

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
import numpy as np

# %%
np.min(X)

# %%
np.max(X)

# %%
np.min(y)

# %%
np.max(y)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Lassen Sie sich Bilder der ersten Einträge in `X` anzeigen.

# %%
first_clothing_item = X[0]
second_clothing_item = X[1]

# %%
type(first_clothing_item)

# %%
first_clothing_item.shape

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
first_clothing_item_image = first_clothing_item.reshape(28, 28)
second_clothing_item_image = second_clothing_item.reshape(28, 28)

# %%
first_clothing_item_image.shape

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
import matplotlib.pyplot as plt

# %%
plt.imshow(first_clothing_item_image, cmap="binary")
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
plt.imshow(second_clothing_item_image, cmap="binary")
plt.show()

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Konvertieren Sie die Werte in `y` in `int`-Werte.

# %%
y[:2]

# %%
y = y.astype(np.int32)

# %%
y[:2]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Teilen Sie die Daten in Trainings- und Test-Daten auf.

# %%
x_train, x_test = X[:60_000], X[60_000:]  # noqa

# %%
y_train, y_test = y[:60_000], y[60_000:]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Speichern Sie ein Dictionary mit den bearbeiteten Daten.
# - Überprüfen Sie, dass die richtigen Daten gespeichert wurden.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
processed_fashion_mnist_data = {
    "x_train": x_train,
    "x_test": x_test,
    "y_train": y_train,
    "y_test": y_test,
}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with open(config.processed_fashion_mnist_pkl_path, "wb") as fashion_mnist_file:
    pickle.dump(processed_fashion_mnist_data, fashion_mnist_file)

# %%
with open(config.processed_fashion_mnist_pkl_path, "rb") as fashion_mnist_file:
    loaded_fashion_mnist_data = pickle.load(fashion_mnist_file)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
assert (loaded_fashion_mnist_data["x_test"] == x_test).all()  # noqa
assert (loaded_fashion_mnist_data["x_train"] == x_train).all()  # noqa
assert (loaded_fashion_mnist_data["y_test"] == y_test).all()  # noqa
assert (loaded_fashion_mnist_data["y_train"] == y_train).all()  # noqa

# %% tags=["keep"]
print("\n\nDone!")
