class TodoList:
    def __init__(self, lst_tasks: list[str]):
        self.lst_tasks = lst_tasks

    def __repr__(self):
        return f"{self.__class__.__name__}(list[str])"

    def __str__(self):
        return '\n'.join(self.lst_tasks)

    def __add__(self, other):
        result = [*self.lst_tasks, *other.lst_tasks]
        return TodoList(result)

    def __len__(self):
        return len(self.lst_tasks)



list1 = TodoList(['task1', 'task2'])
list2 = TodoList(['task3', 'task4'])

list3 = list1 + list2

print(len(list3))
# 4
