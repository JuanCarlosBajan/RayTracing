import numpy as np
from collections import namedtuple
from mathJCB import dot, escalarVectorMultiplication, magnitude, normalized, subtract, vectorAddition, cross,toggleSign

V3 = namedtuple('Point3', ['x', 'y', 'z'])

WHITE = (1,1,1)
BLACK = (0,0,0)

OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2

class Intersect(object):
    def __init__(self, distance, point, normal,texcoords, sceneObj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.texcoords = texcoords
        self.sceneObj = sceneObj

class Material(object):
    def __init__(self, diffuse = WHITE, spec = 1.0,ior = 1.0, texture = None, matType = OPAQUE):
        self.diffuse = diffuse
        self.spec = spec
        self.ior = ior
        self.texture = texture
        self.matType = matType

class Plane(object):
    def __init__(self, position, normal, material):
        self.position = position
        self.normal = normalized(normal)
        self.material = material

    def ray_intersect(self, orig, dir):
        denom = dot(dir, self.normal)

        if abs(denom) > 0.001:
            
            num = dot(subtract(self.position, orig), self.normal)
            t = num/denom

            if t > 0:
                p = vectorAddition(orig, escalarVectorMultiplication(t, dir))
                return Intersect(distance=t,
                                    point=p,
                                    normal=self.normal,
                                    texcoords=None,
                                    sceneObj=self)

        return None

class Triangle(object):
    def __init__(self, a, b, c, material):
        self.a = a
        self.b = b
        self.c = c
        self.material = material
        self.center = V3((a.x+b.x+c.x)/3,(a.y+b.y+c.y)/3,(a.z+b.z+c.z)/3)
        print(a,b,c)

    def ray_intersect(self, orig, dir):

        self.normal = normalized(cross(subtract(self.b, self.a), subtract(self.c,self.a) ))
        #self.normal = toggleSign(self.normal)


        denom = dot(dir, self.normal)

        if abs(denom) > 0.001:
            num = dot(subtract(self.center, orig), self.normal)
            t = num/denom

            if t > 0:
                p = vectorAddition(orig, escalarVectorMultiplication(t, dir))
                sa = dot(cross(subtract(self.b,self.a),subtract(p,self.a)), self.normal)
                sb = dot(cross(subtract(self.c,self.b),subtract(p,self.b)), self.normal)
                sc = dot(cross(subtract(self.a,self.c),subtract(p,self.c)), self.normal)
                if sa <= 0 or sb <= 0 or sc <= 0:
                    return None
                #print(p)
                return Intersect(distance=t,
                                    point=p,
                                    normal=self.normal,
                                    texcoords=None,
                                    sceneObj=self)

        return None

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

        u = 1 - ((np.arctan2(normal[2], normal[0]) / (2 * np.pi)) + 0.5)
        v = np.arccos(-normal[1]) / np.pi

        uvs = (u,v)

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         texcoords= uvs,
                         sceneObj = self)

class Disk(object):
    def __init__(self, position, radius, normal, material):
        self.plane = Plane(position, normal, material)
        self.radius = radius
    
    def ray_intersect(self, orig, dir):

        intersect = self.plane.ray_intersect(orig, dir)

        if intersect is None:
            return None
        
        contactDistance = subtract(intersect.point, self.plane.position)
        contact = normalized(contactDistance)
        if contact <= self.radius:
            return None
        
        return Intersect(distance=intersect.distance,
                        point=intersect.point,
                        normal = self.plane.normal,
                        texcoords= None,
                        sceneObj=self)


class AABB(object):
    def __init__(self, size, position, material):
        self.size = size
        self.position = position
        self.material = material
    
        self.planes = []

        halfSizes = [0,0,0]
        halfSizes[0] = size[0] / 2
        halfSizes[1] = size[1] / 2
        halfSizes[2] = size[2] / 2

        self.planes.append(Plane(vectorAddition(position, V3(halfSizes[0], 0, 0)), V3(1,0,0), material))
        self.planes.append(Plane(vectorAddition(position, V3(-halfSizes[0], 0, 0)), V3(-1,0,0), material))


        self.planes.append(Plane(vectorAddition(position, V3(0, halfSizes[1], 0)), V3(0,1,0), material))
        self.planes.append(Plane(vectorAddition(position, V3(0, -halfSizes[1], 0)), V3(0,-1,0), material))

        self.planes.append(Plane(vectorAddition(position, V3(0, 0, halfSizes[2])), V3(0,0,1), material))
        self.planes.append(Plane(vectorAddition(position, V3(0, 0, -halfSizes[2])), V3(0,0,-1), material))

        self.boundMin = [0,0,0]
        self.boundMax = [0,0,0]

        epsilon = 0.001

        for i in range(3):
            self.boundMin[i] = self.position[i] - (epsilon + halfSizes[i])
            self.boundMax[i] = self.position[i] + (epsilon + halfSizes[i])

    def ray_intersect(self, orig, dir):
        intersect = None
        t = float('inf')

        for plane in self.planes:
            planeInter = plane.ray_intersect(orig, dir)
            if planeInter is not None:
                planePoint = planeInter.point
                if self.boundMin[0] <= planePoint[0] <= self.boundMax[0]:
                    if self.boundMin[1] <= planePoint[1] <= self.boundMax[1]:
                        if self.boundMin[2] <= planePoint[2] <= self.boundMax[2]:
                            if planeInter.distance < t:
                                t = planeInter.distance
                                intersect = planeInter


                                u,v = 0,0

                                if abs(plane.normal[0] > 0):
                                    u = (planeInter.point[1] - self.boundMin[1]) / (self.boundMax[1] - self.boundMin[1])
                                    v = (planeInter.point[2] - self.boundMin[2]) / (self.boundMax[2] - self.boundMin[2])

                                if abs(plane.normal[1] > 0):
                                    u = (planeInter.point[0] - self.boundMin[0]) / (self.boundMax[0] - self.boundMin[0])
                                    v = (planeInter.point[2] - self.boundMin[2]) / (self.boundMax[2] - self.boundMin[2])
                                
                                if abs(plane.normal[2] > 0):
                                    u = (planeInter.point[0] - self.boundMin[0]) / (self.boundMax[0] - self.boundMin[0])
                                    v = (planeInter.point[1] - self.boundMin[1]) / (self.boundMax[1] - self.boundMin[1])

        
        if intersect is None:
            return None
        
        return Intersect(distance=t,
                            point=intersect.point,
                            normal=intersect.normal,
                            texcoords=(u,v),
                            sceneObj=self)


    