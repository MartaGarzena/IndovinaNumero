import random


#contiene la logica del gioco
class Model(object):
    def __init__(self):
        self._NMax = 100
        self._TMax = 6  #numero di vite
        self._T = self._TMax
        #self.NMin = 1
        self._segreto = None
        #random.randint(self.NMin, self.NMAx))

    def reset(self):
        self._segreto = random.randint(0, self._NMax)  #numero casuale
        self._T = self._TMax  #resetta le vite del gioco
        print("segreto: ", self._segreto)

    def play(self, guess):
        """funzione che segue un tentativo
        :param guess:int
        :return: 0 se vinco, 2 se vite finite, 1 se segreto piu grande, -1 se segreto piu piccolo"""
        # ricevo un tentatico e lo confronto con _segreto

        self._T -= 1
        if guess == self._segreto:
            return 0  #vittoria
        if self._T == 0:
            return 2  #sconfitta per numero di vite
        #se arrivo qui, ho ancora vite. Il tentativo va valutato
        if guess > self._segreto:
            return -1  #il segreto è più piccolo guess
        else:
            return 1  #il segreto è più grande del guess

    @property
    def NMax(self):
        return self._NMax

    @property
    def TMax(self):
        return self._TMax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto


if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(50))
    print(m.play(95))
