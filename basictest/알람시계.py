hour, min = map(int, input().split(' '))


if min < 45:
    if hour == 0:
        print(23, min+60-45)
    else:
        print(hour-1, min+60-45)
else:
    print(hour, min-45)
