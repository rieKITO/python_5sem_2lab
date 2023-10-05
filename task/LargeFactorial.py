import threading
import sys
import time

# TASKS
from task.factorial import factorial
from task.InputHandling import correct_input_int

def calculate_factorial(number, threadsCount):

    def partial_factorial(start, end):
        thread.result = factorial(start, end)

    result = 1
    threads = []
    
    # Разделение вычислений на потоки
    for i in range(threadsCount):
        start = (number // threadsCount) * i + 1
        end = (number // threadsCount) * (i + 1)
        
        if i == threadsCount - 1:
            end = number
        
        thread = threading.Thread(target=partial_factorial, args=(start, end))
        threads.append(thread)
        thread.start()
    
    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()
    
    # Вычисление итогового результата
    for thread in threads:
        result *= thread.result

    callsSimpleFactorial, totalTimeSimpleFactorial = factorial.get_stats()

    return result, callsSimpleFactorial, totalTimeSimpleFactorial

def large_factorial_func() -> None:
    sys.set_int_max_str_digits(100000)
    number = correct_input_int("Enter the number:")
    threadsCount = correct_input_int("Enter the count of threads:")
    result, callsSimpleFactorial, totalTimeSimpleFactorial = calculate_factorial(number, threadsCount)

    print(
        f"Number: {number}\n" +
        f"Count of threads: {threadsCount}\n" +
        f"Factorial: {result}\n" +
        f"Number of calls: {callsSimpleFactorial}\n" +
        f"Execution time: {totalTimeSimpleFactorial}"
    )

    factorial.clear_stats()