# A function that prints the sum of the digits of the numbers in a given range
def digits_sum_of_range(x, y):  # the main function

    digits_list = []
    sum_of_digits = 0

    # Below is an intra-function that appends the list named 'digits_list' with the digits of all integers from num1 to
    # num2
    def digits_list_of_range(num1, num2):
        for i in range(num1, num2 + 1):  # num is added 1 to include the ending number when the main function is called
            for digit in str(i):  # converted the int to str to add to the list
                digits_list.append(str(digit))  # appends the above created list variable

    digits_list_of_range(x, y)  # this automatically calles the above created intra function with the specified numbers
    for unit in digits_list:
        sum_of_digits += int(unit)  # converted the initial integers back to int format
    print("Sum of the digits of the numbers between " + str(x) + " and " + str(y) + " is " + str(sum_of_digits))


digits_sum_of_range(1, 1000)  # insert the numbers you desire and enjoy!
