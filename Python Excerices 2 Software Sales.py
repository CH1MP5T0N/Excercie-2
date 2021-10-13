packages = eval(input("Enter the number of packages purchased: "))
if packages < 10:
    print("Discount Amount @ 0%: $ 0.00")
    print(f"Total Amount: $ {packages*99:.2f}")
if 10 <= packages <= 19:
    print(f"Discount Amount @ 10%: $ {(packages*99)*10/100:.2f}")
    print(f"Total Amount: $ {(packages*99)-(packages*99)*10/100:.2f}")
if 20 <= packages <= 49:
    print(f"Discount Amount @ 20%: $ {(packages*99)*20/100:.2f}")
    print(f"Total Amount: $ {(packages*99)-(packages*99)*20/100:.2f}")
if 50 <= packages <= 99:
    print(f"Discount Amount @ 30%: $ {(package*99)*30/100:.2f}")
    print(f"Total Amount: $ {(packages*99)-(packages*99)*30/100:.2f}")
if packages >= 100:
    print(f"Discount Amount @ 40%: $ {(packages*99)*40/100:.2f}")
    print(f"Total Amount: $ {(packagese*99)-(packages*99)*40/100:.2f}")