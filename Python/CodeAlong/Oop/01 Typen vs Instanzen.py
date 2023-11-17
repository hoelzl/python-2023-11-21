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
#  <b>Typen vs. Instanzen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Typen vs Instanzen.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_110_a3_types_vs_instances.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Typen vs. Instanzen
#
# In Python können benutzerdefinierte Datentypen (Klassen) definiert werden.
#
# Um uns darauf vorzubereiten, wollen wir uns den Unterschied zwischen Typen
# und Instanzen von Typen (Objekten) in [Python Tutor](https://tinyurl.com/yc8r5d45)
# ansehen.

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
list_instance = list("abc")


# %% tags=["keep"]
def my_fun(arg: list):
    pass


# %% tags=["keep"]
my_fun(list_instance)

# %% tags=["keep"]
my_fun(list("xyz"))

# %% tags=["keep"]
my_fun(list)
