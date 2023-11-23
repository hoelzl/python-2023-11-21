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
#  <b>Eigenschaften von Listen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 Eigenschaften von Listen.py -->
# <!-- python_courses/slides/module_150_collections/topic_114_b1_finding_in_lists.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Eigenschaften von Listen
#
# - Listen können beliebige Python-Werte speichern
# - Elemente in einer Liste haben eine feste Reihenfolge
# - Auf Elemente einer Liste kann mit einem Index zugegriffen werden
# - Listen können modifiziert werden
#
# Listen können Elemente mit verschiedenen Typen enthalten, die meisten Listen
# enthalten aber Elemente eines einzigen Typs.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Anzahl der Vorkommen eines Elements

# %% tags=["keep"]
numbers = [1, 1, 2, 1, 3, 2, 1]

# %%
numbers.count(1)

# %%
numbers.count(4)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Finden der Position eines Elements

# %% tags=["keep"]
my_list = ["a", "b", "c", "d", "b", "d", "b"]

# %%
my_index = my_list.index("b")
my_index

# %%
my_list[my_index]


# %%
# Fehler
# [1, 3, 5].index(2)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop:
#
# Die Methode `index` wirft eine Exception, wenn das gesuchte Objekt nicht in
# der Liste vorkommt. Schreiben Sie eine Funktion
# ```
# find(element, a_list: list)
# ```
#
# - die einen Index zurückgibt, falls das Element `element` in der Liste
#   vorkommt, und
# - die `None` zurückgibt, falls es nicht vorkommt

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def find(element, a_list: list):
    if element in a_list:
        return a_list.index(element)
    else:
        return None


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
my_list = ["a", "b", "c", "d", "e"]

# %% tags=["keep"]
assert find("a", my_list) == 0

# %% tags=["keep"]
assert find("d", my_list) == 3

# %% tags=["keep"]
assert find("x", my_list) is None


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop:
#
# Schreiben Sie eine Funktion
#
# ```
# remove_all(element, a_list: list)
# ```
#
# die alle Vorkommen von `element` aus `a_list` entfernt

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def remove_all(element, a_list: list):
    for i in range(a_list.count(element)):
        a_list.remove(element)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
my_list = ["a", "b", "c", "d", "e", "a", "a", "b"]

# %% tags=["keep"]
remove_all("a", my_list)
assert my_list == ["b", "c", "d", "e", "b"]

# %% tags=["keep"]
remove_all("x", my_list)
assert my_list == ["b", "c", "d", "e", "b"]
