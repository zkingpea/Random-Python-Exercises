#use dictionaries to create a basic rpg battle game
import time 
import random
import sys

while True:
    player = {"name": "Hero", "health": 100, "attack": 10}
    enemy = {"name": "Goblin", "health": 80, "attack": 8}

    print("\n⚔️ A wild Goblin appears!")
          
    while player["health"] > 0 and enemy["health"] > 0:
        print("\nYour health:", player["health"])
        print("Enemy health:", enemy["health"])

        user_input = input("Press Enter to start attack timing (or type 'quit' to exit): ")
        if user_input.lower == "quit": 
            print("Exiting the game. Goodbye!") 
            sys.exit() #exits game

        print('Get ready...')
        delay = random.uniform(0.4, 2.5) 
        time.sleep(delay)

        print("ATTACK NOW!")
        start = time.time()
        input()
        end = time.time()

        reaction_time = end - start 
        print("Reaction time:", round(reaction_time, 2))

        if reaction_time < 1: 
            damage = player["attack"] * 2
            print("💥 Critical hit!") 
        elif reaction_time < 2: 
            damage = player["attack"] 
            print("✅ Normal hit.")
        else: 
            damage = player["attack"] // 2
            print("🐢 Too slow...")

        enemy["health"] -= damage
        print(f"💥 You dealt {damage} damage to the {enemy['name']}!")

        if enemy["health"] <= 0: 
            print(f"\n🎉 You defeated the {enemy['name']}!") 
            break

        print("\n👹 Goblin is preparing to attack...")

        user_input = input("Press Enter to prepare to block (or type 'quit' to exit): ") 
        if user_input.lower() == "quit": 
            print("Exiting the game. Goodbye!")
            sys.exit()

        print('Get ready...')
        delay = random.uniform(0.6, 2.0) 
        time.sleep(delay)

        print("BLOCK NOW!")
        start = time.time()
        input()
        end = time.time()

        reaction_time = end - start 
        print("Reaction time:", round(reaction_time, 2))

        if reaction_time < 1: 
            damage = enemy["attack"] * 0
            print("🛡️ Perfect Block!") 
        elif reaction_time < 2: 
            damage = enemy["attack"] // 2
            print("🩹 Minor Deflection.")
        else: 
            damage = enemy["attack"]
            print("🤕 Direct Hit...")
    
        player["health"] -= damage
        print(f"🤕 The {enemy['name']} dealt {damage} damage to you!")

        if player["health"] <= 0: 
            print(f"\n💀 You were defeated by the {enemy['name']}.")
