import time
Name=input("Enter your Name : ")
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
if(hour>=5 and hour<12):
    print("Good Morning",Name,"🌅")
elif(hour>=12 and hour<17):
    print("Good Afternoon",Name,"🕑")
elif(hour>=17 and hour<21):
    print("Good Evening",Name,"🌇")
else:
    print("Good Night",Name,"🌃")
