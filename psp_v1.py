import time

global_blink_rate = 0.00035
day = 1
health = 100
inventory = []
energy = 150
food_supply = 0
Shelter = False
searching_for_help_attempt = 0


# For loading the print and make the output appeared more slowly
def blink(name, duration):
    for i in range(len(name)):
        time.sleep(duration)
        print(name[i], end="", flush=True)
    print()
    return ""  # to eliminate output of None when using this in input func


# Fight bear scenario
def fight_bear():
    global health, food_supply, energy, inventory
    if "Knife" in inventory:
        blink(
            """
U DEFEATED THE BEAR
---> HEALTH -25
""",
            global_blink_rate,
        )
        health -= 25
        food_supply += 2
        energy -= 20

    elif not "Knife" in inventory:
        blink(
            """
U DEFEATED THE BEAR
---> HEALTH -50
""",
            global_blink_rate,
        )
        health -= 50
        food_supply += 2
        energy -= 40


# Searching for food
def search_food():
    global food_supply, energy
    blink("SEARCHING FOR FOOD....FOOD FOUND", global_blink_rate)
    blink(
        """
---> FOOD SUPPLY +1
---> ENERGY -20
""",
        global_blink_rate,
    )
    food_supply += 1
    energy -= 20


# For building a shelter
def built_shelter():
    global inventory, energy, Shelter
    if "Rope" in inventory:
        blink("BUILDING A SHELTER....DONEEE✅✅✅", global_blink_rate)
        blink("---> ENERGY -30", global_blink_rate)
        energy -= 30

    elif not "Rope" in inventory:
        blink("BUILDING A SHELTER....DONEEE✅✅✅", global_blink_rate)
        blink("---> ENERGY -50", global_blink_rate)
        energy -= 50


# to show status window
def status_show():
    blink(
        f"""
--- DAY {day} ---
Player name : {player_name}
Health      : {health}
Energy      : {energy}
Food supply : {food_supply}
Inventory   : {inventory}
Shelter     : {shelter_valid}

""",
        global_blink_rate,
    )


# Name selection
player_name = input(blink("Enter your name : ", global_blink_rate))


# Item selection

while not inventory:
    item_select = input(
        blink(
            """
ITEM SELECTION

A ----> [Lighter, Knife, Rope]
B ----> [First aid kit, Knife, Lighter]
C ----> [Lighter, First aid kit, Rope]

Please select your item(A/B/C) : """,
            global_blink_rate,
        )
    )
    if item_select.upper().strip() == "A":
        inventory.extend(["Lighter", "Knife", "Rope"])
    elif item_select.upper().strip() == "B":
        inventory.extend(["First aid kit", "Knife", "Lighter"])
    elif item_select.upper().strip() == "C":
        inventory.extend(["Lighter, First aid kit", "Rope"])
    else:
        print("\nPlease enter correct selection")

#########################################################

