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
numbers[1]

# %%
numbers[1] = 10
numbers

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Test, ob ein Element enthalten ist

# %% tags=["keep"]
numbers = [5, 6, 7]

# %%
5 in numbers

# %%
3 in numbers

# %%
3 not in numbers

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Länge einer Liste

# %% tags=["keep"]
numbers = [2, 4, 6, 8]
numbers

# %%
len(numbers)

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
numbers = [2, 3, 4]
numbers.append(10)
numbers

# %%
numbers = [2, 3, 4]
numbers.extend([10, 20])
numbers

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Append vs. Extend

# %% tags=["keep"]
numbers = [2, 3, 4]

# %%
numbers.append([10, 20])
numbers

# %% tags=["keep"]
numbers = [2, 3, 4]

# %%
numbers.extend([10, 20])
numbers

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Extend vs. `+`

# %% tags=["keep"]
numbers = [2, 3, 4]

# %%
numbers.extend([10, 20])

# %%
numbers

# %% tags=["keep"]
numbers = [2, 3, 4]

# %%
numbers + [50, 60]

# %%
numbers

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Löschen und Einfügen an beliebigen Positionen

# %%
numbers = [2, 3, 4, 5]
numbers.pop()
numbers

# %%
numbers.insert(1, 10)
numbers

# %%
numbers.pop(1)
numbers

# %%
del numbers[1]
numbers

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
numbers.sort()

# %%
numbers

# %% tags=["keep"]
numbers = [3, 8, 6, 1, 9, 2, 5, 4]
numbers

# %%
sorted(numbers)

# %%
numbers


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
"Gelb" in grundfarben

# %% lang="de"
"Grün" in grundfarben

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wie viele Elemente hat die Liste `grundfarben`?
# - Wie viele Elemente hat die Liste `mischfarben`?

# %% lang="de"
len(grundfarben)

# %% lang="de"
len(mischfarben)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir haben vergessen Magenta in die Mischfarben einzufügen.
#
# - Überprüfen Sie, dass der String `"Magenta"` nicht in `mischfarben` enthalten ist.
# - Fügen Sie `Magenta` zu den Mischfarben hinzu.
# - Überprüfen Sie, dass der String `"Magenta"` jetzt in `mischfarben` enthalten ist.
# - Wie lange ist die Liste `mischfarben` jetzt?

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
"Magenta" in mischfarben

# %% lang="de"
mischfarben.append("Magenta")

# %% lang="de"
"Magenta" in mischfarben

# %% lang="de"
len(mischfarben)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# - Ändern Sie das erste Element von `farben` in `Dunkelrot`
# - Was ist jetzt das erste Element von `grundfarben`?

# %% lang="de"
farben[0] = "Dunkelrot"
farben

# %% lang="de"
grundfarben[0]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Was ist das dritte Element der Liste `farben`?

# %% lang="de"
farben[2]

# %% [markdown] lang="de"
# Fügen Sie `Lila` als zweites Element in die Liste `farben` ein.

# %% lang="de"
farben.insert(1, "Lila")

# %% [markdown] lang="de"
# Was ist jetzt das dritte Element der Liste `farben`?

# %% lang="de"
farben[2]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Löschen Sie das zweite Element der Liste `farben`

# %% lang="de"
farben.pop(1)
farben

# %% [markdown] lang="de"
#
# Sortieren Sie die Liste `farben`.

# %% lang="de"
farben.sort()
farben

# %% [markdown] lang="de"
# Was ist jetzt das erste Element der Liste `farben`?

# %% lang="de"
farben[0]

