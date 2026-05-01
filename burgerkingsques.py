# burger king question
# Menu:

# 1. Whopper Burger - ₹150
# 2. Crispy Veg - ₹100 
# 3. Chicken Wings - ₹120 
# Enter the item number (1/2/3): 1
# Enter quantity: 2 
# Do you have a coupon code? (yes/no): yes
# Enter your coupon code: KING50 
# Applying coupon...
# Original Price: ₹300 
# Discount Applied: 50% 
# Final Price: ₹150 
# Thanks for ordering at Burger King! 🍟

print("1 Whopper Burger = ₹150")
print("2 Crispy Veg = ₹100")
print("3 Chicken Wings = ₹120")
order=int(input("enter the item number(1/2/3)"))
if order==1:
    price=150
    order_name=("whopper burger")
elif order==2:
    price=100
    order_name=("crispy veg")
elif order==3:
    price=120
    order_name=("chicken wings")
else:
    print("nothing added")
quantity=int(input("enter the quantity: "))


total_price=price*quantity
print("do you have a coupon code? (yes/no)")
coupon=input("(yes/no)").lower()
print("Applying coupon...")
print("original price:",total_price)
if coupon=="yes":
    coupon_code=(input("enter the coupon code"))
    if coupon_code==("kings50").lower():
        final_price=total_price*0.5
        print("discount applied 50%")
    elif coupon_code==("bk20").lower():
        final_price=total_price-20
        print("discount applied: ₹20")
else:
    final_price=total_price
    print("no discount")
print("final price:",total_price) 
print("Thanks for ordering at Burger King! 🍟")




# railway ticket question
# Requirements:

# 1. Ask the user for their name and age.
# 2. Ask them to choose a class:
# ⿡ First Class – ₹1500
# ⿢ Second Class – ₹1000
# ⿣ Sleeper Class – ₹500
# 3. If the passenger is under 5 years old, the ticket is free.
# 4. If the passenger is a senior citizen (60+), apply a 20% discount.
# 5. Ask if they want to add a meal:
# Yes – ₹200 extra
# No – No extra charge
# 6. Finally, print the passenger details and the final ticket price.

name=str(input("enter your name"))
age=int(input("enter your age"))
ticket=0
print("choose a class")
print(" 1 first class - ₹1500")
print("2 second class - ₹1000")
print("3 sleeper class - ₹500")
choice=int(input("enter your choice(1/2/3)"))

if choice==1:
    ticket=1500
elif choice==2:
    ticket=1000
elif choice==3:
    ticket=500


if age<5:
    ticket=0
if age>60:
    ticket=ticket*0.8

print("do you want add a meal (yes/no)?")
meal=input("(yes/no)").lower()
if meal=="yes":
    ticket+=200
elif meal=="no":
    print("no extra charges")

print("-----Ticket Summary-----")
print("passengers name",name)
print("passengers age",age)
print("class",choice)
print("meal added",meal)
print("final price",ticket)
print("Enjoy your journey! 🎉")
    
    
