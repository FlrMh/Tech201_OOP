# Methods

# Methods in a class are extremely similar to functions.

class MethodExamples:
#
#     # this_can_be_accessed_easily = "Hi, I am easily found!"
#
#     def __init__(self):
#         self.this_can_be_accessed_easily = "Hi, I am easily found!"
#
#
# x = MethodExamples() # an object that is an instance of the class
# print(x.this_can_be_accessed_easily) # prints "Hi, I am easily found!"
# #
# x.this_can_be_accessed_easily = "I have been changed!"
# print(x.this_can_be_accessed_easily) # prints "I have been changed!" ; easy to overwrite

# Private and Public - in other languages.

# Explanation of what python is doing while using innit (to be written from notes):

    def __init__(self):
        self.this_can_be_accessed_easily = "Hi, here I am easily found!"

    def get_this_can_be_accessed_easily(self):
        return self.this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self, value_to_be_set):
        self.this_can_be_accessed_easily = value_to_be_set


x = MethodExamples() # an object that is an instance of the class
print(x.this_can_be_accessed_easily) # prints "Hi, I am easily found!"
#
x.set_this_can_be_accessed_easily = ("I have been changed!")
print(x.this_can_be_accessed_easily) # prints "I have been changed!" ; easy to overwrite
# Calling a clas method = using __ instead of _