import time, sys

class Timey:
    ''' Prints character in stdout\n\nto a terminal* at a timely Interval
\rSimilar to Built-in print()'''
    def __init__(self, text, sec):
        '''text = characters to print\n\nsec = timely interval before each character is printed (should be be floats)'''
        self.text = text
        self.sec = sec
        for char in self.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(sec)
        sys.stdout.write('\n')     

