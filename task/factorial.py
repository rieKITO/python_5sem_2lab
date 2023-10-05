# TASKS
from task.InputHandling import correct_input_int
from task.ProfileDecorator import ProfileDecorator

@ProfileDecorator
def factorial(start, end) -> int:
    if start > end:
        return 1
    else:
        return start * factorial(start + 1, end)

def factorial_func() -> None:
    factorialNum = correct_input_int("Enter the number:")
    # todo correct factorial num
    result = factorial(1, factorialNum)
    callsSimpleFactorial, totalTimeSimpleFactorial = factorial.get_stats()

    print(
        f"Number: {factorialNum}\n" +
        f"Factorial: {result}\n" +
        f"Number of calls: {callsSimpleFactorial}\n" +
        f"Execution time: {totalTimeSimpleFactorial}"
    )

    factorial.clear_stats()