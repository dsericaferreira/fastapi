import warnings
warnings.filterwarnings("ignore")

class Fibonacci():

    def __init__(self):
        pass

    def calculate(lista: int):
        if lista <= 0:
            return []
        elif lista == 1:
            return [0]
        elif lista == 2:
            return [0, 1]
        else:
            f = Fibonacci.calculate(lista - 1)
            f.append(f[-1] + f[-2])
            return f