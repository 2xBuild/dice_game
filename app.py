import data_parser as dp
import func 
import random 



welcome_text = "Welcome to siu-gamble-field. Let's play dice and multiply your money."
print(welcome_text)
ans = input('Can we start ? (yes/no)')

user_session = None


if ans.lower() == "yes":
    
    username = input("what's your username? if you are new , you can create a unique username here.")
    if func.checkUser(dp.users,username):
        # that means user is registered
        password = input("Enter your password.")
        if func.checkPassw(dp.users, username, password):
            print(f"Welcome {username} to siu-gamble-field")
            user_session = username
            
            
        else:
            print("Invalid password. Please try again.")
            exit()
        
        
    else:
        # user is new let's register
        passw = input("Looks like you are new here. Please enter your new password..(passwords are case-sensitive )")
        dp.users.append({"username": username, "password": passw, "balance": 100}) #100 usd is welcome bonus
        if dp.save_users():
            print("Welcome", username, "You have 100 USD as welcome bonus.")
            user_session = username
        else:
            print("Failed to register. Please try again.")
        
        

    
elif ans.lower() == "no":
    print("Okay, see you later.")
    exit()
else:
    print("Invalid answer. It should be yes or no.")
    
    


if user_session: #we can start our game here once user login succesfully
    
    cmds = """
1. balance -  to check your balance
2. play {amount} {your_bet} { runs - optional} - . example = play 50 3 { you are playing bet of 50 usd on 3 dice number ( out of 1,2,3,4,5,6)} [ put runs if you want multiple bets in one command. ]
3. exit - to end game.
4. depsoit {amount} - add fund yourself.

"""
    msg = f"""
    
Here are some commands to start with {cmds}
"""

    print(msg)


    while True:
        cmd = input("Enter....")
        if cmd.split(" ")[0] == "balance":
            bal = func.checkBalance(dp.users,user_session)
            if bal :
                print(f"Balance: {bal} ")
            else:
                print("Error: Couldn't find your balance.")
                
        elif cmd.split(" ")[0] == "play":
            if len(cmd.split(" ")) == 4:
                multi_run = cmd.split(" ")[3]
            elif len(cmd.split(" ")) < 3:
                print("Error: Not enough arguments in play command. example = play 50 3 { you are playing bet of 50 usd on 3 dice number ( out of 1,2,3,4,5,6)}")
                continue
            else:
                multi_run = "1"
                
                
            amt = cmd.split(" ")[1]
            ChosenNumber = cmd.split(" ")[2]
            
            
            
            #  check if user entered int is both field + user has enough balance to play bet
            try:
                amt = int(amt)
                ChosenNumber = int(ChosenNumber)
                multi_run = int(multi_run)
                
            except ValueError:
                print("Error: Amount and your_bet should be a number.")
                continue
            
            
            
            while multi_run > 0:
                multi_run -= 1
                
                userBal = func.checkBalance(dp.users,user_session)

                if userBal < amt:
                    print("Error: You don't have enough balance to play this bet.")
                    continue
                else: 
                    updatedBalance = userBal - amt
                    WinningNumber = random.randint(1,6)
                    if ChosenNumber == WinningNumber:
                        print(f":) Congrats!! You won it. 6x is here for you. your {amt} turned to {amt*6}")
                        updatedBalance = updatedBalance + amt*6
                        print(f"Your bet:{amt} \nYour choice:{ChosenNumber} \nDice Result: {WinningNumber} \nLast Balance: {userBal}\nCurrent Balance:{updatedBalance}")
                        res = func.updateBalance(dp.users,user_session ,updatedBalance)
                        if not res:
                            print("Error: Couldn't update your balance.")
                            continue
                        
                    else:
                        updatedBalance = userBal-amt
                        print(f":( Sorry!! You lost it. Your bet:{amt}\nYour choice:{ChosenNumber} \nDice Result: {WinningNumber} \nLast Balance: {userBal}\nCurrent Balance:{updatedBalance}")
                        res = func.updateBalance(dp.users,user_session, updatedBalance)
                        if not res:
                            print("Error: Couldn't update your balance.")
                            continue
            
                    
        elif cmd.split(" ")[0] == "exit":
            exit()
        
        elif cmd.split(" ")[0] == "deposit":
            fund = cmd.split(" ")[1]
            try:
                fund = int(fund)
                updatedBalance = func.checkBalance(dp.users,user_session) + fund
                res = func.updateBalance(dp.users,user_session, updatedBalance)
                if res:
                    print(f"Your new balance is {updatedBalance}")
            except ValueError:
                print("Error: Amount should be a number.")
                continue
            
            
           
        else:
            print(f"Command is not recognized. Please try again. Here are some valid commands {cmds} ")
            

    
    
