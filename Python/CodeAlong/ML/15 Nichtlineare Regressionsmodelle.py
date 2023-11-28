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
#  <b>Nichtlineare Regressionsmodelle</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 15 Nichtlineare Regressionsmodelle.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_210_non_linear_regressors.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Nichtlineare Regressionsmodelle

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% tags=["keep"]
try:
    import python_courses.slides.module_700_ml_basics.evaluation_tools as et
except ModuleNotFoundError:
    import evaluation_tools as et

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
rng = np.random.default_rng(42)
x = rng.uniform(size=(150, 1), low=0.0, high=10.0)
x_plot = np.linspace(0, 10, 500)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def lin(x):
    return 0.85 * x - 1.5


# %% tags=["keep"]
def fun(x):
    return 2 * np.sin(x) + 0.1 * x**2 - 2


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
x_train, x_test = x[:100], x[100:]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Nearest Neighbors
#
# <img src="img/KnnClassification.svg"
#      style="width: 40%; margin-left: auto; margin-right: auto;"/>

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.neighbors import KNeighborsRegressor

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_non_random_regressor(KNeighborsRegressor, lin, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_non_random_regressor(
    KNeighborsRegressor, lin, x_train, x_test, n_neighbors=1
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_non_random_regressor(
    KNeighborsRegressor, lin, x_train, x_test, n_neighbors=2
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_non_random_regressor(
    KNeighborsRegressor, lin, x_train, x_test, n_neighbors=50
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor(KNeighborsRegressor, lin, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor(KNeighborsRegressor, fun, x_train, x_test)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Entscheidungsbäume

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Entscheidungsbäume trainieren
#
# - (Konzeptionell): Erstellen einer verschachtelten "if"-"then"-"else"-Anweisung
# - Jeder Test vergleicht ein Merkmal mit einem Wert
# - Man versucht, eine Verlustfunktion zu minimieren
#   (z. B. mittlerer quadratischer Fehler)
#
# ```python
# if feature_1 < 1.2:
#     if feature_2 < 3.0:
#         if feature_1 < 0.2:
#             return 25_324
#         else:
#             return 17_145
#     else:
#         ...
# else:
#     ...
# ```

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
x_plot = np.linspace(0, 10, 500)
plt.figure(figsize=(12, 4))
sns.lineplot(x=x_plot, y=fun(x_plot))
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.metrics import mean_squared_error

x_plot = np.linspace(0, 10, 500)
y_plot = np.ones_like(x_plot) * 1.5
print(mean_squared_error(fun(x_plot), y_plot))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(12, 4))
sns.lineplot(x=x_plot, y=fun(x_plot))
sns.lineplot(x=x_plot, y=y_plot)
plt.show()


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def approx(x):
    if x < 6.2:
        return -0.5
    else:
        return 5.5


# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
x_plot = np.linspace(0, 10, 500)
y_plot = [approx(x) for x in x_plot]
print(mean_squared_error(fun(x_plot), y_plot))

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(12, 4))
sns.lineplot(x=x_plot, y=fun(x_plot))
sns.lineplot(x=x_plot, y=y_plot)
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# Using Numpy instead of generating y_plot
plt.figure(figsize=(12, 4))
sns.lineplot(x=x_plot, y=fun(x_plot))
sns.lineplot(x=x_plot, y=np.select([x_plot < 6.2, x_plot >= 6.2], [-0.5, 5.5]))
plt.show()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Vorteile
#
# - Einfach zu verstehen und zu visualisieren
# - Interpretierbar
# - Gut für die Analyse des Datensatzes (z.B. Merkmals-Wichtigkeiten, ...)
# - Robust gegenüber statistischen Schwankungen in den Daten
# - Benötigt wenig Datenvorbereitung (nicht empfindlich gegenüber Mittelwert oder
#   Standardabweichung von Merkmalen, ...)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Nachteile
#
# - Sehr anfällig für Überanpassung
# - Empfindlich gegenüber unbalancierten Datensätzen
# - Nur diskrete Vorhersagen mit achsenausgerichteten Grenzen
# - Instabil, wenn sich die Trainingsdaten ändern (der Baum kann sich vollständig
#   ändern, wenn ein einzelnes Element hinzugefügt wird)

# %% tags=["slide", "keep"] slideshow={"slide_type": "slide"}
from sklearn.tree import DecisionTreeRegressor

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_non_random_regressor(
    DecisionTreeRegressor,
    lin,
    x_train,
    x_test,
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_non_random_regressor(DecisionTreeRegressor, fun, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_non_random_regressor(
    DecisionTreeRegressor, fun, x_train, x_test, max_depth=4
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
dt1 = et.evaluate_non_random_regressor(
    DecisionTreeRegressor, fun, x_train, x_test, max_depth=1
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.tree import plot_tree

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(12, 8))
plot_tree(dt1, ax=ax, precision=1)
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
dt2 = et.evaluate_non_random_regressor(
    DecisionTreeRegressor, fun, x_train, x_test, max_depth=2
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(16, 8))
plot_tree(dt2, ax=ax, precision=1)
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.plot_regressions([dt1, dt2], fun, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
dt3 = et.evaluate_non_random_regressor(
    DecisionTreeRegressor, fun, x_train, x_test, max_depth=3
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(18, 10))
plot_tree(dt3, ax=ax, precision=1)
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.plot_regressions([dt1, dt2, dt3], fun, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
dt1_mae = et.evaluate_non_random_regressor(
    DecisionTreeRegressor, fun, x_train, x_test, max_depth=1, criterion="absolute_error"
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
dt2_mae = et.evaluate_non_random_regressor(
    DecisionTreeRegressor, fun, x_train, x_test, max_depth=2, criterion="absolute_error"
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
dt3_mae = et.evaluate_non_random_regressor(
    DecisionTreeRegressor, fun, x_train, x_test, max_depth=3, criterion="absolute_error"
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.plot_regressions([dt1_mae, dt2_mae, dt3_mae], fun, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.plot_regressions([dt1, dt1_mae], fun, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.plot_regressions([dt2, dt2_mae], fun, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.plot_regressions([dt3, dt3_mae], fun, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor_2(DecisionTreeRegressor, lin, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor_2(DecisionTreeRegressor, lin, x_train, x_test, max_depth=3)
