def arrange(h, n):
    # 'xx호' (n // h) + 1 (호)
    # 'yy층' (n % h) (층)
    floor = n % h
    ho = (n // h) + 1
    
    if ho < 10:
        ho = '0' + str(ho)

    room_number = str(floor) + ho
    return room_number


print(arrange(30, 72))