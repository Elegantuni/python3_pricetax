#!/usr/bin/env python3

import sys
import math

def roundToTenths(data1):
    data1 = data1 * 100

    return math.floor(data1 + 0.5) / 100

price = 0.0
tax =  0.0
dollars_off = 0.0
the_new_price = 0.0
the_input = 0

while True:
    print("Enter 1 to calculate price and price off from tax and the final price")
    print("Enter 2 to calculate price off and final price from price and tax")
    print("Enter 3 to calculate price and tax percentage from price off and the final price")
    print("Enter 4 to calculate price off and tax from the price and final price")
    print("Enter 5 to calculate price and tax price added from tax and the final price")
    print("Enter 6 to calculate price added and final price from price and tax")
    print("Enter 7 to calculate price and tax percentage from price added and the final price")
    print("Enter 8 to calculate price added and tax from the price and final price")

    the_input = int(input(""))

    if the_input == 1:
        tax = float(input("Enter the tax percentage (ex: 50 for 50%): "))
        
        the_new_price = float(input("Enter the final price: "))

        price = -the_new_price / (tax/100 - 1)

        price = roundToTenths(price)

        dollars_off = price - the_new_price

        dollars_off = roundToTenths(dollars_off)

        print("The price is", price)

        print("The price off is", dollars_off)

        sys.exit(0)

    elif the_input == 2:
        price = float(input("Enter the price: "))

        tax = float(input("Enter the tax percentage (ex: 50 for 50%): "))

        dollars_off = price * (tax / 100)

        dollars_off = roundToTenths(dollars_off)

        the_new_price = price - dollars_off

        the_new_price = roundToTenths(the_new_price)

        print("The price off is", dollars_off)

        print("The final price is", the_new_price)

        sys.exit(0)
        
    elif the_input == 3:
        dollars_off = float(input("Enter the price off: "))

        the_new_price = float(input("Enter the final price: "))

        price = the_new_price + dollars_off

        price = roundToTenths(price)

        tax = dollars_off * 100 / price

        tax = roundToTenths(tax)

        print("The price is", price)

        print("The tax percentage is", tax)

        sys.exit(0)

    elif the_input == 4:
        price = float(input("Enter the price: "))

        the_new_price = float(input("Enter the final price: "))

        dollars_off = price - the_new_price

        dollars_off = roundToTenths(dollars_off)

        tax = dollars_off * 100 / price

        tax = roundToTenths(tax)

        print("The price off is", dollars_off)
        
        print("The tax percentage is", tax)

        sys.exit(0)

    elif the_input == 5:
        tax = float(input("Enter the tax percentage (ex: 50 for 50%): "))

        the_new_price = float(input("Enter the final price: "))

        price = the_new_price / (tax/100 + 1)

        price = roundToTenths(price)

        dollars_off = price * tax/100

        dollars_off = roundToTenths(dollars_off)

        while price + dollars_off > the_new_price:
            price = price - 0.01
            dollars_off = price * tax/100
            dollars_off = roundToTenths(dollars_off)

        print("The price added is", dollars_off)

        print("The price is", price)

        sys.exit(0)

    elif the_input == 6:
        price = float(input("Enter the price: "))

        tax = float(input("Enter the tax percentage (ex: 50 for 50%): "))

        dollars_off = price * (tax / 100)

        dollars_off = roundToTenths(dollars_off)

        the_new_price = price + dollars_off

        the_new_price = roundToTenths(the_new_price)

        print("The price added is", dollars_off)

        print("The final price is", the_new_price)

        sys.exit(0)

    elif the_input == 7:
        dollars_off = float(input("Enter the price added: "))

        the_new_price = float(input("Tne the final price: "))

        price = the_new_price - dollars_off

        price = roundToTenths(price)

        tax = dollars_off * 100 / price

        tax = roundToTenths(tax)

        print("The price is", price)

        print("The tax percentage is", tax)

        sys.exit(0)

    elif the_input == 8:
        price = float(input("Enter the price: "))

        the_new_price = float(input("Enter the final price: "))

        dollars_off = the_new_price - price

        dollars_off = roundToTenths(dollars_off)

        tax = dollars_off * 100 / price

        tax = roundToTenths(tax)

        print("The price added is", dollars_off)

        print("The tax percentage is", tax)

        sys.exit(0)

