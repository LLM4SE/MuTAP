# Automatically generated by Pynguin.
import script_61 as module_0


def test_case_0():
    str_0 = 'dN#.'
    var_0 = module_0.correct_bracketing(str_0)
    assert var_0 is False


def test_case_1():
    str_0 = ''
    str_1 = 'Rp\t]Ft\x0ceFt'
    var_0 = module_0.correct_bracketing(str_1)
    assert var_0 is False
    var_1 = module_0.correct_bracketing(str_0)
    assert var_1 is True
    str_2 = 'of&c<K\r'
    str_3 = '"mk\\56?KAqTwG;\r'
    var_2 = module_0.correct_bracketing(str_1)
    assert var_2 is False
    var_3 = module_0.correct_bracketing(str_3)
    assert var_3 is False
    var_4 = module_0.correct_bracketing(str_2)
    assert var_4 is False
    var_5 = module_0.correct_bracketing(str_2)
    assert var_5 is False
    var_6 = module_0.correct_bracketing(str_3)
    assert var_6 is False
    var_7 = module_0.correct_bracketing(str_2)
    assert var_7 is False