class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return product_name

    def remove(self, product_name):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)

    def __repr__(self):
        result = ''

        for p in self.products:
            if p == self.products[-1]:
                result += f"{p.name}: {p.quantity}"
            else:
                result += f"{p.name}: {p.quantity}\n"

        return result
