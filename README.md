# Python for Data Science - Module 00: Starting

This project is the **first module of the Python for Data Science
Piscine at 42**.\
It covers the fundamental basics of the Python programming language,
including:

-   Data structures
-   Script arguments
-   Error handling
-   Basic packaging

------------------------------------------------------------------------

# Technical Requirements

**Python Version**

-   `Python 3.10.x` (**strictly enforced**)

**Linter**

-   `flake8` (aliased as `norminette`)

## Rules

-   No global variables.
-   Explicit library imports only.

``` python
import numpy as np
```

❌ The following is **strictly forbidden** and results in a **score of
0**:

``` python
from <library> import <function>
```

Additional requirements:

-   Starting from **Exercise 05**, all functions must include
    **docstrings (`__doc__`)**.
-   Programs must include:
    -   a `main()` function
    -   the guard:

``` python
if __name__ == "__main__":
    main()
```

------------------------------------------------------------------------

# Project Structure

  ----------------------------------------------------------------------------
  Exercise          Directory         File(s)               Description
  ----------------- ----------------- --------------------- ------------------
  **ex00**          `ex00/`           `Hello.py`            Modify strings in
                                                            **List, Tuple,
                                                            Set, and Dict**
                                                            objects

  **ex01**          `ex01/`           `format_ft_time.py`   Format dates and
                                                            display seconds
                                                            since epoch

  **ex02**          `ex02/`           `find_ft_type.py`     Create a function
                                                            to identify and
                                                            print object types

  **ex03**          `ex03/`           `NULL_not_found.py`   Function to
                                                            identify all types
                                                            of **"Null"
                                                            objects**

  **ex04**          `ex04/`           `whatis.py`           Script to check if
                                                            a number is **Odd
                                                            or Even** via
                                                            arguments

  **ex05**          `ex05/`           `building.py`         Character counter
                                                            for **upper,
                                                            lower,
                                                            punctuation, and
                                                            digits**

  **ex06**          `ex06/`           `ft_filter.py`,       Recode the
                                      `filterstring.py`     `filter` function
                                                            using **list
                                                            comprehensions**

  **ex07**          `ex07/`           `sos.py`              Encode a string
                                                            into **Morse
                                                            Code** using a
                                                            dictionary

  **ex08**          `ex08/`           `Loading.py`          Implement a
                                                            **progress bar**
                                                            using the `yield`
                                                            operator

  **ex09**          `ex09/`           `*.py`, `README.md`,  Create and install
                                      `LICENSE`, etc.       a **custom Python
                                                            package via pip**
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

# Setup & Usage

## 1. Virtual Environment

It is recommended to use a **virtual environment** to manage
dependencies:

``` bash
python3.10 -m venv venv
source venv/bin/activate
pip install flake8
```

------------------------------------------------------------------------

## 2. Running the Linter (Norminette)

To check for **code compliance** as required by the subject:

``` bash
# Alias flake8 to norminette for a familiar 42 workflow
alias norminette='flake8'

norminette path/to/file.py
```

------------------------------------------------------------------------

## 3. Execution Example

Example for **Exercise 04**:

``` bash
python ex04/whatis.py 14
```

Output:

    I'm Even.

------------------------------------------------------------------------

# Evaluation Note

-   Any **uncaught exception** will invalidate the exercises.
-   Functions must **not terminate unexpectedly** (e.g., segmentation
    faults) or they will receive a **score of 0**.
-   Use language features appropriately and **avoid reinventing the
    wheel**.
