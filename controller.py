from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNMax(self):
        return self._model.NMax

    def getTMax(self):
        return self._model.TMax

    def reset(self, event):
        self._model.reset()
        self._view._txtOutT.value = self._model.T
        self._view._lv.controls.clear()
        self._view._btnPlay.disabled = False
        self._view._txtIn.disabled = False
        self._view._lv.controls.append(ft.Text("Indovina il numeros!!"))
        self._view.update()

    def play(self, event):


        tentativoStr = self._view._txtIn.value #è una string

        self._view._txtIn.value = ""
        self._view._txtOutT.value = self._model.T-1

        if tentativoStr == "":
            self._view._lv.controls.append(ft.Text("Inserisci qualcosa su", color="red"))
            self._view.update()
            return

        try:
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lv.controls.append(ft.Text("Inserisci un NUMEROO", color="red"))
            self._view.update()
            return

        res = self._model.play(tentativo) #0 se vinco, 2 se vite finite, 1 se segreto piu grande, -1 se segreto piu piccolo
        if res == 0:
            self._view._lv.controls.append(ft.Text(f"Hai vinto, il numero era {tentativoStr}", color="green"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res == 2:
            self._view._lv.controls.append(ft.Text(f"Hai perso, vite finite. Il numero era: {self._model.segreto}", color="red"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res == 1:
            self._view._lv.controls.append(ft.Text(f"Il numero segreto è piu grande di {tentativoStr}", color="orange"))
            self._view.update()
            return
        elif res == -1:
            self._view._lv.controls.append(ft.Text(f"Il numero segreto è piu piccolo di {tentativoStr}", color="orange"))
            self._view.update()
            return

        self._view.update()
