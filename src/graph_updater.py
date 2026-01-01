class GraphUpdater:
    def update(self,g,n): g['nodes'].update(n['nodes']); g['edges']+=n['edges']; return g
