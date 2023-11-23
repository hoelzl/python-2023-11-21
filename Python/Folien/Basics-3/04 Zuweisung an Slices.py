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
#  <b>Zuweisung an Slices</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Zuweisung an Slices.py -->
# <!-- python_courses/slides/module_150_collections/topic_135_b3_assignment_to_slices.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Zuweisung an Slices
#
# Man kann Werte an Slices zuweisen:

# %%
liste = [1, 2, 3, 4]
liste[1:3]

# %%
liste[1:3] = ["a", "b", "c"]
liste

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
liste[2:2]

# %%
liste[2:2] = ["x"]
liste

# %%
liste[:] = [11, 22, 33]
liste

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Ändern von Prioritäten
#
# Gegeben die folgende Liste von Prioritäten:

# %% lang="de" tags=["keep"]
prioritäten = ["sehr niedrig", "geht so", "extrem hoch"]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ändern Sie die Liste `prioritäten` durch eine Zuweisung an ein Slice in die folgende
# Liste:
# ```python
# ['sehr niedrig', 'niedrig', 'mittel', 'hoch', 'extrem hoch']
# ```

# %% lang="de" tags=["keep"]
prioritäten

# %% lang="de"
prioritäten[1:2]

# %% lang="de"
prioritäten[1:2] = ["niedrig", "mittel", "hoch"]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Verwenden Sie Zuweisung an ein Slice um den Inhalt von `prioritäten` durch
# die Zahlen `5, 4, 3, 2, 1` zu ersetzen.
#
# *Hinweis:* Verwenden Sie dazu eine Range.

# %% lang="de"
prioritäten[:] = range(5, 0, -1)
prioritäten
