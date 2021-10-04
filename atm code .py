card=(input("enter your card"))
if card=="credit card"or "debit card":
    print("credit card")
    atm=(input("enter your language"))
    if atm=="english" or "marathi":
        print("english")
        atm=(input("enter your pin"))
        if atm=="1234" or "4567" or "8900":
            print("1234")
            atm=(input("enter your trasaction"))
            if atm=="cash withdrawn":
                print("withdraw")
                atm=(input("enter your acconut type"))
                if atm=="current account" or "saving account":
                    print("current account")
                    atm=(input("enter check your account amount"))
                    if atm=="yes":
                        print("check the amount")
                        atm=(input("enter your amount"))
                        if atm=="20000" or "40000" or "50000":
                            print("20000")
                            atm=(input("your transaction is sucssful"))
                            if atm=="you want remove your card":
                                print("yes")
                                atm=(input("do you want print recipt"))
                                if atm=="yes" or "no":
                                    print("yes")
                                else:
                                    print("not")
                            else:
                                print("not")
                        else:
                            print("not")
                    else:
                        print("not")
                else:
                    print("not")
            else:
                print("not")
        else:
            print("not")
    else:
        print("not")
else:
    print("not")

                
                                    
                                











    
                    
                        
                        