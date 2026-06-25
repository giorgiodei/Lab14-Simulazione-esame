import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):

        self._model.creaGrafo()
        n, m = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato! "
                    f"Il grafo è costituito di {n} nodi e {m} archi")
        )

        minimo, massimo= self._model.getMinimoeMassimoValore()
        self._view.txt_result.controls.append(
            ft.Text(f"Info: Valore minimo: {minimo} -- Valore massimo: {massimo}")
        )
        self._view.update_page()

    def handle_countedges(self, e):
        valoreSoglia = self._view.txt_name.value
        try:
            valoreSoglia = int(valoreSoglia)
        except ValueError:
            self._view.create_alert("Inserire un numero intero")
            return

        if valoreSoglia <= 0:
            self._view.create_alert("Inserire un numero positivo")
            return

        valoriSottosoglia = self._model.getValoriSottoSoglia(valoreSoglia)
        valoriSopraSoglia = self._model.getValoriSopraSoglia(valoreSoglia)

        self._view.txt_result.controls.append(
            ft.Text(f"Archi con peso maggiore della soglia: {valoriSopraSoglia}")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Archi con peso minore della soglia: {valoriSopraSoglia}")
        )
        self._view.update_page()


    def handle_search(self, e):
        pass