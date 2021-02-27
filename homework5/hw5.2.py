def bunnyears(z):
    if z == 0:
        return 0:
        if z%2 == 0:
            return 3+bunnyears2(z-1)
        else:
            return bunnyears2(z-1)+2
print('bunnyears2(0)->',bunnyears(0))
print('bunnyears2(1)->',bunnyears(1))
print('bunnyears2(2)->',bunnyears(5))
