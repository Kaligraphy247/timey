import time, sys


class Timey:
    """
    Printing text to Terminal
    >>> p = Timey() # init a variable
    >>> p.get_seconds() # 0.05 is the default
    >>> p.set_seconds(1) # set the seconds param to 1 secs
    >>> p.show("test to print") # prints text to the terminal  
    """
    text: str = "default"
    seconds: float = 0.05
    def __init__(self, text=text, sec=seconds):
        self.text = text
        self.secs = float(sec)

    def get_seconds(self) -> float:
        """Gets the current seconds interval value"""
        return self.secs
    
    def set_seconds(self, sec: float) -> None:
        """Sets seconds interval to whatever was provided"""
        self.secs = float(sec)

    def show(self, text: str):
        """Prints text to the terminal at a timely interval"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(float(self.secs))
        sys.stdout.write('\n')

    def show_v2(self, text: str, seconds: float=seconds):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(float(seconds))
        sys.stdout.write('\n')


class TimeyOld:
    '''
    #### Old version of Timey
    All arguments are required.\n
    import TimeyOld as pp
    >>> pp("Sample text", 0.5)
    '''
    def __init__(self, text: str, sec: float):
        '''
        text = characters to print\n\n
        sec = timely interval before each character is printed (should be a float)
        '''
        self.text = text
        for char in self.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(sec)
        sys.stdout.write('\n')