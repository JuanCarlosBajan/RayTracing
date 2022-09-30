from turtle import position
from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.86, 0.9, 0.84), spec = 16)

glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
diamond = Material(diffuse = (0.5, 0.9, 0.9), spec = 32, ior = 1.1, matType = TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("./Raytracer/parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.25 ))
#rtx.lights.append( DirectionalLight(direction = V3(-1,-1,-1), intensity = 0.8 ))
rtx.lights.append( DirectionalLight(direction = V3(0,0,-1), intensity = 0.8 ))
#rtx.lights.append( PointLight(point=V3(0,0,0)))

#rtx.scene.append(Plane(position=V3(0,-10,0), normal=V3(0,1,0), material=brick))
rtx.scene.append(Plane(position=V3(-10,-10,0), normal=V3(-1.2,0,0), material=brick))
rtx.scene.append(Plane(position=V3(10,-10,0), normal=V3(1,0,0), material=stone))
rtx.scene.append(Plane(position=V3(0,10,0), normal=V3(0,-1,0), material=diamond))
rtx.scene.append(Plane(position=V3(0,-10,0), normal=V3(0,1,0), material=diamond))
rtx.scene.append(Plane(position=V3(0,0,-100), normal=V3(0,0,-1), material=stone))
rtx.scene.append(Sphere(center=V3(0,0,-30), radius= 1, material=brick))
#rtx.scene.append(AABB(position=V3(-3,-3,-10),size = (1,1,1), material=glass))

rtx.glRender()

rtx.glFinish("./Raytracer/output.bmp")