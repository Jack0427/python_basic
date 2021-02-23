def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("a,b需為整數")
