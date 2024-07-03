from database.corso_dao import CorsoDao


class Model:

    def __init__(self):
        self.corsi = CorsoDao.get_all_corsi()

    def get_corsi_periodo(self, pd):
        # soluzione con filtro sul periodo fatto da python
        corsi_periodo = []
        for corso in self.corsi:
            if corso.pd == pd:
                corsi_periodo.append(corso)
        return corsi_periodo

        # soluzione con filtro sul periodo fatto nella query
        # return CorsoDao.get_corsi_periodo(pd)

    def get_numero_studenti_periodo(self, pd):
        # soluzione programmatica
        matricole_iscritti = set()  # nel set gli oggetti compaiono una volta sola, non vengono ripetuti,
        # quindi mi serve per mettere tutte le matricole non ripetute
        for corso in self.corsi:
            if corso.pd == pd:
                if corso.matricole is None:
                    corso.matricole = CorsoDao.get_matricole_corso(corso.codins)
                matricole_iscritti = matricole_iscritti.union(corso.matricole)
        return len(matricole_iscritti)

        # soluzione con join da SQL
        # return CorsoDao.get_numero_studenti_periodo(pd)

