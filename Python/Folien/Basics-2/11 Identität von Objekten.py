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
#  <b>Identität von Objekten</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 11 Identität von Objekten.py -->
# <!-- python_courses/slides/module_160_objects/topic_110_identity.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  ## Identität von Objekten

# %% tags=["keep"]
a = [1, 2, 3]
b = [1, 2, 3]
c = b

# %% tags=["keep"]
print(f"a = {a}, b = {b}, c = {c}")

# %% tags=["keep"]
a[0] = 10

# %% tags=["keep"]
print(f"a = {a}, b = {b}, c = {c}")

# %% tags=["keep"]
b[0] = 20

# %% tags=["keep"]
c[1] = 30

# %% tags=["keep"]
print(f"a = {a}, b = {b}, c = {c}")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  ## Test der Identität von Objekten

# %% tags=["keep"]
a = [1, 2, 3]
b = [1, 2, 3]
c = b


# %% [markdown] lang="de"
#
#  `==` testet Gleichheit der Werte, nicht (notwendigerweise) Objektidentität.

# %% tags=["keep"]
a == b

# %% tags=["keep"]
b == c

# %% tags=["keep"]
a[0] = 10
a == b

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  Mit `is` kann man Objektidentität testen:

# %% tags=["keep"]
a = [1, 2, 3]
b = [1, 2, 3]
c = b


# %% tags=["keep"]
a is b

# %% tags=["keep"]
b is c

# %% tags=["keep"]
b[0] = 10

# %% tags=["keep"]
print(f"a = {a}, b = {b}, c = {c}")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  Die Funktion `id()` gibt die Adresse eines Objekts zurück:

# %% tags=["keep"]
id([1, 2, 3])

# %% [markdown] lang="de"
#
#  Meistens stellt man Adressen in hexadezimaler Form dar:

# %% tags=["keep"]
hex(id([1, 2, 3]))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Identität
#
# Gegeben seien die folgenden Listen:

# %% tags=["keep"]
a = [1, 2, 3]
b = [1, 2]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Sind `a` und `b` Listen, die die gleichen Elemente haben?
# - Sind `a` und `b` die gleiche Liste?
# - An welcher Adresse befindet sich `b`?

# %%
a == b

# %%
a is b

# %%
hex(id(b))

# %% tags=["alt"]
addr_b = hex(id(b))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Werten Sie jetzt die folgende Zelle aus:

# %% tags=["keep"]
b.append(3)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Sind `a` und `b` jetzt Listen, die die gleichen Elemente haben?
# - An welcher Adresse befindet sich jetzt `b`?

# %%
a == b

# %%
hex(id(b))

# %%
addr_b == hex(id(b))
