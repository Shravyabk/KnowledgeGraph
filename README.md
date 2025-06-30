#Knowledge Graph


A powerful Python-based system to detect sentence boundaries in unstructured text using a Word Graph-based approach enhanced with entropy measures from the Byte Latent Tokenizer (BLT). The model processes textual data, builds a graph representation of word transitions, and uses entropy analysis to identify potential sentence boundaries—useful for unsupervised NLP tasks like text segmentation or summarization.

Features:-

* Word Graph Generation: Builds a directed graph of word transitions from unstructured text.

* Entropy Scoring: Uses entropy of neighboring nodes to detect potential sentence boundaries.

* BLT Integration: Incorporates Byte-Level representations for deeper semantic understanding.

* Evaluation: Precision, Recall, and F1-score reporting for sentence segmentation accuracy.


Srtucture:

KnowledgeGraph/
├── blt/                         # Cloned BLT repository
│
├── blt_integration/
│   ├── data_utils.py
│   ├── detect_boundary.py
│   ├── evaluate.py
│   ├── generate_groundtruth.py
│   ├── train_blt.py
│   └── visualize_kg.py
│
├── data/
│   ├── raw_text/
│   │   └── hello.html
│   ├── kg.dot
│   ├── node_mapping.json
│   ├── node_mapping.pkl
│   ├── node2vec_embedding.pkl
│   ├── node2vec_model.pkl
│   ├── sentence_boundaries.json
│   ├── sequences.json
│   └── svo_triplets.json
│
├── outputs/
│   └── predicted_boundaries.json
│
├── .gitignore
├── build_graph.py
├── environment.yml
├── README.md
└── requirements.txt




Execution Steps:


      **  python blt_integration/visualize.py
      **  python blt_integration/evaluate.py

