---
jupyter:
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 2
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython2
    version: 2.7.6
  nbformat: 4
  nbformat_minor: 5
---

::: {#590c6a7a34d91438 .cell .code execution_count="1" ExecuteTime="{\"end_time\":\"2024-05-12T20:27:22.829139Z\",\"start_time\":\"2024-05-12T20:27:22.824675Z\"}"}
``` python
text = """
Graphs are a kind of data structure which models a set of objects
(nodes) and their relationships (edges). Recently, researches on
analyzing graphs with machine learning have been receiving more and
more attention because of the great expressive power of graphs, i.e.
graphs can be used as denotation of a large number of systems across
various areas including social science (social networks (Wu et al., 2020),
natural science (physical systems (Sanchez et al., 2018; Battaglia et al.,
2016) and protein-protein interaction networks (Fout et al., 2017)),
knowledge graphs (Hamaguchi et al., 2017) and many other research
areas (Khalil et al., 2017). As a unique non-Euclidean data structure for
machine learning, graph analysis focuses on tasks such as node classifi-
cation, link prediction, and clustering. Graph neural networks (GNNs) are
deep learning based methods that operate on graph domain. Due to its
convincing performance, GNN has become a widely applied graph
analysis method recently. In the following paragraphs, we will illustrate
the fundamental motivations of graph neural networks.
"""
```
:::

::: {#initial_id .cell .code execution_count="2" ExecuteTime="{\"end_time\":\"2024-05-12T20:27:24.410074Z\",\"start_time\":\"2024-05-12T20:27:22.829970Z\"}"}
``` python
from langchain import PromptTemplate
from langchain_core.output_parsers import MarkdownListOutputParser
from langchain.chat_models import ChatOllama

llm = ChatOllama(base_url='http://127.0.0.1:11434', model="llama3:8b-instruct-q5_1")
prompt = PromptTemplate(template=open("prompt_split_en.txt", "r").read(), input_variables=['text'])
parser = MarkdownListOutputParser()
chain = prompt | llm | parser

chunks = chain.invoke({"text": text})

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stdout}
    Всего чанков: 5
    Первые N чанков:
:::

::: {.output .execute_result execution_count="2"}
    ['Graphs are a kind of data structure that models a set of objects (nodes) and their relationships (edges).',
     'Research on analyzing graphs with machine learning has been gaining attention due to the expressive power of graphs.',
     'Graph analysis focuses on tasks such as node classification, link prediction, and clustering.',
     'Graph neural networks (GNNs) are deep learning based methods that operate on graph domain.',
     'GNNs have become a widely applied graph analysis method recently.']
:::
:::
