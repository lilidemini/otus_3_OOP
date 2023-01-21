class Page:
    BASE_URL = 'http://my-page.com'

# attributes
    def __init__(self, url, name):
        self.url = f"{self.BASE_URL}{url}"
        self.name = name

# methods
    def open(self):
        print(f"Open {self.url}")

# создание экземпляров класса Page
page = Page(url="/page", name="PAGE") # экземпляр page
login_page = Page(url="/login", name="LOGIN") # экземпляр login_page
main_page = Page(url="/main", name="MAIN") # экземпляр main_page

# обращение к атрибутам экземпляра
print(page.url) # http://my-page.com/page
print(login_page.url) # http://my-page.com/login
print(main_page.url) # http://my-page.com/main

# обращение к методам экземпляра
page.open() # Open http://my-page.com/page
login_page.open() # Open http://my-page.com/login
main_page.open() # Open http://my-page.com/main

# изменение значения в классе Page
Page.BASE_URL = "http://test.main-page.com"

# изменения в классе изменили BASE_URL для всех экземпляров класса
print(login_page.BASE_URL) # http://test.main-page.com
print(main_page.BASE_URL) # http://test.main-page.com


# изменение значение атрибута BASE_URL только в экземпляре login_page
login_page.url = 'http://local.main-page.com/auth'
print(login_page.url) # http://local.main-page.com/auth

# изменения в экземпляре login_page не влияют на другие экземпляры
print(main_page.url) # http://my-page.com/main
