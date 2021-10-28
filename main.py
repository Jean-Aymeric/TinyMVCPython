from controller.controller import Controller
from model.model import Model
from model.modelBdd import ModelBDD
from model.modeljson import ModelJSON
from view.view import View
from view.viewTkinter import ViewTkinter

controller = Controller()
model = ModelJSON()
viewtk = ViewTkinter()
view = View()
controller.setModel(model)
controller.setView(view)

controller.start()
