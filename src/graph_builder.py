class GraphBuilder:
    def build(self,e,r): return {'nodes':{x['name']:{'type':x['type'],'weight':1.0} for x in e},'edges':r}
