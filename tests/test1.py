def test1(a, b, *, k1, k2):
    pass


def test2(a, b, k1=None, k2=None):
    pass


def test3(a, b, k1=2, k2="hye"):
    pass


def test4(a, b, *, k0=None, k1=2, k2="hye"):
    pass


def test5(a, b, *, k0=None, k1=None, k2=None):
    pass


def test6(a, b, *, k0=None, k1=None, k2):
    pass
