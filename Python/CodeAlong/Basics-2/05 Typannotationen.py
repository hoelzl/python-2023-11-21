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
#  <b>Typannotationen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Typannotationen.py -->
# <!-- python_courses/slides/module_130_functions/topic_130_b3_type_annotations.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Typannotationen
# - Python ist dynamisch typisiert
# - Typen von
#
#   - Variablen
#   - Funktionsparametern
#   - Rückgabewerten von Funktionen
#   - Attributen von Objekten
#   - etc.
#
#   *müssen* nicht angegeben werden
# - Python *erlaubt* es aber diese Typen anzugeben:

# %% tags=["start", "subslide"] slideshow={"slide_type": "subslide"}
def repeat_string(string, count):  # type: ignore
    return string * count

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Typannotationen werden vom Python Interpreter ignoriert:

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Vorteile von Typannotationen
#
# - Dokumentation
# - Typprüfung durch externe Tools
# - Verbesserte Code-Vervollständigung in IDEs


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Typannotationen
#
# Schreiben Sie eine Function `repeat(s: str, n: int) -> str`, die den String `s`
# `n` mal wiederholt:
#
# ```python
# >>> repeat("abc", 3)
# "abcabcabc"
# ```
#
# *Hinweis:* Sie können dazu den Multiplikationsoperator `*` verwenden:
# ```python
# >>> "abc" * 3
# "abcabcabc"
# ```


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Falls Sie VS Code oder PyCharm Professional verwenden:
#
# - Welche Warnungen erhalten Sie in den folgenden Beispielen?
# - Signalisieren diese Warnungen einen Laufzeitfehler?
#
# Falls Sie mit Jupyter Notebooks im Browser arbeiten empfiehlt es sich, den
# Code dieser Aufgabe in eine Python Datei zu kopieren und diese mit Ihrem IDE
# zu öffnen um zu sehen, welche Warnungen angezeigt werden.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Was passiert, wenn Sie `repeat()` mit zwei Zahlen aufrufen?
# - Was passiert, wenn Sie `repeat()` mit zwei Strings aufrufen?

# %%

# %%
