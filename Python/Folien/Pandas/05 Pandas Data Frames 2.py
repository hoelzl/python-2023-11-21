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
df = create_data_frame_with_nans()

# %%
df

# %%
df.isna()

# %%
df.count()

# %%
df

# %%
df.count(axis=1)

# %%
df.isna().sum()

# %%
df.isna().sum(axis=1)

# %%
df

# %%
df.dropna()

# %%
df

# %%
df.dropna(axis=1, inplace=True)

# %%
df

# %%
df = create_data_frame_with_nans()
df

# %%
df.fillna(value=1000)

# %%
df.mean()

# %%
df.fillna(value=df.mean())


# %%
# df.fillna(value=df.mean(axis=1), axis=1)

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
df = create_course_df()
df

# %%
df.groupby("Course")

# %%
df_by_course = df.groupby("Course")

# %%
df_by_course.count()

# %%
df_by_course["Person"].count()

# %%
df_by_course.mean(numeric_only=True)

# %%
df_by_course.std(numeric_only=True)

# %%
df_by_course["Score"].aggregate(["mean", "std"])

# %%
df_by_course.aggregate(["min", "max"])

# %%
df_by_course["Score"].aggregate(["min", "max", "mean", "std"])

# %%
df_by_course.describe()

# %%
df.groupby("Person").apply(list)

# %%
df.groupby("Person")["Score"].mean()
# %%
df.groupby("Person").describe()


# %% [markdown] lang="de"
# ## Operationen (Fortsetzung)

# %%
df = create_course_df()
df

# %%
df.columns

# %%
df.index

# %%
df.sort_values(by="Course")

# %%
df["Course"].values

# %%
df["Person"].values

# %%
df["Course"].unique()

# %%
df["Person"].unique()

# %%
df["Person"].nunique()

# %%
df["Person"].value_counts()

# %% [markdown] lang="de"
# ## Auswahl

# %%
df[df["Score"] > 80]

# %%
df[(df["Score"] > 60) & (df["Score"] <= 80)]

# %% [markdown] lang="de"
#
# ## Transformation von Daten

# %%
df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=["A", "B"])

# %%
df

# %%
df.apply(np.square)

# %%
df.apply(np.sum)

# %%
df.apply(np.sum, axis=1)

# %%
df.apply(lambda n: [np.sum(n), np.mean(n)], axis=1)

# %%
df.apply(
    lambda n: [np.sum(n), np.mean(n)],
    axis=1,
    result_type="expand",
).rename(columns={0: "sum", 1: "mean"})

# %%
df.apply(
    lambda n: {"sum": np.sum(n), "mean": np.mean(n)},
    axis=1,
    result_type="expand",
)

# %% [markdown] lang="de"
# ## Elementweise Anwendung von Funktionen:

# %%
df.map(lambda x: f"Value: {x}")

# %% tags=["keep"]
