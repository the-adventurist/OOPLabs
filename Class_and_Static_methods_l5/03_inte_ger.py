from typing import Optional, Union


class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value) -> Optional[str]:
        if not isinstance(float_value, float):
            return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[value[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"
        try:
            number = int(value)
            return cls(number)
        except ValueError:
            return "wrong type"


