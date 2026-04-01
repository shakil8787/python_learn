class AssertionHelper:
    def varify_true(self, condition):
        if condition:
            print("Assertion passed: Condition is true.")
        else:
            print("Assertion failed: Condition is false.")

hp = AssertionHelper()
hp.varify_true(True)
hp.varify_true(False)