# main loop/game started
while day <= 5 and health > 0 and searching_for_help_attempt < 6:
    if Shelter == False:
        shelter_valid = "❌"
    else:
        shelter_valid = "✅"
    status_show()
    while True:
        action_select_daytime = input(
            blink(
                """
==================================================
                 DAYTIMEE🌄🌄
==================================================

Select Action :
1. Search for food
2. Continue to search for help
3. Built a shelter
4. Eat
5. Use first aid kit

Enter your action : """,
                0.02,
            )
        )
        if action_select_daytime.strip() == "1":
            search_food()
        elif action_select_daytime.strip() == "2":
            blink("SEARCHING FOR HELP...", global_blink_rate)
            blink("---> ENERGY -20", global_blink_rate)
            energy -= 20
            searching_for_help_attempt += 1
        elif action_select_daytime.strip() == "3" and Shelter == False:
            built_shelter()
            Shelter = True
        elif action_select_daytime.strip() == "4" and food_supply > 0:
            if "Lighter" in inventory:
                blink("EATING....🍽️🍽️🍽️", global_blink_rate)
                blink(
                    """
    ---> HEALTH +40
    ---> ENERGY +15
                """,
                    global_blink_rate,
                )
                health = min(100, health + 40)
                energy = min(150, energy + 15)
                food_supply -= 1
            else:
                blink("EATING....🍽️🍽️🍽️", global_blink_rate)
                blink(
                    """
    ---> HEALTH +20
    ---> ENERGY +8
                """,
                    global_blink_rate,
                )
                health = min(100, health + 20)
                energy = min(150, energy + 8)
                food_supply -= 1
        elif action_select_daytime.strip() == "3" and Shelter == True:
            blink("ALREADY BUILT A SHELTER", global_blink_rate)
        elif action_select_daytime.strip() == "4" and food_supply == 0:
            blink("DOESN'T HAVE ENOUGH FOOD SUPPLY", global_blink_rate)
        elif action_select_daytime.strip() == "5":
            if "First aid kit" in inventory:
                blink("---> USING FIRST AID KIT.....➕➕➕", global_blink_rate)
                blink("---> HEALTH +100", global_blink_rate)
                health = min(100, health + 100)
            else:
                blink("DOESN'T HAVE ANY FIRST AID KIT", global_blink_rate)
        else:
            print("Invalid input")
            continue
        break

    while True:
        action_select_night = input(
            blink(
                """
==================================================
                  NIGHTTIME🌙🌙
==================================================
Select Action :
1. Search for food
2. Continue to search for help
3. Sleep
4. Eat

Enter your action : """,
                0.02,
            )
        )

        if action_select_night.strip() == "1":
            blink("YOU ENCOUNTER A BEAR😱😱!!!", global_blink_rate)
            fight_bear()
            energy -= 20
        elif action_select_night.strip() == "2":
            blink("YOU ENCOUNTER A BEAR😱😱!!!", global_blink_rate)
            fight_bear()
            blink("---> ENERGY -20", global_blink_rate)
            searching_for_help_attempt += 1
            energy -= 20
        elif action_select_night.strip() == "3":
            blink("--> SLEEPING...😴😴😴", global_blink_rate)
            blink(
                """
            ---> HEALTH +30
            ---> ENERGY +30
            """,
                global_blink_rate,
            )
            health = min(100, health + 30)
            energy = min(150, energy + 30)
        elif action_select_night.strip() == "4" and food_supply > 0:
            if "Lighter" in inventory:
                blink("---> EATING....🍽️🍽️🍽️", global_blink_rate)
                blink(
                    """
---> HEALTH +40
---> ENERGY +15
---> ENERGY -20
           """,
                    global_blink_rate,
                )
                health = min(100, health + 40)
                energy = min(150, energy + 15)
                food_supply -= 1
                energy -= 20
            else:
                blink("EATING....🍽️🍽️🍽️", global_blink_rate)
                health = min(100, health + 20)
                energy = min(150, energy + 8)
                blink(
                    """
---> HEALTH +20
---> ENERGY +8
---> ENERGY -20

            """,
                    global_blink_rate,
                )
                food_supply -= 1
                energy -= 20
        elif action_select_daytime.strip() == "4" and food_supply == 0:
            blink("DOESN'T HAVE ENOUGH FOOD SUPPLY", global_blink_rate)
            blink("---> ENERGY -20", global_blink_rate)
            energy -= 20
        else:
            print("Invalid input")
            continue

        if day == 3:
            blink("THERE ARE STORM INCOMING⛈️⛈️⛈️!!!!", global_blink_rate)
            if Shelter == True:
                blink("YOU HAVE SHELTERR😮‍💨😮‍💨", global_blink_rate)
            elif Shelter == False:
                blink(
                    """
YOU DOESN\'T HAVE A SHELTERRR😱😱😱

---> HEALTH -30
---> ENERGY -20
""",
                    global_blink_rate,
                )
                health -= 30
                energy -= 20

        if energy < 0:
            health -= 20

        day += 1
        break

# final part --- decided the player win or dead
if health <= 0:
    blink("GAME OVERRR, YOU'RE DEAD☠️☠️☠️", global_blink_rate)
else:
    blink(
        "CONGRATULATION!!! YOU SUCCESSFULLY OVERCAME THE CHALLENGES AND SURVIVED THE ISLAND🎉🎉🎉🎉",
        global_blink_rate,
    )
