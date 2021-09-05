def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    length = len(magicians)
    for i in range(length):
        magicians[i] = 'the Great ' + magicians[i]
    return magicians

magicians = ['harry', 'bob', 'kevin']

show_magicians(magicians)
magicians2 = make_great(magicians[:])
show_magicians(magicians2)
show_magicians(magicians)