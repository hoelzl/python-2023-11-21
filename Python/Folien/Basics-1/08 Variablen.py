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
#  <b>Variablen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 08 Variablen.py -->
# <!-- python_courses/slides/module_120_data_types/topic_130_b1_variables.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Variablen
#
# Wir wollen einen Zaun um unser neues Grundstück bauen.
#
# <img src="img/fence.svg" style="display:block;margin:auto;width:40%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/fence.svg"
#  style="vertical-align:top;overflow:auto;float:right;width:30%"/>
#
# Die gemessenen Längen sind:
# - Birkenweg: 20m
# - Fichtengasse: 30m
#
# Wie lange muss unser Zaun sein?

# %% tags=["keep"]
20 + 30 + (20**2 + 30**2) ** 0.5

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/fence.svg"
#   style="vertical-align:top;overflow:auto;float:right;width:30%"/>
#
# Es ist nicht klar, was die Zahlen in dem<br>
# vorhergehenden Ausdruck bedeuten.
#
# Können wir das besser machen?

# %% lang="de"
länge_birkenweg = 20
länge_fichtengasse = 30

# %% lang="de"
länge_hauptstr = (länge_birkenweg**2 + länge_fichtengasse**2) ** 0.5
länge_gesamt = länge_birkenweg + länge_fichtengasse + länge_hauptstr
ergebnis = länge_gesamt

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Genauere Beschreibung von Variablen
#
# <br/>
# <img src="img/variables-01.svg" style="float:right;margin:auto;width:50%"/>
#
# Eine *Variable* ist
# - ein <span style="color:red;">"Verweis"</span> auf ein "Objekt"
# - der einen <span style="color:red;">Namen</span> hat.
#
# <span style="color:blue;">Ein Objekt</span> kann von
# <span style="color:blue;">mehreren<br/> Variablen</span>
# referenziert werden!

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/variables-01.svg" style="float:right;margin:auto;width:50%"/>
#
# Eine Variable wird
# - erzeugt durch `name = wert`
# - gelesen durch `name`
# - geändert durch `name = wert`
#
# Erzeugen und Ändern von Variablen<br/>
# sind *Anweisungen*.

# %% lang="de" tags=["slide", "keep"] slideshow={"slide_type": "slide"}
länge_birkenweg = 20
print(länge_birkenweg)
länge_birkenweg = 25
print(länge_birkenweg)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Eigenschaften von Variablen in Python
#
# - Eine Variable kann Werte mit beliebigem Datentyp speichern
#     - Es gibt keine `int`-Variablen, etc.
#     - Man sagt: Python ist dynamisch getypt
# - Variablen müssen erzeugt worden sein, bevor sie verwendet werden
# - Man kann Variablen neue Werte zuweisen
#     - Dabei kann der *alte Wert* der Variablen auf der rechten Seite
#       verwendet werden:<br/> `jobs = jobs + 1`

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
x = "Hallo!"
print(x)
x = 123
print(x)
x = x + 1
print(x)
x += 1
print(x)

# %% lang="de"
# diese_variable_gibt_es_nicht

# %%
# nonono = nonono + 1


# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Mini-Workshop: Piraten
#
# Der Legende nach wurde die Beute bei Piratenbanden gerecht durch alle Piraten
# geteilt. Falls sich die Beute sich nicht gerecht aufteilen ließ erhielt der
# Kapitän den überschüssigen Anteil.
#
# Wie viele Golddublonen erhält jeder Pirat einer 8-köpfigen Bande
# (7 Piraten + 1 Kapitän), wenn ein Schatz mit 1000 Golddublonen erbeutet wurde?
#
# (Verwenden Sie Variablen um die Berechnung klarer zu machen.)

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
anzahl_piraten = 8
beute_gesamt = 1000
beute_pro_pirat = beute_gesamt // anzahl_piraten
beute_pro_pirat

# %% [markdown] lang="de"
# Wie viele Golddublonen erhält der Kapitän extra?

# %% lang="de"
beute_kapitän = beute_gesamt % anzahl_piraten
beute_kapitän

# %% [markdown] lang="de"
# Die Piratenbande nimmt 3 neue Piraten-Lehrlinge auf.
#
# Wie verändert sich die Aufteilung der Beute?
#
# (Verwenden Sie Zuweisungen an die existierenden Variablen um das Problem zu
# lösen.)

# %% lang="de"
# anzahl_piraten += 3 # anzahl_piraten = anzahl_piraten + 3
anzahl_piraten = 11  # besser, falls die Zelle evtl. mehrmals ausgewertet wird
beute_pro_pirat = beute_gesamt // anzahl_piraten
beute_pro_pirat

# %% [markdown] lang="de"
# Wie viele Golddublonen erhält der Kapitän in diesem Fall zusätzlich?

# %% lang="de"
beute_kapitän = beute_gesamt % anzahl_piraten
beute_kapitän
