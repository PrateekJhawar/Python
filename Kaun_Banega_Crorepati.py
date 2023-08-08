print("------------WELCOME TO KAUN BANEGA CROREPATI------------\n")
levels = [
  1000, 2000, 30000 ,5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,
  1250000, 2500000, 5000000, 10000000, 70000000
]
money = 0
questions=[
    # Question Number 1 -  ₹1,000/-
    [
    "In which programming language is the KBC game has been created? \nYour options are : ",
    "Javascript", "Python", "Java", "C++", 2
    ],

    # Question Number 2 - ₹2,000/-
    [
    "The International Literacy Day is observed on ? \nYour options are : ", 
     "Sep 8","Nov 28","May 2","Sep 22",1
     ],

    # Question Number 3- ₹3,000/-
    ["What is the name of the first artificial satellite launched into space? \nYour options are : ",
    "Sputnik 1", "Explorer 1", "Luna 1", "Pioneer 10", 1],

    # Question Number 4 - ₹5,000/-
    ["What is the name of the first computer to be mass-produced? \nYour options are : ", "ENIAC",
    "UNIVAC I", "IBM 1401", "IBM 360", 2],

    # Question Number 5 - ₹10,000/-
    [
    "What is the name of the first artificial intelligence to beat a human at a game? \nYour options are : ",
    "Deep Blue", "Watson", "AlphaGo", "GPT-3", 3 ],

    # Question Number 6 - ₹20,000/-
    ["The abbreviation fob stands for ? \nYour options are :",
     "Fellow of Britain","Free of Bargain","Free on Board","None of these",3],

    # Question Number 7 - ₹40,000/-
    [
    "Who painted the Mona Lisa? \nYour options are : ", 
    "Pablo Picasso", "Vincent van Gogh","Leonardo da Vinci", "Michelangelo", 3],

    # Question Number 8 - ₹80,000/-
    ["Which battle in 1757 marked the beginning of British occupation in India? \nYour options are : ",
     "Plassey","Assaye","Buxar","Cuddalore",1],

    # Question Number 9 - ₹1,60,000/-
    ["The songs of Raj Kapoors movie were always a super hit. One of the blockbuster Raj Kapoor films was the movie 'Bobby'. Can you identify the music director of this film? \nYour options are : ",
     "Adnan Sami","Anand Raj Anand","Anil Biswas","Laxmikant-Pyarelal",4],

    # Question Number 10 - ₹3,20,000/-
    ['Who famously said, "If I see someone laughing, then see! For 60 overs they should feel hell out there"? \nYour options are : '
     "Virat Kohli","Mahendra Singh Dhoni","Ricky Ponting ","Steve Waugh",1],

    # Question Number 11 - ₹6,40,000/-
    ["Who was the first Indian director of the Indian Institute of Science, Bangalore, the brainchild of Jamshedji Nusserwanji Tata? \nYour options are : ",
     "Dorabji Tata", "CV Raman", "Homi Jehangir Bhabha","Satish Dhawan",2],

    # Question Number 12 - ₹12,50,000/-
    ["After which historical or mythological figure did Sri Lanka name its first satellite? \nYour options are : ",
     "Kuber", "Buddha", "Vibhishana", "Ravana",4],

    # Question Number 13 - ₹25,00,000/-
    ["Who was the Indian bowler off whom Australian legend Don Bradman got a single to reach his 100th first class century? \nYour options are :",
     "Baqa Jilani", "Commandur Rangachari", "Gogumal Kishenchand","Kanwar Rai Singh",3],

    # Question Number 14 - ₹50,00,000/-
    ["Which of these states has had the most number of its governors become presidents of India? \nYour options are : ",
     "Rajasthan","Bihar","Punjab","Andhra Pradesh",2],

    # Question Number 15 - ₹1,00,00,000/-
    ["Which is the only bird with a digestive system that ferments vegetation as a bovine does, which enables it to eat leaves and buds exclusively? \nYour options are : ",
     "Shoebill stork","Hoatzin"," Shoveler","Galapagos",2],

    # Question Number 16 - ₹7,00,00,000/-
    ["Which of these is not one of the names of three of Akbar’s grandsons when they were briefly converted to Christianity after being handed over to Jesuit priests?\nYour options are : ",
    "Don Felipe", "Don Henrique", "Don Carlos", "Don Francisco",4],
]
# print(questions)
print(
  "Rules : \n \n 1) There are 20 questions \n\n 2) For each question you have 4 options out of which 1 is correct \n\n 3) There are 2 checkpoints one at 7th question and one at 14th question \n\n 4) If you want to quit the game in between you can quit by entering 0 . The amount you earned till last question will be your winning amount.\n\n"
)

input("Press enter to start the game ")
for i in range(0 , len(questions)):
  question=questions[i]
  print(f"\n\nQuestion :{i+1} for Rupees : {levels[i]} \n")
  print(f"{question[0]} \n")
  print(f"1) {question[1]}       2) {question[2]} ")
  print(f"3) {question[3]}       4) {question[4]} \n")
  ans=int(
    input(
      "Enter the correct option no. 1, 2, 3, 4 and press enter. Or to quit the game enter 0 : "
    ))
  if(ans==0):
    money=levels[i-1]
    break
  if(ans==question[5]):
    print(f"\n\nCongratulations ! Correct Answer , You have won rs. {levels[i]}")
    if(i == 5):
      money =  10000
    elif(i==10):
      money = 320000
  else:
    print(f"Wrong answer ! Your total winning amount is {money}.\n")
    break
print(f"You have taken the Home Money is {money}")
    