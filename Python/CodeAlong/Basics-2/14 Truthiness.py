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
#  <b>Truthiness</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 14 Truthiness.py -->
# <!-- python_courses/slides/module_140_control_flow/topic_130_b3_truthiness.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Truthiness
#
# Die `if`-Anweisung kann als Argument beliebige Python-Werte bekommen,
# nicht nur Boolesche Werte.
#
# Folgende Werte gelten als *falsch*
#
# - `None` und `False`
# - `0` und `0.0` (und Null-Werte von anderen Zahlentypen)
# - Leere Strings, Listen und andere Collections: `""`, `[]`, ...
# - Manche Werte von benutzerdefinierten Datentypen
#
#  Alle anderen Werte gelten als wahr.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def check(value):
    if value:
        print(f"{value!r} is truthy.")
    else:
        print(f"{value!r} is falsy.")

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wie wird das verwendet?

# %%

# %%

# %%
# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Truthiness
#
# Für welche Werte von `x` ist `len(x) - 1` falsy?


# %% [markdown] lang="de" tags=["answer"]
# *Antwort:* 

# %% [markdown] lang="de"
#
# Geben Sie zwei Beispielwerte mit verschiedenem Typ an.

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Gibt es einen String `s`, für den `s[0]` falsy ist?

# %% [markdown] lang="de" tags=["answer"]
# *Antwort:* 

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#
# Finden Sie 3 verschiedene Argumente, für die die Funktion `is_truthy_and_falsy()`
# den Wert `True` zurückgibt.
#
# *Hinweis:* Bitte schreiben Sie niemals Code wie `is_truthy_and_falsy()`!

# %% tags=["keep"]
def is_truthy_and_falsy(x):
    if not (len(x) - 1) and not x[0]:
        return True
    else:
        return False

# %%

# %%

# %%
