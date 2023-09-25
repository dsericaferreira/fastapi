class Fibonacci:

    def __init__(self):
        pass

    @staticmethod
    def calculate(elements: int):
        if elements <= 0:
            return []
        elif elements == 1:
            return [0]
        elif elements == 2:
            return [0, 1]
        else:
            f = Fibonacci.calculate(elements - 1)
            f.append(f[-1] + f[-2])
            return f