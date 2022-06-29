import random

import time

jackpot = 10

money = 200

print ("Hello and welcome to jacobs casino!")
time.sleep(0.8)

print ("   Today you will be playing the classic slot machine")
time.sleep(0.5)

print ("   I will give you a strating ballence of £200")
time.sleep(0.5)

print ("   It is £10 pound to play\n")
time.sleep(3)

play = input("Would you like to play [Y/N] (make sure its lower case)\n")

if play == "y" or play == "Y" or play == "yes" or play == "YES" or play == "yea" or play == "YEA":
  print ("lets get started then !\n")
  time.sleep(0.5)


elif play == "1905":
  print ("Hello Master Cook\n")
  time.sleep(1)
  cook = int(input("How much money would you like to take out of your bank account ?\n"))
  money = money +int(cook)
  print("money = £" + str(money)+"\n")


else:
  print ("Hopefully we can play another time then.")
  time.sleep(0.5)
  exit()


while money >= 10 :
  
  input("Press enter to roll\n")


  money = money -10


  jackpot = jackpot +10


  n1 = random.randint(1,7)
  n2 = random.randint(1,7)
  n3 = random.randint(1,7)


  print ("    _______   ")
  print (" __/JACKPOT\__")
  print ("|  _________  |")
  print ("| |_________| | /\ ")
  print ("|=============| ||")
  print ("| {"+str(n1)+"} "+"{"+str(n2)+"} "+"{"+str(n3) + "} |"+" ||")
  print ("|=============|_||")
  print ("| /  SLOT!  \ |__|")
  print ("| \ MACHINE / |")
  print ("|  _________  |")
  print ("|_|         |_|")
  print("_____________________\n")
  time.sleep(2)


  if n1==1 and n2==1 and n3==1:
    print("Well done you won £250 \n")
    money = money +250


  elif n1==2 and n2==2 and n3==2:
    print("Well done you won £250 \n")
    money = money +250


  elif n1==3 and n2==3 and n3==3:
    print("Well done you won £250 \n")
    money = money +250


  elif n1==4 and n2==4 and n3==4:
    print("Well done you won £250 \n")
    money = money +250


  elif n1==5 and n2==5 and n3==5:
    print("Well done you won £250 \n")
    money = money +250


  elif n1==6 and n2==6 and n3==6:
    print("Well done you won £250 \n")
    money = money +250


  elif n2 == (n1+1) and n3 ==(n2+1):
    # 123 234 345 456
    print ("Well done you won £200 \n")
    money = money +200


  elif n2 == (n1-1) and n3 == (n2-2):
    # 654 543 432 321
    print ("Well done you won £100 \n")
    money = money +100


  elif n1 == n2 or n1 == n3 or n2 == n3:
    # 112 113 114 226 661 ETC
    chance = random.randint (1,5)
    if chance == 1:
      print ("Well done its your lucky day you won 500 from a 1/5 chance \n ")
      money = money +500
    else:
      print ("You didnt win money from the 1/5 chance for having 2 of the same numebers! \n")


  elif n1 ==7 and n2 ==7 and n3 ==7:
    print ("!!!\*JACOBPOT*/!!! that means you win £" + str(jackpot)+"\n")
    money = money + jackpot
    print ("this means you have a gran total of £" +str(money+"\n"))


  elif n1 ==6 and n2 ==4 and n3 ==5:
    print ("!!!\*JACOBPOT*/!!! that means you win £" + str(jackpot)+"\n")
    money = money + jackpot
    print ("this means you have a gran total of £" +str(money+"\n"))



  print("money = £" + str(money)+"\n")
  print("Jackpot = £" + str(jackpot) + "\n")
  if money == 0:
    print ("GAME OVER")
    print("would you like to play again, if so prees run !\n")
    exit()
