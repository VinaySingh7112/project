import random
from stage import stages
from wordlist import word_list



print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                  ''')






word = random.choice(word_list)
# print(word)
display = []
for i in range(len(word)):
  display.append('_')
for i in range(0,len(word),2):
  letter = word[i]
  display[i] = letter
print(display)
game = True
live = 6

while game:
  player_choice = input("guess the letter: ").lower()

  for position in range(len(word)):
    letter = word[position]
    if player_choice == letter:
      display[position] = letter
  if "_" not in display:
    game = False
    print('YOU Won!')
  
  if player_choice not in word:
    print(stages[live])
    live-=1
    if live < 0:
      game =False
      print('YOU lose')
      print(word)

   
  print(display)


