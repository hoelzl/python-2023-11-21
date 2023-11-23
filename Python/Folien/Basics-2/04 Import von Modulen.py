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
#  <b>Import von Modulen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Import von Modulen.py -->
# <!-- python_courses/slides/module_130_functions/topic_115_a3_modules.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Import von Modulen
#
# Ein Großteil der Funktionalität von Python ist nicht direkt im Interpreter
# verfügbar, sondern in externen Modulen (und Packages). Die Python Distribution
# enthält mehr als 200 solche Module.
#
# Mit der `import` Anweisung kann man diese Funktionalität verfügbar machen:

# %%
import math

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Auf die Funktionen aus dem `math` Modul kann man dann mit der Syntax
# `math.floor` zugreifen:

# %%
math.floor(2.5)

# %%
math.floor(2.9)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir haben in einem früheren Video die folgende Funktion definiert, um die Länge
# der Hypotenuse in einem rechtwinkligen Dreieck aus den beiden Katheten zu berechnen:

# %% tags=["keep"]
def pythagoras(a, b):
    c = (a**2 + b**2) ** 0.5
    return c


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Funktion `pythagoras` steht im `math`-Modul unter dem Namen `hypot`
# zur Verfügung:

# %%
math.hypot(3, 4)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit `from`...`import` können Namen aus einem Modul direkt in den aktuellen
# Namensraum importiert werden:

# %%
from math import isclose

# %%
isclose(0.1 + 0.2, 0.3)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Module können beim Import umbenannt werden:

# %%
import math as m

# %%
m.hypot(3, 4)

# %% [markdown] lang="de"
#
# Ebenso mit `from` importierte Namen:

# %%
from math import hypot as pythagoras

# %%
pythagoras(3, 4)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Module


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Im [Modul `os`](https://docs.python.org/3/library/os.html)
# stellt Python Funktionen zur Verfügung, die Information über das
# verwendete Betriebssystem und die Umgebung des Python-Prozesses liefern.
#
# Verwenden Sie die `getcwd()`-Funktion aus dem `os`-Modul um das Arbeitsverzeichnis
# des laufenden Python-Prozesses zu erfahren.

# %%
import os

# %%
os.getcwd()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Bestimmen Sie mit der Funktion `cpu_count()` aus dem `os`-Modul, wie viele
# Prozessorkerne Ihr Computer (nach Meinung von Python) hat.

# %%
os.cpu_count()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Das [`random`-Modul](https://docs.python.org/3/library/random.html) bietet
# verschiedene Zufallszahlengeneratoren an. Verwenden Sie
# die `randint()`-Funktion daraus um eine ganze Zahle zwischen 1 und 6 (einschließlich)
# zu erzeugen.
#
# Werten Sie die Zelle mehrfach aus um sich zu überzeugen, dass dabei unterschiedliche
# Zahlen generiert werden.

# %%
from random import randint

# %%
randint(1, 6)
