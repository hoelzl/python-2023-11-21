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
#  <b>Vordefinierte Funktionen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 Vordefinierte Funktionen.py -->
# <!-- python_courses/slides/module_120_data_types/topic_140_b1_built_in_functions.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Vordefinierte Funktionen
#
# Einige Funktionen in Python sind vom Interpreter
# [vordefiniert](https://docs.python.org/3/library/functions.html#built-in-functions).
# Viele weitere können durch Module geladen werden.

# %%
print("Hello, world!")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Umwandlung von Datentypen
#
# - Python nimmt keine automatischen Umwandlungen von Datentypen vor.
# - Man kann aber die Konversion oft explizit durchführen.

# %%
type(123)

# %%
int("123")

# %%
int(3.8)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Praktisch jedes Objekt in Python lässt sich in einen String umwandeln:

# %%
str(1.2)

# %% [markdown] lang="de"
#
# Aber natürlich gibt es Fälle, in denen Python die Konversion in den gewünschten Typ
# nicht durchführen kann:

# %%
# int("Hello, there!")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Andere Eingebaute Funktionen

# %%
abs(10)

# %%
abs(-10)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
round(4.4)

# %%
round(4.6)

# %% tags=["keep"]
print(round(0.5), round(1.5), round(2.5), round(3.5))

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Vordefinierte Funktionen
#
# In diesem Workshop sollen Sie einige Aufgaben mit vordefinierten Funktionen lösen.
# Manche der Funktionen wurden noch nicht besprochen. Verwenden Sie die [Tabelle der
# vordefinierten
# Funktionen](https://docs.python.org/3/library/functions.html#built-in-functions)
# um geeignete Kandidaten zu finden.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wandeln Sie die Zahl `1.5` in einen String um.

# %%
str(1.5)

# %% [markdown] lang="de"
#
# Bestimmen Sie das Maximum der Zahlen 2.5 und 1.7 mit einer eingebauten Funktion.

# %%
max(2.5, 1.7)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wandeln Sie den String "1.234" in eine Gleitkommazahl um und addieren Sie `2.345`
# dazu.

# %%
float("1.234") + 2.345
