def films():
    movie_list = []
    cont = True
    while cont is True:
        film = input("What is your favorite film of yours? ")
        movie_list.append(film)
        carry = input("Any more? (Y/N) ")
        if carry.lower() == "y":
            continue
        else:
            break
    return movie_list

print(films())

