def calcular(a, b, operacao):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return None

    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        if b == 0:
            return None
        return a / b
    elif operacao == '^':
        return a ** b
    else:
        return None
