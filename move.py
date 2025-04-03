class Move:

    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    def is_valid(self):
        return 1 <= self._value <= 9
    
    def get_row(self):
        if self._value in (1, 2, 3):
            return 0    # First Row
        elif self._value in (4, 5, 6):
            return 1    # Second Row
        else:
            return 2    # Third Row

    def get_column(self):
        if self._value in (1, 4, 7):
            return 0    # First Column
        elif self._value in (2, 5, 8):
            return 1    # Second Column
        else:
            return 2    # Third Column
        

#        col0 col1 col2
# row 0: | 1 | 2 | 3 |
# row 1: | 4 | 5 | 6 |
# row 2: | 7 | 8 | 9 |

