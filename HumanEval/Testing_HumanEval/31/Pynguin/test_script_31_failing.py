# Automatically generated by Pynguin.
import script_31 as module_0


def test_case_0():
    try:
        int_0 = -2191
        var_0 = module_0.is_prime(int_0)
        assert var_0 is False
        float_0 = None
        var_1 = module_0.is_prime(float_0)
    except BaseException:
        pass


def test_case_1():
    try:
        int_0 = 2903
        var_0 = module_0.is_prime(int_0)
        assert var_0 is True
        bytes_0 = b'\xf1\xe5\xfaV\xfc\x9d\xe4{P\xb4\x07n\xf1\xa7*\x9b'
        int_1 = -833
        var_1 = module_0.is_prime(int_1)
        assert var_1 is False
        var_2 = module_0.is_prime(bytes_0)
    except BaseException:
        pass
