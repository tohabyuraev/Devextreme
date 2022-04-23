import math
from typing import Union

from .lebedev import liblebedev


def graph_3_2(
    M: Union[float, int],
    lambda_n: Union[float, int],
    lambda_c: Union[float, int]):
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
        (комбинации конус-цилиндр)
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
        argument[0] = - math.sqrt(1 - M ** 2) / lambda_n
    else:
        argument[0] = math.sqrt(M ** 2 - 1) / lambda_n

    return liblebedev.graph_3_2(
        argument[0], 
        argument[1],
    )


def graph_3_3(
    M: Union[float, int],
    lambda_n: Union[float, int],
    lambda_c: Union[float, int]):
    """
    Функция возвращает значения по графику 3.3
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
        (комбинации оживало-цилиндр)
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
        argument[0] = - math.sqrt(1 - M ** 2) / lambda_n
    else:
        argument[0] = math.sqrt(M ** 2 - 1) / lambda_n

    return liblebedev.graph_3_3(
        argument[0], 
        argument[1],
    )


def graph_3_4(
    M: Union[float, int],
    lambda_c: Union[float, int],
    cil_type: Union[float, int]):
    """
    Функция возвращает значения по графику 3.4
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    lambda_c: float, int
        Удлинение цилиндрической части
    cil_type: float, int
        Тип цилиндрического торца
        (0 - плоский; 1 - сферический)

    Returns
    -------
    float
        К-т подъемной силы изолированного фюзеляжа
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной М - float или int')
    elif not isinstance(lambda_c, (float, int)):
        raise TypeError('Тип переменной lambda_c - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')

    argument = {
        0: 0,
        1: cil_type,
    }

    if M < 1:
        argument[0] = - math.sqrt(1 - M ** 2) / lambda_c
    else:
        argument[0] = math.sqrt(M ** 2 - 1) / lambda_c

    return liblebedev.graph_3_4(
        argument[0],
        argument[1],
    )


def graph_3_5(
    M: Union[float, int],
    lambda_k: Union[float, int],
    c: Union[float, int],
    chi_05: Union[float, int]):
    """
    Функция возвращает значения по графику 3.5
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    lambda_k: float, int
        Удлинение двух консолей крыла
    c: float, int
        Относительная толщина профиля крыла
    chi_05: float, int
        Угол стреловидности по линии середин хорд, рад

    Returns
    -------
    float
        К-т подъемной силы изолированного крыла
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной М - float или int')
    elif not isinstance(lambda_k, (float, int)):
        raise TypeError('Тип переменной lambda_k - float или int')
    elif not isinstance(c, (float, int)):
        raise TypeError('Тип переменной c - float или int')
    elif not isinstance(chi_05, (float, int)):
        raise TypeError('Тип переменной chi_05 - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif lambda_k < 0.0:
        raise ValueError('Значение lambda_k должно быть больше нуля')
    elif c < 0.0:
        raise ValueError('Значение c должно быть больше нуля')

    argument = {
        0: 0,
        1: lambda_k * math.pow(c, 1 / 3),
        2: lambda_k * math.tan(chi_05),
    }

    if M < 1:
        argument[0] = - math.sqrt(1 - M ** 2) * lambda_k
    else:
        argument[0] = math.sqrt(M ** 2 - 1) * lambda_k

    return liblebedev.graph_3_5(
        argument[0],
        argument[1],
        argument[2],
    ) * lambda_k


def graph_3_13(
    M: Union[float, int]):
    """
    Функция возвращает значения по графику 3.13
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока

    Returns
    -------
    float
        Поправочный множитель chi_m
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')

    return liblebedev.graph_3_13(M)


