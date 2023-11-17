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
#  <b>Dateien</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 08 Dateien.py -->
# <!-- python_courses/slides/module_310_working_with_data/topic_110_a2_files.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Dateien
#
# Bislang gehen am Ende der Programmausführung alle Daten, die wir berechnet
# haben, verloren.
#
# Die einfachste Variante, Daten zu persistieren ist sie in einer Datei zu speichern.
#
# Bitte überprüfen Sie vor der Ausführung von Code in diesem Notebook, dass Ihr
# aktuelles Arbeitsverzeichnis keine wichtigen Daten enthält!


# %% tags=["keep"]
import os

# %% tags=["keep"]
os.getcwd()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  - Mit `open()` kann eine Datei zum Lesen oder Schreiben geöffnet werden.
#  - Der `mode` Parameter gibt an, ob die Datei zum Lesen oder Schreiben geöffnet
#    wird:
#    - `r`: Lesen
#    - `w`: Schreiben. Der Inhalt der Datei wird gelöscht
#    - `a`: Schreiben. Die neuen Daten werden ans Ende der Datei geschrieben.
#    - `x`: Schreiben. Die Datei darf nicht existieren.
#    - `r+`: Lesen und Schreiben.
#  - Wird ans Ende von `mode` der Buchstabe `b` angehängt, so wird die Datei als
#    Binärdatei behandelt.


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
file = open("my-data-file.txt", "w")
file.write("The first line.\n")
file.write("The second line.\n")
file.close()

# %% tags=["keep"]
file = open("my-data-file.txt", "r")
contents = file.read()
file.close()
print(contents)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  - Dateien müssen immer mit `close()` geschlossen werden, auch wenn der
#    Programmteil, in dem die Datei verwendet wird, eine Exception auslöst.
#  - Das könnte mit `try ... finally` erfolgen.
#  - Python bietet dafür ein eleganteres Konstrukt:

# %% tags=["keep"]
with open("my-data-file.txt", "r") as file:
    contents = file.read()
print(contents)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mode-Werte zum Schreiben

# %% tags=["keep"]
with open("my-data-file.txt", mode="w") as file:
    file.write("Another line.\n")
    file.write("Yet another line.\n")

# %% tags=["keep"]
with open("my-data-file.txt", mode="r") as file:
    contents = file.read()
print(contents)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
with open("my-data-file.txt", mode="a") as file:
    file.write("Let's try this again.\n")
    file.write("Until we succeed.\n")

# %% tags=["keep"]
with open("my-data-file.txt", "r") as file:
    contents = file.readlines()
print(contents)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
# with open("my-data-file.txt", mode="x") as file:
#     file.write("Let's try this again.\n")
#     file.write("Until we succeed.\n")

# %% tags=["alt"]
from pathlib import Path

# %% tags=["alt"]
Path("my-data-file.txt").unlink(missing_ok=True)


# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Mini-Workshop: Lesen und Schreiben in Dateien
#
# Schreiben Sie eine Funktion
# `write_text_to_file(text: str, file_name: str)-> None`,
# die den String `text` in die Datei `file_name` schreibt, sofern
# diese *nicht* existiert und eine Exception vom Typ `FileExistsError` wirft,
# falls die Datei existiert.
#
# *Hinweis:*  Beachten Sie die möglichen Werte für das `mode` Argument von
# `open()`.

# %%
def write_text_to_file(text, file_name):
    with open(file_name, "x") as file:
        file.write(text)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Testen Sie die Funktion, indem Sie zweimal hintereinander versuchen den
# Text `Python 3.11` in die Datei `my-private-file.txt` zu schreiben.

# %% tags=["alt"]
from pathlib import Path

# %% tags=["alt"]
Path("my_private_file.txt").unlink(missing_ok=True)

# %%
write_text_to_file("Python 3.11", "my_private_file.txt")


# %%
# write_text_to_file("Python 3.11", "my_private_file.txt")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Schreiben Sie eine Funktion `annotate_file(file_name: str) -> None`, die
# - den Inhalt der Datei `file_name` gefolgt von dem Text `(annotated version)`
#   auf dem Bildschirm ausgibt, falls sie existiert
# - den Text `No file found, we will bill the time we spent searching.` ausgibt
#   falls sie nicht existiert
# - in beiden Fällen den Text `Our invoice will be sent by mail.` ausgibt.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def annotate_file(file_name):
    try:
        with open(file_name, "r") as file:
            print(file.read())
            print("(annotated version)")
    except FileNotFoundError:
        print("No file found, we will bill the time we spent searching.")
    finally:
        print("Our invoice will be sent by mail.")


# %%
annotate_file("my_private_file.txt")

# %%
annotate_file("does-not-exist.txt")

# %% tags=["alt"]
Path("my_private_file.txt").unlink(missing_ok=True)
Path("my-data-file.txt").unlink(missing_ok=True)
