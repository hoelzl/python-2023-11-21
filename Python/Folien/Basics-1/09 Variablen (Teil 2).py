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
#  <b>Variablen (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 Variablen (Teil 2).py -->
# <!-- python_courses/slides/module_120_data_types/topic_132_b1_variables_part2.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Variablennamen in Python
#
# - Fangen mit einem Buchstaben oder Unterstrich `_` an
#     - Umlaute gelten auch als Buchstaben
# - Können Ziffern, Buchstaben und Unterstriche `_` enthalten
# - Können viele andere Unicode-Zeichen enthalten
#     - Es ist aber meist besser, das zu vermeiden...
# - Groß- und Kleinschreibung wird unterschieden
#     - `A` ist eine andere Variable als `a`
#

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# 2fast4u = 2

# %% tags=["keep"]
ähnlichkeitsmaß = 0.1

# %% tags=["keep"]
_größenmaßstäbe_der_fußgängerübergänge = 0.3
_größenmaßstäbe_der_fußgängerübergänge

# %% tags=["keep"]
# me@foo = 1

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
α = 0.2
β = 0.7
γ = α**2 + 3 * β**2
print(γ)
αβγ = α * β * γ
print(αβγ)
Σ = 1 + 2 + 3
print(Σ)
# ∑ = 1 + 2 + 3 # Unzulässig!


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
variable_1 = 123
VARIABLE_1 = 234
Variable_1 = 345
variablE_1 = 456

# %% tags=["keep"]
print(variable_1)
print(VARIABLE_1)
print(Variable_1)
print(variablE_1)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Stil
#
# - Variablennamen werden klein geschrieben
#     - Außer konstanten Variablen: `CONSTANT_VAR`
# - Bestandteile werden durch Unterstriche `_` getrennt
#     - Dieser Stil nennt sich Snake-Case
# - Variablen, die mit zwei Unterstrichen anfangen und aufhören haben
#   typischerweise eine spezielle Bedeutung (*Dunders*):
#     - `__class__`, `__name__`
#     - Normale benutzerdefinierte Variablen sollten nicht als Dunders benannt
#       werden

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
print(__name__)
print(type(__name__))

# %% [markdown] lang="de"
#
# **Bitte nicht nachmachen, obwohl es möglich ist:**

# %%
__my_var__ = 123

# %%
__my_var__

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# - Manchmal werden "private" Variablen mit einem führenden Unterstrich
#   geschrieben: `_my_var`
#   - Das ist (für globale Variablen) besonders relativ verbreitet
#   - In Klassen gibt es weitere Konventionen
# - Die meisten Python-Projekte folgen den Konventionen in
#   [PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

# %%
_my_var = 234

# %%
_my_var

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
_my_var = 1
print(_my_var)
_my_var = _my_var + 5
print(_my_var)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Zuweisung an mehrere Variablen
#
# In Python können mehrere Variablen gleichzeitig definiert bzw. mit neuen
# Werten versehen werden:

# %%
a, b = 1, 2
print(a)
print(b)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Code Cleanup
#
# Der folgende Code enthält Verstöße gegen die in Python verwendete Syntax und die
# üblichen Konventionen. Code mit Syntaxfehlern ist auskommentiert. Korrigieren Sie
# ihn, so dass der Code in Python evaluiert werden kann und den Richtlinien für
# Variablennamen entspricht.

# %% lang="de" tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
__anzahl_der_teilnehmer__ = 10
# Preisgeld für den 1. und 2. Platz
# 1terPlatz = 500
# 2terPlatz = 250
GesamtesPreisgeld = 1000
# Summe der Preisgelder für die ersten beiden Plätze
# ΣPreisgelder = 1terPlatz + 2terPlatz

# %% lang="de"
anzahl_der_teilnehmer = 10
erster_platz = 500
zweiter_platz = 250
gesamtes_preisgeld = 1000
summe_preisgelder = erster_platz + zweiter_platz
