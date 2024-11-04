from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Логирует вызов функции и ее результат в файл или на консоль."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"
            except Exception as e:
                log_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message + "\n")
                    print(log_message)
            else:
                print(log_message)

        #            return result
        return wrapper

    return decorator

if __name__ == '__main__':

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y


    @log()
    def my_function_(x, y):
        return x + y

    print(my_function(1,2))

    print(my_function_(3,2))
