# Automatically generated by Pynguin.
import script_72 as module_0


def test_case_0():
    bytes_0 = b'_\xaf\xa1\xf0\xa5\x15\x95\x96B\xea\xd0\x13'
    int_0 = -2266
    var_0 = module_0.will_it_fly(bytes_0, int_0)


def test_case_1():
    bytes_0 = b'_\xaf\xa1\xf0\xa5\x15\x95\x96B\xea\xd0\x13'
    int_0 = 2542
    var_0 = module_0.will_it_fly(bytes_0, int_0)
    assert var_0 is False


def test_case_2():
    bytes_0 = b'T'
    int_0 = 2518
    var_0 = module_0.will_it_fly(bytes_0, int_0)
    assert var_0 is True


def test_case_3():
    bytes_0 = b'A?'
    int_0 = 976
    var_0 = module_0.will_it_fly(bytes_0, int_0)
    assert var_0 is False
    int_1 = -853
    tuple_0 = int_1, int_1
    bool_0 = False
    var_1 = module_0.will_it_fly(tuple_0, bool_0)
    assert var_1 is True
