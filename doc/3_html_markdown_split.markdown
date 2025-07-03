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

::: {#d4f25810fce9ec0 .cell .markdown}
# Нарезка HTML и Markdown документов по главам и подглавам

В данном юпитер-блокноте мы рассмотрим как можно при помощи библиотеки
LangChain нарежать на чанки документы пришедшие к нам в формате HTML и
Markdown.
:::

::: {#d0b5f9186d96d072 .cell .markdown}
## Нарезка HTML-документов

В качестве примера возъмём следующего вида HTML-документ:
:::

::: {#5e3bb41b6b8669a2 .cell .code execution_count="5" ExecuteTime="{\"end_time\":\"2024-05-12T20:24:53.059165Z\",\"start_time\":\"2024-05-12T20:24:53.056628Z\"}"}
``` python
html_string = """
<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>Foo</h1>
        <p>Some intro text about Foo.</p>
        <div>
            <h2>Bar main section</h2>
            <p>Some intro text about Bar.</p>
            <h3>Bar subsection 1</h3>
            <p>Some text about the first subtopic of Bar.</p>
            <h3>Bar subsection 2</h3>
            <p>Some text about the second subtopic of Bar.</p>
        </div>
        <div>
            <h2>Baz</h2>
            <p>Some text about Baz</p>
        </div>
        <br>
        <p>Some concluding text about Foo</p>
    </div>
</body>
</html>
"""
```
:::

::: {#1245e88228bfb53b .cell .markdown}
Используя следующие код нарежем документ на секции поменьше:
:::

::: {#initial_id .cell .code execution_count="6" ExecuteTime="{\"end_time\":\"2024-05-12T20:24:53.067260Z\",\"start_time\":\"2024-05-12T20:24:53.060289Z\"}"}
``` python
from langchain_text_splitters import HTMLHeaderTextSplitter

headers_to_split_on = [("h1", "Header 1"), ("h2", "Header 2"), ("h3", "Header 3")]
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
chunks = html_splitter.split_text(html_string)

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stdout}
    Всего чанков: 8
    Первые N чанков:
:::

::: {.output .execute_result execution_count="6"}
    [Document(page_content='Foo'),
     Document(page_content='Some intro text about Foo.  \nBar main section Bar subsection 1 Bar subsection 2', metadata={'Header 1': 'Foo'}),
     Document(page_content='Some intro text about Bar.', metadata={'Header 1': 'Foo', 'Header 2': 'Bar main section'}),
     Document(page_content='Some text about the first subtopic of Bar.', metadata={'Header 1': 'Foo', 'Header 2': 'Bar main section', 'Header 3': 'Bar subsection 1'}),
     Document(page_content='Some text about the second subtopic of Bar.', metadata={'Header 1': 'Foo', 'Header 2': 'Bar main section', 'Header 3': 'Bar subsection 2'}),
     Document(page_content='Baz', metadata={'Header 1': 'Foo'}),
     Document(page_content='Some text about Baz', metadata={'Header 1': 'Foo', 'Header 2': 'Baz'}),
     Document(page_content='Some concluding text about Foo', metadata={'Header 1': 'Foo'})]
:::
:::

::: {#e72962943ba698aa .cell .markdown}
## Нарезка Markdown-документа

Следующий пример похож на предыдущий, но тут мы уже будем нарезать на
чанки Markdown-документ:
:::

::: {#ec33bab52cf0e2b3 .cell .code execution_count="7" ExecuteTime="{\"end_time\":\"2024-05-12T20:24:53.070185Z\",\"start_time\":\"2024-05-12T20:24:53.068102Z\"}"}
``` python
markdown_string = """
# Foo
## Bar
Hi this is Jim
Hi this is Joe

### Boo
Hi this is Lance

## Baz
Hi this is Molly
"""
```
:::

::: {#106760067f80e901 .cell .markdown}
Код нарезки выглдяти следующим образом:
:::

::: {#66ce873fc457d99d .cell .code execution_count="8" ExecuteTime="{\"end_time\":\"2024-05-12T20:24:53.075921Z\",\"start_time\":\"2024-05-12T20:24:53.071512Z\"}"}
``` python
from langchain_text_splitters import MarkdownHeaderTextSplitter

headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
chunks = markdown_splitter.split_text(markdown_string)

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stdout}
    Всего чанков: 3
    Первые N чанков:
:::

::: {.output .execute_result execution_count="8"}
    [Document(page_content='Hi this is Jim\nHi this is Joe', metadata={'Header 1': 'Foo', 'Header 2': 'Bar'}),
     Document(page_content='Hi this is Lance', metadata={'Header 1': 'Foo', 'Header 2': 'Bar', 'Header 3': 'Boo'}),
     Document(page_content='Hi this is Molly', metadata={'Header 1': 'Foo', 'Header 2': 'Baz'})]
:::
:::

::: {#270ac7e7b32b4322 .cell .markdown}
Как видно из результата работы класс, нарезка Markdown более совершенна
чем нарезка HTML, так как не создаются дубликаты, именно поэтому
Markdown этом формат который я предпочитаю при создании RAG систем.
:::
