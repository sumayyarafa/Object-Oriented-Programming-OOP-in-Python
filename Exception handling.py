def process_input(x, y):
    try:
        result = 10 / x
        print(f"Outer try: result = {result}")
        try:
            if y < 0:
                raise ValueError("Negative value for y not allowed.")
            elif y == 0:
                raise ZeroDivisionError("y cannot be zero.")
            result = result / y
            print(f"Inner try: result = {result}")
        except ValueError as ve:
            print(f"Inner except ValueError: {ve}")
        except ZeroDivisionError as ze:
            print(f"Inner except ZeroDivisionError: {ze}")
        finally:
            print("Inner finally block executed.")
    except ZeroDivisionError as ze:
        print(f"Outer except ZeroDivisionError: {ze}")
    finally:
        print("Outer finally block executed.")

process_input(5, 2)
process_input(0, 2)
process_input(5, -1)

#----------------------------
filename = 'search.py'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words")

#--------------------------------

while True:
    try:
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter denominator: '))
        result = number1 / number2
    except ValueError:
        print('You must enter two integers\n')
    except ZeroDivisionError:
        print('Attempted to divide by zero\n')
    else:
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
        break

















