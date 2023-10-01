from model_elements import PoligonalModel, Flash, Camera, Scene
from abc import ABC, abstractmethod


class IModelChangedObserver(ABC):
    @abstractmethod
    def apply_update_model(self):
        pass


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender):
        pass


class ModelStore(IModelChanger):
    def __init__(self):
        self.models = PoligonalModel()
        self.scenes = Scene()
        self.flashes = Flash()
        self.camera = Camera()
        self.__change_observers = IModelChangedObserver()

    def get_scena(self, num: int) -> Scene:
        return Scene()

    def notify_change(self, sender: IModelChanger):
        return sender