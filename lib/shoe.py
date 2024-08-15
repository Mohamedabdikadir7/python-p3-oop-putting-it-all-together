class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Use a private attribute for validation
        self.size = size  # Use the property setter for validation
        self.condition = 'New'  # Initialize condition attribute

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'  # Set condition to 'New' after repair

    def __repr__(self):
        return f"Shoe(brand='{self.brand}', size={self._size}, condition='{self.condition}')"

# Example of usage
if __name__ == "__main__":
    shoe = Shoe("Adidas", 9)
    print(shoe)  # Should print: Shoe(brand='Adidas', size=9, condition='New')
    shoe.cobble()  # Should print: Your shoe is as good as new!
    print(shoe)  # Should print: Shoe(brand='Adidas', size=9, condition='New')
