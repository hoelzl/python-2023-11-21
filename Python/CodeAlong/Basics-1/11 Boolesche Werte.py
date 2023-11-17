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
#  <b>Boolesche Werte</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 11 Boolesche Werte.py -->
# <!-- python_courses/slides/module_140_control_flow/topic_110_b1_booleans.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Vergleiche, Boolesche Werte

# %% [markdown] lang="de"
# Gleichheit von Werten wird mit `==` getestet:

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Das Ergebnis eines Vergleichs ist ein Boolescher Wert (Wahrheitswert)
#
# - `True`
# - `False`

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Gleichheit von Zahlen

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Vorsicht: Rundungsfehler!

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Ungleichheit von Zahlen
#
# Der Operator `!=` testet, ob zwei Zahlen verschieden sind

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Vergleich von Zahlen

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Vergleichsoperatoren auf anderen Typen
#
# Die Vergleichsoperatoren lassen sich auch auf viele andere Typen anwenden
# (genaueres später).

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Der Wert `None`
#
# `None` ist ein Wert, der von Python verwendet wird, um das Fehlen eines
# sinnvollen Wertes anzuzeigen. Jupyter druckt `None` nicht als Wert einer Zelle
# aus:


# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Um auf `None` zu testen wird oft der Operator `is` verwendet.

# %%

# %% [markdown] lang="de"
#
# `is` testet Objektidentität und ist im Allgemeinen nicht mit `==`
# austauschbar.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop: Vergleiche
#
# Ist $2^{16}$ größer als $32\,000\,\,/\,\,2$?

# %%

# %% [markdown] lang="de"
# Ist $72$ ohne Rest durch $3$ teilbar?

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Gegeben die folgenden Variablendefinitionen:

# %% tags=["keep"]
var1 = 2**2**4
var2 = 3**12
var3 = 100 * 200 * 300
var4 = 4**3**2

# %% [markdown] lang="de"
#
# Ist das Maximum von `var1` und `var2` größer als das Minimum von `var3` und `var4`?

# %%
