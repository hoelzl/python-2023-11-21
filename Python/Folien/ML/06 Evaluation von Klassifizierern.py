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
#  <b>Evaluation von Klassifizierern</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 Evaluation von Klassifizierern.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_150_evaluating_classifiers.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Evaluation von Klassifizierern

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#  # Wie gut sind wir?
#
#  Woher wissen wir, wie gut unser Modell funktioniert?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Was kann schief gehen?
#
#  <img src="img/ag/Figure-03-015.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Was kann schief gehen?
#
#  <img src="img/ag/Figure-03-021.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Was kann schief gehen?
#
#  <img src="img/ag/Figure-03-022.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Was kann schief gehen?
#
#  <img src="img/ag/Figure-03-017.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Confusion Matrix
#
#  <img src="img/ag/Figure-03-018.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Confusion Matrix
#
#  <img src="img/ag/Figure-03-019.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Genauigkeit (Accuracy): Wie viel haben wir richtig gemacht?
#
#
#  <img src="img/ag/Figure-03-028.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Genauigkeit (Accuracy): Wie viel haben wir richtig gemacht?
#
#  <img src="img/ag/Figure-03-029.png" style="width:60%; padding: 30px 100px 0"/>


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Genauigkeit (Accuracy): Wie viel haben wir richtig gemacht?
#
#  <img src="img/ag/Figure-03-023.png" style="width: 100%; padding: 30px 100px 0"/>


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Präzision: Wie gut sind unsere positiven Ergebnisse?
#
#  <img src="img/ag/Figure-03-030.png" style="width: 80%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Präzision: Wie gut sind unsere positiven Ergebnisse?
#
#  <img src="img/ag/Figure-03-024.png" style="width: 80%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Recall: Wie viele positive Ergebnisse haben wir verloren?
#
#  <img src="img/ag/Figure-03-031.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Recall: Wie viele positive Ergebnisse haben wir verloren?
#
#  <img src="img/ag/Figure-03-026.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Beschreiben von Klassifikations-Ergebnissen
#
#  <img src="img/ag/Figure-03-033.png" style="width: 80%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Beschreiben von Klassifikations-Ergebnissen
#
#  <img src="img/ag/Figure-03-034.png" style="width: 50%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#  ## Beschreiben von Klassifikations-Ergebnissen
#
#  <img src="img/ag/Figure-03-032.png" style="width: 50%; padding: 30px 100px 0"/>


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-00.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-01.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-02.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-03.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-04.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-05.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-06.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-07.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-08.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Precision/Recall Tradeoff
#
#  <img src="img/precision-recall-09.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#  ## Precision/Recall Tradeoff
#
#  <img src="img/ag/Figure-03-017.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Precision/Recall Tradeoff
#
# <img src="img/ag/Figure-03-035.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Precision/Recall Tradeoff
#
# <img src="img/ag/Figure-03-036.png" style="width: 70%; padding: auto"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Precision/Recall Tradeoff
#
# <img src="img/ag/Figure-03-037.png" style="width: 80%; padding: auto"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Precision/Recall Tradeoff
#
# <img src="img/ag/Figure-03-038.png" style="width: 70%; padding: auto"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#  ## F1: Evaluierung des Precision/Recall Tradeoffs
#
#  <img src="img/ag/Figure-03-039.png" style="width: 100%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#  ## Unbalancierte Daten
#
#  <img src="img/ag/Figure-03-020.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#  ## Unbalancierte Daten
#
#  <img src="img/ag/Figure-03-040.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#  ## Unbalancierte Daten
#
#  <img src="img/ag/Figure-03-041.png" style="width: 60%; padding: 30px 50px 0"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#  ## Unbalancierte Daten
#
#  <img src="img/ag/Figure-03-042.png" style="width: 60%; padding: 30px 100px 0"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#  ## Unbalancierte Daten
#
#  <img src="img/ag/Figure-03-043.png" style="width: 100%; padding: 30px 100px 0"/>
