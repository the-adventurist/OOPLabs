from typing import Sequence


class reverse_iter:
    def __init__(self, iterable_obj: Sequence) -> None:
        self.iterable_obj = iterable_obj
        self.start_index = len(iterable_obj)
        self.end_index = - 1
        self.current_index = self.start_index

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index -= 1
        if self.current_index == self.end_index:
            raise StopIteration
        current_number = self.iterable_obj[self.current_index]
        return current_number


reversed_list = reverse_iter([1, 2, 30, 4])
for item in reversed_list:
    print(item)
