import json
import os


class User:
    Save_File = "save.json"

    def __init__(self,name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.title = "E-Rank Hunter"

        self.load_progress()

    def show_status(self):
        print("\n===========================")
        print("       STATUS: HUNTER       ")
        print("===========================")
        print(f"Hunter : {self.name}")
        print(f"Rank   : {self.title}")
        print(f"Level  : {self.level}")
        print(f"XP     : {self.xp} / 100")
        print("===========================")    
    def gain_xp(self, amount):
        self.xp += amount 
        print(f"{self.name} gained {amount} XP!")
        self.check_level_up()
        self.save_progress()

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
            self.title = "C-Rank Hunter"
        elif self.level < 20:
            self.title = "B-Rank Hunter"
        elif self.level < 25:
            self.title = "A-Rank Hunter"
        else:
            self.title = "S-Rank Hunter"

    def save_progress(self):
        data = {
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "title": self.title
        }
        with open(self.Save_File, "w") as file:
            json.dump(data, file)

    def load_progress(self):
        if not os.path.exists(self.Save_File):
            return
        with open(self.Save_File, "r") as file:
            data = json.load(file)
        if data["name"] == self.name:
            self.level = data["level"]
            self.xp = data["xp"]
            self.title = data["title"]
