s1 = [20, 30, 40]
s2 = [2, 5]
final_ans = 0
total = "und"
first_prompt = "Are the numbers 20, 30, and 40 all divisible by 2 and 5?"
second_prompt = "Are the numbers 20, 32, and 40 all divisible by 2 and 5?"

for i in s1:
    x = i

    for i in s2:
        y = i
        
        if (x % y == 0):
            final_ans = final_ans + 1
        else:
            final_ans = final_ans
            
if final_ans == 6:
    total = "True"
else:
    total = "False"

print(first_prompt)
print(total)
    
s1 = [20, 32, 40]
s2 = [2, 5]

for i in s1:
    x = i

    for i in s2:
        y = i
        
        if (x % y == 0):
            final_ans = final_ans + 1
        else:
            final_ans = 0
            
if final_ans == 6:
    total = "True"
else:
    total = "False"

print(second_prompt)
print(total)