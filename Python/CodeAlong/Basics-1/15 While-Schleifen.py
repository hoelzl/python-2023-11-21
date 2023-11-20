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
#  <b>While-Schleifen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 15 While-Schleifen.py -->
# <!-- python_courses/slides/module_140_control_flow/topic_210_a3_while_part2.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  # While-Schleifen
#
#  Manchmal wollen wir einen Teil eines Programms immer wieder ausführen:
#
#  - Zahlenraten bis die richtige Zahl gefunden wurde
#  - Physik-Simulation bis das Ergebnis genau genug ist
#  - Verarbeitung von Benutzereingaben in interaktiven Programmen
#
#  Wenn wir die Anzahl der Wiederholungen nicht von vornherein wissen,
#  verwenden wir dafür in der Regel eine While-Schleife.

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}


# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  ## Beenden von Schleifen
#
# Manchmal ist es leichter, die Abbruchbedingung einer Schleife im Rumpf zu
# bestimmen, statt am Anfang. Mit der Anweisung `break` kann man eine
# Schleife vorzeitig beenden:

# %% lang="de"

# %%


# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Zahlenraten
#
# - Schreiben Sie ein Programm, das eine Zufallszahl zwischen 1 und 100 erzeugt
# und den Benutzer solange raten lässt, bis er die Zahl erraten hat.
# - Nach jedem Versuch soll dem Benutzer angezeigt werden, ob die geratene Zahl
# zu groß oder zu klein war.

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Fügen Sie Ihrem Programm eine Begrenzung der Rate-Versuche hinzu.   
#   Wenn der Benutzer die Zahl in weniger als 6 Versuchen errät, soll die Meldung
#   `Gut geraten!` ausgegeben werden, ansonsten `Schlecht geraten!`.
# - Erweitern Sie das Programm, sodass nach dem Ende des Spiels die Anzahl der
#   benötigten Versuche ausgegeben wird.

# %%

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Erweitern Sie das Programm, sodass der Benutzer entscheiden kann, ob er
#   erneut spielen möchte.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Run an experiment
#
# - Schreiben Sie ein Programm, das ein Experiment ausführt
# - Das Experiment besteht darin, eine Zufallszahl zu erzeugen und zu prüfen,
#   ob diese größer als 0.8 ist.
# - Wenn das Experiment erfolgreich war, soll `Erfolg!` ausgegeben werden,
#   andernfalls `Fehlschlag.`.
# - Führen Sie das Experiment solange aus, bis es erfolgreich war.
# - Geben Sie die Anzahl der benötigten Versuche aus.
#

# %% lang="de" tags=["slide"] slideshow={"slide_type": "slide"}

# %%

# %%
# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Wörterspiel
#
# - Schreiben Sie ein Programm, das ein zufälliges Wort aus einer Liste von Wörtern erzeugt
# - und den Benutzer raten lässt, bis er das Wort erraten hat.


# %% lang="de"

# %%

# %%
