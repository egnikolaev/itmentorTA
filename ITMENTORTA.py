import sys

def calculate(expression):

    try:
        # Добавляем пробелы вокруг оператора, если их нет
        new_expression = ""
        for char in expression:
            if char in "+-*/":
                new_expression += " " + char + " "
            else:
                new_expression += char
        expression = " ".join(new_expression.split())  # Убираем лишние пробелы

        parts = expression.split()
        if len(parts) != 3:
            raise ValueError("throws Exception")

        try:
            num1 = int(parts[0])
            num2 = int(parts[2])
        except ValueError:
            raise ValueError("throws Exception")

        operator = parts[1]

        if not (1 <= num1 <= 10 and 1 <= num2 <= 10):
            raise ValueError("throws Exception")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("throws Exception")
            result = num1 // num2

        return str(result)

    except ValueError as e:
        print("throws Exception")
        sys.exit()
    except Exception as e:
        print("throws Exception")
        sys.exit()


def main():
    while True:
        user_input = input("Введите арифметическое выражение (два числа от 1 до 9 и знак между ними,например, '5+3' или '5 + 3'): ")
        try:
            result = calculate(user_input)
            print(result)
        except SystemExit:
            break


if __name__ == "__main__":
    main()