# Automatically generated by Pynguin.
import script_80 as module_0


def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    var_0 = module_0.is_happy(set_0)
    assert var_0 is False


def test_case_1():
    str_0 = 'i|SLNL1AIIDV'
    dict_0 = {}
    tuple_0 = str_0, dict_0, dict_0
    bytes_0 = b'\xba\xe5j#\xd5\x96\x99\x16$5My\xfd'
    var_0 = module_0.is_happy(bytes_0)
    assert var_0 is True
    var_1 = module_0.is_happy(tuple_0)
    assert var_1 is False
