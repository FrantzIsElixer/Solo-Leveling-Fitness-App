from user import User
from quests import Quest

# Ask for users name
name = input("Enter your name: ")
player = User(name)

# Create daily workouts
quests = [
    Quest("30 Push-ups", 25),
    Quest("50 Sit-ups", 25),
    Quest("1 Mile Run", 50)
]

# Game loop
while True:
    print("\n--- DAILY WORKOUTS ---")
    player.show_status()

    for i, quest in enumerate(quests, start=1):
        status = "✅" if quest.completed else "❌"
        print(f"{i}. {quest.name} ({quest.xp_reward} XP) {status}")

    print("4. Quit")

    choice = input("Choose a workout: ")

    if choice == "4":
        print("💪 Workout session ended. Good job!")
        break

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(quests):
            quests[choice - 1].complete(player)
        else:
            print("Invalid choice.")
    else:
        print("Please enter a number:")
