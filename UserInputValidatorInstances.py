import UserInputValidator_program as uiv

validation1 = uiv.UserInputValidator(["72", "cake", "-25", "3000"])
print(validation1.validate_positive_integers())

validation2 = uiv.UserInputValidator(["66", "pizza", "-1", "1337"])
print(validation2.validate_positive_integers())