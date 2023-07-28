class custom_range:
    def __init__(self, start_index: int, end_index: int) -> None:
        self.start_index = start_index
        self.end_index = end_index
        self.current_index = start_index - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index > self.end_index:
            raise StopIteration

        return self.current_index



one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
