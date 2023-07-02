DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

BALLANCED = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
UNBALLANCED = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)

    def pop(self):
        if not self.isEmpty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def ballance(part):
    stack = Stack()
    for item_ in part:
        if item_ in DICT:
            stack.push(item_)
        elif item_ == DICT.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.isEmpty()


if __name__ == '__main__':
    for part in BALLANCED + UNBALLANCED:
        print(f'{part}')
        print(f'{ballance(part)}')
