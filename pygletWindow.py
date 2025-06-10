import pyglet

display = pyglet.display.get_display()          # get display resolution
screens = display.get_screens()
screenX = [screen.width for screen in screens]
screenY = [screen.height for screen in screens]

dim = int(screenY[0]/15) # always get the main screen resolution
posX = int(screenX[0]/2)
posY = int(screenY[0]/2)
velX = int(screenX[0]/150)
velY = int(screenY[0]/150)
dim2 = dim/2

fps = 60

window = pyglet.window.Window(style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS) # init display
window.set_size(dim, dim)
window.set_location(int(posX-dim/2), int(posY-dim/2)) # set window pos

pyglet.gl.glClearColor(255, 255, 255, 1.0) # create white bg

keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

@window.event   # update loop
def update(dt):
    global posX
    global posY
    window.set_location(int(posX-dim2), int(posY-dim2)) # change window pos

    if keys[pyglet.window.key.W]: #input handler
        posY-=velY
    if keys[pyglet.window.key.S]:
        posY+=velY
    if keys[pyglet.window.key.A]:
        posX-=velX
    if keys[pyglet.window.key.D]:
        posX+=velX
    
    if posX > screenX[0]-dim2:
        posX = screenX[0]-dim2
    if posX < dim2:
        posX = dim2
    if posY > screenY[0]-dim2:
        posY = screenY[0]-dim2
    if posY < dim2:
        posY = dim2

pyglet.clock.schedule_interval(update, 1/fps) # update speed 

@window.event
def on_draw():
    window.clear()

pyglet.app.run()