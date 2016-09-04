from pymongo import MongoClient

class MongoData(object):
    """Handles all Mongo transactions"""
    #this class handles all direct Mongo transactions
    #It has methods to return all products
    #only those product based on criteria
    #and a method to insert a new product
    #in addition it has methods for adding
    #reviews and getting all reviews
    #for a particular product

    client=MongoClient()
    db=client.TechStore

    def _init_(self):
        self.client=MongoClient()
        self.db=client.TechStore

    #get all products
    def getCursorAllProduct(self):
        cursor=self.db.productCollection.find()
        self.client.close()
        return cursor
    
    #get products based on some criteria
    def getCursorProductCriteria(self, criteria):
        cursor=self.db.productCollection.find(criteria)
        self.client.close()
        return cursor

    #get last _id
    def getCountProducts(self):
        result = db.productCollection.count()
        return result


    #insert a new product
    def insertProduct(self, document):
        result=self.db.productCollection.insert_one(document)
        self.client.close()
        return result

    #get review count
    def getCountReviews(self):
        result = db.reviewCollection.count()
        return result

    #insert a review
    def insertReview(self, document):
         result=self.db.reviewCollection.insert_one(document)
         self.client.close()
         return result

     #return reviews based on product
    def getReviewbyProduct(self, productName):
        criteria = { "product" : productName}
        cursor = self.db.reviewCollection.find(criteria)
        return cursor
