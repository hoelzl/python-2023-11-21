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
#  <b>Setuptools und Installation</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 12 Setuptools und Installation.py -->
# <!-- python_courses/slides/module_190_packaging_and_distribution/topic_210_a5_setuptools_and_installation.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  # Setuptools: Distribution von Python Paketen
#
#  - Setuptools sind das Standard-Tool um installierbare Python-Pakete zu erzeugen.


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Beispiel: Erstellen einer Anwendung mit Bibliothek
#
#  - Hinzufügen von `setup.cfg` und `pyproject.toml`-Dateien mit Information über
#    die zu installierenden Packages und Skripte
#  - Hinzufügen einiger Hilfsdateien (`README.md`, `LICENSE`)
#  - Erstellen der Distribution mit `python -m build` (Benötigt das PyPA `build`
#    [package](https://github.com/pypa/build))
#  - Installation mit `pip` und dem generierten Wheel
#  - Installation während der Entwicklung: `pip install -e .`

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Workshop
#
# - `Workshop TODO Liste 3`
# - Abschnitt "Packaging"
