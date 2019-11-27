class Solucion:

    def convinacionSumas(self, candidatos, target):
        candidatos.sort()
        res = set()
        intermedia = []
        self.recursion(candidatos, target, res, intermedia)
        return [list(i) for i in res]

    def recursion(self, candidatos, target, res, intermedia):
        for i in candidatos:
            if target == i:
                temp = intermedia + [i]
                temp.sort()
                if temp is not None:
                    res.add(tuple(temp))
                return
            elif target > i:
                self.recursion(candidatos, target - i, res, intermedia + [i])
            else:
                return


test = Solucion()
print(test.convinacionSumas([2, 2, 6, 7], 10))