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
#  <b>Dictionaries</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 Dictionaries.py -->
# <!-- python_courses/slides/module_150_collections/topic_160_b1_dictionaries.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Dictionaries
#
# - Dictionaries sind eine Datenstruktur, die Schlüssel (Keys) auf Werte abbildet
# - Für Keys sind viele Typen möglich:
#   - Integer-Werte
#   - Strings
#   - Tupel
#   - ...
# - Modifizierbare Objekte, wie z.B. Listen, können nicht als Schlüssel verwendet werden
# - Werte können beliebige Python Objekte sein
# - Die Einträge in einem Dictionary sind nicht in einer bestimmten Reihenfolge
#   angeordnet
# - Einträge können hinzugefügt, gelöscht und modifiziert werden.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Leeres Dictionary:

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Dictionary mit String-Keys:

# %% tags=["keep"]
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}
translations

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Zugriff mit Default-Wert

# %% tags=["keep"]
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Modifikation von Elementen

# %% tags=["keep"]
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Hose"}
translations

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Update mit Default-Wert

# %% tags=["keep"]
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}
translations

# %%

# %%

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
translations = {"snake": "Schlange", "bat": "Fledermaus", "horse": "Pferd"}
translations

# %%

# %%

# %%

# %%
# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Secondhand Verkauf
#
# Sie beschließen nicht mehr benötigte Kleidung bei einem Secondhand-Shop zu verkaufen.
# Um zu berechnen, wie hoch die Einnahmen sein werden,
# schreiben Sie eine Funktion
# `gesamtpreis(kleidungsstücke: list, preise: dict) -> float`:
#
# - `kleidungsstücke` ist eine Liste mit allen Kleidungsstücken, die Sie verkaufen
#   wollen, z.B.
#   ```python
#   ["Wintermantel", "Cordhose", "Smoking"]
#   ```
# - `preise` ist ein Dictionary mit den Preisen, die der Händler für jedes
#   Kleidungsstück bezahlt, z.B.
#   ```python
#   {"Wintermantel": 80, "Smoking": 40}
#   ```
# - Die Funktion `gesamtpreis()` gibt den Betrag zurück, den Ihnen der Händler für
#   die Kleidungsstücke in `kleidungsstücke` bezahlt.
# - Wenn in `kleidungsstücke` Einträge sind, die nicht in `preise` vorkommen,
#   dann kauft der Händler diese Kleidungsstücke nicht und Sie bekommen 0 Euro dafür.

# %% lang="de"

# %% lang="de" tags=["keep"]
alte_kleidung = ["Wintermantel", "Cordhose", "Smoking"]
secondhand_preise = {"Wintermantel": 80, "Smoking": 40}

# %% lang="de" tags=["keep"]
assert gesamtpreis(alte_kleidung, secondhand_preise) == 120
assert gesamtpreis(alte_kleidung + ["Smoking"], secondhand_preise) == 160

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Vorbereitung für den nächsten Workshop

# %% tags=["keep"]
advice = "Don't worry be happy"

# %% tags=["keep"]
words = advice.split()

# %% tags=["keep"]
" ".join(words)

# %% tags=["keep"]
smileys = {"worry": "\U0001f61f", "happy": "\U0001f600"}


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# Schreiben Sie eine Funktion `replace_words(text: str, replacements: dict)`, die alle
# Wörter, die in `dict` als Key vorkommen durch ihren Wert in `dict` ersetzen.
#
# ```python
# >>> replace_words(advice, smileys)
# "Don't 😟 be 😀"
# ```

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Hinweise
#
# - Splitten Sie `text` in eine Liste `words` aus einzelnen Wörtern
#
# - Erzeugen Sie eine neue leere Liste `new_words`
#
# - Iterieren Sie über `words` und fügen Sie jedes Wort, das nicht im Wörterbuch
#   vorkommt unverändert an `new_words` an; fügen Sie für jedes Wort, das im Wörterbuch
#   vorkommt seine Übersetzung an
#
# - Fügen Sie `new_words` mit der `join()`-Methode zu einem String zusammen

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["keep"]
assert replace_words(advice, smileys) == "Don't 😟 be 😀"

# %% tags=["keep"]
assert replace_words("happy happy", smileys) == "😀 😀"

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop "Inverser Index"
#
# Schreiben Sie eine Funktion `first_index(a_list: list) -> dict`, die ein Dictionary
# `d` zurückgibt, für das gilt:
#
# - Die Schlüssel in `d` sind alle in `a_list` vorkommenden Werte
# - Für jeden Wert `elt`, der in `a_list` enthalten ist, ist der Wert von `d[elt]`
#   der erste Index, an dem `elt` in `a_list` vorkommt
#
# ```python
# >>> first_index(["a", "b", "b"])
# {'a': 0, 'b': 1}
# ```
#
# *Hinweis:* Eine einfache Lösung verwendet die Funktion `enumerate()`.
#
# Stellen Sie sicher, dass Ihre Lösung die vorgegebenen Tests erfüllt.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
example_values = ["a", "b", "c", "b", "a", "c", "a"]

# %% tags=["keep"]
ii = first_index(example_values)

# %% tags=["keep"]
assert ii["a"] == 0

# %% tags=["keep"]
assert ii["b"] == 1

# %% tags=["keep"]
assert ii["c"] == 2

# %% tags=["keep"]
assert ii.get("d") is None

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Schreiben Sie eine Funktion `inverse_index(a_list: list) -> dict`, die ein Dictionary
# `d` zurückgibt, für das gilt:
#
# - Die Schlüssel in `d` sind alle in `a_list` vorkommenden Werte
# - Für jeden Wert `elt`, der in `a_list` enthalten ist, ist der Wert von `d[elt]`
#   die Liste mit allen Indizes, an dem `elt` in `a_list` vorkommt
#
# ```python
# >>> inverse_index(["a", "b", "b"])
# {'a': [0], 'b': [1, 2]}
# ```


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
example_values = ["a", "b", "c", "b", "a", "c", "a"]

# %% tags=["keep"]
ii = inverse_index(example_values)

# %% tags=["keep"]
assert ii["a"] == [0, 4, 6]

# %% tags=["keep"]
assert ii["b"] == [1, 3]

# %% tags=["keep"]
assert ii["c"] == [2, 5]

# %% tags=["keep"]
assert ii.get("d") is None
