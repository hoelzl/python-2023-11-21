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

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Analysieren der Daten
#
# Der Wert in `mnist` ist ein scikit-learn `Bunch`. Das ist ein Typ, der ähnlich zu
# einem Dictionary ist, aber Einträge können mit den beiden (äquivalenten)
# Syntax-Varianten `bunch["key"]` und `bunch.key` gelesen und geschrieben werden.

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.utils import Bunch

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Analysieren von `data` und `target`

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Verwenden der geläufigen Variablennamen

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Umwandeln in Numpy Arrays

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Analysieren des Wertebereichs

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Analysieren einzelner Einträge

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Umwandeln in Bilder

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Anzeigen der Bilder

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Umwandeln der Klassen in Zahlen

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Die Zahl 7

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Aufspalten in Trainings- und Test-Set

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Exportieren der Daten

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Exkurs: Vergleich von Listen und Numpy Arrays

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Sanity Checks

# %%

# %%

# %%

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

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Analysieren Sie den Typ und die Keys des geladenen Objekts
# - Analysieren Sie das Format der `data`- und `target`-Attribute.
# - Lassen Sie sich die Beschreibung im `DESCR`-Attribut anzeigen.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Konvertieren Sie die beiden Attribute in Numpy Arrays und speichern Sie die
#   Resultate in Variablen `X` und `y`.
# - Analysieren Sie dir Form der erhaltenen Arrays und die Wertebereiche der Elemente.


# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Lassen Sie sich Bilder der ersten Einträge in `X` anzeigen.

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Konvertieren Sie die Werte in `y` in `int`-Werte.

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Teilen Sie die Daten in Trainings- und Test-Daten auf.

# %%

# %%

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

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["keep"]
print("\n\nDone!")
