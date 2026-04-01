class BaseTest:
    def setup(self):
        print("browser setup")

class login(BaseTest):
    def test_login(self):
        print("login test executed")


lg = login()
lg.setup()
lg.test_login()