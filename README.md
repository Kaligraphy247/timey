# Timey
### Prints characters after a set timed interval


> # working progress

## How to Use
- pip install ?

        from timey import Timey
- **OR**

        from timey import Timey as tp
or any other alias you wish to use.

- Usage 

        Timey(text, sec)

        tp(text, sec)
    - **``text``** can be strings or intergers

    - **``sec``** should be floats, but can also be intergers
    - **``sec``** must be positive numbers

            tp('Hello, world', 0.07)

            Timey('Foo Bar Baz', 1)

            Timey(f'Foo Bar Baz {opt_var_here}', 1.0)

            Timey('Foo {} Baz'.format(opt_var_here), 1.0)
