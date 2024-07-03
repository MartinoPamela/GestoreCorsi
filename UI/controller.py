import flet as ft


# il controller deve sempre gestire gli input dell'utente, per vedere se ci sono errori, se non è stato dato
# il controller è quasi sempre fatto così, c'è gestione dell'errore, chiamata al modello e stampa di risultati,
# o comunque fare qualcosa che modifichi l'interfaccia grafica
class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._pd = None

    def get_corsi_periodo(self, e):
        """
        questo metodo deve leggere da una tendina il periodo didattico, poi deve chiedere al modello di dargli tutti i
        corsi di quel periodo didattico e poi stamparli
        per leggerli dal menù a tendina posso leggerlo qui dentro con una variabile oppure posso nella view definire un
        metodo che viene chiamato ogni volta che la tendina viene consultata
        """
        # pd = self._view.dd_periodo.value
        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico")
            return
        corsi = self._model.get_corsi_periodo(self._pd)
        self._view.lst_result.controls.clear()
        for corso in corsi:
            self._view.lst_result.controls.append(ft.Text(corso))
        self._view.update_page()

    def get_studenti_periodo(self, e):
        """
        Deve stampre il numero totale di studenti iscritti a corsi attivi in un determinato periodo didattico
        """
        if self._pd is None:
            self._view.create_alert("Selezionare un periodo didattico")
            return
        numero_studenti = self._model.get_numero_studenti_periodo(self._pd)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"Gli studenti iscritti a corsi del periodo didattico {self._pd}"
                                                      f" sono: {numero_studenti}"))
        self._view.update_page()

    def get_studenti_corso(self, e):
        pass

    def get_dettaglio_corso(self, e):
        pass

    def leggi_tendina(self, e):
        self._pd = int(e.control.value)  # visto che questo è un evento chiamato dalla tendina stessa possiamo accedere
        # al suo contenuto anche utilizzando l'evento
