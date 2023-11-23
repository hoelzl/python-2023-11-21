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
#  <b>Assertions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 17 Assertions.py -->
# <!-- python_courses/slides/module_170_exceptions/topic_120_a3_assertions.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Assertions
#
# Das Assert-Statement ist nur eine kompakte Schreibweise, um eine bestimmte Art von
# Fehler (einen `AssertionError`) auszulösen, wenn eine Bedingung falsch ist:

# %% tags=["keep"]
my_var = 1

# %%
assert my_var == 1

# %%
if my_var != 1:
    raise AssertionError()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# assert my_var == 2

# %% tags=["keep"]
# if my_var != 2:
#     raise AssertionError()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Assert mit optionalem Fehler-Text:

# %%
assert my_var == 1, "my_var should be 1"

# %%
if my_var != 1:
    raise AssertionError("my_var should be 1")

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
# assert my_var == 2, "my_var should be 2"

# %% tags=["keep"]
# if my_var != 2:
#     raise AssertionError("my_var should be 2")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Asserts können mit dem `-O`-Flag deaktiviert werden.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import subprocess
import shutil

# %% tags=["keep"]
python_exe = shutil.which("python")
assert python_exe
python_exe

# %% tags=["keep"]
with open("test_assert.py") as f:
    print(f.read())

# %% tags=["keep"]
# %less test_assert.py

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
cp = subprocess.run([python_exe, "test_assert.py"], capture_output=True, text=True)
print(cp.stderr)


# %% tags=["keep"]
cp = subprocess.run(
    [python_exe, "-O", "test_assert.py"], capture_output=True, text=True
)
print(cp.stderr)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Asserts sind nützlich, um Annahmen über den Programmzustand zu dokumentieren.
# - Sie sind aber nicht dazu gedacht, Fehler in Eingaben abzufangen.

# %% tags=["keep"]
def bad_user_input():
    number = input("Please enter a number: ")
    assert number.isdigit(), "Input must be a number!"
    return int(number)


# %% tags=["keep"]
def better_user_input():
    number = input("Please enter a number: ")
    if not number.isdigit():
        raise ValueError("Input must be a number!")
    return int(number)
