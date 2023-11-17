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
#  <b>For-Schleifen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 12 For-Schleifen.py -->
# <!-- python_courses/slides/module_150_collections/topic_120_b1_for_loops.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Iteration über Listen
#
# In Python kann man mit der `for`-Schleife über Listen iterieren.
#
# Die `for`-Schleife entspricht dem range-based for aus C++,
# `for-in`/`for-of` aus JavaScript oder der `for-each`-Schleife
# aus Java, nicht der klassischen `for`-Schleife
# aus C, C++ oder Java.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
number_list = [0, 1, 2, 3, 4]
number_list

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Syntax der `for`-Schleife
#
# ```python
# for <Element-var> in <Liste>:
#     <Rumpf>
# ```

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Mini-Workshop
#
# Schreiben Sie eine Funktion `print_all(items: list)`, die die Elemente der
# Liste `items` auf dem Bildschirm ausgibt, jeweils ein Element pro Zeile:
#
# ```python
# >>> print_all([1, 2, 3])
# 1
# 2
# 3
# >>>
# ```
# Was passiert, wenn Sie die Funktion mit einem String als Argument aufrufen,
# z.B. `print_all("abc")`


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Einkaufsliste
#
# Definieren Sie Variablen
# - `meine_einkaufsliste`, die eine Liste mit den Strings `Tee` und `Kaffee`
#   enthält,
# - `eine_andere_einkaufsliste`, die ebenfalls eine Liste mit den Strings
#   `Tee` und `Kaffee` enthält.

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Definieren Sie eine Funktion `drucke_einkaufsliste(einkaufsliste)`, die die
# als Argument übergebene Einkaufsliste ausdruckt:
#
# ```
# Einkaufsliste:
#   Tee
#   Kaffee
# ```

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Testen Sie die Funktion `drucke_einkaufsliste(einkaufsliste)` mit beiden
# Einkaufslisten.

# %% lang="de"

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Definieren Sie eine Funktion `kaufe(produkt, einkaufsliste)`, das `produkt`
# zu  `einkaufsliste` hinzufügt.

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Fügen Sie `Butter` und `Brot` zur Einkaufsliste `meine_einkaufsliste` hinzu.

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Drucken Sie beide Einkaufslisten nochmal aus.

# %% lang="de"

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

# %% lang="de"
