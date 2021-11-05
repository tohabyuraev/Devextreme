from .lebedev import liblebedev


def graph_5_11(d: float, l: float):
    """
    Функция возвращает значения по графику 5.11
        Лебедев А. А., Чернобровкин Л. С. Динамика полета БЛА

    Parameters
    ----------
    d : float
        Относительный диаметр
    l : float
        Удлинение консолей крыла

    Returns
    -------
    float
        Параметр f_1
    """
    if not isinstance(d, float):
        raise Exception('Переменная d должна быть типа float')
    if not isinstance(l, float):
        raise Exception('Переменная lambda_k должна быть типа float')
    return liblebedev.graph_5_11(d, l)