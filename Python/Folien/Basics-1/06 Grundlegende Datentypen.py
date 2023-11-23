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
#  <b>Grundlegende Datentypen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 Grundlegende Datentypen.py -->
# <!-- python_courses/slides/module_120_data_types/topic_110_b1_data_types.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Woraus besteht ein Programm?
#
# Wir wollen ein Programm schreiben, das
#
# ```
# Hello, world!
# ```
#
# auf dem Bildschirm ausgibt.
#
# Was benötigen wir dazu?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Was benötigen wir dazu?
#
# - Daten
#     - den Text `Hello, world!`
# - Anweisungen
#     - *Gib den folgenden Text auf dem Bildschirm aus*
# - Kommentare
#     - Hinweise für den Programmierer, werden von Python ignoriert

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Kommentare
#
# - `#` gefolgt von beliebigem Text
# - bis zum Ende der Zeile

# %% tags=["keep"]
# Das ist ein Kommentar.
# Alle Zeilen in dieser Zelle werden
# von Python ignoriert.


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Daten
#
# - Zahlen: `123`, `3.141592`
# - Text (Strings): `'Das ist ein Text'`, `"Hello, world!"`

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
123

# %%
1 + 2

# %%
3.141592

# %%
2.1 + 3.8

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
# fmt: off
3,141592

# %%
2,1 + 3,8
# fmt: on


# %%
"Hello, world!"

# %% lang="de"
# fmt: off
'Das ist ein Text'
# fmt: on

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
"1"

# %%
"1" + "2"

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
"""Ein Text,
der über mehrere Zeilen geht."""

# %% lang="de" tag=["del"]
"Benachbarte " "Stringliterale " "werden zusammengefügt"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Anzeige von Werten mit der `print()` Funktion
#
# Um Werte anzuzeigen kann man die `print()`-Funktion verwenden:
#
# `print(...)` gibt den in Klammern eingeschlossenen Text auf dem Bildschirm
# aus.

# %%
print(123)

# %%
print("Hello, world!")

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# Der `print()` Funktion können mehrere Argumente übergeben werden.
# - Die Argumente werden durch Kommata getrennt
# - Alle Argumente werden in einer Zeile ausgegeben, mit Leerzeichen zwischen
#   den Argumenten.

# %%
print("Der Wert von 1 + 1 ist", 1 + 1, ".")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Durch Angabe eines *benannten Arguments* `sep=''` kann die Ausgabe der
# Leerzeichen unterdrückt werden:

# %%
print("Der Wert von 1 + 1 ist", 1 + 1, ".", sep="")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Es sind auch beliebige andere Strings als Wert des Arguments `sep` zulässig:

# %%
# CSV (don't do this!)
print(1, 3, 7.5, 2, sep=",")

# %%
# Uh, oh
print(1, 3, 7.5, 2, "who, me?", sep=",")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit dem Argument `end` kann man bestimmen, welcher String am Zeilenende
# ausgegeben wird:

# %%
print("a", end=", ")
print("b", end=", ")
print("c")

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Grundlegende Datentypen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Wie können Sie den String `Hello, world!` in Python darstellen?

# %% tags=["keep"]
"Hello, world!"

# %% [markdown] lang="de"
# Wie können Sie den String `Hello, World!` auf dem Bildschirm ausgeben?

# %% tags=["keep"]
print("Hello, World!")

# %% [markdown] lang="de"
# Wie können Sie Ihren Namen als Text (String) in Python darstellen?

# %%
"Matthias"

# %% [markdown] lang="de"
#
# Wie können Sie die Zahl 123 in Python darstellen?

# %%
123

# %% [markdown] lang="de"
# Wie können Sie Ihren Namen auf dem Bildschirm ausgeben?

# %%
print("Matthias")

# %% [markdown] lang="de"
# Wie können Sie die Zahl 123 auf dem Bildschirm ausgeben?

# %%
print("Matthias")

# %% [markdown] lang="de"
# Wie können Sie
#
# ```
# 130 g   Mehl
# 250 ml  Milch
# 1 EL    Vanillezucker
# 1 Prise Salz
# ```
#
# auf dem Bildschirm ausgeben?

# %%
print("130 g   Mehl")
print("250 ml  Milch")
print("1 EL    Vanillezucker")
print("1 Prise Salz")

# %% tags=["alt"]
# Alternativ:
# fmt: off
print("130 g   Mehl", "250 ml  Milch", "1 EL    Vanillezucker", "1 Prise Salz",
      sep="\n")
# fmt: on

# %% tags=["alt"]
# Alternativ:
print(
    """130 g   Mehl
250 ml  Milch
1 EL    Vanillezucker
1 Prise Salz"""
)

# %% tags=["alt"]
# Alternativ:
# fmt: off
print("130 g   Mehl\n"
      "250 ml  Milch\n"
      "1 EL    Vanillezucker\n"
      "1 Prise Salz")  # fmt: on
