print("Welcome to my computer quiz!")

playing = input("Want to play? : ")
score = 0
if playing != "yes":
  quit()

print("okay! let's gooooo..")

#CPU
answer = input("What does CPU stands for? :")
if answer.lower() == "central processing unit":
  print('correct!')
  score += 1
else:
  print('incorrect!!!')

#GPU
answer = input("What does GPU stands for? :")
if answer.lower() == "general processing unit":
  print('correct!')
  score+=1
else:
  print('incorrect!!!')

 #RAM 
answer = input("What does RAM stands for? :")
if answer.lower() == "random access memory":
  print('correct!')
  score += 1
else:
  print('incorrect!!!')

#PSU
answer = input("what does PSU stands for? : ")
if answer.lower() == "power supply unit":
  print('correct!')
  score += 1
else:
  print('incorrect!!!')

#displaying score
print("you got ",score," questions correct :) ")
print("that is ", (score/4)*100 , " ,keep it up ;")





















