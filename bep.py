import math
import numpy as np


def insert():
    while True:
        try:
            p = float(
                input(f"{'Insert Price(ea)':<25} ---> ").replace(" ", ""))
            vc = float(
                input(f"{'Insert Variable Cost(ea)':<25} ---> ").replace(" ", ""))
            fc = float(
                input(f"{'Insert Fixed Cost':<25} ---> ").replace(" ", ""))
            print("-" * 145)

            break
        except ValueError:
            print("-" * 145)
            print(f"{'Input Type Error':<25} ---> Insert Int or Float")
            print("-" * 145)

    return p, vc, fc


def showValues(p, vc, fc):
    print(f"|{'Price(ea)':^46}| |{'Variable Cost(ea)':^45}| |{'Fixed Cost':^46}|")
    print(f"|{p:^46,.0f}| |{vc:^45,.0f}| |{fc:^46,.0f}|")
    print("-" * 145)

    while True:
        check_values = input(f"{'Correct? (y/n)':<25} ---> ")

        if check_values == "y" or check_values == "n":
            break

    return check_values


def calBep(p, vc, fc):
    margin = (1 - (vc / p)) * 100
    bep_quantity = math.ceil((fc / (1 - (vc / p))) / p)
    bep_sales = p * bep_quantity

    return margin, bep_quantity, bep_sales


def getListBepQuantity(bep_quantity):
    lst = []

    for i in reversed(range(1, 11)):
        lst.append(math.ceil(bep_quantity * (1 - 0.1 * i)))

    lst.append(bep_quantity)

    for i in range(1, 11):
        lst.append(math.ceil(bep_quantity * (1 + 0.1 * i)))

    return np.array(lst)


def mulList(lst, target):
    return np.array(lst * target)


def showChart(p, vc, fc, margin, bep_quantity, bep_sales):
    list_bep_quantity = getListBepQuantity(bep_quantity)
    list_sales = mulList(list_bep_quantity, p)
    list_vc = mulList(list_bep_quantity, vc)
    list_fc = np.empty(21)
    list_fc.fill(fc)
    list_tc = list_vc + list_fc
    list_earnings = list_sales - list_tc

    print("=" * 145)
    print(f"|{'BEP Chart':^143}|")
    print("=" * 145)
    print(f"|{'(Unit: Won)':>143}|")
    print("-" * 145)
    print(f"|{'Price(ea)':^22}| |{'Variable Cost(ea)':^21}| |{'Fixed Cost':^21}| |{'Margin(%)':^21}| |{'BEP Quantity':^21}| |{'BEP Sales':^22}|")
    print(f"|{p:^22,.0f}| |{vc:^21,.0f}| |{fc:^21,.0f}| |{margin:^21,.1f}| |{bep_quantity:^21,.0f}| |{bep_sales:^22,.0f}|")
    print("-" * 145)
    print(f"|{'No.':^5}| |{'Quantity':^20}| |{'Sales':^20}| |{'Variable Cost':^20}| |{'Fixed Cost':^20}| |{'Total Cost':^20}| |{'Earnings':^20}|")

    for i in range(len(list_bep_quantity)):
        if i == 10:
            print("-" * 145)

        print(
            f"|{i:^5}| |{list_bep_quantity[i]:>20,.0f}| |{list_sales[i]:>20,.0f}| |{list_vc[i]:>20,.0f}| |{list_fc[i]:>20,.0f}| |{list_tc[i]:>20,.0f}| |{list_earnings[i]:>20,.0f}|")

        if i == 10:
            print("-" * 145)

    print("=" * 145)


def main():
    while True:
        print(f"{'Version 1.1':>145}")
        print("=" * 145)
        print(f"|{'BEP Calculator':^143}|")
        print("=" * 145)

        while True:
            p, vc, fc = insert()
            check_values = showValues(p, vc, fc)

            if p == 0 or vc == 0 or fc == 0:
                print("-" * 145)
                print(f"{'Zero Division Error':<25} ---> Values cannot be 0")
                print("-" * 145)

                continue
            elif (1 - (vc / p)) == 0:
                print("-" * 145)
                print(
                    f"{'Zero Division Error':<25} ---> Price(ea) and Variable Cost(ea) cannot be same")
                print("-" * 145)

                continue

            if check_values == "y":
                break

            print("-" * 145)

        margin, bep_quantity, bep_sales = calBep(p, vc, fc)
        showChart(p, vc, fc, margin, bep_quantity, bep_sales)

        while True:
            check_out = input(f"{'Finish? (y/n)':<25} ---> ")

            if check_out == "y" or check_out == "n":
                break

        if check_out == "y":
            break


if __name__ == "__main__":
    main()
