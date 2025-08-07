import random

result_list = list(""for _ in range(6))

for _ in range(100):
    num = random.randint(1,6)
    result_list[num-1] += "*"

for i in range(6):
    print(f"{i+1}:{"".join(result_list[i])}")
