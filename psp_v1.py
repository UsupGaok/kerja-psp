import time

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
            0.035,
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
            0.035,
        )
        health -= 50
        food_supply += 2
        energy -= 40


# Searching for food
def search_food():
    global food_supply, energy
    blink("SEARCHING FOR FOOD....FOOD FOUND", 0.035)
    blink(
        """
---> FOOD SUPPLY +1
---> ENERGY -20
""",
        0.035,
    )
    food_supply += 1
    energy -= 20


# For building a shelter
def built_shelter():
    global inventory, energy, Shelter
    if "Rope" in inventory:
        blink("BUILDING A SHELTER....DONEEE✅✅✅", 0.035)
        blink("---> ENERGY -30", 0.035)
        energy -= 30

    elif not "Rope" in inventory:
        blink("BUILDING A SHELTER....DONEEE✅✅✅", 0.035)
        blink("---> ENERGY -50", 0.035)
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
        0.035,
    )


# Name selection
player_name = input(blink("Enter your name : ", 0.035))


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
            0.035,
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
        blink("SEARCHING FOR HELP...", 0.035)
        blink("---> ENERGY -20", 0.035)
        energy -= 20
        searching_for_help_attempt += 1
    elif action_select_daytime.strip() == "3" and Shelter == False:
        built_shelter()
        Shelter = True
    elif action_select_daytime.strip() == "4" and food_supply > 0:
        if "Lighter" in inventory:
            blink("EATING....🍽️🍽️🍽️", 0.035)
            blink(
                """
---> HEALTH +40
---> ENERGY +15
            """,
                0.035,
            )
            health = min(100, health + 40)
            energy = min(150, energy + 15)
            food_supply -= 1
        else:
            blink("EATING....🍽️🍽️🍽️", 0.035)
            blink(
                """
---> HEALTH +20
---> ENERGY +8
            """,
                0.035,
            )
            health = min(100, health + 20)
            energy = min(150, energy + 8)
            food_supply -= 1
    elif action_select_daytime.strip() == "3" and Shelter == True:
        blink("ALREADY BUILT A SHELTER", 0.035)
    elif action_select_daytime.strip() == "4" and food_supply == 0:
        blink("DOESN'T HAVE ENOUGH FOOD SUPPLY", 0.035)
    elif action_select_daytime.strip() == "5":
        if "First aid kit" in inventory:
            blink("---> USING FIRST AID KIT.....➕➕➕", 0.035)
            blink("---> HEALTH +100", 0.035)
            health = min(100, health + 100)
        else:
            blink("DOESN'T HAVE ANY FIRST AID KIT", 0.035)

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
        blink("YOU ENCOUNTER A BEAR😱😱!!!", 0.035)
        fight_bear()
        energy -= 20
    elif action_select_night.strip() == "2":
        blink("YOU ENCOUNTER A BEAR😱😱!!!", 0.035)
        fight_bear()
        blink("---> ENERGY -20", 0.035)
        searching_for_help_attempt += 1
        energy -= 20
    elif action_select_night.strip() == "3":
        blink("--> SLEEPING...😴😴😴", 0.035)
        blink(
            """
        ---> HEALTH +30
        ---> ENERGY +30
        """,
            0.035,
        )
        health = min(100, health + 30)
        energy = min(150, energy + 30)
    elif action_select_night.strip() == "4" and food_supply > 0:
        if "Lighter" in inventory:
            blink("---> EATING....🍽️🍽️🍽️", 0.035)
            blink(
                """
---> HEALTH +40
---> ENERGY +15
---> ENERGY -20
           """,
                0.035,
            )
            health = min(100, health + 40)
            energy = min(150, energy + 15)
            food_supply -= 1
            energy -= 20
        else:
            blink("EATING....🍽️🍽️🍽️", 0.035)
            health = min(100, health + 20)
            energy = min(150, energy + 8)
            blink(
                """
---> HEALTH +20
---> ENERGY +8
---> ENERGY -20

            """,
                0.035,
            )
            food_supply -= 1
            energy -= 20
    elif action_select_daytime.strip() == "4" and food_supply == 0:
        blink("DOESN'T HAVE ENOUGH FOOD SUPPLY", 0.035)
        blink("---> ENERGY -20", 0.035)
        energy -= 20

    if day == 3:
        blink("THERE ARE STORM INCOMING⛈️⛈️⛈️!!!!", 0.035)
        if Shelter == True:
            blink("YOU HAVE SHELTERR😮‍💨😮‍💨", 0.035)
        elif Shelter == False:
            blink(
                """
YOU DOESN\'T HAVE A SHELTERRR😱😱😱

---> HEALTH -30
---> ENERGY -20
""",
                0.035,
            )
            health -= 30
            energy -= 20

    if energy < 0:
        health -= 20

    day += 1

# final part --- decided the player win or dead
if health <= 0:
    blink("GAME OVERRR, YOU'RE DEAD☠️☠️☠️", 0.035)
else:
    blink(
        "CONGRATULATION!!! YOU SUCCESSFULLY OVERCAME THE CHALLENGES AND SURVIVED THE ISLAND🎉🎉🎉🎉",
        0.035,
    )
