class Credentials:
    def __init__(self):
        self.__password = "secret"

    def get_password(self):
        return self.__password

cred = Credentials()
print(cred.get_password())