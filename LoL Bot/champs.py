

class champs:
    
    def caitlyn(self):
        spells = [1, 3, 1, 3, 1, 4, 1, 3, 1, 3, 4, 3, 2, 2, 2, 4, 2, 2]
        activespells = ['q', 'e']
        placement = [(1182, 197), (998, 318)]
        cdq = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        cde = [18, 18, 18, 16, 16, 16, 16, 14, 14, 12, 12, 10, 10, 10, 10, 10, 10, 10]
        return spells, activespells, placement, cdq, cde

    def ashe(self):
        spells = [2, 3, 2, 3, 2, 4, 2, 3, 2, 3, 4, 3, 1, 1, 1, 4, 1, 1]
        activespells = ['q']
        placement = [(1, 1)]
        cdq = [10, 9, 8, 7, 6]
        cde = []
        return spells, activespells, placement, cdq, cde

    def graves(self):
        spells = [1, 3, 1, 2, 1, 4, 1, 3, 1, 3, 4, 3, 3, 2, 2, 4, 2, 2]
        activespells = ['q', 'e']
        placement = [(1, 1), (1, 1)]
        cdq = [12, 11, 10, 9, 8]
        cde = [7]
        return spells, activespells, placement, cdq, cde
