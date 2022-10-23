# Timey
### Prints characters after a set timed interval


## How to Use
- `pip install timey_terminal`

```python
>>> from timey import Timey
>>> p = Timey()
>>> p.show("Sample Text") # prints the provided text to the terminal
>>> p.get_seconds() # get the current interval at which each character is printed.  Default = 0.05s
>>> p.set_seconds(x) # sets the secs to what was provided.
```

- **OR**
```python
from timey import TimeyOld as pp
>>> pp("Testing", 0.5) # print each character every 0.5 secs
>>> pp("Sample text", 2) # print each character every 2 secs
```