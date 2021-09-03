class conversation_stack:
    '''
    check size before popping
    '''
    def __init__(self, stack=[]):
        self.stack = stack

    def push(self, item: str):
        self.stack.append(item)

    def pop(self) -> str:
        return self.stack.pop()

    def peek(self) -> str:
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

    def is_not_empty(self):
        return self.size() != 0