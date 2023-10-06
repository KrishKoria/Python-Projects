def count_local_variables():
    a = 10
    b = "Hello"
    c = [1, 2, 3]
    d = {1: 2, 3: 4}
    local_variables = locals()
    local_variables_count = len(local_variables) - 1
    return local_variables_count


print(f"The number of local variables is :{count_local_variables()}")
