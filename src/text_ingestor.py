class TextIngestor:
    def ingest(self, texts):
        return [{'id':i,'text':t} for i,t in enumerate(texts)]
