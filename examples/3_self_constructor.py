class Page:
    BASE_URL = 'http://my-page.com'

# attributes
    def __init__(self, url, name):
        self.url = f"{self.BASE_URL}{url}"
        self.name = name

# methods
    def open(self):
        # обязательно в методе передавать (self)
        # иначе будет ошибка, при вызове этого метода в экземпляре,
        # так как self всегда неявно передается

        # self можно назвать как угодно, например this, это как "плейсхолдер"
        # поэтому могут быть разные названия даже внутри одного кода, ошибки не будет

        print(f"Open {self.url}")

    def change_name(self, new_name):
        self.name = new_name

# создание экземпляра класса
login_page = Page(url="/login", name="LOGIN")

# обращение к атрибуту
print(login_page.name) # LOGIN

# вызов метода
print(login_page.change_name("AUTH"))

# обращение к атрибуту после изменения значения в атрибуте NAME
print(login_page.name) # AUTH
