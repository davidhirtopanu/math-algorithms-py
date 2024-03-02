#Specify values for the observed statistics
observed_stat_input = input("Write down the observed statistics: ")

observed_stat_arr_str = observed_stat_input.split()

observed_stat_arr = [float(x) for x in observed_stat_arr_str]
print("You have entered " + str(observed_stat_arr))

#Specify values for the expected
shud_ui_merj = False
invalid_columns = []

left_merge = -1
right_merge = -1
expected_stat_input = input("Write down the expected statistics: ")

expected_stat_arr_str = expected_stat_input.split()

expected_stat_arr = [float(x) for x in expected_stat_arr_str]
print("You have entered: " +str(expected_stat_arr))

exp_stat_length = len(expected_stat_arr)

for i in range(exp_stat_length):
    if expected_stat_arr[i] <= 5:
        invalid_columns.append(i)
        shud_ui_merj = True

midpoint = (exp_stat_length + 1) / 2

for i in range(len(invalid_columns)):
    if invalid_columns[i] > midpoint:
        if invalid_columns[i] > right_merge:
            right_merge = invalid_columns[i]
    elif invalid_columns[i] < midpoint:
        if left_merge == -1:
            left_merge = invalid_columns[i]
        else:
            if left_merge > invalid_columns[i]:
                left_merge = invalid_columns[i]

if shud_ui_merj:
    if right_merge != -1:
        merge_start = right_merge
        steps_back = 1
        column_value = expected_stat_arr[right_merge]
        while column_value <= 5:
            column_value = column_value + expected_stat_arr[right_merge+(steps_back*-1)]
            if column_value <= 5:
                merge_start -= 1
                steps_back += 1
        print("Steps back: " +str(steps_back))

        expected_stat_arr[right_merge + (steps_back*-1)] = column_value
        expected_stat_arr = expected_stat_arr[:right_merge + (steps_back*-1) + 1]

        print(expected_stat_arr)

        obs_length = len(observed_stat_arr)
        obs_total = 0
        for i in range(steps_back+1):
            obs_total += observed_stat_arr[(obs_length-1) + (i*-1)]

        observed_stat_arr[(obs_length-1) + (steps_back*-1)] = obs_total
        observed_stat_arr = observed_stat_arr[:obs_length + (steps_back * -1)]

        print("Obs arr: " + str(observed_stat_arr))

    if left_merge != -1:
        merge_start = left_merge
        steps_forward = 1
        column_value = expected_stat_arr[left_merge]
        while column_value <= 5:
            column_value = column_value + expected_stat_arr[left_merge+steps_forward]
            if column_value <= 5:
                merge_start -= 1
                steps_forward += 1
        print("Steps forward: " + str(steps_forward))

        expected_stat_arr[left_merge + steps_forward] = column_value
        expected_stat_arr = expected_stat_arr[left_merge + steps_forward:]

        obs_total = 0
        for i in range(steps_forward+1):
            obs_total += observed_stat_arr[i]

        observed_stat_arr[steps_forward] = obs_total
        observed_stat_arr = observed_stat_arr[steps_forward:]
        print("observed stat array: " + str(observed_stat_arr))


#print(invalid_columns)
#print(left_merge)
#print(right_merge)

#Specify the frequency
frequency = input("How many trials are there in total? ")


def calculate_chi_squared():
    total = 0
    for i in range(len(observed_stat_arr)):
        result = observed_stat_arr[i]**2 / expected_stat_arr[i]
        total += result

    chi_sq = total - float(frequency)
    print(chi_sq)



calculate_chi_squared()
