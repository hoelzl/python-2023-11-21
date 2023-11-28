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
#  <b>Was ist Maschinelles Lernen?</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 Was ist Maschinelles Lernen.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_120_what_is_ml.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Die Ursprünge des maschinellen Lernens
#
# - Ein Computer kann so programmiert werden, dass er lernt, besser Dame zu spielen,
#   als der Programmierer, der das Programm geschrieben hat.<br>
#   *(Arthur Samuel, 1959)*
#
# - Das Programmieren von Computern, um aus Erfahrung zu lernen, sollte letztendlich
#   die Notwendigkeit für einen Großteil dieses detaillierten Programmieraufwands
#   beseitigen.<br>
#   *(Arthur Samuel, 1959)*

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Biologische Inspiration
#
# <img src="img/ag/Figure-10-001.png"
#      style="width: 80%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Eine mögliche Antwort (Andrew Glassner)
#
# Der Begriff maschinelles Lernen beschreibt eine wachsende Zahl von Techniken, die
# alle ein Ziel haben: aussagekräftige Informationen aus Daten zu gewinnen.
#
# „Daten“ bezieht sich hier auf alles, was aufgezeichnet und gemessen werden kann.
# [...]
#
# "Sinnvolle Information" ist alles, was wir aus den Daten extrahieren können, was
# uns in irgendeiner Weise nützlich sein wird.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Andrew Glassners Bücher
#
# <img src="img/glassner-book.jpg"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] tags=["slide"] slideshow={"slide_type": "slide"}
#
# <img src="img/ag/Figure-01-001.png">

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/ag/Figure-01-002.png">

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Eine andere Antwort (nach von François Chollet)
#
# - Ein Teil der Künstlichen Intelligenz (KI)
# - KI: Computer dazu bringen, Probleme zu lösen, die zuvor nur von Menschen gelöst
#   werden konnten
# - KI muss nicht lernen, z. B. Expertensysteme
# - ML: Verhalten mit zusätzlichen Daten verbessern

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Programm vs. Modell
#
# <img src="img/program-vs-model-01.png"
#      style="width: 80%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Programm vs. Modell
#
# <img src="img/program-vs-model-02.png"
#      style="width: 80%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Programm vs. Modell
#
# <img src="img/program-vs-model-03.png"
#      style="width: 50%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Programm vs. Modell
#
# <img src="img/program-vs-model-04.png"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Programm vs. Modell
#
# <img src="img/program-vs-model-06.png"
#      style="width: 40%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Beispiel: MNIST-Daten
#
# <img src="img/ag/Figure-01-023.png" style="float: right;width: 40%;"/>
#
# Wir wollen handgeschriebene Ziffern erkennen:

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Regelbasierte Systeme: Feature Engineering
#
# Extraktion relevanter Merkmale aus Daten durch Menschen.


# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/ag/Figure-01-003.png"
#      style="width: 40%; margin-left: auto; margin-right: auto;">

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/ag/Figure-01-004.png"
#      style="width: 20%; margin-left: auto; margin-right: auto;">

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Überwachtes Lernen (Klassifizierung)
#
# (Lernen aus gekennzeichneten Daten)
#
# <img src="img/ag/Figure-01-007.png"
#      style="width: 70%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Trainieren eines Klassifizierers
#
# - Zeige einem Lern-Algorithmus viele mit Labels versehene Daten
# - Prüfe, ob er Beispiele anhand von Merkmalen richtig klassifizieren kann
#
# - Die Bewertung muss auf anderen Daten basieren als das Training
# - Andernfalls könnte der Lernende nur die Beispiele speichern, die er gesehen hat

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Trainieren eines Modells
#
# <img src="img/program-vs-model-10.png"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Trainieren eines Modells
#
# <img src="img/program-vs-model-12.png"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Der ML Workflow
#
# <img src="img/ml-workflow-data.png"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Der ML Workflow
#
# <img src="img/ml-workflow-backtrack.png"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Oft: Trainingsschleife
#
# <img src="img/ag/Figure-08-001.png"
#      style="width: 50%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Aber welches Modell?
#
# <img src="img/program-vs-model-12.png"
#      style="width: 40%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auswahl eines Modells
#
# <img src="img/choosing-ml-models-01.png"
#      style="width: 80%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auswahl eines Modells
#
# <img src="img/choosing-ml-models-03.png"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auswahl eines Modells
#
# <img src="img/choosing-ml-models-05.png"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auswahl eines Modells
#
# <img src="img/choosing-ml-models-07.png"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auswahl eines Modells
#
# <img src="img/choosing-ml-models-09.png"
#      style="width: 60%; margin-left: auto; margin-right: auto;"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Zurück zu den MNIST-Daten
#
# <img src="img/ag/Figure-01-023.png" style="float: right;width: 40%;"/>
#
# Lassen Sie uns das in der Praxis versuchen:
#
# - Herunterladen und Vorbereiten der Daten
# - Trainieren eines Modells
# - Bewerten seiner Leistung
