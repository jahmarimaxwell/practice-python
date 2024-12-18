# pip install pyglet
import pyglet
 
# importing shapes from pyglet library
from pyglet import shapes
 
# Canvas
window = pyglet.window.Window(960, 540)
batch = pyglet.graphics.Batch()
 
# Making Green Circle
circle = shapes.Circle(700, 150, 100, 
                       color=(50, 225, 30),
                       batch=batch)
 
@window.event
def on_draw():
    window.clear()
    batch.draw()
 
 
pyglet.app.run()