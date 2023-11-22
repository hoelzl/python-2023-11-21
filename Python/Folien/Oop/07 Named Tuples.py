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
#  <b>Named Tuples</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 07 Named Tuples.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_136_named_tuples.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Named Tuples

# %%
from typing import NamedTuple


# %%
class SimplePoint(NamedTuple):
    x: float = 0.0
    y: float = 0.0

    def move(self, dx=0.0, dy=0.0):
        return SimplePoint(self.x + dx, self.y + dy)


# %%
p1 = SimplePoint()
p1

# %%
p1.move(2, 3)

# %%
p1 == (0, 0)

# %%
p1[0]

# %%
for c in p1:
    print(c)

# %%
# p1.x = 1.0

# %%
