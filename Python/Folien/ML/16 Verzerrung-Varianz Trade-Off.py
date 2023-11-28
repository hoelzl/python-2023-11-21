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
#  <b>Verzerrung-Varianz Trade-Off</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 16 Verzerrung-Varianz Trade-Off.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_220_bias_variance_tradeoff.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Verzerrung-Varianz Trade-Off

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error

# %% tags=["keep"]
try:
    import python_courses.slides.module_700_ml_basics.evaluation_tools as et
except ModuleNotFoundError:
    import evaluation_tools as et

# %% tags=["keep"]
sns.set_theme()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
rng = np.random.default_rng(42)
x = rng.uniform(size=(150, 1), low=0.0, high=10.0)
x_train, x_test = x[:100], x[100:]
x_plot = np.linspace(0, 10, 500)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def lin(x):
    return 0.85 * x - 1.5


# %% tags=["keep"]
def fun(x):
    return 2 * np.sin(x) + 0.1 * x**2 - 2


# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Bias/Variance Tradeoff
#
# <img src="img/low-bias-low-variance.png"
#      style="width: 22%; display: inline-block;"/>
# <img src="img/low-bias-high-variance.png"
#      style="width: 22%; display: inline-block;"/>
# <img src="img/high-bias-low-variance.png"
#      style="width: 22%; display: inline-block;"/>
# <img src="img/high-bias-high-variance.png"
#      style="width: 22%; display: inline-block;"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/ag/Figure-09-008.png" style="width: 40%; padding: 20px;"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/ag/Figure-09-009.png" style="width: 80%; padding: 20px;"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/ag/Figure-09-010.png" style="width: 40%; padding: 20px;"/>

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

# %% tags=["keep"]
x = np.linspace(0, 10, 500)
y = et.randomize(fun, x, 2.0)
lr_reg = LinearRegression().fit(x.reshape(-1, 1), y)
dt_reg = DecisionTreeRegressor().fit(x.reshape(-1, 1), y)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def plot(reg, ax):
    sns.lineplot(x=x, y=fun(x), ax=ax, color="red")
    sns.lineplot(x=x, y=y, ax=ax, alpha=0.5)
    sns.lineplot(x=x, y=reg.predict(x.reshape(-1, 1)), ax=ax)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(ncols=2, figsize=(20, 6))
plot(lr_reg, ax[0])
plot(dt_reg, ax[1])
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
x = np.linspace(0, 10, 500)
fix, ax = plt.subplots(figsize=(22, 12))
ax.plot(x, et.randomize(fun, x, scale=0.5))
ax.plot(x, fun(x), color="r")
plt.show()


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def fun(x):
    return 2 * np.sin(x) + 0.1 * x**2 - 2


# %% tags=["keep"]
def fun2(x):
    return 2.8 * np.sin(x) + 0.3 * x + 0.08 * x**2 - 2.5


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(22, 12))
ax.plot(x, et.randomize(fun2, x, scale=0.4), color="orange")
ax.plot(x, fun2(x), color="yellow")
ax.plot(x, fun(x), color="r")
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(22, 12))
ax.fill_between(
    x,
    1.8 * np.sin(x) + 0.09 * x**2 - 5,
    2.1 * np.sin(x) + 0.11 * x**2 + 1,
    alpha=0.2,
)
ax.plot(x, et.randomize(fun2, x, scale=0.4), color="orange")
ax.plot(x, fun2(x), color="yellow")
ax.plot(x, fun(x), color="r")
ax.plot(x, np.select([x <= 6, x > 6], [-0.5, 3.5]), color="darkgreen")
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(22, 12))
ax.fill_between(
    x,
    1.8 * np.sin(x) + 0.09 * x**2 - 5,
    2.1 * np.sin(x) + 0.11 * x**2 + 1,
    alpha=0.2,
)
ax.plot(x, et.randomize(fun2, x, scale=0.4), color="orange")
ax.plot(x, et.randomize(fun, x, scale=1))
ax.plot(x, fun2(x), color="yellow")
ax.plot(x, fun(x), color="r")
ax.plot(x, np.select([x <= 6, x > 6], [-0.5, 3.5]), color="darkgreen")
plt.show()

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Overfitting erkennen
#
# - Die Leistung auf den Trainingsdaten ist viel besser als auf den
#   Test/Validierungsdaten

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Reduzieren von Overfitting
#
# - Sammeln Sie mehr/unterschiedlichere Trainingsdaten
# - Führen Sie (besseres) Feature-Engineering durch
# - Verringern Sie die Modellkapazität
# - Regularisieren Sie das Modell
# - Verwenden Sie Kreuzvalidierung (Cross-Validation)
# - Führen Sie Datenaugmentierung der Trainingsdaten durch
# - Fügen Sie Batch-Normalisierung, Dropout, ... Schichten zu Ihrem neuronalen Netz
# - Beenden Sie das Training frühzeitig
# - ...

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
rng = np.random.default_rng(42)
dt_reg = DecisionTreeRegressor()
x_train = rng.uniform(size=(100, 1), low=0.0, high=10.0)
y_train = et.randomize(fun, x_train, scale=1.5)
y_test = et.randomize(fun, x_train, scale=1.5)
dt_reg.fit(x_train, y_train)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
mae = mean_absolute_error(y_train, dt_reg.predict(x_train))
mse = mean_squared_error(y_train, dt_reg.predict(x_train))
mae, mse

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
mae_test = mean_absolute_error(y_test, dt_reg.predict(x_train))
mse_test = mean_squared_error(y_test, dt_reg.predict(x_train))
mae_test, mse_test

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fun_mae = mean_absolute_error(y_train, fun(x_train))
fun_mse = mean_squared_error(y_train, fun(x_train))
fun_mae, fun_mse

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(16, 6))
sns.lineplot(x=x_train[:, 0], y=fun(x_train)[:, 0])
sns.scatterplot(x=x_train[:, 0], y=y_train[:, 0])
sns.lineplot(x=x_plot, y=dt_reg.predict(x_plot.reshape(-1, 1)))
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor_2(DecisionTreeRegressor, fun, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor_2(DecisionTreeRegressor, fun, x_train, x_test, max_depth=2)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor_2(DecisionTreeRegressor, fun, x_train, x_test, max_depth=3)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor_2(
    DecisionTreeRegressor, fun, x_train, x_test, max_depth=3, criterion="absolute_error"
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor_2(
    DecisionTreeRegressor,
    fun,
    x_train,
    x_test,
    max_leaf_nodes=20,
    criterion="absolute_error",
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor_2(
    DecisionTreeRegressor, fun, x_train, x_test, min_samples_split=16
)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor_2(DecisionTreeRegressor, fun, x_train, x_test, min_samples_leaf=8)

# %%
