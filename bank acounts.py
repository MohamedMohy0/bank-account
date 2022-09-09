from turtle import up


order1=input("are you already have an account?:")
if order1 =="yes":
    accountname=input("enter the name of the account:")
    password=input("enter the password:")
    def update():
        file = open(accountname + ".txt", "w")
        file.truncate()
        file.write("the account names is:"+"\n"+accountname+("\n")+"the password is:"+"\n"+password)
        file.write("\n"+"the money in this account is :"+"\n"+str(money))
        file.close()
        file = open(accountname + ".txt", "r")
        print(file.read())
        file.close()

    try:

        file=open(accountname+".txt","r")
        n=0
        for line in file.readlines():
            n=n+1
            if n==4:
                x=line
            elif n==6:
                money=line
        if (str(password)+"\n")==x:
            file = open(accountname + ".txt", "r")
            print(file.read())
            file.close()
            order2=input("are you want to deposit or draw?:")
            if order2=="draw":
                rate=int(input("enter the money you want to draw:"))
                money=int(money)-rate
                if money>0:
                    update()
                else :
                    print("sorry you dont have enogh money in the account")
            elif order2=="deposit":
                rate=int(input("enter the money you want to draw:"))
                money=int(money)+rate
                update()
            else :
                print("wrong input")
        else:
            print("wrong password")
            file.close()
    except FileNotFoundError:
        print("there is no account has this name")
    except ValueError:
        print("wrong input")


elif order1 == "no":
    try:
        accountname=input("enter the new account name:")
        password=input("enter the password:")
        money=int(input("enter the money you want to deposit:"))
        file = open(accountname + ".txt", "w")
        file.write("the account names is:"+"\n"+accountname+("\n")+"the password is:"+"\n"+password)
        file.write("\n"+"the money in this account is :"+"\n"+str(money))
        file.close()
    except ValueError:
        print("wrong input")
else :
    print("wrong input")