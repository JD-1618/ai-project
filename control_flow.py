# 1.control flow (if / else)
score = 85
if score >=80:
    print("passed! Ready for AI.")
else: 
    print("keep practicing.")
#2. For loop(repeating an action for each item)
numbers =[1, 2, 3, 4, 5]
doubled = []
for n in numbers:
    doubled.append(n * 2)
print(f"doubled with loop:{doubled}")
# List comprehension (one-line shortcut for the same loop)
doubled_fast = [n * 2 for n in numbers]
print(f"doubled with comprehension:{doubled_fast}")