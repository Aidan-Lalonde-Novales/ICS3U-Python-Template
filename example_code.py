#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program ...

import constants


def main():
    # this function calculates ...

    # input
    diameter = float(input("Enter the diameter of your pizza (inches): "))

    # process
    sub_total = constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("Your pizza will cost ${0:,.2f}".format(total))
    print("\nDone.")


if __name__ == "__main__":
    main()
