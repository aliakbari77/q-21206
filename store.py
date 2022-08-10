import datetime
from models import Product, User


class Store:
    def __init__(self):
        self.products: Product = dict()
        self.users: User = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        try:
            self.products[product] = self.products[product] - amount
            if (self.products[product] <= 0):
                del self.products[product]
        except:
            raise Exception("Not Enough Products")
    
    def add_user(self, username):
        countOfUsername = self.users.count(username)
        if (countOfUsername != 0):
            return None
        
        self.users.append(User(username))
        
        return username

    def get_total_asset(self):
        totalAsset = 0
        for i in self.products:
            totalAsset += i.price * self.products[i]
        
        return totalAsset
            

    def get_total_profit(self):
        totalProfit = 0
        for i in self.users.bought_products:
            totalProfit += i.price
        
        return totalProfit

    def get_comments_by_user(self, user):
        userComments = []
        for i in self.products.comments:
            if (i.user == user):
                userComments.append(i.text)
        
        return userComments

    def get_inflation_affected_product_names(self):
        pass

    def clean_old_comments(self, date: datetime):
        for i in self.products.comments:
            if(i.date_added < date):
                del self.products.comments[i]

    def get_comments_by_bought_users(self, product):
        pass