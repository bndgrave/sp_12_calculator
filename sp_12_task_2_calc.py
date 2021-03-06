import operator


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        value = self.__items.pop()
        return value


def calc_result(expression:str):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
    }
    elements = expression.split(' ')
    operands = Stack()
    for element in elements:
        if element.isdigit() or element[1:].isdigit():
            operands.push(int(element))
        else:
            operand_1 = operands.pop()
            operand_2 = operands.pop()
            operands.push(
                operators[element](operand_2, operand_1)
            )
    return operands.pop()


if __name__ == '__main__':
    expression = input()
    result = calc_result(expression)
    print(result)
