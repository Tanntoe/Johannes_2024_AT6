import UserInputValidator_program as uiv

validation1 = uiv.UserInputValidator(["72", "cake", "-25", "3000"])
print(validation1.validate_positive_integers())

validation2 = uiv.UserInputValidator(["66", "pizza", "-1", "1337"])
print(validation2.validate_positive_integers())

#Did not follow the instructions well enough and called the initiations in the previous commit. I will instead commit this comment and
#a new instance.

validation3 = uiv.UserInputValidator(["1", "ring", "2", "rule", "them", ":-1"])
print(validation3.validate_positive_integers())