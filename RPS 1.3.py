import random 
r = random.randint(1,3) 

print("""
    ___           __     ___                      ____    _                   
   / _ \___  ____/ /__  / _ \___ ____  ___ ____  / __/___(_)__ ______  _______
  / , _/ _ \/ __/  '_/ / ___/ _ `/ _ \/ -_) __/ _\ \/ __/ (_-<(_-< _ \/ __(_-<
 /_/|_|\___/\__/_/\_\ /_/   \_,_/ .__/\__/_/   /___/\__/_/___/___|___/_/ /___/
                               /_/                                            
   Rock Paper Scissors © 
      By Cole Turner 
""") 

points = 0                     
print("   | SETTINGS |")
print("")
user = str(input("Username: "))  
if user == "EXIT":
    print("Game Exited")
    exit()
print("")
if user == "dev":
    points = 999

color = str(input("Change text color? ")) 
color = color.upper() 
if color == "BLUE":
    print("\033[0;34m ") 
elif color == "RED":
    print("\033[0;31m ") 
elif color == "GREEN":
    print("\033[0;32m ") 
elif color == "YELLOW":
    print("\033[0;33m ") 
elif color == "PURPLE":
    print("\033[0;35m ") 
elif color == "CYAN":
    print("\033[0;36m ") 
elif color == "BLACK":
    print("\033[0;30m ")
elif color == "EXIT":
    print("Game Exited")
    exit()
else:
    print("No color change.")
    print("")

border = str(input("Do you want borders? "))
border = border.upper()
if border == "NO":
    print("Ok, No Borders Selected") 
    print("")
elif border == "YES":
    print("") 
    print("------------------------------")
elif border == "EXIT":
    print("Game Exited")
    exit()
else:
    print("Ok, No Borders Selected")
    print("")
