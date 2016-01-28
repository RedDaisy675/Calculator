
class Calculator():
    def __init__(self, number_type):
        self.total = 0
        self.last_total = 0
        #to allow further extension, seperate out the operations portion
        # of the calculator class
        self.operation = Operation(number_type)

    def add(self, *arg):
        return self.operation.perform_operation(self, "add", arg)

    def subtract(self, *arg):
        return self.operation.perform_operation(self, "subtract", arg)

    def multiply(self, *arg):
        return self.operation.perform_operation(self, "multiply", arg)

    def divide(self, *arg):
        return self.operation.perform_operation(self, "divide", arg)
