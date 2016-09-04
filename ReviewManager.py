import Review
class ReviewManager(object):
    """description of class"""
    reviewList=[]

    def jsonToObject(self,rev):
        
        product=rev["product"]
        date=rev["date"]
        email=rev["email"]
        rating=rev["rating"]
        text=rev["reviewText"]
        revObj = Review.Review(product,date,email,rating,reviewText)
        self.reviewList.append(revObj)

    def getReviews(self):
        return self.reviewList



