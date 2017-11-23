from typing import TypeVar, Callable, Generic, overload

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')


class PZFunc(Generic[A, B]):
    def __init__(self, f: Callable[[A], B]) -> None:
        """This is a PythonZ function (a wrapper around normal python function)

        This function is a typical definition of a function in functional
        programing, you can only take one parameter and return one parameter
        :param f: the real function to use
        """
        self._f = f

    def __call__(self, a: A) -> B:
        """Used to call a PythonZ function

        :param a: the input
        :return: the result
        """
        return self._f(a)

    def __mul__(self, other: 'PZFunc[C, A]') -> 'PZFunc[C, B]':
        """Function composition with PythonZ function, same as haskell's '.'

        :param other: the function to composite
                (the function to apply first,
                 or the function on the right)
        """
        return PZFunc(lambda x: self(other(x)))

    def __mod__(self, value: A) -> B:
        """Apply current function to value, same as haskell's '$'

        :param value: the value to apply to
        :return: the result of the application
        """
        return self._f(value)


A1 = TypeVar('A1')
A2 = TypeVar('A2')
A3 = TypeVar('A3')
A4 = TypeVar('A4')
A5 = TypeVar('A5')
A6 = TypeVar('A6')
R = TypeVar('R')


@overload
def curry(f: Callable[[A1], R]) -> PZFunc[A1, R]:
    """curry a function with 1 parameter"""
    ...


@overload
def curry(f: Callable[[A1, A2], R]) -> PZFunc[A1, PZFunc[A2, R]]:
    """curry a function with 2 parameters"""
    ...


@overload
def curry(f: Callable[[A1, A2, A3], R]) -> PZFunc[A1, PZFunc[
        A2, PZFunc[A3, R]]]:
    """curry a function with 3 parameters"""
    ...


@overload
def curry(f: Callable[[A1, A2, A3, A4], R]) -> PZFunc[A1, PZFunc[
        A2, PZFunc[A3, PZFunc[A4, R]]]]:
    """curry a function with 4 parameters"""
    ...


@overload
def curry(f: Callable[[A1, A2, A3, A4, A5], R]) -> PZFunc[A1, PZFunc[
        A2, PZFunc[A3, PZFunc[A4, PZFunc[A5, R]]]]]:
    """curry a function with 5 parameters"""
    ...


@overload
def curry(f: Callable[[A1, A2, A3, A4, A5, A6], R]) -> PZFunc[A1, PZFunc[
        A2, PZFunc[A3, PZFunc[A4, PZFunc[A5, PZFunc[A6, R]]]]]]:
    """curry a function with 6 parameters"""
    ...


def curry(f: Callable) -> PZFunc:
    """To curry a function, type system only support less than 7 parameters

    :param f: the normal un-curried python function
    :return: A curried PythonZ function
    """
    return PZFunc(lambda x: curry(lambda *args: f(x, *args)))
