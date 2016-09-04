class ProductClass(object):
    """mongo product class"""
    #This class stores product information
    def __init__(self, product, price, quantityAvailable):
        self.product = product
        self.price = price
        self.quantityAvailable=quantityAvailable



