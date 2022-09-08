from mathJCB import normalized
from collections import namedtuple

V3 = namedtuple('Point3', ['x', 'y', 'z'])

DIR_LIGHT = 0
POINT_LIGHT = 1
AMBIENT_LIGHT = 2

class DirectionalLight(object):
    def __init__(self, direction = (0,-1,0), intensity = 1, color = (1,1,1)):
        self.direction = normalized(V3(direction[0],direction[1],direction[2]))
        self.intensity = intensity
        self.color = color
        self.lightType = DIR_LIGHT

class AmbientLight(object):
    def __init__(self, intensity = 0.1, color = (1,1,1)):
        self.intensity = intensity
        self.color = color
        self.lightType = AMBIENT_LIGHT