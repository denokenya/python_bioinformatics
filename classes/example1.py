class Molecule:
    def __init__(self, name):
        if not name:
            raise Exception("Name must be set to something")
        self.name = name

    def getName(self):
        return self.name

    def getCapitalizedName(self):
        name = self.getName()
        return name.capitalize()


class Protein(Molecule):

    def __init__(self, name, sequence):
        Molecule.__init__(self, name)
        self.aminoAcids = []

        for code in sequence:
            aminoAcid = AminoAcid(code)
            self.aminoAcids.append(aminoAcid)

        def getAminoAcids(self):
            return self.aminoAcids

        def getSequence(self):
            return [aminoAcid.code for aminoAcid in self.aminoAcids]

        def getMass(self):
            mass = 18.0
            aminoAcids = self.getAminoAcids()
            for aminoAcid in aminoAcids():
                mass += aminoAcid.getMass()
            return mass


class AminoAcid:
    massDict = {
        "A": 71.07, "R": 156.18, "N": 114.08, "D": 115.08,
        "C": 103.10, "Q": 128.13, "E": 129.11, "G": 57.05,
        "H": 137.14, "I": 113.15, "L": 113.15, "K": 128.17,
        "M": 131.19, "F": 147.17, "P": 97.11, "S": 87.07,
        "T": 101.10, "W": 186.20, "Y": 163.17, "V": 99.13
    }
    acceptableCodes = set(massDict.keys())

    def __init__(self, code):
        if code not in self.acceptableCodes:
            text = 'code ="%s", must be in list %s'
            raise Exception(text % (code, sorted(self.acceptableCodes)))
        self.code = code

    def getMass(self):
        return self.massDict[self.code]


water = Molecule('Aqua')
print("molecule attributes")
print("molecule name =", water.name)

print("Molecule function calls")
print("molecule name =", water.getName())
print("molecule capitalisedName =", water.getCapitalizedName())

myProtein = Protein("Fictitious", "MPLAILV")
print("protein attributes")
print("protein name =", myProtein.name)
print("protein amino acids =", myProtein.aminoAcids)

print("protein function calls")
print("protein name=", myProtein.getName())
print("protein amino acids =", myProtein.getAminoAcids())
print("protein sequence=", myProtein.getSequence())
print("protein mass =", myProtein.getMass())
