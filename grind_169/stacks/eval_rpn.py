
def evalRPN(tokens):
    operators = ["+", "-", "*", "/"]
    stack = []
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append(b + a)
            elif token == "-":
                stack.append(b - a)
            elif token == "*":
                stack.append(b * a)
            elif token == "/":
                # Truncate toward zero
                stack.append(int(b / a))
    return stack[-1]


# Example
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))  # 9
