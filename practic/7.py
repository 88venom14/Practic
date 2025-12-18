def tokenize(expr: str):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i].isdigit():
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(int(num))
            continue
        if expr[i] in '+-*/()':
            tokens.append(expr[i])
            i += 1
        else:
            raise ValueError(f"Недопустимый символ: '{expr[i]}'")
    return tokens

def infix_to_postfix(tokens):
    output = []
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        if isinstance(token, int):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Несбалансированные скобки")
            stack.pop()
        elif token in precedence:
            while (
                stack and
                stack[-1] != '(' and
                stack[-1] in precedence and
                precedence[stack[-1]] >= precedence[token]
            ):
                output.append(stack.pop())
            stack.append(token)
        else:
            raise ValueError(f"Неизвестный токен: {token}")

    while stack:
        if stack[-1] in '()':
            raise ValueError("Несбалансированные скобки")
        output.append(stack.pop())

    return output


def eval_postfix(postfix):
    stack = []
    for token in postfix:
        if isinstance(token, int):
            stack.append(token)
        else:
            if len(stack) < 2:
                raise ValueError("Недостаточно операндов")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                stack.append(int(a / b))
    if len(stack) != 1:
        raise ValueError("Некорректное выражение")
    return stack[0]


def calculate(expression: str) -> int:
    tokens = tokenize(expression)
    postfix = infix_to_postfix(tokens)
    result = eval_postfix(postfix)
    return result

if __name__ == "__main__":

    test_cases = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "15 / 3 - 2",
        "10 - 2 - 3",
        "2 * (5 + 3) / 4",
        "100 / 10 / 2",
        "((2 + 3) * (5 - 1)) / 2"
    ]
    for expr in test_cases:
            res = calculate(expr)
            print(f"  {expr} = {res}")