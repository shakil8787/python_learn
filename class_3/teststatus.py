class Teststatus:

    def passed(self):
        print("Test passed successfully!")

    def failed(self):
        print("Test failed successfully!")

st=Teststatus()
st.passed()
st.failed()