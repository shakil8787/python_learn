from idlelib import browser


class Browser:
    def start(self):
        print("browser is starting")

class Chrome(Browser):
    def start(self):
        print("chrome is starting")

class Firefox(Browser):
    def start(self):
        print("firefox is starting")

# def run_test(browser):
#     browser.start()
#     print("running test")
#
# run_test(Chrome())
# run_test(Firefox())

ch =Chrome()
ch.start()