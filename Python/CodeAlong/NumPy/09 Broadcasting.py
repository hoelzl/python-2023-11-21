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
#  <b>Broadcasting</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 Broadcasting.py -->
# <!-- python_courses/slides/module_600_numpy/topic_170_a5_np_broadcasting.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Broadcasting
#
# Die meisten Operationen in Numpy können auch mit Skalaren ausgeführt werden:

# %% tags=["keep"]
import numpy as np

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%


# %% [markdown] lang="de"
#
# ### Regeln für Broadcasting:
#
# Wenn eine Operation auf `a` und `b` durchgeführt wird:
#
# - Die Achsen (Shapes) von `a` und `b` werden von rechts nach links verglichen.
#
# - Wenn `a` und `b` die gleiche Länge für eine Achse haben, sind sie kompatibel
#
# - Wenn entweder `a` oder `b` die Länge 1 für eine Achse hat, wird es konzeptionell
#   entlang dieser Achse so oft wiederholt wie nötig.
#
# - Wenn `a` und `b` unterschiedliche Längen entlang einer Achse haben und
#   keines von beiden die Länge 1 hat, sind sie inkompatibel.
#
# - Das Array mit dem niedrigeren Rang wird so behandelt, als hätte es Rang
#   1 für die fehlenden Achsen, die fehlenden Achsen werden links angehängt

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
