#1. Base class with state (__init__)
class learner:
    def __init__(self, name):
        self.name = name 
        self.xp = 0
    def study(self, points):
        self.xp += points
        return f"{self.name} earned {points} XP! Total XP: {self.xp}"
jd = learner("JD")
print(jd.study(50))
#2. Subclass extending learner 
class AIlearner(learner):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model
    def build_ai(self):
        return f"{self.name} (XP:{self.xp}) is building with {self.model}!"
pro_jd = AIlearner("JD", "GPT")
pro_jd.study(100)
print(pro_jd.build_ai())
        