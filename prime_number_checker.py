def prime_checker(number):
    is_prime=True
    for i in range(2,number):
      if number % i==0:
          is_prime=False
    if is_prime:  
      print("it's a prime numeber")
    else:
        print("It,s a not prime numeber")
        
n=int(input("check this number :-"))
prime_checker(n)