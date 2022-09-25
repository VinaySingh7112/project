print('''
                 '
                  )                    `
                 /(l                   /)
                (  \                  / (
                ) * )                ( , )
                 \#/                  \#'
               .-"#'-.             .-"#"=,
            (  |"-.='|            '|"-,-"|
            )\ |     |  ,        /(|     | /(         ,
   (       /  )|     | (\       (  \     | ) )       ((
   )\     (   (|     | ) )      ) , )    |/ (        ) \
  /  )     ) . )     |/  (     ( # (     ( , )      /   )
 ( * (      \#/|     (`# )      `#/|     |`#/      (  '(
  \#/     .-"#'-.   .-"#'-,   .-"#'-.   .-=#"-;     `#/
.-"#'-.   |"=,-"|   |"-.-"|)  1"-.-"|   |"-.-"|   ,-"#"-.
|"-.-"|   |  !  |   |     |   |     |   |     !   |"-.-"|
|     |   |     |._,|     |   |     |._,|     a   |     |
|     |   |     |   |     |   |     |   |     p   |     |
|     |   |     |   |     |   |     |   |     x   |     |
'-._,-'   '-._,-'   '-._,-'   '-._,-'   '-._,-"   '-._,-''')


print("welcome to treasure island your mission is to find the treasure  ")
candition=input("left or right   ").lower()
if candition =='right':
  print("fall into a hole game over  ")
elif candition== 'left':
  candition_1=input("swim or wait  ").lower()
  if candition_1== 'swim':
    print("attacked by trout game over ")
  elif candition_1=="wait":
    candition_2=input("which door ?  red  blue and yellow   ").lower()
    if candition_2=='red':
      print("burned by fire game over ")
    elif candition_2=='blue':
      print("eaten by beasts game over")
    elif candition_2=="yellow":
      print("you win")
    else:
      print(" opse game over ")  
  else:
    print(" opse game over ")  
else:
  print(" opse game over ")  
