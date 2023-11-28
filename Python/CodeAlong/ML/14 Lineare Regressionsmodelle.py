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
#  <b>Lineare Regressionsmodelle</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 14 Lineare Regressionsmodelle.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_200_linear_regressors.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Lineare Regressionsmodelle

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
rng = np.random.default_rng(42)
x = rng.uniform(size=(150, 1), low=0.0, high=10.0)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
plt.figure(figsize=(20, 1), frameon=False)
plt.yticks([], [])
plt.scatter(x, np.zeros_like(x), alpha=0.4)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def lin(x):
    return 0.85 * x - 1.5


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def fun(x):
    return 2 * np.sin(x) + 0.1 * x**2 - 2


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
x_plot = np.linspace(0, 10, 500)
plt.figure(figsize=(12, 6))
sns.lineplot(x=x_plot, y=lin(x_plot))
sns.lineplot(x=x_plot, y=fun(x_plot))
plt.show()


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def randomize(fun, x, scale=0.5):
    return fun(x) + rng.normal(size=x.shape, scale=scale)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
x_train, x_test = x[:100], x[100:]

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
y_lin_train = lin(x_train).reshape(-1)
y_lin_test = lin(x_test).reshape(-1)
y_fun_train = fun(x_train.reshape(-1))
y_fun_test = fun(x_test).reshape(-1)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
y_rand_lin_train = randomize(lin, x_train).reshape(-1)
y_rand_lin_test = randomize(lin, x_test).reshape(-1)
y_rand_fun_train = randomize(fun, x_train.reshape(-1))
y_rand_fun_test = randomize(fun, x_test).reshape(-1)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
y_chaos_lin_train = randomize(lin, x_train, 1.5).reshape(-1)
y_chaos_lin_test = randomize(lin, x_test, 1.5).reshape(-1)
y_chaos_fun_train = randomize(fun, x_train, 1.5).reshape(-1)
y_chaos_fun_test = randomize(fun, x_test, 1.5).reshape(-1)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(12, 8))
sns.lineplot(x=x_train[:, 0], y=y_lin_train, color="red", ax=ax)
sns.scatterplot(x=x_train[:, 0], y=y_rand_lin_train, ax=ax)
sns.scatterplot(x=x_train[:, 0], y=y_chaos_lin_train, ax=ax)
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(12, 8))
sns.lineplot(x=x_train[:, 0], y=y_fun_train, color="red", ax=ax)
sns.scatterplot(x=x_train[:, 0], y=y_rand_fun_train, ax=ax)
sns.scatterplot(x=x_train[:, 0], y=y_chaos_fun_train, ax=ax)
plt.show()

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  ## Lineare Regression

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.linear_model import LinearRegression

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
lr_lin = LinearRegression()
lr_rand_lin = LinearRegression()
lr_chaos_lin = LinearRegression()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
lr_lin.fit(x_train, y_lin_train)
lr_rand_lin.fit(x_train, y_rand_lin_train)
lr_chaos_lin.fit(x_train, y_chaos_lin_train)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
print("lr_lin", lr_lin.coef_, lr_lin.intercept_)
print("lr_rand_lin", lr_rand_lin.coef_, lr_rand_lin.intercept_)
print("lr_chaos_lin", lr_chaos_lin.coef_, lr_chaos_lin.intercept_)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
y_lr_lin_pred = lr_lin.predict(x_test)
y_lr_rand_lin_pred = lr_rand_lin.predict(x_test)
y_lr_chaos_lin_pred = lr_chaos_lin.predict(x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
fig, ax = plt.subplots(figsize=(12, 8))
sns.lineplot(x=x_test[:, 0], y=y_lr_lin_pred, ax=ax)
sns.scatterplot(x=x_test[:, 0], y=y_lin_test, ax=ax)

sns.lineplot(x=x_test[:, 0], y=y_lr_rand_lin_pred, ax=ax)
sns.scatterplot(x=x_test[:, 0], y=y_rand_lin_test, ax=ax)

sns.lineplot(x=x_test[:, 0], y=y_lr_chaos_lin_pred, ax=ax)
sns.scatterplot(x=x_test[:, 0], y=y_chaos_lin_test, ax=ax)
plt.show()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sklearn.metrics import mean_absolute_error, mean_squared_error

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
mae_lin = mean_absolute_error(y_lin_test, y_lr_lin_pred)
mae_rand_lin = mean_absolute_error(y_rand_lin_test, y_lr_rand_lin_pred)
mae_chaos_lin = mean_absolute_error(y_chaos_lin_test, y_lr_chaos_lin_pred)

mse_lin = mean_squared_error(y_lin_test, y_lr_lin_pred)
mse_rand_lin = mean_squared_error(y_rand_lin_test, y_lr_rand_lin_pred)
mse_chaos_lin = mean_squared_error(y_chaos_lin_test, y_lr_chaos_lin_pred)

rmse_lin = np.sqrt(mean_squared_error(y_lin_test, y_lr_lin_pred))
rmse_rand_lin = np.sqrt(mean_squared_error(y_rand_lin_test, y_lr_rand_lin_pred))
rmse_chaos_lin = np.sqrt(mean_squared_error(y_chaos_lin_test, y_lr_chaos_lin_pred))

print(
    "No randomness:      "
    f"MAE = {mae_lin:.2f}, MSE = {mse_lin:.2f}, RMSE = {rmse_lin:.2f}"
)
print(
    "Some randomness:    "
    f"MAE = {mae_rand_lin:.2f}, MSE = {mse_rand_lin:.2f}, RMSE = {rmse_rand_lin:.2f}"
)
print(
    "Lots of randomness: "
    f"MAE = {mae_chaos_lin:.2f}, MSE = {mse_chaos_lin:.2f}, RMSE = {rmse_chaos_lin:.2f}"
)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ## Visualisierung und Evaluierung


# %% tags=["keep"]
try:
    import python_courses.slides.module_700_ml_basics.evaluation_tools as et
except ModuleNotFoundError:
    import evaluation_tools as et

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_non_random_regressor(LinearRegression, fun, x_train, x_test)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Underfitting
#
# Underfitting tritt auf, wenn das Modell nicht in der Lage ist, die Trainingsdaten
# genau genug zu repräsentieren.


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor(LinearRegression, lin, x_train, x_test)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
et.evaluate_regressor(LinearRegression, fun, x_train, x_test)
