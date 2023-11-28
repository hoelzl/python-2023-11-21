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
#  <b>Plotten von Ergebnissen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 17 Plotten von Ergebnissen.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_230_plotting_results.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Plotten von Ergebnissen

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
rng = np.random.default_rng(42)
x = rng.uniform(size=(150, 1), low=0.0, high=10.0)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(20, 1))
plt.yticks([], [])
plt.scatter(x, np.zeros_like(x), alpha=0.4)


# %% tags=["slide"] slideshow={"slide_type": "slide"}
def lin(x):
    return 0.85 * x - 1.5


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def fun(x):
    return 2 * np.sin(x) + 0.1 * x**2 - 2


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
x_plot = np.linspace(0, 10, 500)
plt.figure(figsize=(20, 8))
sns.lineplot(x=x_plot, y=lin(x_plot))
sns.lineplot(x=x_plot, y=fun(x_plot))


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def randomize(fun, x):
    return fun(x) + rng.normal(size=x.shape, scale=0.5)


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(20, 8))
sns.lineplot(x=x_plot, y=randomize(lin, x_plot))
sns.lineplot(x=x_plot, y=randomize(fun, x_plot))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(20, 8))
sns.scatterplot(x=x_plot, y=randomize(lin, x_plot))
sns.scatterplot(x=x_plot, y=randomize(fun, x_plot))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(20, 8))
x_vec = x.reshape(-1)
sns.scatterplot(x=x_vec, y=randomize(lin, x_vec))
sns.scatterplot(x=x_vec, y=randomize(fun, x_vec))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(20, 8))
x_vec = x.reshape(-1)
sns.regplot(x=x_vec, y=randomize(lin, x_vec))
sns.regplot(x=x_vec, y=randomize(fun, x_vec))

# %%
x_train, x_test = x[:100], x[100:]
y1_train = randomize(lin, x_train).reshape(-1)
y1_test = randomize(lin, x_test).reshape(-1)
y2_train = randomize(fun, x_train.reshape(-1))
y2_test = randomize(fun, x_test).reshape(-1)

# %%
x_train.shape, x_test.shape, y1_train.shape, y1_test.shape, y2_train.shape, y2_test.shape

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sklearn.linear_model import LinearRegression

lr1 = LinearRegression()
lr1.fit(x_train, y1_train)
lr1_pred = lr1.predict(x_test)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(20, 8))
plt.scatter(x_train, y1_train, alpha=0.6)
plt.scatter(x_test, lr1_pred, c="green")
plt.plot(x_test, lr1_pred, c="red")
plt.scatter(x_test, y1_test, c="orange")

# %%
error_per_sample = y1_test - lr1_pred
error = error_per_sample.mean()
error

# %%
abs_error_per_sample = np.abs(y1_test - lr1_pred)
square_error_per_sample = (y1_test - lr1_pred) ** 2

abs_error_per_sample.mean(), square_error_per_sample.mean()

# %%
from sklearn.metrics import mean_absolute_error, mean_squared_error

mean_absolute_error(y1_test, lr1_pred), mean_squared_error(y1_test, lr1_pred)

# %%
from sklearn.linear_model import LinearRegression

lr2 = LinearRegression()
lr2.fit(x_train, y2_train)
lr2_pred = lr2.predict(x_test)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(20, 8))
plt.scatter(x_train, y2_train)
plt.plot(x_test, lr2_pred, c="red")
plt.scatter(x_test, lr2_pred, c="green")
plt.scatter(x_test, y2_test, c="orange")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
mean_absolute_error(y1_test, lr2_pred), mean_squared_error(y1_test, lr2_pred)

# %%
