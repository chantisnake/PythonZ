from pythonz.basic import PZFunc


@PZFunc
def add1(n: int) -> int:
    return n + 1


def test_call():
    assert 2 == add1(1)


def test_apply():
    assert 3 == add1 % 2


def test_compose():
    assert 3 == add1 * add1 % 1
