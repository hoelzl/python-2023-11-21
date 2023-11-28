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
#  <b>Hauspreise in Kalifornien</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 23 Hauspreise in Kalifornien.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_400_housing.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Hauspreise in Kalifornien

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Herunterladen und Analysieren der Daten

# %% tags=["keep"]
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from IPython.display import display
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

# %% tags=["keep"]
np.set_printoptions(precision=2)


# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
#
# ## Erzeugen von Data Frames
#
# Für tabellarische Daten ist es oft sinnvoll Pandas Data Frames zu erzeugen, da
# diese viele Funktionen zur Analyse und zum Bearbeiten derartiger Datensätze anbieten.

# %% tags=["keep"]
simple_df = pd.DataFrame(
    data={
        "attr_1": [1, 2, 3, 4],
        "attr_2": [1.0, 2.0, 3.0, 4.0],
        "attr_3": [0.1, 0.5, 0.2, 0.6],
    }
)

# %%

# %%

# %%

# %% tags=["keep"]
simple_data = np.array([[1, 1.0, 0.1], [2, 2.0, 0.5], [3, 3.0, 0.2], [4, 4.0, 0.6]])

# %% tags=["keep"]
simple_columns = ["attr_1", "attr_2", "attr_3"]

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% tags=["keep"]
pprint(all_columns, compact=True)
print("Length =", len(all_columns))

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% tags=["keep"]
x, y = california_housing.data, california_housing.target

# %% tags=["keep"]
pprint(x)
pprint(y)

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

# %% tags=["keep"]
pprint(y[:5], compact=True)
pprint(y_train[:5], compact=True)
pprint(y_test[:5], compact=True)

# %%

# %%

# %% tags=["keep"]
lat_idx = all_columns.index("Latitude")
print(lat_idx)
lng_idx = all_columns.index("Longitude")
print(lng_idx)

# %%

# %%

# %%

# %%

# %%

# %%

# %% tags=["keep"]
housing_df.plot(
    kind="scatter",
    x="Longitude",
    y="Latitude",
    alpha=0.4,
    s=housing_df["Population"] / 50,
    figsize=(8, 6),
    c="Target",
    cmap="jet",
    colorbar=True,
)
plt.show()

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Trainieren von Modellen

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

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
