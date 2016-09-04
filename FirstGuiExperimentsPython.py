from tkinter import *
from tkinter import ttk
import ProductManagement
import MongoData
import time

#class for creating a window and an
#entry form for a new review
#it inherits from tkinter.Frame
#I used absolute placement
#instead of a grid, which would
#probably provide more flexibility

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of the master widget      
        self.master.title("TechStore")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a label instance
        self.prompt = Label(self, text="Choose a product to Review")

        # placing the lable on the window
        self.prompt.place(x=10, y=0)
        
        #calling the product management class
        #to get the products
        pm = ProductManagement.ProductManagement()
        #making sure the product list is populated
        pm.populateProducts()
        products=pm.getProducts()

        #creating the Combobox and populating it with products
        self.productsCombo=ttk.Combobox(self, values=products,state=READABLE)
        self.productsCombo.place(x=10, y=25)
        
        # creating email label
        self.emailLabel=Label(self, text="Enter your email")
        self.emailLabel.place(x=10, y=55)

        #creating email entry box
        self.emailEntry=Entry(self)
        self.emailEntry.place(x=10, y=75) 

        #creating the rating label
        self.ratingLabel=Label(self, text="Rate the product 1 to 5")
        self.ratingLabel.place(x=10, y=105)
        
        #creating the Entry for ratings
        self.rating=Entry(self)
        self.rating.place(x=10, y=125)

        #creating the review label
        self.reviewLabel =Label(self, text="Enter your review")
        self.reviewLabel.place(x=10, y=150)

        #creating the multiline Text enty
        #I wanted to add a scollbar, but every
        #attempt at it made the text box take
        #over the whole screen
        self.review =Text(self, height=10, width=50)
        self.review.place(x=10, y=170)
        
        #add the save review button
        save=Button(self.master, text="Save Review",command = self.insertReview)
        save.place(x=10, y=360)

        #add the exit button, which kills the window
        #but doesn't make it disappear
        #the lambda allows the button to contain
        #the quit command in its own constructor
        exit=Button(self.master, text="Exit",command = lambda:exit.quit())
        exit.place(x=100, y=360)
       
    #this method takes the values from the combo
    #and text boxes and passes them to
    #the MongoData class where they are
    #inserted. The structure of the review
    #is somewhat different and simpler
    #than the original in the Mongo examples
    def insertReview(self):
         p=self.productsCombo.get()
         
         email=self.emailEntry.get()
         r=self.rating.get()
         rev=self.review.get("1.0",END)
         revDate=time.strftime("%c")

         document = {
            "product" : p,
            "email" : email,
            "date" : revDate,
            "rating" : r,
            "reveiw" : rev
            }
         md = MongoData.MongoData()
         result=md.insertReview(document)
         insertResult=Label(self, text=result)
         insertResult.place(x=10, y=385)

   

         

root = Tk()

#size of the window
root.geometry("500x400")

app = Window(root)
root.mainloop()  



