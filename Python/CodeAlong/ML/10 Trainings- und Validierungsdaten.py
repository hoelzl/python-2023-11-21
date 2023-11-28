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
#  <b>Trainings- und Validierungsdaten</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 Trainings- und Validierungsdaten.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_175_training_data.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Trainings- und Validierungs-Daten
#
# - Bei der Suche nach guten Hyperparametern trainieren wir typischerweise viele
#   Modelle
# - Wenn wir unsere Test-Daten verwenden, um dabei die Performance zu evaluieren,
#   dann sind sie nicht mehr zur Bestimmung der Modell-Performance geeignet
# - Eine Möglichkeit damit umzugehen ist, die Trainingsdaten nochmal zu splitten:
#   - Trainingsdaten
#   - Validierungs-Daten zum Hyperparmeter Tuning
#   - Test-Daten um das fertige Modell zu evaluieren

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Cross-Validation
#
# - Ein Problem bei diesem Vorgehen ist, dass wir die Anzahl der Trainingsdaten dadurch
#   weiter verringern.
# - Eine andere Möglichkeit zum Hyperparameter-Tuning ist Cross-Validation:


# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/cross-validation.png"
#      style="display:block;margin:auto;width:80%"/>
#
# <span style="font-size:10pt">Image from
#     <a href="https://github.com/scikit-learn/scikit-learn/blob/main/doc/images/grid_search_cross_validation.png">Scikit-Learn repository</a>.
#     License: <a href="https://github.com/scikit-learn/scikit-learn/blob/main/COPYING">3-clause BSD License</a>.</span>
