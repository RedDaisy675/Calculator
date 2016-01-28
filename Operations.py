class Operation():
    def __init__(self, number_type):
        #to allow for customization of answer accuracy. It can be modified or extended
        #to determine type based on the presense of a decimal point or computation
        #result
        self.number_type = number_type

    def convert_to_number(self, value):
        return int(value) if self.number_type == "int" else float(value)

    def perform_operation(self, instance, operation, arg):
        current_value = 0
        return_value = "Nothing has been computed yet :("
        for value in arg:
            return_value = ("One of the values entered (value '%s') is not a valid number, \
                        please enter numberical values only" % value)

            if operation == "multiply":
                try:
                    current_value = 1
                    current_value *= self.convert_to_number(value)
                except ValueError:
                    return return_value
 
            elif operation == "add":
                #divert "value" in the event that it is an entire expression (1+2) instead of
                #(1,2). Both are to be allowed. 
                if "+" not in value:
                    try:
                        current_value += self.convert_to_number(value)
                    except ValueError:
                        return return_value
                else:
                    return "Ran out of time :(. But this was a cool assignment!"
            elif operation == "divide":
                return "Currently not implemented"
            elif operation == "subtract":
                return "Currently not implemented"
            elif operation == "custom":
                return "Please try a different operation, \
                    there are no custom operations defined yet! :)"
        return current_value

    def subtract(self, *arg):
        pass

    def multiply(self, *arg):
        pass

    #a function that would evaluate the values if the numbers were passed in as
    #an entire expression
    def determine_order(self, expression):
        pass
    
    def remove_parens(self, expression):
        pass

    def retrieve_last_result(self):
        return self.last_total
