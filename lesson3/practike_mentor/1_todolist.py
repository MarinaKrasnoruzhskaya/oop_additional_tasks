class TodoList:
    def __init__(self, lst_tasks: list[str]):
        self.lst_tasks = lst_tasks

    def __repr__(self):
        return f"{self.__class__.__name__}(list[str])"

    def __str__(self):
        return '\n'.join(self.lst_tasks)


tasks = ['task1', 'task2']

list1 = TodoList(tasks)

print(repr(list1)) #TodoList(list[str])

print(list1)
# task1
# task2