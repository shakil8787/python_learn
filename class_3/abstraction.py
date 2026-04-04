from abc import ABC, abstractmethod

class Browser(ABC):

    @abstractmethod
    def start(self):
        pass

class Chrome(Browser):
    def start(self):
        print("ক্রোম ব্রাউজার শুরু হয়েছে।")

class Firefox(Browser):
    def start(self):
        print("ফায়ারফক্স ব্রাউজার শুরু হয়েছে।")

ch =Chrome()
ch.start()
print("================================")
fh=Firefox()
fh.start()