class User:
    def __init__(self,name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.title = "E-Rank Hunter"

    def show_status(self):
        print(f"\n{self.name} | Level: {self.level} | XP: {self.xp}") 
    
    def gain_xp(self, amount):
        self.xp += amount 
        print(f"{self.name} gained {amount} XP!")
        self.check_level_up()

    def check_level_up(self):
        while self.xp >= 100:
            self.level += 1
            self.xp -= 100
            self.update_title()
            print(f"Congrats {self.name} Leveled Up! Your Now Level {self.level}")

    def update_title(self):
        if self.level <5:
            self.title ="E-Rank Hunter"
        elif self.level < 10:
            self.title = "D-Rank Hunter"
        elif self.level < 15:
            self.level = "C-Rank Hunter"
        elif self.level < 20:
            self.level = "B-Rank HUnter"
        elif self.level < 25:
            self.level = "A-Rank Hunter"
        else:
            self.title = "S-Rank Hunter"