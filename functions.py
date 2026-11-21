# 1. Function with a default argument 
def greet_learner(name, city="pune"):
    return f"welcome {name} from {city}!"
print(greet_learner ("JD"))
print(greet_learner("JD", "mumbai"))
#2 *args (any number of extra items)
def add_scores(*args):
    return sum(args)
print(f"total score:{add_scores(10, 20, 30,)}")
#3. **kwargs (any number of labeled key=value pairs)
def show_profile(**kwargs):
 print(f"profile details:{kwargs}")
show_profile(name="JD", track="AI", day=1)
#4. Lambda (mini one-line function)
square= lambda x:x * x 
print(f"Square of 5:{square(5)}")
