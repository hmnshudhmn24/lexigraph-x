from .text_ingestor import TextIngestor
from .entity_linker import EntityLinker
from .relation_extractor import RelationExtractor
from .graph_builder import GraphBuilder
from .graph_updater import GraphUpdater
class LexiGraphOrchestrator:
    def __init__(self): self.ing=TextIngestor(); self.el=EntityLinker(); self.re=RelationExtractor(); self.gb=GraphBuilder(); self.gu=GraphUpdater(); self.graph={'nodes':{},'edges':[]}
    def process(self,texts):
        for d in self.ing.ingest(texts):
            e=self.el.extract(d['text']); r=self.re.extract(d['text'],e); g=self.gb.build(e,r); self.graph=self.gu.update(self.graph,g)
        return self.graph