print("Input 'help' to view various game functions.") 
print("")
wins = 0 
losses = 0 
ties = 0 
effect = 0
expiry = 0 
total_points = 0 
gamble = 0 
garage = 0
while points != 99999: 
    import random 
    r = random.randint(1,3)
    move = str(input("Your Move?: ")) 
    move = move.upper()
    
    if move == "DEV":
        points = 999 
        print("Developer Mode Enabled")
    
    if move == "R":
        move = "ROCK"
    if move == "S":
        move = "SCISSORS" 
    if move == "P":
        move = "PAPER"
    
    if r == 1:
        comp_move = "Rock" 
    elif r == 2:
        comp_move = "Paper" 
    elif r == 3:
        comp_move = "Scissors" 
    comp_move = comp_move.upper() 
    if move == "ROCK" or move == "PAPER" or move == "SCISSORS":
        print("Computer Move: " + comp_move)
    
    if move == "EXIT":
        print("")
        print("Game Exited")
        break
    if move == "ROCK" and comp_move == "ROCK":          # T
        ties = ties + 1
        print("Tie")                                        
    elif move == "ROCK" and comp_move == "PAPER":       # L
        losses = losses + 1
        points = points - 1
        print("You Lose") 
    elif move == "ROCK" and comp_move == "SCISSORS":    # W
        wins = wins + 1 
        points = points + 1 
        total_points = total_points + 1
        if effect == 2:
            points = points + 1 
            total_points = total_points + 1
        print("You Win")  
    elif move == "PAPER" and comp_move == "ROCK":       # W
        wins = wins + 1
        points = points + 1 
        total_points = total_points + 1
        if effect == 2:
            points = points + 1 
            total_points = total_points + 1
        print("You Win") 
    elif move == "PAPER" and comp_move == "PAPER":      # T
        ties = ties + 1
        print("Tie")  
    elif move == "PAPER" and comp_move == "SCISSORS":   # L
        losses = losses + 1
        points = points - 1
        print("You Lose")  
    elif move == "SCISSORS" and comp_move == "ROCK":    # L
        losses = losses + 1
        points = points - 1
        print("You Lose")  
    elif move == "SCISSORS" and comp_move == "PAPER":   # W
        wins = wins + 1
        points = points + 1 
        total_points = total_points + 1
        if effect == 2:
            points = points + 1 
            total_points = total_points + 1
        print("You Win") 
    elif move == "SCISSORS" and comp_move == "SCISSORS":   # T
        ties = ties + 1
        print("Tie") 
    elif move != "SCISSORS" and move != "ROCK" and move != "PAPER" and move != "SETTINGS" and move != "STATS" and move != "STORE" and move != "DEV" and move != "SIMULATE" and move != "USER" and move != "SIM" and move != "HELP" and move != "VERSION":
        print("Incorrect Input")
    
    if move == "ROCK" or move == "PAPER" or move == "SCISSORS":
        print("Points: " + str(points))
    print("")
    if points == 3 and (move == "ROCK" or move == "PAPER" or move == "SCISSORS"):
        print("You are up 3!") 
        print("") 
    if points == -3 and (move == "ROCK" or move == "PAPER" or move == "SCISSORS"):
        print("You are down 3! :( ")
        print("")
    if border == "YES":
        print("------------------------------") 
    
    #####################################
    settings = "XY"
    color = "NO"
    
    if move == "SETTINGS":
        settings = str(input("Change Settings? ")) 
        print("")
        settings = settings.upper() 

    if settings == "YES":
        color = str(input("Change text colour to: "))  
        color = color.upper()
        if color == "BLUE":
            print("\033[0;34m ") 
        elif color == "RED":
            print("\033[0;31m ") 
        elif color == "GREEN":
            print("\033[0;32m ") 
        elif color == "YELLOW":
            print("\033[0;33m ") 
        elif color == "PURPLE":
            print("\033[0;35m ") 
        elif color == "CYAN":
            print("\033[0;36m ") 
        elif color == "BLACK":
            print("\033[0;30m ")
        elif color =="WHITE":
            print("\033[0;37m ")
        elif color == "EXIT":
            exit()
        else:
            print("No color change.")
            if border == "YES":
                print("------------------------------") 
            else:
                print("")
    elif settings != "YES" and settings != "XY": 
        print("No settings changes.") 
        if border == "YES":
            print("------------------------------") 
        else:
            print("")
    #####################################
    
    rounds_played = wins + losses + ties 
    if move == "STATS" and rounds_played > 0:
        print("| STATISTICS |") 
        print("")
        print("Rounds Played: " + str(rounds_played))
        print("Wins: " + str(wins)) 
        print("Losses: " + str(losses))
        print("Ties: " + str(ties)) 
        win_percentage = ((wins / rounds_played) * 100) 
        print("Win Percentage: " + str(win_percentage)) 
        print("Total Points Earned: " + str(total_points))
        if border == "YES":
            print("------------------------------")
        else:
            print("")
    elif move == "STATS" and rounds_played == 0:
        print("No Games Played...") 
        print("")
    
    if move == "STORE":
        print("| STORE |") 
        print("") 
        print("Your Points: " + str(points))
        print("") 
        print("1. Gamble - Gamble up to all of your points. (Must have at least 1 point.)")
        print("2. Double Points (10 Rounds) -- 3 Points") 
        print("3. Add <^> to your name -- 20 Points")
        print("4. Basic Car -- 50 points")
        print("5. Epic Car -- 120 points")
        print("")
        buy = str(input("Buy: ")) 
        buy = buy.upper() 
        if buy == "DOUBLE POINTS" or buy =="2" and points >= 3:
            points = points - 3 
            effect = 2
            expiry = rounds_played 
            print("Double Points Purchased !") 
            print("") 
            if border == "YES":
                print("------------------------------") 
        elif buy == "GAMBLE" or buy == "1" and points >= 1:
            print("Gamble Enabled")
            print("To Gamble, go to RPS Simulator") 
            print("")
            if border == "YES":
                print("------------------------------")
            gamble = 1
        elif buy == "<^>" and points >= 20 or buy == "3" and points >= 20:
            print("<^> Purchased !") 
            user = user + " <^>" 
            points = points - 20 
            print("") 
            if border == "YES":
                print("------------------------------")
        elif buy == "BASIC CAR" and points >= 50 or buy == "4" and points >= 50:
            print("Car Purchsed !") 
            print("Added to Username !") 
            garage = 1
            points = points - 50 
            print("") 
            if border == "YES":
                print("------------------------------")
        elif buy == "EPIC CAR" and points >= 120 or buy == "5" and points >= 120:
            print("Car Purchsed !") 
            print("Added to Username !") 
            garage = 2
            points = points - 120
            print("") 
            if border == "YES":
                print("------------------------------")
        else:
            print("Purchase Failed") 
            if points < 3:
                print("Not Enough Points")
            print("") 
            if border == "YES":
                print("------------------------------")
    if rounds_played == expiry + 10 and effect == 2:
        effect = 0 
        print("") 
        print("Effect has expired.") 
        print("") 
        if border == "YES":
            print("------------------------------")
    
    if move == "USER":
        print(user) 
        if garage == 1:
            print("      ________    _")
            print("     /        \  / ")
            print("  ---________ _--") 
            print("  ( )        ( ) ")
            print("") 
        elif garage == 2:
            print(""" 
                     _..-------++._
                 _.-'/ |      _||  \---._
           __.--'`._/_\j_____/_||___\    `----.
      _.--'_____    |          \     _____    /
    _j    /,---.\   |        =o |   /,---.\   |_
   [__]==// .-. \ ==`===========/==// .-. \ =[__]
     `-._|\ `-' /|___\_________/___|\ `-' /|_.' 
           `---'                     `---'
""")
    if move == "SIMULATE" or move == "SIM":
        print("| RPS Simulator |")
        print("")  
        
        if gamble == 1:
            bet_val = int(input("How much would you like to bet? ")) 
            if bet_val > points:
                print("You cannot bet more than you have.") 
                print("")
                bet_val = int(input("How much would you like to bet? ")) 
                if bet_val > points:
                    print("You cannot bet more than you have, try again.")
                    gamble = 3 
            bet_player = int(input("On player 1 or 2? ")) 
            if bet_player != 1 and bet_player != 2:
                print("You can only bet on player 1 or player 2.") 
                print("")
                bet_player = int(input("On player 1 or 2? ")) 
                if bet_player != 1 and bet_player != 2:
                    print("You can only bet on player 1 or player 2, try again.") 
                    gamble = 3
            print("")
            print("Choose how much rounds they play.")
            print("")
        
        simulate_rounds = str(input("How many rounds would you like to simulate? "))
        print("")
        rounds_simulated = 0
        comp1_wins = 0 
        comp2_wins = 0
        sim_ties = 0
        while rounds_simulated != simulate_rounds:
            comp1 = random.randint(1,3) 
            comp2 = random.randint(1,3) 
            if comp1 == 1:
                comp1 = "Rock" 
            elif comp1 == 2:
                comp1 = "Paper" 
            elif comp1 == 3:
                comp1 = "Scissors" 
            comp1 = comp1.upper()  
            if comp2 == 1:
                comp2 = "Rock" 
            elif comp2 == 2:
                comp2 = "Paper" 
            elif comp2 == 3:
                comp2 = "Scissors" 
            comp2 = comp2.upper()  
            
            if comp1 == "ROCK" and comp2 == "ROCK":
                sim_ties = sim_ties + 1
                rounds_simulated = rounds_simulated + 1 
            elif comp1 == "ROCK" and comp2 == "PAPER":
                comp2_wins = comp2_wins + 1 
                rounds_simulated = rounds_simulated + 1 
            elif comp1 == "ROCK" and comp2 == "SCISSORS":
                comp1_wins = comp1_wins + 1 
                rounds_simulated = rounds_simulated + 1
            elif comp1 == "PAPER" and comp2 == "ROCK":
                comp1_wins = comp1_wins + 1 
                rounds_simulated = rounds_simulated + 1
            elif comp1 == "PAPER" and comp2 == "PAPER":
                sim_ties = sim_ties + 1 
                rounds_simulated = rounds_simulated + 1 
            elif comp1 == "PAPER" and comp2 == "SCISSORS":
                comp2_wins = comp2_wins + 1
                rounds_simulated = rounds_simulated + 1 
            elif comp1 == "SCISSORS" and comp2 == "ROCK":
                comp2_wins = comp2_wins + 1 
                rounds_simulated = rounds_simulated + 1 
            elif comp1 == "SCISSORS" and comp2 == "PAPER":
                comp1_wins = comp1_wins + 1 
                rounds_simulated = rounds_simulated +1 
            elif comp1 == "SCISSORS" and comp2 == "SCISSORS":
                sim_ties = sim_ties + 1 
                rounds_simulated = rounds_simulated + 1 
            if int(rounds_simulated) / int(simulate_rounds) == 0.25:
                print("[] 25%")
            if int(rounds_simulated) / int(simulate_rounds) == 0.5:
                print("[][] 50%")
            if int(rounds_simulated) / int(simulate_rounds) == 0.75:
                print("[][][] 75%")
            if int(rounds_simulated) / int(simulate_rounds) == 1:
                print("[][][][] 100%")
                print("")
            if str(rounds_simulated) == str(simulate_rounds): 
                print("Simulation Complete") 
                print("")
                break 
        comp1_percent = (comp1_wins / rounds_simulated) * 100 
        comp2_percent = (comp2_wins / rounds_simulated) * 100 
        tie_percent = (sim_ties / rounds_simulated) * 100 
        print("Rounds Simulated: " + str(rounds_simulated)) 
        print("Player 1 Wins: " + str(comp1_wins)) 
        print("Player 2 Wins: " + str(comp2_wins)) 
        print("Ties: " + str(sim_ties)) 
        print("")  
        print("Player 1 Win Percentage: " + str(comp1_percent) + " %")
        print("Player 2 Win Percentage: " + str(comp2_percent) + " %")
        print("Tie Percentage: " + str(tie_percent) + " %")
        print("")
        if border == "YES":
                print("------------------------------") 
        if gamble == 1:
            print("| GAMBLE |") 
            print("")
            if comp1_wins > comp2_wins and bet_player == 1:
                print("Player 1 Wins, you have doubled the points you bet!") 
                points = (bet_val * 2) + points
                print("Your Points: " + str(points))
                gamble = 0 
            elif comp1_wins < comp2_wins and bet_player == 1:
                print("Player 2 Wins, you have lost the bet.") 
                points = points - bet_val 
                print("Your Points: " + str(points))
                gamble = 0
            elif comp1_wins > comp2_wins and bet_player == 2:
                print("Player 1 Wins, you have lost the bet.") 
                points = points - bet_val 
                print("Your Points: " + str(points))
                gamble = 0
            elif comp1_wins < comp2_wins and bet_player == 2:
                print("Player 2 Wins, you have doubled the points you bet!") 
                points = (bet_val * 2) + points
                print("Your Points: " + str(points))
                gamble = 0
            elif comp1_wins == comp2_wins:
                print("Tie, you don't lose or gain points.")
                print("Your Points: " + str(points)) 
                gamble = 0
            print("") 
            if border == "YES":
                print("------------------------------") 
  
    if move == "VERSION":
        print("Rock Paper Scissors ©")
        print("By Cole Turner, 24-11-2021.")
        print("")
        print("Version 1.3 - 14-12-2021.")
        print("Store Update, sim load bar, UI update, fixes, etc.")
        print("")
        if border == "YES":
            print("------------------------------")
    
    if move == "HELP":
        print("| HELP |") 
        print("")  
        print("FUNCTION - INPUT")
        print("")
        print("Help - help")
        print("Settings - settings") 
        print("Statistics - stats") 
        print("Store - store") 
        print("RPS Simulator - sim") 
        print("Username - user") 
        print("Close Game - exit")
        print("Version - version")
        print("") 
        if border == "YES":
                print("------------------------------") 