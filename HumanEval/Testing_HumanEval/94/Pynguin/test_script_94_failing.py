# Automatically generated by Pynguin.
import script_94 as module_0


def test_case_0():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        var_0 = module_0.skjkasdkd(set_0)
    except BaseException:
        pass


def test_case_1():
    try:
        bytes_0 = b"@\xa8'\xb7l\xca`"
        var_0 = module_0.skjkasdkd(bytes_0)
        assert var_0 == 0
    except BaseException:
        pass


def test_case_2():
    try:
        bytes_0 = b'Q\xe9\xba\xea\xce\x11\x16c'
        var_0 = module_0.skjkasdkd(bytes_0)
        assert var_0 == 8
        float_0 = 3170.2194
        dict_0 = {var_0: var_0, var_0: var_0}
        list_0 = [bytes_0, dict_0, float_0, dict_0]
        var_1 = module_0.skjkasdkd(list_0)
    except BaseException:
        pass
