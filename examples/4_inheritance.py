# inheritance - наследование

# создание родительского класса Browser
class Browser:
    def open(self, url):
        print(f"Open url {url}")

    def refresh(self):
        print("Page refreshed")

# создание класса-потомка родительского класса Browser
class Chrome(Browser): # у потомка Chrome родительский класс в круглых скобках (Browser)

    # потомок выполняет методы класса-родителя

    # в потомке можно создавать дополнительные методы,
    # выполняемые только им:
    def logs(self):
        print('Chrome logs')

    # в потомке можно переопределять методы класса-родителя,
    # переопределение метода отразится только при вызове метода потомком
    def refresh(self):
        print("Super refresh")


# создание класса-потомка родительского класса Browser
class Firefox(Browser):

    def set_headlees(self):
        pass

# потомок наследует методы родителя и выполняет их:
firefox = Firefox()
firefox.open('http://yandex.ru') # Open url http://yandex.ru

chrome = Chrome()
chrome.open('http://google.com') # Open url http://google.com
