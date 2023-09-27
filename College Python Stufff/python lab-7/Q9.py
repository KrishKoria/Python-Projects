def change_variable_value():
    variable = "initial value"
    print(variable)


global variable
variable = "final value"

change_variable_value()
print(variable)
