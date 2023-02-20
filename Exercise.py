class Person:
    def _init__(self, name, address, telephonenum):
        self.__name = name
        self.__address = address
        self.__telephonenum = telephonenum

    # method print_person that would display all attributes of the class
    def print_person(self):
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print(f"Telephone Number: {self.__telephonenum}")


class Customer(Person):
    def __init__(self, name, address, telephonenum, customer_number, mailing_list):
        super().__init__(name, address, telephonenum)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def print_person(self):
        return super().print_person()
