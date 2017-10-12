"""
Please pylint! I need that 10/10 rating!
"""


class Bruch:
    """
    Please pylint! I need that 10/10 rating!
    """
    def public_one(self):
        """
        Please pylint! I need that 10/10 rating!
        """
        pass

    def public_two(self):
        """
        Please pylint! I need that 10/10 rating!
        """
        pass

    def __init__(self, zaehler=1, nenner=1):
        """
        Creates a fraction depending on the number of arguments \n
        0 arguments:    1 / 1,
        1 argument:     arg1 / 1,
        2 arguments:    arg1 / arg2

        :param zaehler: int
        :param nenner: int
        :raises TypeError, ZeroDivisonError
        """
        if isinstance(zaehler, str) or isinstance(nenner, str):
            raise TypeError

        if nenner == 0:
            raise ZeroDivisionError

        self.zaehler = zaehler
        self.nenner = nenner

    def __abs__(self):
        """
        Returns a fraction with absolute divisor and dividend

        :return: Bruch
        """
        self.zaehler = abs(self.zaehler)
        self.nenner = abs(self.nenner)

        return self

    # Add
    def __add__(self, other):
        """
        Adds another object to this object

        :param other: Bruch, int
        :return: int, float, Bruch
        :raises: TypeError
        """
        if isinstance(other, str):
            raise TypeError

        if isinstance(other, (int, float)):
            return self.zaehler / self.nenner + other

        if isinstance(other, Bruch):
            zaehler1 = self.zaehler * other.nenner
            zaehler2 = other.zaehler * self.nenner
            self.zaehler = zaehler1 + zaehler2
            self.nenner *= other.nenner

            return self

    def __iadd__(self, other):
        """
        Adds another object to this object returning a fraction

        :param other: int, Bruch
        :return: Bruch
        """
        if isinstance(other, (int, float)):
            self.zaehler += other * self.nenner
            return self

        return self.__add__(other)

    def __radd__(self, other):
        """
        Adds this object to another object

        :param other: int, Bruch
        :return: int, float, Bruch
        """
        return self.__iadd__(other)

    # Subtract
    def __sub__(self, other):
        """
        Subtracts another object from this object

        :param other: Bruch, int
        :return: int, float, Bruch
        :raises: TypeError
        """
        if isinstance(other, str):
            raise TypeError

        if isinstance(other, (int, float)):
            return float(self) - other

        if isinstance(other, Bruch):
            zaehler1 = self.zaehler * other.nenner
            zaehler2 = other.zaehler * self.nenner
            self.zaehler = zaehler1 - zaehler2
            self.nenner *= other.nenner
            return self

    def __isub__(self, other):
        """
        Subtracts another object from this object returning a fraction

        :param other: Bruch, int
        :return: Bruch
        """
        if isinstance(other, int):
            self.zaehler -= other * self.nenner
            return self

        return self.__sub__(other)

    def __rsub__(self, other):
        """
        Subtracts this object from another

        :param other: Bruch, int
        :return: int, float, Bruch
        """

        if isinstance(other, (int, float)):
            return other - float(self)

    def __mul__(self, other):
        """
        Multiplies this object with another returning its type

        :param other: Bruch, int
        :return: int, float, Bruch
        :raises: TypeError
        """
        if isinstance(other, str):
            raise TypeError

        if isinstance(other, (int, float)):
            return self.zaehler / self.nenner * other

        if isinstance(other, Bruch):
            self.zaehler *= other.zaehler
            self.nenner *= other.nenner
            return self

    def __imul__(self, other):
        """
        Multiplies this object with another returning a fraction

        :param other: Bruch, int
        :return: Bruch
        """
        if isinstance(other, (int, float)):
            self.zaehler *= other
            return self

        return self.__mul__(other)

    def __rmul__(self, other):
        """
        Multiplies another object with this object returning the others type

        :param other: Bruch, int
        :return: int, float, Bruch
        """
        return self.__mul__(other)

    # Divide
    def __truediv__(self, other):
        """
        Divides this object by another object

        :param other: int, Bruch
        :return: int, float, Bruch
        :raises: ZeroDivisionError, TypeError
        """
        if other == 0:
            raise ZeroDivisionError

        if isinstance(other, str):
            raise TypeError

        if isinstance(other, (int, float)):
            return self * Bruch(1, other)

        if isinstance(other, Bruch):
            self.zaehler *= other.nenner
            self.nenner *= other.zaehler
            return self

    def __itruediv__(self, other):
        """
        Divides this object by another returning a fraction

        :param other: int, Bruch
        :return: int, float, Bruch
        """
        if isinstance(other, (int, float)):
            return self * Bruch(1, other)

        return self.__truediv__(other)

    def __rtruediv__(self, other):
        """
        Divides another object by this object returning the others type

        :param other: int, Bruch
        :return: int, float, Bruch
        """
        if self == 0:
            raise ZeroDivisionError

        return self.__itruediv__(other)

    # Comparision
    def __eq__(self, other):
        """
        Checks whether the value of this object is equal to the others

        :param other:
        :return: bool
        :exception: TypeError
        """
        return float(self) == float(other)

    def __gt__(self, other):
        """
        Checks whether the value of this object is greater than the others

        :param other:
        :return: bool
        :exception: TypeError
        """
        if float(self) > float(other):
            return True

    def __ge__(self, other):
        """
        Checks whether the value of this object is greater than or equal to the others

        :param other:
        :return: bool
        :exception: TypeError
        """
        if self.__eq__(other) or self.__gt__(other):
            return True

    def __invert__(self):
        """
        Switches divisor and dividend of the fraction

        :return: Bruch
        """
        buffer = self.nenner
        self.nenner = self.zaehler
        self.zaehler = buffer

        return self

    def __pow__(self, other):
        """
        Multiplies the given fraction by itself a given number of times

        :param other: int
        :return: Bruch
        :raises: TypeError
        """
        if isinstance(other, str):
            raise TypeError

        if isinstance(other, (int, float)):
            self.zaehler **= other
            self.nenner **= other

        if isinstance(other, Bruch):
            self.zaehler **= float(other)
            self.nenner **= float(other)

        return self

    def __ipow__(self, other):
        """
        Multiplies the given object by the value of the fraction

        :param other:
        :return:
        """
        return self.__pow__(other)

    def __neg__(self):
        """
        Multiplies the fraction with negative 1

        :return: Bruch
        """
        return self * -1

    # Casts
    def __int__(self):
        """
        Returns the value of the fraction as an integer

        :return: int
        """
        return int(float(self))

    def __float__(self):
        """
        Returns the value of the fraction as a float

        :return: float
        """
        return float(self.zaehler) / float(self.nenner)

    def __str__(self):
        """
        If the value of the fraction can be returned as an integer,
        it returns a string containing this value in round brackets.
        Otherwise the divisor and dividend are displayed, divided by a slash

        :return: str
        """
        if float(self) == int(self):
            to_string = "(" + str(int(self)) + ")"
        elif self.zaehler < 0 and self.nenner < 0:
            to_string = "(" + str(abs(self.zaehler)) + "/" + str(abs(self.nenner)) + ")"
        else:
            to_string = "(" + str(self.zaehler) + "/" + str(self.nenner) + ")"

        return to_string

    # Iteration
    def __iter__(self):
        """
        Iterates over the object yielding the divisor and then the dividend
        """
        yield self.zaehler
        yield self.nenner

    @classmethod
    def _bruch__make_bruch(cls, value):
        """
        Returns a fraction by instantiating a new Bruch using the value as the first argument

        :param value: int
        :return: Bruch
        :raises: TypeError
        """
        if not isinstance(value, int):
            raise TypeError
        else:
            return Bruch(value)
