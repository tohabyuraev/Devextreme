import math
import typing

from .lebedev import liblebedev


def graph_3_2(
    M: typing.Union[float, int],
    lambda_n: typing.Union[float, int],
    lambda_c: typing.Union[float, int]):
    """
    Функция возвращает значения по графику 3.2
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    lambda_n: float, int
        Удлинение носовой части ЛА
    lambda_c: float, int
        Удлинение цилиндрической части ЛА

    Returns
    -------
    float
        К-т подъемной силы изолированного фюзеляжа
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной М - float или int')

    elif not isinstance(lambda_n, (float, int)):
        raise TypeError('Тип переменной lambda_n - float или int')
    
    elif not isinstance(lambda_c, (float, int)):
        raise TypeError('Тип переменной lambda_c - float или int')

    argument = {
        0: 0,
        1: lambda_c / lambda_n,
    }

    if M < 0:
        raise ValueError('Переменная M < 0')
    elif M < 1:
        argument[0] = math.sqrt(1 - M ** 2) / lambda_n
    else:
        argument[0] = math.sqrt(M ** 2 - 1) / lambda_n

    return liblebedev.graph_3_2(argument[0], argument[1])


def graph_5_11(
    d: typing.Union[float, int],
    l: typing.Union[float, int]):
    """
    Функция возвращает значения по графику 5.11
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    d : float, int
        Относительный диаметр
    l : float, int
        Удлинение консолей крыла

    Returns
    -------
    float
        Параметр f_1
    """
    if not isinstance(d, (float, int)):
        raise TypeError('Тип переменной d - float или int')
    
    elif not isinstance(l, (float, int)):
        raise TypeError('Тип переменной l - float или int')
    
    return liblebedev.graph_5_11(d, l)