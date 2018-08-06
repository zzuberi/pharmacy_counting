# Class to hold each record an allow sorting
class Record:
    def __init__(self,med,name,initcost):
        self.med = med
        self.names = set([self.cleanName(name)])
        self.totcost = float(initcost)
        
    def addName(self,name):
        self.names.add(self.cleanName(name))
        
    def addVal(self,cost):
        if cost is not '':
            self.totcost += float(cost)
        
    def nameCount(self):
        return len(self.names)
    
    def totVal(self):
        if self.totcost.is_integer():
            return int(self.totcost)
        return '{:.2f}'.format(self.totcost)
    
    def cleanName(self,names):
        for name in names:
            if name is not '':
                name = str.upper(name[0]) + str.lower(name[1:])
        return names[0]+names[1]
    
    def __lt__(self,other):
        if self.totcost < other.totcost:
            return True
        elif self.totcost == other.totcost and self.med > other.med:
            return True
        else:
            return False