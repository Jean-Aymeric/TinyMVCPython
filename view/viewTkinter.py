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
        self.__window.geometry("400x200")
        self.__message = tkinter.StringVar(value="TOTO")
        tkinter.Label(self.__window, textvariable=self.__message).pack()
        self.__num = tkinter.IntVar(value=0)
        tkinter.Label(self.__window, textvariable="Entrez un numéro :").pack()
        tkinter.Entry(self.__window, textvariable=self.__num).pack()
        self.__num.trace_add("write", self.__numChange)

    def setActionPerformer(self, actionPerformer: IActionPerformer) -> None:
        self.__actionPerformer = actionPerformer

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def showMessage(self, message: str) -> None:
        self.__message.set(message)
        self.__window.update_idletasks()

    def askNum(self) -> int:
        self.__window.mainloop()

    def __numChange(self, *args):
        self.__actionPerformer.performUpdateNum(self.__num.get())
