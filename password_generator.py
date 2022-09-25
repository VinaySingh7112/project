import random



letters=['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['1','2','3','4','5','6','7','8','9','0']
specal_carector=['@','#','$','%','^','&','*']

letter_choice = int(input('how much letter you want: '))
number_choice = int(input('how much number: '))
specal_carector_choice = int(input('how much special charector: '))

total_letter = ''
for _ in range(letter_choice):
    l = letters[random.randint(0,25)]
    total_letter+=l


total1=''
for a in range(number_choice):
    n=number[random.randint(0,9)]
    total1+=n


total2=''
for b in range (specal_carector_choice):
    s=specal_carector[random.randint(0,6)]
    total2+=s

generator_pass = total1+total2+total_letter

pass_list = []
for password in generator_pass:
    pass_list.append(password)

random.shuffle(pass_list)

generator_pass = ''
for pwd  in pass_list:
    generator_pass+=pwd


print(f"your password is {generator_pass}")
