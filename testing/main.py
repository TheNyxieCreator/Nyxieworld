from ursina import *
from ursina.prefabs.first_person_controller import *

def update():
    if player.y < 0:
        player.position = (17,0,-19)

app = Ursina()

maze = Entity(model='map_1', texture='brick', scale=30, collider='mesh')
maze.level = 1

player = FirstPersonController(position=(17,0,-19))

window.title = 'My Game'
window.exit_button.visible = False
window.exit_button.enabled = False
window.borderless = False
window.fullscreen = False

app.run()

