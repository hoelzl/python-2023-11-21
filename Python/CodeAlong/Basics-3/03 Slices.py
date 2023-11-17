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
#  <b>Slices</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Slices.py -->
# <!-- python_courses/slides/module_150_collections/topic_130_b3_slices.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Slices
#
# Mit der Notation `liste[m:n]` kann man eine "Teilliste" von `liste`
# extrahieren.
#
# - Das erste Element ist `liste[m]`
# - Das letzte Element ist `liste[n-1]`

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Einfache Slices

# %% tags=["keep"]
string_list = ["a", "b", "c", "d", "e"]

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Slices ohne Endwerte

# %% tags=["keep"]
string_list = ["a", "b", "c", "d", "e"]

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Slices mit Schrittweite $>$ 1

# %% tags=["keep"]
string_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
string_list[1], string_list[7]

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Slices mit negativer Schrittweite

# %% tags=["keep"]
string_list = ["a", "b", "c", "d", "e"]
string_list[1], string_list[4]

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Slice
#
# Gegeben sei die folgende Liste:


# %% tags=["keep"]
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Extrahieren Sie von `my_list` eine Liste mit allen Elementen außer den ersten beiden.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Extrahieren Sie von `my_list` eine Liste, die aus dem 2. und 3. Element besteht.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Extrahieren Sie von `my_list` eine neue Liste, die alle Elemente außer dem
# ersten und dem letzten enthält.

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Extrahieren Sie von `my_list` eine neue Liste, die alle Elemente mit ungeradem
# Index enthält (also die Elemente an Position 1, 3, 5, 7 und 9).

# %%
