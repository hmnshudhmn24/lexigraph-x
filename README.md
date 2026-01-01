# LexiGraph-X 

**LexiGraph-X** is a **Level-5 NLP-driven knowledge graph engine** that builds and continuously updates **dynamic knowledge graphs** from raw text streams.

It combines **entity linking, relation extraction, temporal graph updates, and context-aware node weighting**, enabling intelligent graph construction from unstructured data.



## 🚀 Key Capabilities

- 🧠 Entity Linking  
- 🔗 Relation Extraction  
- ⏱️ Temporal Graph Updates  
- 🎯 Context-Aware Node Weighting  
- 🕸️ Dynamic Knowledge Graph Construction  
- 🤗 Hugging Face–Ready (`graph-ml`)  


## 🧠 System Architecture

```
Raw Text Stream
   ↓
Text Ingestor
   ↓
Entity Linker
   ↓
Relation Extractor
   ↓
Context Encoder
   ↓
Graph Builder
   ↓
Temporal Graph Updater
   ↓
Node Weighting
   ↓
Dynamic Knowledge Graph
```



## 📥 Input Format

```json
{
  "texts": [
    "OpenAI developed ChatGPT.",
    "ChatGPT is used by developers worldwide."
  ]
}
```



## 📤 Output Format

```json
{
  "nodes": [
    {
      "name": "OpenAI",
      "type": "ORG",
      "weight": 1.05
    },
    {
      "name": "ChatGPT",
      "type": "TECH",
      "weight": 1.05
    }
  ],
  "edges": [
    {
      "source": "OpenAI",
      "relation": "developed_by",
      "target": "ChatGPT"
    }
  ]
}
```



## 🛠️ Installation & Usage

```bash
git clone https://huggingface.co/<your-username>/lexigraph-x
cd lexigraph-x
python inference.py
```



## 📁 Project Structure

```
lexigraph-x/
├── configs/
├── data/
├── src/
├── inference.py
├── evaluation.py
├── README.md
├── model_card.md
├── LICENSE
└── requirements.txt
```



## 🎯 Use Cases

- Knowledge graph construction  
- NLP-driven information extraction  
- Research in graph intelligence  
- Text-to-graph pipelines  



## 🔮 Future Improvements

- Transformer-based NER
- Graph Neural Networks
- Knowledge graph visualization



## 📜 License

Apache License 2.0

