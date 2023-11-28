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
#  <b>Feature-Engineering</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 19 Feature-Engineering.py -->
# <!-- python_courses/slides/module_700_ml_basics/topic_250_feature_engineering.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Feature-Engineering

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

# %% tags=["keep"]
try:
    import python_courses.slides.module_700_ml_basics.evaluation_tools as et
except ModuleNotFoundError:
    import evaluation_tools as et

# %% tags=["keep"]
sns.set_theme()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
rng = np.random.default_rng(42)


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def lin(x):
    return 0.85 * x - 1.5


# %% slideshow={"slide_type": "-"}
def fun(x):
    return 2 * np.sin(x) + 0.1 * x**2 - 2


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
x = rng.uniform(size=(150, 1), low=0.0, high=10.0)
x_train, x_test = x[:100], x[100:]
x_plot = np.linspace(0, 10, 500)
x_train[:3]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
y_lin_train = lin(x_train).reshape(-1)
y_lin_test = lin(x_test).reshape(-1)
y_fun_train = fun(x_train.reshape(-1))
y_fun_test = fun(x_test).reshape(-1)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
x_squares = x * x
x_squares[:3]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
x_sins = np.sin(x)
x_sins[:3]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
x_train_aug = np.concatenate([x_train, x_train * x_train, np.sin(x_train)], axis=1)
x_train_aug[:3]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
x_test_aug = np.concatenate([x_test, x_test * x_test, np.sin(x_test)], axis=1)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
# from sklearn.linear_model import Ridge
# lr_aug_lin = Ridge()
lr_aug_lin = LinearRegression()
lr_aug_lin.fit(x_train_aug, y_lin_train)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
lr_aug_lin.coef_, lr_aug_lin.intercept_

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
y_aug_lin_pred = lr_aug_lin.predict(x_test_aug)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
mean_absolute_error(y_lin_test, y_aug_lin_pred), mean_squared_error(
    y_lin_test, y_aug_lin_pred
)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
x_test.shape, x_plot.shape

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
et.train_and_plot_aug(lin, x_train_aug, x_plot, x_test)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
et.train_and_plot_aug(fun, x_train_aug, x_plot, x_test, scale=0.0)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
et.train_and_plot_aug(fun, x_train_aug, x_plot, x_test, scale=0.5)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
et.train_and_plot_aug(fun, x_train_aug, x_plot, x_test, scale=1.5)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
et.train_and_plot_aug(fun, x_train_aug, x_plot, x_test, scale=3)


# %%
def fun2(x):
    return 2.8 * np.sin(x) + 0.3 * x + 0.08 * x**2 - 2.5


# %%
et.train_and_plot_aug(fun2, x_train_aug, x_plot, x_test, scale=1.5)

# %%
et.train_and_plot_aug(
    lambda x: np.select([x <= 6, x > 6], [-0.5, 3.5]), x_train_aug, x_plot, x_test
)
