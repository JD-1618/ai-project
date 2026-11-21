name = "JD" 
age = 25
score = 98.5
is_ready = True

print(f"hi {name}, age {age} score {score}, ready: {is_ready}")
# Lists (ordered, changables)
tools = ["VS code", "python" ,"git"]
tools.append("github")
print(f"Tools list:{tools}")
print (f"First tool:{tools[0]}")
print (f"second tool:{tools[1]}")
# Tupels (ordered, unchangeable)
dimensions = (1920, 1080)
print(f"screen size:{dimensions}")
print (f"width:{dimensions[0]}")
# sets (unique items, unordered)
tags = {"ai", "python", "ai" ,"git"}
tags.add("vscode")
print(f"unique tags: {tags}")
# dictionaries (key-value pairs)
user = {"name": "JD", "role":"Ai lerner", "level": 1}
user["city"] = "Pune"
print(f"user profile: {user}")
print(f"user role:{user['role']}")
print(f"user city: {user['city']}")
