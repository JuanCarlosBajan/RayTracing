from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, gourad, gouradIntense
from shaders import flat, unlit, gourad, toon, glow, textureBlend, jccc, jccc2, jccc3, normalMap

width = 1400
height = 800

rend = Renderer(width, height)


"""
rend.active_texture = Texture("model.bmp")

rend.active_texture = Texture("earthDay.bmp")
rend.active_texture2 = Texture("earthNight.bmp")
rend.active_shader = textureBlend

rend.glLoadModel("earth.obj",
                 translate = V3(0, 0, -10),
                 scale = V3(0.01,0.01,0.01),
                 rotate = V3(0,90,0))



#rend.active_texture = Texture("models/model.bmp")
#rend.active_shader = gourad
#rend.glLoadModel("models/model.obj",
#                 translate = V3(-4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = toon
#rend.glLoadModel("models/model.obj",
#                 translate = V3(0, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = glow
#rend.glLoadModel("models/model.obj",
#                 translate = V3(4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

rend.glLoadModel("model.obj",
                 translate = V3(width/2, height/2, 0),
                 rotate = V3(0, 180, 0), 
                 scale = V3(1000,1000,1000)) """

#rend.active_texture2 = Texture("earthNight.bmp")
#rend.active_shader = textureBlend
""" 
rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(2.5, 2.2, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(-2.5, 2.2, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(0, 2.2, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.active_texture = Texture("BitMap/Models&Outputs/bn.bmp")
rend.active_shader = jccc2

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(2.5, -1, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(-2.5, -1, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(0, -1, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.active_texture = Texture("BitMap/Models&Outputs/bn.bmp")
rend.active_shader = jccc3

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(2.5, -4.5, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(-2.5, -4.5, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(0, -4.5, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glFinish("BitMap/Models&Outputs/output.bmp") """

rend.normal_map = Texture("BitMap/Models&Outputs/normal.bmp")
rend.active_texture = Texture("BitMap/Models&Outputs/rough.bmp")
rend.active_shader = normalMap
rend.background =  Texture("BitMap/Models&Outputs/background.bmp")

rend.glClearBackground()

rend.dirLight = V3(0,0,0)
rend.dirLight2 = V3(0,0,0)
rend.active_shader = gouradIntense
rend.glLoadModel("BitMap/Models&Outputs/Stone.obj",
                 translate = V3(-4.3, -4.3, -11),
                 scale = V3(0.2,0.3,0.2),
                 rotate = V3(0,0,190))

rend.dirLight = V3(0,1,0)
rend.dirLight2 = V3(-0.5,-0.5,0)
rend.active_shader = gouradIntense
rend.glLoadModel("BitMap/Models&Outputs/Stone.obj",
                 translate = V3(-4, -4, -10),
                 scale = V3(0.2,0.2,0.2),
                 rotate = V3(0,40,0))

rend.normal_map = None
rend.active_texture = Texture("BitMap/Models&Outputs/bn.bmp")
rend.active_shader = None

rend.dirLight = V3(0,1,0)
rend.dirLight2 = V3(-0.5,-0.5,0)
rend.active_shader = jccc
rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(3, -7, -20),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.dirLight = V3(0,1,0)
rend.dirLight2 = V3(-0.5,-0.5,0)
rend.active_shader = jccc2
rend.glLoadModel("BitMap/Models&Outputs/face.obj",
                 translate = V3(6, -7, -20),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(0,0,0))

rend.dirLight = V3(0,1,0)
rend.dirLight2 = V3(-0.5,-0.5,0)
rend.active_shader = jccc3
rend.glLoadModel("BitMap/Models&Outputs/model.obj",
                 translate = V3(9.5, -6, -20),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))


rend.dirLight = V3(0,0,1)
rend.dirLight2 = V3(0,0,1)
rend.active_shader = jccc
rend.glLoadModel("BitMap/Models&Outputs/earth.obj",
                 translate = V3(7.5, -10, -25),
                 scale = V3(0.03,0.007,0.01),
                 rotate = V3(0,0,0))

rend.glFinish("BitMap/Models&Outputs/output.bmp")