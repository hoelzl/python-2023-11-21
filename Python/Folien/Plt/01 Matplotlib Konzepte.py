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
plt.figure(figsize=(8, 4))
plt.plot(xs, ys1, label="sin(x)")
plt.plot(xs, ys2, label="cos(x/2) $\cdot$ sin(1.5x)")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("PyPlot Plot")
plt.legend()
plt.show()

# %%
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(xs, ys1, label="sin(x)")
ax.plot(xs, ys2, label="cos(x/2) $\cdot$ sin(1.5x)")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_title("Object Oriented Plot")
ax.legend()
plt.show()

# %%
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16, 4))
fig.tight_layout()
ax1.plot(xs, ys1, label="sin(x)")
ax1.plot(xs, ys2, label="cos(x/2) $\cdot$ sin(1.5x)")
ax1.set_title("First plot")
ax1.legend()
ax2.plot(xs, xs, label="$x$")
ax2.plot(xs, xs**2, label="$x^2$")
ax2.set_title("Second plot")
ax2.legend()
plt.show()

# %% [markdown]
#
# <img src="img/numpy-anatomy.webp"
#      style="display:block;margin:auto;width:50%"/>
#
# [Image source](https://matplotlib.org/stable/tutorials/introductory/usage.html)

# %%
