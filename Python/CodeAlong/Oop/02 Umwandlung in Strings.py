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
#  <b>Umwandlung in Strings</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 Umwandlung in Strings.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_110_a2_conversion_to_strings.py -->

# %% "slideshow": [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Umwandlung in Strings
#
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings umgewandelt
# werden können:
#
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm
#   erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# %% tags=["keep"]
text = "Hallo\nWelt!"

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %% tags=["keep"]
my_list = ["a", "b", "c"]

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die `print()`-Funktion wendet `str()` auf ihre Argumente an:

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# In F-Strings werden Werte mit `str()` in Strings umgewandelt. Mit dem Postfix
# `!r` kann statt dessen `repr()` verwendet werden.


# %% tags=["keep"]
text = "Hi,\nthere!"

# %% tags=["keep"]
print(f"{text}")

# %% tags=["keep"]
print(f"{text!s}")

# %% tags=["keep"]
print(f"{text!r}")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Umwandlung in Strings
#
# Welche Funktion wurde verwendet, um die folgenden Ausgaben zu erzielen?

# %% [markdown]
# ```python
# >>> my_string = "Hello, world!"
# >>> print(???(my_string))
# Hello, world!
# ```

# %% tags=["keep"]
my_string = "Hello, world!"

# %%

# %% [markdown]
# ```python
# >>> print(???(my_string))
# 'Hello, world!'
# ```

# %%
