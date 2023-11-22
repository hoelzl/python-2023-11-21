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
#  <b>Benutzerdefinierte Module</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 Benutzerdefinierte Module.py -->
# <!-- python_courses/slides/module_180_modules_and_packages/topic_110_a5_modules.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  - Der Python Interpreter bietet nur einen kleinen Teil der für die meisten
#    Programme benötigten Funktionalität
#    - Keine Interaktion mit dem Betriebssystem
#    - Kein Netzwerkfunktionalität
#    - Keine GUI
#    - ...
#  - Durch *Module* und *Packages* kann diese Funktionalität bei Bedarf geladen
#    werden.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Importieren eines Pakets

# %%
import os

# %% [markdown] lang="de"
#
# Verwenden der Funktionalität: aktuelles Verzeichnis

# %%
os.getcwd()

# %% [markdown] lang="de"
#
# Auflisten des aktuellen Verzeichnisses:

# %%
os.listdir(os.getcwd())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  Python bietet viele Standardmodule an, die mit dem Interpreter installiert
#  werden:
#
#  - abc: Abstract base classes
#  - argparse: Kommandozeilenargumente
#  - asyncio: Asynchrone Programmierung
#  - collections: Container-Datentypen
#  - ...
#
#  [Hier](https://docs.python.org/3/py-modindex.html) ist eine vollständigere Liste.

# %%
{"num-cpus": os.cpu_count(), "pid": os.getpid()}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Interne Darstellung von Code im Python-Interpreter:

# %%
import ast

# %%
ast.dump(ast.parse("print(123)"), False)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ## Benutzerdefinierte Module
#
#  Ein benutzerdefiniertes Modul ist eine Datei mit Python-Code.
#
#  Wie wir schon gesehen haben:
#  - Wenn sich ein Python-Modul im Suchpfad befindet, kann es mit `import`
#    geladen werden.
#  - Jupyter Notebooks lassen sich nicht (ohne zusätzliche Pakete) als Module laden.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
# Welche Python-Dateien gibt es im aktuellen Verzeichnis?
for filename in os.listdir(os.getcwd()):
    if filename[-3:] == ".py":
        print(filename)

# %% [markdown] lang="de"
#
# Anzeigen des Quellcodes von `my_test_module.py`

# %% tags=["keep"]
# # %pycat my_test_module.py

# %% [markdown] lang="de"
#
# Andere Möglichkeit den Quellcode anzuzeigen:

# %%
with open("my_test_module.py", "r") as file:
    text = file.read()

print(text)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Laden von Modulen
#
# - Die `import`-Anweisung lädt die zum Modul gehörige Datei
# - Top-Level Code wird ausgeführt
# - Das Modul wird in einem Cache gespeichert

# %% tags=["keep"]
# noinspection PyUnresolvedReferences
import my_test_module


# %%
# Top-level code wird NICHT mehr ausgeführt
import my_test_module


# %%
my_test_module.add1(2)


# %%
# add1


# %%
import my_test_module as mm

# %%
mm.add1(1)


# %%
mm.perform_complex_computation(17)


# %%
from my_test_module import multiply_by_2


# %%
multiply_by_2(2)


# %%
from my_test_module import multiply_by_2 as mult2


# %%
mult2(4)


# %%
# Im Regelfall besser vermeiden:
from my_test_module import *


# %%
multiply_by_2(3)


# %%
add1(3)


# %%
# Anzeigen aller definierten Namen:
dir(my_test_module)


# %%
[name for name in dir(my_test_module) if name[0] != "_"]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Einschub: Automatischer Reload von Modulen
#
# In IPython (und damit Jupyter Notebooks) ist es möglich das automatische Laden
# von modifizierten Modulen zu aktivieren:

# %% tags=["keep"]
# %load_ext autoreload
# %autoreload 2

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# In Startup-Skripten kann man syntaktische Warnungen vermeiden, wenn man statt dessen
# schreibt:

# %% tags=["keep"]
try:
    get_ipython().run_line_magic("load_ext", "autoreload")  # noqa
    get_ipython().run_line_magic("autoreload", "2")  # noqa
except NameError:
    pass

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ## Beispiel: `HttpServer`
#
# Der Python Interpreter hat keinen eingebauten HTTP Server. Mittels der
# Standardbibliothek ist es aber nicht schwer einen zu schreiben.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ### Beispiel: `ModuleTest`
#
# Das `ModuleTest` Beispiel zeigt, wie ein Programm aus mehreren Modulen
# bestehen kann.

# %% tags=["keep"]
__name__
