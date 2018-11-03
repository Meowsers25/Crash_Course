class Users():

    def __init__(self, first_name, last_name, id, city):
        self.first = first_name
        self.last = last_name
        self.id = id
        self.city = city

    def describe_user(self):
        print(f"{self.first.title()} {self.last.title()} lives in {self.city.title()}.")
        print(f"{self.last.title()} ID: {self.id}")

    def greet_user(self):
        print(f"Hello {self.id}, welcome to the Terrordome.")

user_1 = Users('Chris', 'lamothe', 'de34jks', 'providence')
user_2 = Users('mr', 'robot', '88rd3sw3', 'new york')
user_3 = Users('luna', 'lamothe', 'woof123', 'prov')

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()    