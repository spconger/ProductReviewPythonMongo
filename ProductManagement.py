import json
import Product
import pymongo
import MongoData

class ProductManagement(object):
    """manages productclass objects"""
    #This class manages the productClass objects
    #The gets the json results and converts
    #them to ProductClass objects
    #which are then stored in a list
    #It has methods to create the object
    #and store it.
    #Return a list of just the product names
    #and one to return just an individual
    #project that matches a product name
    prodList=[]
    def _init_(self):
        prodlist=self.prodList
         
    def populateProducts(self):
        md = MongoData.MongoData()
        cursor=md.getCursorAllProduct()
        for document in cursor:
           self.jsonToObject(document)

    #method for converting json to objects
    def jsonToObject(self,prod):
        
        product=prod["product"]
        price=prod["price"]
        quantityAvailable=prod["quantityAvailable"]
        productObj = Product.ProductClass(product, price,quantityAvailable)
        self.prodList.append(productObj)

    #method for returning product names
    def getProducts(self):
        products=[]
        
        for index in range(len(self.prodList)):
           
            self.prodList[index].product
            products.append(self.prodList[index].product)

        return products
            
    #method for returning single product info by name
    def getProductsByName(self, productName):
        info
        for index in range(len(self.prodList)):
            if self.prodList[index].product==productName:
                info=self.prodList[index].product + " "
                + self.prodList[index].price + " " 
                + self.prodList[index].quantityAvailable
                break
        return info




