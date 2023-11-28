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
#  <b>Pandas Data Frames 2</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Pandas Data Frames 2.py -->
# <!-- python_courses/slides/module_610_pandas/topic_140_pandas_data_frames_3.py -->

# %% tags=["keep"]
import numpy as np
import pandas as pd


# %% [markdown] lang="de"
# ## Fehlende Werte

# %% tags=["keep"]
def create_data_frame_with_nans():
    return pd.DataFrame(
        {
            "A": [1, 2, np.nan, np.nan, 0],
            "B": [5, 6, 7, np.nan, 0],
            "C": [9, 10, 11, 12, 0],
            "D": [13, 14, 15, 16, 0],
            "E": [np.nan, 18, 19, 20, 0],
        }
    )

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%


# %%

# %% [markdown] lang="de"
# ## Gruppieren

# %% tags=["keep"]
def create_course_df():
    data = {
        "Course": [
            "Python",
            "Python",
            "Python",
            "Python",
            "Java",
            "Java",
            "Java",
            "C++",
            "C++",
        ],
        "Person": [
            "Jack",
            "Jill",
            "John",
            "Bill",
            "Jack",
            "Bill",
            "Davy",
            "Jack",
            "Diane",
        ],
        "Score": [97, 92, 38, 73, 81, 52, 62, 86, 98],
    }
    return pd.DataFrame(data)

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
# %%


# %% [markdown] lang="de"
# ## Operationen (Fortsetzung)

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
# ## Auswahl

# %%

# %%

# %% [markdown] lang="de"
#
# ## Transformation von Daten

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
# ## Elementweise Anwendung von Funktionen:

# %%

# %% tags=["keep"]
