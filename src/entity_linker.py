import re
class EntityLinker:
    def extract(self,text): return [{'name':w,'type':'UNKNOWN'} for w in re.findall(r'[A-Z][a-z]+',text)]
