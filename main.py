from config import logger

# TASK
from task.BubbleSort import bubble_sort_interface
from task.factorial import factorial_func
from task.LargeFactorial import large_factorial_func

def correct_input_main_menu_choice(type: str = None) -> int:
    isCorrect = False

    while isCorrect == False:

        try:
            number = int(input(f"-> "))

            if number < 1 or number > 4:
                logger.warning("Inaccessible value entered!")

            else:
                isCorrect = True

        except:
            logger.warning("Inaccessible value entered!")

    return number

def main_menu() -> None:
    print(
        f"\n-- Number of calls, Execution time --\n" +
        f"Choice the task:\n" +
        f"1) Bubble sort\n" +
        f"2) One-thread factorial\n" +
        f"3) Many-thread factorial\n" +
        f"4) Exit"
    )

def main():
    isExit = False
    while isExit == False:
        main_menu()
        choice = correct_input_main_menu_choice()
        
        match choice:
            case 1:
                bubble_sort_interface()
            case 2:
                factorial_func()
            case 3:
                large_factorial_func()
            case 4:
                isExit = True

if __name__ == '__main__':
    main()