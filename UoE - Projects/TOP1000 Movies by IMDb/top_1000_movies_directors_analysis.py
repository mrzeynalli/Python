# Chebyshev’s Theorem
# At least (1-1/k^2) of all observations are within k standard deviation (except k=1)
import math


def k_finder():

    percent = float(input('What percent are you looking for?\n'))
    ratio_of_p = percent / 100
    k = math.sqrt(1 / (1-ratio_of_p))

    print(f"\nThe {percent}% of observations lie within {round(k)} standard deviations of the distribution")


def Poisson_probs_finder():
    lambda_value = int(input("How many events happen within a time interval?\nYour input: "))
    x_value = int(input("\nHow many events do you want to calculate the probability of?\nYour input: "))

    #checks if the input value for lambda is intereger
    if not isinstance(lambda_value,int):
        print("Wrong input. Please, put in integers.")

    # checks if the input value for X is intereger
    elif not isinstance(x_value,int):
        print("Wrong input. Please, put in integers")


    else:
        # Poisson distribution formula
        prob = ( (math.e ** (-lambda_value)) * (lambda_value ** x_value) ) / math.factorial(x_value)

        # Prints the result
        print(f"\nThe probability of getting {x_value} events in a time interval, given that an average of {lambda_value} "
              f"events happens, is {prob}.")

Poisson_probs_finder()