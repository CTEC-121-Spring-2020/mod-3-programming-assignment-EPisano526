# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Esther Pisano


def shippingCost(orderSubTotal):
    shippingCost = 2.99
    # enter code here to test for free
    if orderSubTotal >= 10:
        shippingCost = 0

    return shippingCost


def unitTest():
    print("Shipping cost if subtotal < 10.00:\n", shippingCost(5.99))
    print("Shipping cost if subtotal = 10.00:\n", shippingCost(10.00))
    print("Shipping cost if subtotal > 10.00:\n", shippingCost(11.99))


if __name__ == "__main__":
    unitTest()
