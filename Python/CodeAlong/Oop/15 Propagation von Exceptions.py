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
#  <b>Propagation von Exceptions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 15 Propagation von Exceptions.py -->
# <!-- python_courses/slides/module_170_exceptions/topic_114_a1_stack_unwinding.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Stack-Unwinding
#
# Visualisierung auf [PythonTutor](https://shorturl.at/jpuJS).
#
# Wenn eine Exception ausgelöst wird, werden geschachtelte Funktionsaufrufe so lange
# abgebrochen, bis ein passender Handler gefunden wird:

# %% tags=["keep"]
from enum import Enum


# %% tags=["keep"]
class ErrorType(Enum):
    VALUE = "ValueError"
    LOOKUP = "LookupError"
    INDEX = "IndexError"


# %%

# %%

# %% tags=["keep"]
def raise_and_handle_error(error_type: ErrorType):
    print("    raise_and_handle_error(): before try")
    try:
        print("    raise_and_handle_error(): before raise")
        if error_type == ErrorType.VALUE:
            raise ValueError(">>> ValueError")
        elif error_type == ErrorType.LOOKUP:
            raise LookupError(">>> LookupError")
        else:
            raise IndexError(">>> IndexError")
        print("    raise_and_handle_error(): after raise")  # noqa
    except LookupError as error:
        print(f"<<< raise_and_handle_error(): caught LookupError {error}")
    print("    raise_and_handle_error(): after except")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def intermediate_fun(error_type: ErrorType):
    print("  intermediate_fun(): before call")
    raise_and_handle_error(error_type)
    print("  intermediate_fun(): after call")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def outer_caller(error_type: ErrorType = ErrorType.VALUE):
    print("outer_caller(): before calling")
    intermediate_fun(error_type)
    print("outer_caller(): after calling")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
outer_caller(ErrorType.LOOKUP)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
outer_caller(ErrorType.INDEX)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
# outer_caller(ErrorType.VALUE)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def outer_caller_with_try(error_type: ErrorType = ErrorType.VALUE):
    print("outer_caller(): before try")
    try:
        print("outer_caller(): before calling")
        intermediate_fun(error_type)
        print("outer_caller(): after calling")
    except Exception as error:
        print(f"<<< outer_caller(): caught Exception: {error}")
    print("outer_caller(): after except")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
outer_caller_with_try(ErrorType.VALUE)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
outer_caller_with_try(ErrorType.INDEX)  # noqa


# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Workshop: Verschachtelte Ausnahmen
#
# In diesem Workshop wollen wir betrachten, wie sich verschachtelte Ausnahmen
# verhalten.
#
# Gegeben seien die folgenden Funktionen.
#
# Welche Ausgabe erwarten Sie für Aufrufe von `outer_caller_ws()` und
# `outer_caller_with_try_ws()` mit den verschiedenen `ErrorType`-Werten?

# %% tags=["keep"]
def raise_and_handle_error_ws(exception_type: ErrorType):
    print("    raise_and_handle_error_ws(): before try")
    try:
        print("    raise_and_handle_error_ws(): before raise")
        if exception_type == ErrorType.VALUE:
            raise ValueError(">>> ValueError")
        elif exception_type == ErrorType.LOOKUP:
            raise LookupError(">>> LookupError")
        else:
            raise IndexError(">>> IndexError")
    except LookupError as error:
        print(f"<<< raise_and_handle_error_ws(): caught LookupError {error}")
        raise
    except ValueError as error:
        print(f"<<< raise_and_handle_error_ws(): caught ValueError {error}")
    print("    raise_and_handle_error_ws(): after except")


# %% tags=["keep"]
def intermediate_fun_ws(exception_type: ErrorType):
    print("  intermediate_fun_ws(): before call")
    try:
        raise_and_handle_error_ws(exception_type)
    except IndexError as error:
        print(f"<<< intermediate_fun_ws(): caught IndexError {error}")
        raise TypeError(">>> inner TypeError") from error
    except LookupError as error:
        print(f"<<< intermediate_fun_ws(): caught LookupError {error}")
        raise TypeError(">>> inner TypeError")
    except Exception as error:
        print(f"<<< intermediate_fun_ws(): caught Exception {error}")
        print("  intermediate_fun_ws(): re-raising exception")
        raise
        print("  intermediate_fun_ws(): re-raised exception")  # type: ignore
    print("  intermediate_fun_ws() after call")


# %% tags=["keep"]
def outer_caller_ws(exception_type: ErrorType = ErrorType.VALUE):
    print("outer_caller_ws(): before calling")
    intermediate_fun_ws(exception_type)
    print("outer_caller_ws(): after calling")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def outer_caller_with_try_ws(exception_type: ErrorType = ErrorType.VALUE):
    print("outer_caller_ws(): before try")
    try:
        print("outer_caller_ws(): before calling")
        intermediate_fun_ws(exception_type)
        print("outer_caller_ws(): after calling")
    except Exception as error:
        print(f"<<< outer_caller_ws(): caught Exception {error}")
    print("outer_caller_ws(): after except")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%
