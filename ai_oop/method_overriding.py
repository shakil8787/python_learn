class animal:
    def speak(self):
        print("প্রাণীটি শব্দ করছে")

class dog(animal):
    def sound(self):
        print("কুকুরটি ঘেউ ঘেউ করছে")

d = dog()
d.sound()