class Search:
    max_num = 0.
    min_num = 0.
    search_num = 0.
    is_integer = True

    def __init__(self):
        pass

    def input_max_and_min(self):
        self.max_num = raw_input("Enter max number: ")
        self.min_num = raw_input("Enter min number: ")
        self.change_type_of_numbers()

    def integer_or_decimal(self):
        decision = raw_input("Integer or Decimal values [i/d]?: ")
        if decision == 'i':
            self.is_integer = True
            self.change_type_of_numbers()
        else:
            self.is_integer = False
            self.change_type_of_numbers()

    def change_type_of_numbers(self):
        if self.is_integer:
            self.max_num = int(self.max_num)
            self.min_num = int(self.min_num)
            self.search_num = int(self.search_num)
        else:
            self.max_num = float(self.max_num)
            self.min_num = float(self.min_num)
            self.search_num = float(self.search_num)

    def define_search_num(self):
        self.search_num = (self.max_num - self.min_num)/2 + self.min_num

    def search_upper(self):
        self.min_num = self.search_num
        self.define_search_num()

    def search_lower(self):
        self.max_num = self.search_num
        self.define_search_num()

    def get_search_num(self):
        return self.search_num

    def ask_where_to_search(self, choice):
        if choice == 'u':
            self.search_upper()
        else:
            self.search_lower()




