from contract.iview import IView
from contract.imodel import IModel
from contract.iobservable import IObservable
from contract.iactionperformer import IActionPerformer
from contract.observer import Observer
import tkinter.messagebox

class ViewTkinter(Observer, IView):
    __model: IModel
    __observable: IObservable
    __actionPerformer: IActionPerformer

    def __init__(self):
        self.__createWindow()

    def __createWindow(self):
        self.__window = tkinter.Tk()
        self.__window.title("A tiny Python MVC")
        self.__window.geometry("400x800")

    def setActionPerformer(self, actionPerformer: IActionPerformer) -> None:
        self.__actionPerformer = actionPerformer

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def showMessage(self, message: str) -> None:
        tkinter.messagebox.showinfo("A tiny Python MVC", message)
