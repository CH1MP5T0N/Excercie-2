edge1 = eval(input("Enter the length of edge1: "))
edge2 = eval(input("Enter the length of edge2: "))
edge3 = eval(input("Enter the length of edge3: "))
perimeter = edge1 + edge2 + edge3
if edge1 + edge2 >= edge3 and edge2 + edge3 >= edge1 and edge3 + edge1 >= edge2:
    print(f"The perimeter is {perimeter}")
else: print("The input is invalid")