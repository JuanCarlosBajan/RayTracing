from gl import Raytracer, V3
from figures import *
from lights import *


width = 500
height = 500

# Materiales

snow = Material(diffuse = (0.99, 0.98, 0.91))
white = Material(diffuse = (1, 1, 1))
black = Material(diffuse = (0, 0, 0))
gray = Material(diffuse = (0.5, 0.5, 0.5))
orange = Material(diffuse = (1, 0.27, 0))



rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))


rtx.scene.append( Sphere(V3(0,3,-10), 1.8, snow)  )
rtx.scene.append( Sphere(V3(0,0,-10), 2.3, snow)  )
rtx.scene.append( Sphere(V3(0,-3,-10), 3, snow)  )
rtx.scene.append( Sphere(V3(0.35,3,-8.5), 0.4, white)  )
rtx.scene.append( Sphere(V3(-0.35,3,-8.5), 0.4, white)  )
rtx.scene.append( Sphere(V3(0.4,3,-8.2), 0.2, black)  )
rtx.scene.append( Sphere(V3(-0.4,3,-8.2), 0.2, black)  )
rtx.scene.append( Sphere(V3(0.45,3.1,-8.1), 0.1, white)  )
rtx.scene.append( Sphere(V3(-0.35,3.1,-8.1), 0.1, white)  )
rtx.scene.append( Sphere(V3(0.25,2.2,-8.45), 0.2, gray)  )
rtx.scene.append( Sphere(V3(-0.25,2.2,-8.45), 0.2, gray)  )
rtx.scene.append( Sphere(V3(0.6,2.5,-8.45), 0.2, gray)  )
rtx.scene.append( Sphere(V3(-0.6,2.5,-8.45), 0.2, gray)  )
rtx.scene.append( Sphere(V3(0,2.55,-8.45), 0.3, orange)  )
rtx.scene.append( Sphere(V3(0,0.8,-8.2), 0.6, black)  )
rtx.scene.append( Sphere(V3(0,-0.8,-8), 0.7, black)  )
rtx.scene.append( Sphere(V3(0,-2.4,-7.4), 0.8, black)  )

rtx.glRender()

rtx.glFinish("output.bmp")