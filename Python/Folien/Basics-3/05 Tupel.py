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
#  <b>Tupel</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Tupel.py -->
# <!-- python_courses/slides/module_150_collections/topic_150_b1_tuples.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Tupel
#
# Tupel sind ähnlich zu Listen, allerdings sind Tupel nach ihrer Konstruktion
# unveränderlich. Funktionen und Methoden für Listen, die die Liste nicht
# destruktiv modifizieren sind in der Regel auch auf Tupel anwendbar.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Tupel-Literale
#
# - Elemente durch Kommata getrennt: `1, 2, 3, 4`
# - In vielen Fällen müssen Tupel eingeklammert werden: `(1, 2, 3)`

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
my_tuple = 1, 2, 3
my_tuple

# %%
type(my_tuple)

# %%
my_tuple = (1, 2, 3)
my_tuple

# %%
type(my_tuple)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Leeres Tupel

# %%
empty_tuple = ()
empty_tuple

# %%
type(empty_tuple)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Singleton-Tupel

# %%
# fmt: off
non_tuple = (1)
non_tuple
# fmt: on

# %%
type(non_tuple)

# %%
singleton_tuple = (1,)
singleton_tuple

# %%
type(singleton_tuple)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Heterogenes Tupel

# %%
mixed_tuple = ("a", 1, True)

# %%
type(mixed_tuple)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Operationen auf Tupeln
#
# - Viele der Operationen auf Listen lassen sich auf Tupel anwenden.
# - Die Operationen, die Listen verändern sind nicht anwendbar.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Konstruktion von Tupeln

# %% tags=["keep"]
values = (1, 2, 3)
values

# %%
tuple([1, 2, 3, 4])

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Konkatenation von Tupeln

# %% tags=["keep"]
values = (1, 2, 3)

# %%
values + ("a", "b")

# %%
values

# %%
values * 3

# %%
values

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Tupel und Indizes

# %% tags=["keep"]
values = (1, 2, 3)

# %%
values[1]

# %%
values.index(2)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Funktionen und Methoden

# %% tags=["keep"]
values = (1, 2, 3, 1, 2, 1, 2)

# %%
len(values)

# %%
values.count(1)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Schleifen über Tupel

# %%
for x in 1, 2, 3:
    print(x)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Illegale Operationen

# %% tags=["keep"]
values = (1, 2, 3)

# %%
# values[1] = 10

# %%
# values.append(4)
# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Mini-Workshop: Funktionen mit mehreren Rückgabewerten
#
# Schreiben Sie eine Funktion `min_max(numbers)`, die das Minimum und das
# Maximum aus einer Liste von Zahlen zurückgibt.
# ```python
# >>> min_max([5, 3, 1, 7, 2])
# (1, 7)
# ```


# %%
def min_max(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    return min_number, max_number


# %% tags=["keep"]
assert min_max([5, 3, 1, 7, 2]) == (1, 7)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Zufällige Tupel
#
# Die folgenden Anweisungen erzeugen ein Tupel von Zufallszahlen mit
# zufälliger Länge:


# %% tags=["keep"]
import random

random.seed(2022)
my_tuple = random.choices(range(1000), k=random.randint(5_000, 15_000))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wie viele Elemente enthält `my_tuple`?

# %%
len(my_tuple)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Kommt die Zahl 1 in `my_tuple` vor?
# Falls ja, bei welchem Index ist ihr erstes Vorkommen?

# %%
1 in my_tuple

# %%
my_tuple.index(1)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Drucken Sie eine Tabelle, die angibt, wie oft jede der Zahlen 0 bis 9
# in `my_tuple` vorkommt.

# %%
for i in range(10):
    print(f"{i}: {my_tuple.count(i)}")
