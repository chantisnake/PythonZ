from pythonz.basic import PZFunc


def add1(n: int) -> int:
    return n + 1


pz_add1 = PZFunc(add1)
pz_add1(1)


def test_call():
    assert 2 == pz_add1(1)


def test_apply():
    assert 3 == pz_add1 % 1


def test_compose():
    assert 3 == pz_add1 * pz_add1 % 1
