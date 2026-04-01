class TestCase2:
    test_type = "regression"

    #constructor
    def __init__(self, name, environment):
        self.test_name = name
        self.environment = environment

    def run_test(self):
        print("test type: ", TestCase2.test_type)
        print("running test: ", self.test_name)
        print("environment: ", self.environment)

#create instances of testcase2
test1 = TestCase2("login test", "staging")
print(test1.test_type)
test1.run_test()# Output: login test
test2 = TestCase2("checkout test", "production")
print(test1.test_type)
test2.run_test()