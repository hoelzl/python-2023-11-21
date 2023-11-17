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
#  <b>String-Interpolation</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 String-Interpolation.py -->
# <!-- python_courses/slides/module_120_data_types/topic_170_a4_string_interpolation.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # String Interpolation: F-Strings
#
# Python bietet die Möglichkeit, Werte in Strings einzusetzen:

# %% lang="de"

# %% lang="de" tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
spieler_name = "Hans"
anzahl_spiele = 10
anzahl_gewinne = 2

ausgabe = f"Hallo {spieler_name}!\nSie haben {anzahl_spiele}-mal gespielt und dabei {anzahl_gewinne}-mal gewonnen."
print(ausgabe)

# %% lang="de" tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
ausgabe = f"""\
Hallo {spieler_name}!
Sie haben {anzahl_spiele}-mal gespielt \
und dabei {anzahl_gewinne}-mal gewonnen.\
"""
print(ausgabe)

# %% lang="de" tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
ausgabe = (
    f"Hallo {spieler_name}!\n"
    f"Sie haben {anzahl_spiele}-mal gespielt "
    f"und dabei {anzahl_gewinne}-mal gewonnen."
)
print(ausgabe)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Begrüßung
#
# Schreiben Sie eine Funktion `drucke_begrüßung(name)`, die eine personalisierte
# Begrüßung ausgibt, z.B.
# ```
# Hallo, Hans!
# Schön Sie heute wieder bei uns begrüßen zu dürfen.
# Wir wünschen Ihnen viel Spaß, Hans.
# ```
# Verwenden Sie dazu String-Interpolation.

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% lang="de"

# %%
