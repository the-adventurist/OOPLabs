class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        print(self.__username)
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        contain_upper_case_letter = [l for l in value if l.isupper()]
        contain_at_least_one_digit = [d for d in value if d.isdigit()]
        if len(value) < 8 or not contain_upper_case_letter or not contain_at_least_one_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}"' \
               f' and password: {"*" * len(self.__password)}'

correct_profile = Profile("Username",
"Passw0rd")
print(correct_profile)