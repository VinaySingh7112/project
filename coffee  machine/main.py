from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine=MoneyMachine()
money_machine.report()
menu=Menu()
 
is_on=True
while is_on:
    options=menu.get_items() 
    choice=input(f"What word you like?({options}):")
    if  