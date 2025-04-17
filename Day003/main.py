print("\"Welcome to Treasure Island\"")
print("You've been dropped onto an uncharted island and found two diff paths into the jungle.")
print("______________________👨🏽‍🦯  or  👨🏽‍🦯‍➡️️_______________________")
path = input("Which way You wanna go? Type 'l' for left or 'r' for right: ").lower()
if path == "r":
    print("👨🏽‍🦯‍➡️﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏🏛️﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    path2 = input("You reach a lake with an old temple in the center.\n"
          "Type 'w' to wait for a boat or 's' to swim? ").lower()
    if path2 == "w":
        print("﹏﹏﹏﹏﹏﹏﹏️﹏﹏﹏﹏﹏﹏﹏🚣🏾‍﹏🏛️﹏﹏﹏﹏️﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
        door = input("You reached the temple unharmed"
              " & found three ancient doors\nmarked with symbols:"
              " snake, moon, and fish. Choose: 's', 'm', or 'f'? ").lower()
        if door == "s":
            print("🚪 👨🏽‍🦯‍➡️  🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍")
            print("You've entered a room full of snakes. Game Over.")
        elif door == "m":
            print("🚪👨🏽‍🦯‍➡️______________________________✨💰💎💰👑💰👑💰👑💎✨")
            print("You've found the Treasure. You WIN!")
        elif door == "f":
            print("🚪  ")
            print("﹏🐡🐡🐡🐡🐡🐡🏊🏽‍🐡🐡🐡🐡🐡🐡﹏")
            print("You've fell into pool of piranhas. GAME OVER")
        else:
            print("invalid inputs")
    elif path2 == "s":
        print("﹏﹏﹏﹏﹏﹏﹏﹏﹏️𓆌﹏﹏﹏️𓆌﹏🏊🏽‍♂️𓆌﹏️﹏️﹏️𓆌﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
        print("you got eaten by crocodiles while swimming. GAME OVER")
    else:
        print("invalid inputs")
elif path == "l":
    print("        👨🏽‍🦯")
    print("🗲﹏﹏﹏﹏﹏🗲")
    print("You fell into an old well. GAME OVER")
else:
    print("invalid inputs")
