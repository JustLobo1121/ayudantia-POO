class Jugador:
    def __init__(self, n):
        self.n = n

class Rana:
    def __init__(self, c, d):
        self.c = c
        self.d = d

class Laguna:
    def __init__(self, j):
        self.j = j
        self.p = [Rana('V', 1) for _ in range(3)] + [None] + [Rana('R', -1) for _ in range(3)]

    def estado(self):
        print([r.c[0] if r else '_' for r in self.p])

    def mover(self, i):
        if not (0 <= i < 7) or not self.p[i]: return False
        r = self.p[i]
        s1, s2 = i + r.d, i + (r.d * 2)

        if 0 <= s1 < 7 and not self.p[s1]:
            self.p[s1], self.p[i] = r, None
        elif 0 <= s2 < 7 and not self.p[s2] and self.p[s1]:
            self.p[s2], self.p[i] = r, None
        else:
            print("Error")
            return False
        return True

    def victoria(self):
        return [r.c[0] if r else '_' for r in self.p] == ['R','R','R','_','V','V','V']

    def posibles(self):
        for i, r in enumerate(self.p):
            if r:
                s1, s2 = i + r.d, i + (r.d * 2)
                if 0 <= s1 < 7 and not self.p[s1]: return True
                if 0 <= s2 < 7 and not self.p[s2] and self.p[s1]: return True
        return False

def main():
    l = Laguna(Jugador(input("Jugador: ")))
    while True:
        l.estado()
        if l.victoria():
            print("Ganaste")
            break
        if not l.posibles():
            print("Bloqueo")
            break
        l.mover(int(input("  0    1    2    3    4    5    6   mov: ")))

if __name__ == "__main__":
    main()