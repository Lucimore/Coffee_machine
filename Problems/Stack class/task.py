class Stack():

    def __init__(self):
        self.my_stack = []

    def push(self, elm):
        self.my_stack.append(elm)

    def pop(self):
        last_el = len(self.my_stack) - 1
        self.my_stack.remove(last_el)
        return last_el

    def peek(self):
        return len(self.my_stack) - 1

    def is_empty(self):
        if not self.my_stack:
            return True
        return False
