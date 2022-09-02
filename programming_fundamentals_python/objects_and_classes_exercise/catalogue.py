class Catalogue:
    def __init__(self, name: str):
        self.products = []
        self.name = name

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        filtered_list = [product for product in self.products if product[0] == first_letter]
        return filtered_list

    def __repr__(self):
        string = f"Items in the {self.name} catalogue:"
        for item in sorted(self.products):
            string += f"\n{item}"
        return string


