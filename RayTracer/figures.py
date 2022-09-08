import numpy as np

from mathJCB import dot, escalarVectorMultiplication, magnitude, normalized, subtract, vectorAddition

WHITE = (1,1,1)
BLACK = (0,0,0)

class Intersect(object):
    def __init__(self, distance, point, normal, sceneObj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObj = sceneObj

class Material(object):
    def __init__(self, diffuse = WHITE):
        self.diffuse = diffuse


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = subtract(self.center, orig)
        tca = dot(L, dir)
        d = (magnitude(L) ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        # P = O + t0 * D
        P = vectorAddition(orig, escalarVectorMultiplication( t0 , dir))
        normal = subtract(P, self.center)
        normal = normalized(normal)

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         sceneObj = self)