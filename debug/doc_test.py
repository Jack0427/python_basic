def fun_demo(a, b):
    """
      >>> fun_demo(1, 2)
      3
      >>> fun_demo('a', 'b')
      'ab'
      >>> fun_demo([1,2], [3,4])
      [1, 2, 3, 4]
      >>> fun_demo(1,'2')
      Traceback (most recent call last):
      TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
