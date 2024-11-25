class UserInputValidator():

    def __init__(self, list_of_strings):
        self._list_of_strings = list_of_strings
        self._new_list = []
        self._message = ""

    def validate_positive_integers(self):
        for i in self._list_of_strings:
            if i.isdigit():
                self._new_list.append(i)
        return f"{self._new_list} \n{self.result()}"
    
    def result(self):
        if len(self._new_list) > 0:
            self._message = "The list has positive integers"
        else:
            self._message = "The list has no positive integers"
        
        return self._message
