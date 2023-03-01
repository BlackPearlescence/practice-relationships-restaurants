from review import Review
from restaurant import Restaurant
class Customer:
    def __init__(self,first_name:str,last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
    def get_first_name(self) -> str:
        return self.first_name
    def get_last_name(self) -> str:
        return self.last_name
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    def get_reviews(self):
        return self.reviews
    def add_review(self,restaurant,rating):
        new_review = Review(self,restaurant,rating)
        self.reviews.append(new_review)
        restaurant.reviews.append(new_review)
    def review_count(self) -> int:
        return len(self.reviews)
    
rest = Restaurant("Blah")   
customer = Customer('Jane', 'Doe')
review = Review(customer, rest, 5)
review1 = Review(customer, rest, 10)
review2 = Review(customer, rest, 12)
review3 = Review(customer, rest, 5)
rest.reviews = [review,review1,review2,review3]
avg = rest.average_rating()
print(avg)