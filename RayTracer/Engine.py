from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 504
height = 504

# Materiales

brick = Material(diffuse = (1, 0, 0), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
blueMirror = Material(diffuse = (0.2, 0.2, 0.9), spec = 64, matType = REFLECTIVE)
yellowMirror = Material(diffuse = (0.9, 0.9, 0.2), spec = 64, matType = REFLECTIVE)

glass = Material (diffuse = (0.9, 0.9,0.9), spec=100, ior=1.325, matType=TRANSPARENT)
purpleGlass = Material (diffuse = (0.9, 0.6,0.9), spec=100, ior=1.325, matType=TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("RayTracer/parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))
#rtx.lights.append( PointLight(point = (0,0,0)))

rtx.scene.append( Triangle(a= V3(-2,0,-5), b=V3(1,2,-5), c=V3(-1, 5, -5), material= brick)  )

rtx.glRender()

rtx.glFinish("RayTracer/output.bmp")