from controller.controller import Controller
from model.model import Model
from view.view import View
from view.viewTkinter import ViewTkinter

controller = Controller()
model = Model()
view = ViewTkinter()
controller.setModel(model)
controller.setView(view)

controller.start()
