import client


def test_float_division():
    result = client.getRatio(100.00, 50.0)
    assert result == 2.0
    return result


def test_integer_division():
    result = client.getRatio(10, 2)
    assert result == 5
    return result


def test_zero_division():
    result = client.getRatio(10, 0)
    assert result is None
    return result


if __name__ == '__main__':
    print(f'Float Division Result: {test_float_division()}')
    print(f'Integer Division Result: {test_integer_division()}')
    print(f'Zero Division Result: {test_zero_division()}')


