import pygal

from  _15_10_random_walker import RandomWalker


rw = RandomWalker()
rw.walker()

hist = pygal.Bar()

hist.x_labels = list(str(x) for x in rw.steps_x)
hist.x_title = 'x'
hist.y_title = 'y'
hist.title = 'RandomWalker'

hist.add('Random', rw.steps_y)
hist.render_to_file('RandomWalker.svg')
print(rw.steps_x)
print(rw.steps_y)