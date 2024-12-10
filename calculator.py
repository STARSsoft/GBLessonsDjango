def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите действительное число.")

def input_operator():
    while True:
        operator = input("Введите оператор (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Ошибка: введите корректный оператор.")

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль невозможно."
        else:
            return num1 / num2

def main():
    print("Простой калькулятор")
    num1 = input_number("введите первое число: ")
    operator = input_operator()
    num2 = input_number("введите второе число: ")
    
    result = calculate(num1, operator, num2)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
