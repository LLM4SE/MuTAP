# Automatically generated by Pynguin.
import q2 as module_0


def test_case_0():
    try:
        bool_0 = True
        str_0 = 'X"D"2bO#Wur-J66A'
        list_0 = [bool_0, bool_0, str_0]
        str_1 = 'V\r)z<^;fgcOLH*K\n'
        var_0 = module_0.contains_unique_day(list_0, str_1)
        assert var_0 is False
        int_0 = None
        bytes_0 = b'\x84t&\x9b\xe4\x83#S\xee\x9cQ)d\xfd\x9d'
        var_1 = module_0.unique_month(int_0, bytes_0)
    except BaseException:
        pass


def test_case_1():
    try:
        str_0 = 'l'
        var_0 = module_0.contains_unique_day(str_0, str_0)
    except BaseException:
        pass


def test_case_2():
    try:
        str_0 = '|'
        list_0 = [str_0, str_0, str_0]
        var_0 = module_0.unique_month(str_0, list_0)
        assert var_0 is False
        str_1 = 'X"D"2bO#Wur-J66A'
        str_2 = 'Wvr\x0cT*\x0c@\nn#'
        set_0 = {var_0, var_0, str_1}
        var_1 = module_0.contains_unique_day(str_2, set_0)
    except BaseException:
        pass


def test_case_3():
    try:
        float_0 = -716.0
        list_0 = [float_0, float_0, float_0]
        tuple_0 = list_0, float_0, list_0
        tuple_1 = list_0, tuple_0
        var_0 = module_0.contains_unique_day(float_0, tuple_1)
        assert var_0 is False
    except BaseException:
        pass