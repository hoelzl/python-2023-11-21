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
#  <b>Matplotlib Konzepte</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Matplotlib Konzepte.py -->
# <!-- python_courses/slides/module_620_visualization/topic_110_a3_matplotlib_concepts.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# Konzepte von Matplotlib
#
# Matplotlib hat zwei Varianten der Interaktion:
#
# - Automatisches Management von Grafiken (Figures) mit pyplot
# - Objektorientiert


# %% tags=["keep"]
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# %% tags=["keep"]
xs = np.linspace(0.0, 10.0, 200)
ys1 = np.sin(xs)
ys2 = np.cos(xs / 2.0) * np.sin(xs * 1.5)

# %%

# %%

# %%

# %% [markdown]
#
# <img src="img/numpy-anatomy.webp"
#      style="display:block;margin:auto;width:50%"/>
#
# [Image source](https://matplotlib.org/stable/tutorials/introductory/usage.html)

# %%
