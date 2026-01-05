class Quest:
    def __init__(self, name, xp_reward):
        self.name = name
        self.xp_reward = xp_reward
        self.completed = False

    def complete(self, user):
        if self.completed:
            print(f"❌ You already completed '{self.name}' today.")
            return
    
        print(f"✅ Quest Completed: {self.name}")
        user.gain_xp(self.xp_reward)
        print(f"+{self.xp_reward} XP earned!")
        self.completed = True