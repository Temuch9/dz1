from dz import hello_name, distance

def test_hello_name():
    assert hello_name("Артём") == "Привет, Артём"
    assert hello_name("Вася") == "Привет, Вася"
    assert hello_name("Саня") == "Привет, Саня"

def test_distance():
    assert distance(4,80) == 320
    assert distance(5, 90) == 450
    assert distance(2, 100) == 55