def graph_3_21(
    M: Union[float, int],
    lambda_n: Union[float, int]):
    """
    Функция возвращает значения по графику 3.21
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    lambda_n: float, int
        Удлинение носовой части ЛА

    Returns
    -------
    float
        Коэффициент торможения потока
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(lambda_n, (float, int)):
        raise TypeError('Тип переменной lambda_n - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif lambda_n <= 0.0:
        raise ValueError('Значение lambda_n должно быть больше нуля')

    return liblebedev.graph_3_21(M, lambda_n)


def graph_3_22(
    M: Union[float, int],
    x: Union[float, int],
    b: Union[float, int]):
    """
    Функция возвращает значения по графику 3.22
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    x: float, int
        Расстояиние между консолями
    b: float, int
        САХ консолей в м

    Returns
    -------
    float
        Коэффициент торможения потока от обтекания передних
        несущих поверхностей (вспомогательная величина)
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(x, (float, int)):
        raise TypeError('Тип переменной x - float или int')
    elif not isinstance(b, (float, int)):
        raise TypeError('Тип переменной b - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif b <= 0.0:
        raise ValueError('Значение b должно быть больше нуля')

    return liblebedev.graph_3_22(M, x / b)


def graph_3_25(
    l_r: Union[float, int],
    l_k: Union[float, int],
    eta_k: Union[float, int]):
    """
    Функция возвращает значения по графику 3.25
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    l_r: float, int
        Размах рулей
    l_k: float, int
        Размах консолей
    eta_k: float, int
        Сужение консолей

    Returns
    -------
    float
        Коэффициент n характеризующий
        относительную эффективность рулей
    """
    if not isinstance(l_r, (float, int)):
        raise TypeError('Тип переменной l_r - float или int')
    elif not isinstance(l_k, (float, int)):
        raise TypeError('Тип переменной l_k - float или int')
    elif not isinstance(eta_k, (float, int)):
        raise TypeError('Тип переменной eta_k - float или int')

    if l_r < 0.0:
        raise ValueError('Значение l_r должно быть больше нуля')
    elif l_k < 0.0:
        raise ValueError('Значение l_k должно быть больше нуля')
    elif eta_k < 0.0:
        raise ValueError('Значение eta_k должно быть больше нуля')

    return liblebedev.graph_3_25(l_r / l_k, eta_k)


def graph_3_28(
    M: Union[float, int],
    b_otn: Union[float, int],
    lambda_k: Union[float, int]):
    """
    Функция возвращает значения по графику 3.28
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    b_otn: float, int
        Относительная хорда руля
    lambda_k: float, int
        Удлинение консолей

    Returns
    -------
    float
        Коэффициент n характеризующий относительную
        эффективность рулей, расположенных вдоль
        задней кромки стабилизаторов
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(b_otn, (float, int)):
        raise TypeError('Тип переменной b_otn - float или int')
    elif not isinstance(lambda_k, (float, int)):
        raise TypeError('Тип переменной lambda_k - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif M > 1.0:
        raise ValueError('Значение M должно быть меньше единицы')
    elif b_otn < 0.0:
        raise ValueError('Значение b_otn должно быть больше нуля')
    elif b_otn > 1.0:
        raise ValueError('Значение b_otn должно быть меньше единицы')
    elif lambda_k < 0.0:
        raise ValueError('Значение lambda_k должно быть больше нуля')

    return liblebedev.graph_3_28(b_otn, lambda_k * math.sqrt(1 - M ** 2))


def graph_3_29(
    M: Union[float, int],
    T: Union[float, int]):
    """
    Функция возвращает значения по графику 3.29
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    T: float, int
        Тип коэффициента:
        1 - С_1
        2 - C_2

    Returns
    -------
    float
        Коэффициенты (C_1, C_2) определяющие давление на
        поверхности профиля по теории второго приближения
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(T, (float, int)):
        raise TypeError('Тип переменной T - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif T not in (1, 2):
        raise ValueError('Значение T должно быть равно 1 или 2')

    return liblebedev.graph_3_29(M, T)


def graph_3_32(
    M: Union[float, int],
    alpha: Union[float, int]):
    """
    Функция возвращает значения по графику 3.32
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    T: float, int
        Угол атаки, [рад]

    Returns
    -------
    float
        Коэффициенты (C_1, C_2) определяющие давление на
        поверхности профиля по теории второго приближения
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(alpha, (float, int)):
        raise TypeError('Тип переменной alpha - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')

    return liblebedev.graph_3_32(M * math.sin(alpha))


def graph_3_35(
    M: Union[float, int],
    eta_k: Union[float, int],
    cy_iz_kr: Union[float, int]):
    """
    Функция возвращает значения по графику 3.35
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    eta_k: float, int
        Сужение консолей крыла
    cy_iz_kr: float, int
        к-т подьемной силы из. крыльев

    Returns
    -------
    float
        Коэффициент А
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(eta_k, (float, int)):
        raise TypeError('Тип переменной eta_k - float или int')
    elif not isinstance(cy_iz_kr, (float, int)):
        raise TypeError('Тип переменной cy_iz_kr - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif eta_k <= 0.0:
        raise ValueError('Значение eta_k должно быть больше нуля')
    
    return liblebedev.graph_3_35(M, eta_k, cy_iz_kr)


def graph_4_2(
    Re: Union[float, int],
    xt: Union[float, int]):
    """
    Функция возвращает значения по графику 4.2
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    Re: float, int
        Число Рейнольдса
    xt: float, int
        Отн. коор-та точки перехода ламинарного
        пограничного слоя в турбулентный

    Returns
    -------
    float
        Удвоенный к-т трения плоской пластинки
    """
    if not isinstance(Re, (float, int)):
        raise TypeError('Тип переменной Re - float или int')
    elif not isinstance(xt, (float, int)):
        raise TypeError('Тип переменной xt - float или int')

    if Re < 0.0:
        raise ValueError('Значение Re должно быть больше нуля')
    elif xt < 0.0:
        raise ValueError('Значение xt должно быть больше нуля')

    return liblebedev.graph_4_2(Re, xt)


def graph_4_3(
    M: Union[float, int],
    x: Union[float, int]):
    """
    Функция возвращает значения по графику 4.3
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    x: float, int
        Отн. координата тоски перехода ламинарного
        пограничного слоя в тербелентный

    Returns
    -------
    float
        Множитель eta_m
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(x, (float, int)):
        raise TypeError('Тип переменной x - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif x < 0.0:
        raise ValueError('Значение x должно быть больше нуля')

    return liblebedev.graph_4_3(M, x)


def graph_4_5(
    M: Union[float, int],
    RehL: Union[float, int]):
    """
    Функция возвращает значения по графику 4.5
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    RehL: float, int
        Произведение числа Рейнольдса и относительной
        высоты неровностей поверхности

    Returns
    -------
    float
        Критичсекое число Рейнольдса
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(RehL, (float, int)):
        raise TypeError('Тип переменной RehL - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif RehL < 0.0:
        raise ValueError('Значение RehL должно быть больше нуля')

    return liblebedev.graph_4_5(M, RehL)


def graph_4_8(
    M: Union[float, int],
    T: Union[float, int]):
    """
    Функция возвращает значения по графику 4.8
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    T: 0 or 1
        Тип температуры:
        0 - восстановления,
        1 - поверхности тела

    Returns
    -------
    float
        Отн. температура полной
        стабилизпции пограничного слоя
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif T not in (0, 1):
        raise ValueError('Тип может быть единица или ноль')

    return liblebedev.graph_4_8(M, T)


def graph_4_9(
    M: Union[float, int],
    T_c: Union[float, int],
    T_r: Union[float, int]):
    """
    Функция возвращает значения по графику 4.9
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    T_c: float, int
        Температура поверхности тела
    T_r: 0 or 1
        Температура восстановления

    Returns
    -------
    float
        Влияние температураы поверхности тела
        на критическое число Рейнольдса
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(T_c, (float, int)):
        raise TypeError('Тип переменной T_c - float или int')
    elif not isinstance(T_r, (float, int)):
        raise TypeError('Тип переменной T_r - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif T_c < 0.0:
        raise ValueError('Значение T_c должно быть больше нуля')
    elif T_r < 0.0:
        raise ValueError('Значение T_r должно быть больше нуля')

    return liblebedev.graph_4_9(M, T_c / T_r)


def graph_4_10(
    M: Union[float, int],
    lambda_n: Union[float, int]):
    """
    Функция возвращает значения по графику 4.10
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    lambda_n: float, int
        Удлинение носовой части ЛА

    Returns
    -------
    float
        Поправочный множитель k_kon (отношение к-та сопротивления
        трения конуса к к-ту сопротивления плоской пластинки)
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(lambda_n, (float, int)):
        raise TypeError('Тип переменной lambda_n - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif lambda_n < 0.0:
        raise ValueError('Значение lambda_n должно быть больше нуля')

    return liblebedev.graph_4_10(M, lambda_n)


def graph_4_11(
    M: Union[float, int],
    lambda_n: Union[float, int]):
    """
    Функция возвращает значения по графику 4.11
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    lambda_n: float, int
        Удлинение носовой части ЛА

    Returns
    -------
    float
        Коэффициент силы сопротивления
        конической носовой части
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(lambda_n, (float, int)):
        raise TypeError('Тип переменной lambda_n - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif lambda_n < 0.0:
        raise ValueError('Значение lambda_n должно быть больше нуля')

    return liblebedev.graph_4_11(M, lambda_n)


def graph_4_12(
    M: Union[float, int],
    lambda_n: Union[float, int]):
    """
    Функция возвращает значения по графику 4.12
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    lambda_n: float, int
        Удлинение носовой части ЛА

    Returns
    -------
    float
        Коэффициент силы сопротивления
        конической носовой части
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(lambda_n, (float, int)):
        raise TypeError('Тип переменной lambda_n - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif lambda_n < 0.0:
        raise ValueError('Значение lambda_n должно быть больше нуля')

    return liblebedev.graph_4_12(M, lambda_n)


def graph_4_13(
    M: Union[float, int],
    lambda_n: Union[float, int]):
    """
    Функция возвращает значения по графику 4.13
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    lambda_n: float, int
        Удлинение носовой части ЛА

    Returns
    -------
    float
        Коэффициент силы сопротивления
        носовой части с эллиптической образующей
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(lambda_n, (float, int)):
        raise TypeError('Тип переменной lambda_n - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif lambda_n < 0.0:
        raise ValueError('Значение lambda_n должно быть больше нуля')

    return liblebedev.graph_4_13(M, lambda_n)


def graph_4_15(
    M: Union[float, int],
    theta: Union[float, int]):
    """
    Функция возвращает значения по графику 4.15
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока [-]
    T: float, int
        Угол полураствора фиктивного конуса [град]

    Returns
    -------
    float
        Число Маха на поверхности конуса [-]
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(theta, (float, int)):
        raise TypeError('Тип переменной theta - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif theta < 0.0:
        raise ValueError('Значение theta должно быть больше нуля')

    return liblebedev.graph_4_15(M, theta)


def graph_4_24(
    M: Union[float, int],
    eta_korm: Union[float, int],
    lambda_k: Union[float, int],
    korm_type: Union[float, int]):
    """
    Функция возвращает значения по графику 4.24
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    eta_korm: float, int
        Сужение кормовой части
    lambda_k: float, int
        Удлинение кормовой части
    korm_type: float, int
        Тип кормовой части:
        0 - прямолинейная
        1 - параболическая
    
    Returns
    -------
    float
        К-т сопротивления кормовой части
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(eta_korm, (float, int)):
        raise TypeError('Тип переменной eta_korm - float или int')
    elif not isinstance(lambda_k, (float, int)):
        raise TypeError('Тип переменной lambda_k - float или int')
    elif not isinstance(korm_type, (float, int)):
        raise TypeError('Тип переменной korm_type - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif eta_korm < 0.0:
        raise ValueError('Значение eta_korm должно быть больше нуля')
    elif lambda_k < 0.0:
        raise ValueError('Значение lambda_k должно быть больше нуля')

    return liblebedev.graph_4_24(M, eta_korm, lambda_k, korm_type)


def graph_4_27(
    M: Union[float, int],
    eta_korm: Union[float, int],
    lambda_k: Union[float, int]):
    """
    Функция возвращает значения по графику 4.27
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    eta_korm: float, int
        Сужение кормовой части
    lambda_k: float, int
        Удлинение кормовой части
    
    Returns
    -------
    float
        К-т влияния сужения кормовой части
        на коэффициент донного давления
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(eta_korm, (float, int)):
        raise TypeError('Тип переменной eta_korm - float или int')
    elif not isinstance(lambda_k, (float, int)):
        raise TypeError('Тип переменной lambda_k - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif eta_korm < 0.0:
        raise ValueError('Значение eta_korm должно быть больше нуля')
    elif lambda_k < 0.0:
        raise ValueError('Значение lambda_k должно быть больше нуля')

    argument = {
        0: M,
        1: (1 - eta_korm) / (2 * lambda_k * eta_korm ** 2)
    }

    return liblebedev.graph_4_27(
        argument[0],
        argument[1],
    )


def graph_4_28(
    c: Union[float, int],
    x: Union[float, int]):
    """
    Функция возвращает значения по графику 4.28
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    c: float, int
        Относительная толщина профиля
    x: float, int
        Относительная коор-та точки перехода

    Returns
    -------
    float
        Поправочный коэффициент eta_c
    """
    if not isinstance(c, (float, int)):
        raise TypeError('Тип переменной c - float или int')
    elif not isinstance(x, (float, int)):
        raise TypeError('Тип переменной x - float или int')

    if c < 0.0:
        raise ValueError('Значение c должно быть больше нуля')
    elif x < 0.0:
        raise ValueError('Значение x должно быть больше нуля')

    return liblebedev.graph_4_28(c, x)


def graph_4_29(
    chi: Union[float, int]):
    """
    Функция возвращает значения по графику 4.29
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    chi: float, int
        Угол стреловидности [град]

    Returns
    -------
    float
        Относительное число Рейнольдса
    """
    if not isinstance(chi, (float, int)):
        raise TypeError('Тип переменной chi - float или int')

    if chi > 90.0:
        raise ValueError('Значение c должно быть меньше 90 град')

    return liblebedev.graph_4_29(chi)


def graph_4_30(
    M: Union[float, int],
    c: Union[float, int],
    chi_c: Union[float, int],
    eta_k: Union[float, int],
    lambda_k: Union[float, int]):
    """
    Функция возвращает значения по графику 4.30
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    c: float, int
        Относительная толщина профиля
    chi_c: float, int
        Угол стреловидности по линии
        макс. толщин крыла
    eta_k: float, int
        Сужение консолей крыла
    lambda_k: float, int
        Удлинение консолей крыла

    Returns
    -------
    float
        c_хв/ (lambda_k * c ** 2)
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(c, (float, int)):
        raise TypeError('Тип переменной c - float или int')
    elif not isinstance(chi_c, (float, int)):
        raise TypeError('Тип переменной chi_c - float или int')
    elif not isinstance(eta_k, (float, int)):
        raise TypeError('Тип переменной eta_k - float или int')
    elif not isinstance(lambda_k, (float, int)):
        raise TypeError('Тип переменной lambda_k - float или int')

    if M < 1.0:
        raise ValueError('Значение M должно быть больше единицы')
    elif c < 0.0:
        raise ValueError('Значение c должно быть больше нуля')
    elif chi_c < 0.0:
        raise ValueError('Значение chi_c должно быть больше нуля')
    elif eta_k < 0.0:
        raise ValueError('Значение eta_k должно быть больше нуля')
    elif lambda_k < 0.0:
        raise ValueError('Значение lambda_k должно быть больше нуля')

    argument = {
        '0': lambda_k * math.sqrt(M ** 2 - 1),
        '1_0': lambda_k * math.tan(chi_c),
        '1_1': lambda_k * c ** (1 / 3),
        '2': eta_k,
    }

    return liblebedev.graph_4_30(
        argument['0'],
        argument['1_0'],
        argument['1_1'],
        argument['2'],
    )


def graph_4_32(
    M: Union[float, int],
    chi_c: Union[float, int]):
    """
    Функция возвращает значения по графику 4.32
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    chi_c: float, int
        Угол стреловидности по линии
        максимальных толщин, [рад]

    Returns
    -------
    float
        Коэффициент phi
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(chi_c, (float, int)):
        raise TypeError('Тип переменной chi_c - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')

    if M < 1.0:
        argument = 0.0
    else:
        argument = math.sqrt(M ** 2 - 1) - math.tan(chi_c)

    return liblebedev.graph_4_32(argument)


def graph_4_34(
    c: Union[float, int],
    c_n: Union[float, int],
    x_c: Union[float, int]):
    """
    Функция возвращает значения по графику 4.34
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    c: float, int
        Относительная толщина профиля
    c_n: float, int
        К-т нормальной силы крыла
    x_c: float, int
        Отн. коор-та линии макс. толщин

    Returns
    -------
    float
        Критическое число Маха
    """
    if not isinstance(c, (float, int)):
        raise TypeError('Тип переменной c - float или int')
    elif not isinstance(c_n, (float, int)):
        raise TypeError('Тип переменной c_n - float или int')
    elif not isinstance(x_c, (float, int)):
        raise TypeError('Тип переменной x_c - float или int')

    if c < 0.0:
        raise ValueError('Значение c должно быть больше нуля')
    elif c_n < 0.0:
        raise ValueError('Значение c_n должно быть больше нуля')
    elif x_c < 0.0:
        raise ValueError('Значение x_c должно быть больше нуля')

    return liblebedev.graph_4_34(c, c_n, x_c)


def graph_4_35(
    M_kr: Union[float, int],
    lambda_k: Union[float, int]):
    """
    Функция возвращает значения по графику 4.35
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Критическое число Маха по
        линии максимальных толщин
    lambda_k: float, int
        Удлинение консолей крыльев

    Returns
    -------
    float
        Изменение критического числа Маха
    """
    if not isinstance(M_kr, (float, int)):
        raise TypeError('Тип переменной M_kr - float или int')
    elif not isinstance(lambda_k, (float, int)):
        raise TypeError('Тип переменной lambda_k - float или int')

    if M_kr < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif lambda_k < 0.0:
        raise ValueError('Значение lambda_k должно быть больше нуля')

    return liblebedev.graph_4_35(M_kr, lambda_k)


def graph_4_36(
    M_kr: Union[float, int],
    chi_c: Union[float, int]):
    """
    Функция возвращает значения по графику 4.36
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Критическое число Маха по
        линии максимальных толщин
    chi_c: float, int
        Угол стреловидности по линии
        максимальных толщин, [град]

    Returns
    -------
    float
        Изменение критического числа Маха
    """
    if not isinstance(M_kr, (float, int)):
        raise TypeError('Тип переменной M_kr - float или int')
    elif not isinstance(chi_c, (float, int)):
        raise TypeError('Тип переменной chi_c - float или int')

    if M_kr < 0.0:
        raise ValueError('Значение M_kr должно быть больше нуля')
    elif chi_c < 0.0:
        raise ValueError('Значение chi_c должно быть больше нуля')

    return liblebedev.graph_4_36(M_kr, chi_c)


def graph_4_38(
    M: Union[float, int]):
    """
    Функция возвращает значения по графику 4.38
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока

    Returns
    -------
    float
        Коэффициент донного давления профиля
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')

    return liblebedev.graph_4_38(M)


def graph_4_40(
    M: Union[float, int],
    lambda_n: Union[float, int],
    nose_type: Union[float, int]):
    """
    Функция возвращает значения по графику 4.40
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    lambda_n: float, int
        Удлинение носовой части ЛА
    nose_type: float, int
        Тип носовой части:
        0 - оживальная
        1 - коническая

    Returns
    -------
    float
        Коэффициент zeta
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной М - float или int')
    elif not isinstance(lambda_n, (float, int)):
        raise TypeError('Тип переменной lambda_n - float или int')
    elif not isinstance(nose_type, (float, int)):
        raise TypeError('Тип переменной nose_type - float или int')

    argument = {
        0: 0,
        1: nose_type,
    }

    if M < 0:
        raise ValueError('Переменная M < 0')
    elif M < 1:
        argument[0] = - math.sqrt(1 - M ** 2) / lambda_n
    else:
        argument[0] = math.sqrt(M ** 2 - 1) / lambda_n

    return liblebedev.graph_4_40(
        argument[0],
        argument[1],
    )


def graph_4_42(
    M: Union[float, int],
    chi_0: Union[float, int],
    lambda_k: Union[float, int]):
    """
    Функция возвращает значения по графику 4.42
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    chi_0: float, int
        Угол стреловидности по передней кромке крыла [град]
    lambda_k: float, int
        Удлинение консолей крыла

    Returns
    -------
    float
        Коэффициент пропорциональности в формуле к-та
        подсасывающей силы изоированных крыльев
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(chi_0, (float, int)):
        raise TypeError('Тип переменной chi_0 - float или int')
    elif not isinstance(lambda_k, (float, int)):
        raise TypeError('Тип переменной lambda_k - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif lambda_k < 0.0:
        raise ValueError('Значение lambda_k должно быть больше нуля')

    argument = {
        0: 0,
        1: lambda_k * math.tan(math.radians(chi_0)),
    }

    if M < 1:
        argument[0] = - lambda_k * math.sqrt(1 - M ** 2)
    else:
        argument[0] = lambda_k * math.sqrt(M ** 2 - 1)

    return liblebedev.graph_4_42(
        argument[0],
        argument[1],
    )


def graph_4_43(
    M: Union[float, int],
    chi_0: Union[float, int],
    alpha: Union[float, int]):
    """
    Функция возвращает значения по графику 4.43
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    chi_0: float, int
        Угол стреловидности по передней кромке крыла [град]
    alpha: float, int
        Угол атаки летательного аппарата [град]

    Returns
    -------
    float
        Коэффициент реализации подсасывающей силы
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(chi_0, (float, int)):
        raise TypeError('Тип переменной chi_0 - float или int')
    elif not isinstance(alpha, (float, int)):
        raise TypeError('Тип переменной alpha - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')

    argument = {
        0: 0,
        1: alpha,
    }

    if M < 1:
        argument[0] = - math.sqrt(1 - M ** 2) / math.tan(math.radians(chi_0))
    else:
        argument[0] = + math.sqrt(M ** 2 - 1) / math.tan(math.radians(chi_0))

    return liblebedev.graph_4_43(
        argument[0],
        argument[1],
    )


def graph_5_7(
    M: Union[float, int],
    lambda_n: Union[float, int],
    lambda_c: Union[float, int]):
    """
    Функция возвращает значения по графику 5.7
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
        Параметр delta x_f
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
        argument[0] = - math.sqrt(1 - M ** 2) / lambda_n
    else:
        argument[0] = math.sqrt(M ** 2 - 1) / lambda_n

    return liblebedev.graph_5_7(
        argument[0],
        argument[1],
    )


def graph_5_8(
    M: Union[float, int],
    eta_k: Union[float, int],
    chi_05: Union[float, int],
    lambda_k: Union[float, int]):
    """
    Функция возвращает значения по графику 5.8
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    eta_k: float, int
        Сужение консолей крыла
    chi_05: float, int
        Угол стреловидности по линии
        середин хорд [рад]
    lambda_k: float, int
        Удлинение консолей крыла

    Returns
    -------
    float
        Координата фокуса изолированных крыльев
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной M - float или int')
    elif not isinstance(eta_k, (float, int)):
        raise TypeError('Тип переменной eta_k - float или int')
    elif not isinstance(chi_05, (float, int)):
        raise TypeError('Тип переменной chi_05 - float или int')
    elif not isinstance(lambda_k, (float, int)):
        raise TypeError('Тип переменной lambda_k - float или int')

    if M < 0.0:
        raise ValueError('Значение M должно быть больше нуля')
    elif eta_k < 0.0:
        raise ValueError('Значение eta_k должно быть больше нуля')
    elif lambda_k < 0.0:
        raise ValueError('Значение lambda_k должно быть больше нуля')

    argument = {
        0: 0,
        1: eta_k,
        2: lambda_k * math.tan(chi_05),
    }
    if M < 1:
        argument[0] = - math.sqrt(1 - M ** 2) * lambda_k
    else:
        argument[0] = math.sqrt(M ** 2 - 1) * lambda_k

    return liblebedev.graph_5_8(
        argument[0],
        argument[1],
        argument[2],
    )


def graph_5_9(
    M: Union[float, int],
    c: Union[float, int],
    lambda_k: Union[float, int]):
    """
    Функция возвращает значения по графику 5.9
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    M: float, int
        Число Маха набегающего потока
    c: float, int
        Относительная толщина профиля
    lambda_k: float, int
        Удлинение консолей крыла

    Returns
    -------
    float
        Коэффициент влияния на положение
        фокуса прямоугольных крыльев
    """
    if not isinstance(M, (float, int)):
        raise TypeError('Тип переменной М - float или int')
    elif not isinstance(c, (float, int)):
        raise TypeError('Тип переменной c - float или int')
    elif not isinstance(lambda_k, (float, int)):
        raise TypeError('Тип переменной lambda_k - float или int')

    argument = {
        0: 0,
        1: lambda_k * c ** (1 / 3),
    }

    if M < 0:
        raise ValueError('Переменная M < 0')
    elif M < 1:
        argument[0] = - math.sqrt(1 - M ** 2) * lambda_k
    else:
        argument[0] = + math.sqrt(M ** 2 - 1) * lambda_k

    return liblebedev.graph_5_9(
        argument[0],
        argument[1],
    )


def graph_5_11(
    d: Union[float, int],
    l: Union[float, int]):
    """
    Функция возвращает значения по графику 5.11
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    d: float, int
        Относительный диаметр
    l: float, int
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
