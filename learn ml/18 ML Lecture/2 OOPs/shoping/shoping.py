
# Online Shopping System:
#    - **Classes**: `Product`, `ShoppingCart`, `Order`, `User`, `PaymentMethod`, `ShippingMethod`.
#    - **OOP Concepts**:
#      - **Abstraction**: Abstract the `PaymentMethod` and `ShippingMethod` to allow different implementations.
#      - **Encapsulation**: Use accessors and modifiers for managing product details and user information.
#      - **Inheritance**: Different types of products can inherit from a base `Product` class.

#    - **Features**:
#      - Product browsing and searching.
#      - Shopping cart management.
#      - Order placement and payment processing.
#      - Shipping options.
#      - User accounts.

class User:
    buyer_accounts = {}
    seller_accounts = {}

    def __init__(self):
        self.__username = None
        self.__pin = None
        self.option = None
        self.name = None
        self.PIN = None
        self.money = None
        self.product_in_cart = 0

    def set_username_pin(self, name, password, option):
        self.__username = name
        self.__pin = password

        # Append the key-value pair
        # my_dict['satyam'] = 1234
        option[self.__username] = [[self.__pin]]

        if option == User.buyer_accounts:
            self.money = int(input("Enter Amount :"))
            option[self.__username] = [[self.__pin, self.money, self.product_in_cart]]

    def get_username(self):
        return self.__username

    def get_pin(self):
        return self.__pin

    def create_account(self):
        self.option = int(input("Enter Options 1 . Buyer  2. Seller"))
        if self.option == 1:
            self.buyer()
        elif self.option == 2:
            self.seller()
        else:
            print("Option dang se daal")

    def buyer(self):
        self.account_creation("buy")

    def seller(self):
        self.account_creation("sell")

    def account_creation(self, acc_type):

        self.name = input("Enter User name for  Account :")
        self.PIN = input("Enter PIN  for Account :")

        if acc_type == "buy":
            self.option = User.buyer_accounts
        else:
            self.option = User.seller_accounts

        if self.name in self.option:
            print("Username all ready taken , 🥺 try again")
            self.buyer()
        else:
            self.set_username_pin(self.name, self.PIN, self.option)

    @staticmethod
    def print_details():
        print(User.buyer_accounts)
        print(User.seller_accounts)


class Product(User):

    def __init__(self):
        super().__init__()
        self.description = None
        self.price = None
        self.new_product = None
        self.username = None
        self.password = None
        pass

    def verify_seller(self):
        print("SELLER VERIFICATION 🔐")
        self.username = input("Enter your seller username :")
        self.password = input("Enter your seller password :")

        if (self.username in User.seller_accounts) and User.seller_accounts[self.username][0][0] == self.password:
            print(self.username, "Loging Success full 😃")
            return True
        else:
            print("Sale chor Seller🔫 ")
            return False

    def add_product(self):
        if self.verify_seller():
            self.name = input("Enter product name: ")
            self.price = int(input("Enter price: "))
            self.description = input("Enter description: ")

            # Create a new list with the product details
            self.new_product = [self.name, self.price, self.description]
            User.seller_accounts[self.username].append(self.new_product)

        # printing details
        print(User.seller_accounts)
        print(User.buyer_accounts)


class Shoping_cart(Product, User):
    def __init__(self):
        super().__init__()
        self.fetch_seller_name = None
        pass

    def menu(self):
        satyam = True
        while satyam:
            print("""
                    1.create_account
                    2.verify_seller
                    3.verify_user
                    4.menu
                    5. add_product
                    6. buy_products
                    7. quiet
                    
                    """)
            opt = int(input("Enter option :"))
            match opt:
                case 1:
                    self.create_account()
                case 2:
                    self.verify_seller()
                case 3:
                    self.verify_user()
                case 4:
                    self.menu()
                case 5:
                    self.add_product()
                case 6:
                    self.buy_products()
                case _:
                    satyam = False

    def verify_user(self):
        print("USER VERIFICATION 🔐")
        self.username = input("Enter your  username :")
        self.password = input("Enter your user password :")

        if (self.username in User.buyer_accounts) and User.buyer_accounts[self.username][0][0] == self.password:
            print(self.username, "Loging Success full 😃")
            return
        else:
            print("Sale chor User🔫 ")

    def buy_products(self):
        self.fetch_seller_name = User.seller_accounts[self.username][1]
        self.verify_user()
        for i in self.fetch_seller_name:
            print(i)


obj = Shoping_cart()
obj.menu()
