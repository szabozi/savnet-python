class Stack(object):
    def __init__(self, default_list):
        self.__stack_list = default_list or []

    def push(self, valoare):
        self.__stack_list.append(valoare)

    def pop(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value

    def display_stack(self):
        print(self.__stack_list)

    def is_empty(self):
        """
        test if the stack is true or not
        :return: True when empty, False otherwise
        """
        return len(self.__stack_list) == 0


s1 = Stack([item for item in range(10)])
s2 = Stack([])

while not s1.is_empty():
    s1.display_stack()
    s2.push(s1.pop())
    s2.display_stack()




