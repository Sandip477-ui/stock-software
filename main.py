from produck import produck


option_text = """"
what do you want to do ?
1. add produck
2. view all produck
3. view produck with id
"""
option = int(input(option_text))
if option == 1:

    p = produck(id=0,name="", qty=0, price=0)
    p.id = int(input(f'enter produck  id: '))
    p.name= input(f"enter your produck  name: ")
    p. qty = int(input(f"enter your produck qty: "))
    p.price = float(input(f"enter your produck  price:"))

    f= open("produck.csv",'a')
    f.write(f"{p.id},{p.name},{p.qty},{p.price}\n")
    f.close()
    print(" produck added scuccessfully")
elif option ==2:
    f = open("produck.csv",'r')
    print("All producks are: \n------------------")
    print(f.read())
    print("----------------------")

