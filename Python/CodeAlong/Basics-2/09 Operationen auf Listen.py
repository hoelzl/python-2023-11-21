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
#  <b>Operationen auf Listen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 Operationen auf Listen.py -->
# <!-- python_courses/slides/module_150_collections/topic_112_b1_list_operations.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Modifikation von Listeneinträgen

# %% tags=["keep"]
numbers = [2, 4, 6, 8]
numbers

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Test, ob ein Element enthalten ist

# %% tags=["keep"]
numbers = [5, 6, 7]

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Länge einer Liste

# %% tags=["keep"]
numbers = [2, 4, 6, 8]
numbers

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Methoden auf Listen
#
# - Viele Operationen auf Listen sind als sog. *Methoden* implementiert.
# - Eine Methode ist sehr ähnlich zu einer Funktion, gehört aber zu einem Objekt.
# - Das "Objekt zu dem die Methode gehört" steht vor dem Methodennamen.
# - Die Syntax ist `object.my_method()`.
# - Die Bedeutung ist ähnlich zu `my_method(object)`.
# - Viele Methoden verändern das Objekt, auf dem sie arbeiten, destruktiv.

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Einfügen und Löschen von Elementen
#
# - Einfügen und Löschen sind an beliebigen Stellen möglich.
# - Aus Effizienzgründen ist es zweckmäßig Elemente am Ende der Liste
#   einzufügen und zu löschen.

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Append vs. Extend

# %% tags=["keep"]
numbers = [2, 3, 4]

# %%

# %% tags=["keep"]
numbers = [2, 3, 4]

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Extend vs. `+`

# %% tags=["keep"]
numbers = [2, 3, 4]

# %%

# %%

# %% tags=["keep"]
numbers = [2, 3, 4]

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Löschen und Einfügen an beliebigen Positionen

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Sortieren von Listen
#
# - Mit der Methode `sort()` können Listen sortiert werden. Dabei wird die Reihenfolge
#   der Elemente in der Liste geändert, auf der die Methode aufgerufen wird.
# - Mit der Funktion `sorted()` kann eine neue Liste erzeugt werden, die die Elemente
#   der ursprünglichen Liste in sortierter Reihenfolge enthält.


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
numbers = [3, 8, 6, 1, 9, 2, 5, 4]
numbers

# %%

# %%

# %% tags=["keep"]
numbers = [3, 8, 6, 1, 9, 2, 5, 4]
numbers

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Farben (Teil 2)
#
# Gegeben seien die folgenden Listen:

# %% lang="de" tags=["keep"]
grundfarben = ["Rot", "Grün", "Blau"]
mischfarben = ["Cyan", "Gelb"]
farben = grundfarben + mischfarben

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Überprüfen Sie, ob Gelb eine Grundfarbe ist, ob also der String `"Gelb"`
#   in `grundfarben` enthalten ist.
# - Ist Grün eine Grundfarbe?

# %% lang="de"

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wie viele Elemente hat die Liste `grundfarben`?
# - Wie viele Elemente hat die Liste `mischfarben`?

# %% lang="de"

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir haben vergessen Magenta in die Mischfarben einzufügen.
#
# - Überprüfen Sie, dass der String `"Magenta"` nicht in `mischfarben` enthalten ist.
# - Fügen Sie `Magenta` zu den Mischfarben hinzu.
# - Überprüfen Sie, dass der String `"Magenta"` jetzt in `mischfarben` enthalten ist.
# - Wie lange ist die Liste `mischfarben` jetzt?

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% lang="de"

# %% lang="de"

# %% lang="de"


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# - Ändern Sie das erste Element von `farben` in `Dunkelrot`
# - Was ist jetzt das erste Element von `grundfarben`?

# %% lang="de"

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Was ist das dritte Element der Liste `farben`?

# %% lang="de"

# %% [markdown] lang="de"
# Fügen Sie `Lila` als zweites Element in die Liste `farben` ein.

# %% lang="de"

# %% [markdown] lang="de"
# Was ist jetzt das dritte Element der Liste `farben`?

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Löschen Sie das zweite Element der Liste `farben`

# %% lang="de"

# %% [markdown] lang="de"
#
# Sortieren Sie die Liste `farben`.

# %% lang="de"

# %% [markdown] lang="de"
# Was ist jetzt das erste Element der Liste `farben`?

# %% lang="de"

