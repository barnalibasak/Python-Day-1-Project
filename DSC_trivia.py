print("        WELCOME TO DSC Trivia!!!")
res = input('   Are you ready to play (yeah / nope): ') 
ans=''
point=0

if res.lower() == 'yeah' :
    ans = input("1. What is full from of DSC?\n")
    if ans.lower() == "developer student club":
        print("         You are correct !!")
        point +=1
    else:
        print("         Sorry! You are incorrect.")

    ans = input("2. DSC is a ____ community.\n")
    if ans.lower() == "technical":
        print("         You are correct !!")
        point +=1
    else:
        print("         Sorry! You are incorrect.")

    ans = input("3.Who heads a DSC community ?\n")
    if ans.lower() == "dsc lead":
        print("         You are correct !!")
        point +=1
    else:
        print("         Sorry! You are incorrect.")

    ans = input("4. Are you enjoying the DSC SIT community?\n")
    if ans.lower() == "yes":
        print("         You are correct !!")
        point +=1
    else:
        print("         Sorry! You are incorrect.")

    print(" Thanks a lot for taking DSC trivia!!")
    print("    You have got: ",point,"POINTS!!")
    print("              Well done!! :)")
    print(" Have a great experiences at DSC SIT.")
else:
    print("       Oho! We can play it next time :)")
    print("     Have a great experiences at DSC SIT.")    