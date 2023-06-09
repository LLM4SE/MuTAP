def generate_test_case():
    assert sort_age([("M", 23), ("F", 19), ("M", 30)]) == [("M", 30), ("M", 23), ("F", 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30), ("F", 25)]) == [("M", 30), ("M", 23), ("F", 25), ("F", 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30), ("F", 25), ("F", 25)]) == [("M", 30), ("M", 23), ("F", 25), ("F", 25), ("F", 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30), ("F", 25), ("F", 25), ("F", 25)]) == [("M", 30), ("M", 23), ("F", 25), ("F", 25), ("F", 25), ("F", 19)]
    assert sort_age([("M", 23), ("F", 19), ("M", 30), ("F", 25), ("F", 25), ("F", 25), ("M", 30)]) == [("M", 30), ("M", 30), ("M", 23), ("F", 25), ("F", 25), ("F", 25), ("F", 19)]
