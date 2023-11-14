class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self.items[-1]

    def size(self):
        return len(self.items)

def get_balance(lines):
    stack = Stack()
    open_brack = '([{'
    close_brack = ')]}'
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for line in lines:
        if line in open_brack:
            stack.push(line)
        elif line in close_brack:
            if stack.is_empty():
                return False
            pop_st = stack.pop()
            if pairs[line] != pop_st:
                return False
    return stack.is_empty()


def check_balance(lines):
    if get_balance(lines):
        return "Сбалансированно"
    else:
        return "Несбалансированно"


print(check_balance("(((([{}]))))"))
print(check_balance("[([])((([[[]]])))]{()}"))
print(check_balance("{{[()]}}"))
#несбалансированно
print(check_balance("}{}"))
print(check_balance("{{[(])]}}"))
print(check_balance("[[{())}]"))