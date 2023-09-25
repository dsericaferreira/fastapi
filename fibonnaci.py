import warnings
warnings.filterwarnings("ignore")

class Fibonacci:

    def __init__(self):
        pass

    @staticmethod
    def calculate(elementos: int):
        if elementos <= 0:
            return []
        elif elementos == 1:
            return [0]
        elif elementos == 2:
            return [0, 1]
        else:
            f = Fibonacci.calculate(elementos - 1)
            f.append(f[-1] + f[-2])
            return f