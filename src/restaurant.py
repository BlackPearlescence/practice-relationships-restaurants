from functools import reduce
class Restaurant:
    def __init__(self,name:str):
        self.name = name
        self.reviews = []
    def get_name(self) -> str:
        return self.name
    def get_reviews(self):
        return self.reviews
    def average_rating(self):
        ratings = [review.rating for review in self.reviews]
        return reduce(lambda a,b: a+b,ratings) / len(ratings)
    
