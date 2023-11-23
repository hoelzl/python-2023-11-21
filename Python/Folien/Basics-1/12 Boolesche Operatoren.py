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
#  <b>Boolesche Operatoren</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 12 Boolesche Operatoren.py -->
# <!-- python_courses/slides/module_140_control_flow/topic_112_b1_boolean_operators.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Operatoren auf Booleschen Werten
#

# %%
1 < 2 and 3 < 2

# %%
1 < 2 or 3 < 2

# %%
not (1 < 2)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Wann ist ein logischer Ausdruck wahr?
#
# | Operator | Operation                      | `True` wenn...                 |
# |:--------:|:-------------------------------|:-------------------------------|
# | and      | logisches "Und" (Konjunktion)  | beide Argumente `True`         |
# | or       | logisches "Oder" (Disjunktion) | mindestens ein Argument `True` |
# | not      | logisches "Nicht" (Negation)   | Argument `False`               |

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Verkettung von Vergleichen

# %%
1 < 2 and 2 < 3

# %%
1 < 2 < 3

# %%
1 < 3 and 3 <= 2

# %%
1 < 3 <= 2

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop: Operatoren, Vergleiche
#
# Gegeben die folgenden Variablendefinitionen:

# %% tags=["keep"]
var1 = 3 ** (3 * 4)
var2 = 4**3**2
var3 = (3**3) ** 3
var4 = (2**3) ** 4

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ist `var1` durch `var3` teilbar und gleichzeitig `var2` durch `var4` teilbar?

# %%
var1 % var3 == 0 and var2 % var4 == 0

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Sind die Variablen `var1`, `var2`, `var3` und `var4` aufsteigend angeordnet,
# gilt also `var1` < `var2` und `var2` < `var3` und `var3` < `var4`?

# %%
var1 < var2 and var2 < var3 and var3 < var4

# %% [markdown] lang="de" tags=["alt"]
#
#  Eine bessere Lösung ist:

# %% tags=["alt"]
var1 < var2 < var3 < var4

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Sind die Variablen `var1`, `var2`, `var3` und `var4` absteigend angeordnet,
# gilt also `var1` > `var2` und `var2` > `var3` und `var3` > `var4`?

# %%
var1 > var2 > var3 > var4

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ist der Wert von `var1` zwischen `1_000` und `10_000`?

# %%
1_000 <= var4 <= 10_000
