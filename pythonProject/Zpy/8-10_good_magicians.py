def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    length = len(magicians)
    for i in range(length):
        magicians[i] = 'the Great ' + magicians[i]

magicians = ['harry', 'bob', 'kevin']

show_magicians(magicians)
make_great(magicians)

show_magicians(magicians)