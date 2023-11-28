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
#  <b>Zufallsarrays</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 Zufallsarrays.py -->
# <!-- python_courses/slides/module_600_numpy/topic_140_a5_np_random_arrays.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Zufallsarrays

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Gleichverteilt zwischen 0 und 1

# %% tags=["keep"]
import numpy as np

# %% tags=["keep"]
rng = np.random.default_rng(2023)

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Ganzzahlig

# %% tags=["keep"]
rng = np.random.default_rng(2023)

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Normalverteilt

# %% tags=["keep"]
rng = np.random.default_rng(2023)

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Andere Verteilungen
#
# Eine Liste aller Verteilungen und ihrer Parameter ist in der
# [Numpy Dokumentation](https://shorturl.at/jotu0)

# %% tags=["keep"]
rng = np.random.default_rng(2023)

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Zufallsarrays
#
# Erzeugen Sie folgende Arrays:


# %% [markdown] lang="de"
#
# Ein $2\times 5$ Array, das gleichverteilte Zufallszahlen in $[0, 1)$ enthält.

# %% tags=["keep"]
rng = np.random.default_rng(2023)

# %%


# %% [markdown] lang="de"
#
# Ein $3\times 3$ Array, das gleichverteilte Zufallszahlen in $[3, 5)$ enthält.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Einen Vektor der Länge 5, der standard-normalverteilte Zahlen enthält.


# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ein $3 \times 4$ Array, das normalverteilte Zahlen mit
# Mittelwert $5$ und Standardabweichung $0.5$ enthält.

# %%
