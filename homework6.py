

product=100
while True:
    demand= int(input("How much you want?:"))
    if product >= demand:
        print("Wait A Second I Will Give You The Product")
        product=product=demand
    else:
        print("I Can't Give You What You What")
        break