class User:
    def __init__(self,name):
        self.name = name
        self.level = 1
        self.xp = 0

    def show_stats(self):
        print(f"\n{self.name} | Level: {self.level} | XP: {self.xp}") 
    
    def add_xp(self, amount):
        self.xp += amount 
        print(f"{self.name} gained {amount} XP!")
        self.check_level_up()

    def check_level_up(self):
        while self.xp >= 100:
            self.level += 1
            self.xp -= 100
            print(f"Congrats {self.name} Leveled Up! Your Now Level {self.level}")



