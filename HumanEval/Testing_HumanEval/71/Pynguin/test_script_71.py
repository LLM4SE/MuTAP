# Automatically generated by Pynguin.
import script_71 as module_0


def test_case_0():
    str_0 = '&\\y'
    str_1 = 'AYz:cT'
    str_2 = 'Y`h\r{Y;0'
    var_0 = module_0.triangle_area(str_0, str_1, str_2)
    assert var_0 == -1


def test_case_1():
    str_0 = 'Tbs'
    str_1 = '#LuNaLs3Ec|@'
    var_0 = module_0.triangle_area(str_0, str_1, str_1)
    assert var_0 == -1


def test_case_2():
    str_0 = '{U&%;Nk'
    str_1 = 'e,Bmk\x0b'
    str_2 = 'Y`h\r{YV;0'
    var_0 = module_0.triangle_area(str_1, str_0, str_2)
    assert var_0 == -1
