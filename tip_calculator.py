print("welcome to the tip calculator")
total_bill=int(input("what is your total bill   "))
tip_parsent=int(input("what percent tip  "))
how_many=int(input("how many people  "))
tip_total = total_bill*tip_parsent/100
bill_person =  (total_bill+tip_total) / how_many
print(f"each person will pay {bill_person}") 