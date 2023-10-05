from config import logger

def correct_input_int(type: str) -> int:
    isCorrect = False

    while isCorrect == False:

        try:
            number = int(input(f"\n{type}\n-> "))
            isCorrect = True

        except:
            logger.warning("Inaccessible value entered!")

    return number

def correct_input_float(type: str) -> float:
    isCorrect = False

    while isCorrect == False:

        try:
            number = float(input(f"\n{type}\n-> "))
            isCorrect = True

        except:
            logger.warning("Inaccessible value entered!")

    return number