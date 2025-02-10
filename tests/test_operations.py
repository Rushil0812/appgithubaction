from src.math_operations import add, sub

def test_add():
    assert add(3, 5) == 8
    assert add(3, -5) == -2
    
def test_sub():
    assert sub(5, 2) == 3
    assert sub(5, -2) == 7