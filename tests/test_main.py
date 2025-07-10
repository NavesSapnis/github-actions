from main import some_logic


def test_some_logic_true():
    assert some_logic(True) is True
    assert some_logic([1, 2, 3]) == [1, 2, 3]
    assert some_logic([]) == []    
    