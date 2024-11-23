def calculator_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Ошибка"
        except SyntaxError:
            return "Ошибка "
        except Exception as e:
            return f"Ошибка {e}"

    return wrapper

@calculator_decorator
def calculate(expression):
    return eval(expression)
