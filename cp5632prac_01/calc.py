price = 0
num_items = int(input("Enter number of items :"))
for i in range(num_items):
    print("price of item:")
    price += float(input())
print("Total price for ", num_items,"item is $",price)