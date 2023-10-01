class Point3D:
    pass


class Angle3D:
    pass


class Color:
    pass


class Type:
    pass


class Poligon:
    def __init__(self):
        self.points = Point3D()


class Texture:
    pass


class PoligonalModel:
    def __init__(self):
        self.poligons = Poligon()
        self.textures = Texture()


class Flash:
    def __init__(self):
        self.location = Point3D()
        self.angle = Angle3D()
        self.color = Color()
        self.power = float()

    def rotate(self, angle3d):
        pass

    def move(self, point3d):
        pass


class Scene:
    def __init__(self):
        self.id = int()
        self.models = [PoligonalModel]
        self.flashes = Flash()
        self.camera = [Camera]

    def method_1(self, type: Type) -> Type:
        return type

    def method_2(self, type_1: Type, type_2: Type) -> Type:
        return type_1


class Camera:
    def __init__(self):
        self.location = Point3D()
        self.angle = Angle3D()

    def rotate(self, angle3d):
        pass

    def move(self, point3d):
        pass