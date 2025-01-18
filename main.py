from ursina import *

app = Ursina()

world = Entity(model='map_test', texture='folder', scale=10, collider='mesh')

window.title = 'My Game'
window.exit_button.visible = False
window.exit_button.enabled = False
window.borderless = False
window.fullscreen = False

Sky()
EditorCamera()
app.run()