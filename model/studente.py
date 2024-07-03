from dataclasses import dataclass


@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str

    def __eq__(self, other):  # confronto solo la matricola perché è la chiave primaria
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.matricola})"
