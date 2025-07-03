# Segmentus
![logo.jpeg](doc/logo.jpeg)
**Segmentus** is an application designed to split text into chunks, which makes search more efficient when building RAG (Retrieval-Augmented Generation) systems. The tool is intended for developers and data scientists working with large text corpora who need to optimize the process of information retrieval and improve the performance of language models. By dividing text into manageable chunks, Segmentus helps to speed up search operations and enhance the quality of data used in machine learning and natural language processing tasks. <br/>

The main features of the project include:
* efficient text segmentation algorithms;
* flexible configuration options to adapt segmentation to specific tasks;
* an intuitive interface for easy integration into existing systems;
* support for various text formats.

## Dependency
```shell
# install dependency
pip install --upgrade pip
pip install kagglehub
pip install docling
# splitter
pip install langchain
pip install langchain_text_splitters
pip install sentence_transformers
```

## Database

## CLI 
```bash
python3 cli scratch/example/myfile.txt algorithm
``
