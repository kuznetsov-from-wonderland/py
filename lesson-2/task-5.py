my_list = [7, 5, 3, 3, 2]

print(f"Rating - {my_list}")

stop = 'STOP'
print(f"В любой момент введите {stop}, чтобы остановить выполнение ☝️")

num = input("Your input (number) ")

while num != stop:
    is_valid = num.isdigit()
    if not is_valid:
        print('Invalid input')
        print(f"Current Rating - {my_list}")
        num = input("Your input (number) ")
    else:
        digit = int(num)
        my_list.append(digit)
        my_list.sort()
        my_list.reverse()
        print(f"Current Rating - {my_list}")
        num = input("Your input (number) ")
