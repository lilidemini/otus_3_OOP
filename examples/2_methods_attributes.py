class Page:
    name='PAGE'
    url='http://localhost/page'

# methods
    def open(self):
        print(f"opened: {self.url}")


page.open()
assert page.url

# attributes
page = Page(url='/page', name='main')
