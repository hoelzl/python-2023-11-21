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
#  <b>Packages</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 Packages.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_120_a3_packages.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Packages
#
# - Pakete sind eine Methode, um Module in einer Hierarchie zu strukturieren:
#   `a.b.c`
# - Ein Paket ist eine Kombination aus mehreren Modulen
# - `b` ist ein Unterpaket von `a`
# - `c` ist ein Untermodul (oder Unterpaket) von `b`

# %%
import html.entities
from html.parser import HTMLParser

# %%
html.entities.entitydefs["Psi"]

# %%
HTMLParser()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Struktur von Packages
#
#  - Hierarchie durch Verzeichnisse und Python Dateien
#    - Z.B. Verzeichnis `html` mit Unterverzeichnissen `parser`, `entities`
#  - Benötigt eine `__init__.py` Datei in jedem Verzeichnis, aus dem Code importiert
#    werden soll
#  - Die `__init__.py` Datei kann leer sein (und ist oft leer)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  <img src="img/package-structure.png" alt="Package structure"
#       style="display:block;margin:auto;width:40%"></img>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Finden von Packages
#
#  - Python sucht in `sys.path` nach dem Package-Verzeichnis.
#  - Dieser kann durch die Environment-Variable `PYTHONPATH` oder direkt von
#    Python aus beeinflusst werden.
#  - In den meisten Fällen ist es besser, keine komplizierten Operationen an
#    `sys.path` vorzunehmen.

# %% tags=["keep"]
import sys

# %%
sys.path

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Das `import` statement
#
#  `import a.b.c`:
#
#  - `a` und `b` müssen Packages (Verzeichnisse) sein
#  - `c` kann ein Modul oder ein Package sein
#
#  `from a.b.c import d`
#  - `a` und `b` müssen Packages sein
#  - `c` kann ein Modul oder ein Package sein
#  - `d` kann ein Modul, ein Package oder ein Name (d.h. eine Variable, eine Funktion,
#    eine Klasse, usw.) sein

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Referenzen innerhalb eines Packages
#
#  - `from . import a` importiert `a` aus dem aktuellen Package
#  - `from .. import a` importiert `a` aus dem übergeordneten Package
#  - `from .foo import a` importiert `a` aus dem "Geschwistermodul" `foo`

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ## Beispiel: `MessageQueue`
#
#  Das `MessageQueue` Beispiel zeigt, wie ein Programm aus mehreren Packages
#  bestehen kann.
