class vowels:
    def __init__(self, text: str) -> None:
        self.text = text
        self.all_vowels = ["a", "i", "e", "o", "u", "y"]
        self.current_letter_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_letter_idx += 1
        if self.current_letter_idx == len(self.text):
            raise StopIteration

        current_letter = self.text[self.current_letter_idx]
        if current_letter.lower() in self.all_vowels:
            return current_letter
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
