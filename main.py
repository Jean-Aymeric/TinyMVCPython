from controller.controller import Controller
from model.model import Model
from view.view import View
from view.viewTkinter import ViewTkinter

controller = Controller()
model = Model()
viewtk = ViewTkinter()
view = View()
controller.setModel(model)
controller.setView(viewtk)

controller.start()
