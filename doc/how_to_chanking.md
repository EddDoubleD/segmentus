::: {#55eb8474d4ccd12d .cell .markdown}

Нарезка чанков фиксированной длинны
В данном блокноте мы рассмотрим два самых базовых метода нарезки текста н чанки, первый из них будет резать входной текст на стройки фиксированной длинны. :::

::: {#bf8351aff2175441 .cell .markdown}

Решение без сторонних библиотек
В данном примере используется текст Конституции Российской Федерации. :::

::: {#dad600d4afe24240 .cell .code execution_count="1" ExecuteTime="{"end_time":"2024-05-12T20:23:33.935491Z","start_time":"2024-05-12T20:23:33.931807Z"}"}

file_path = 'constitutionrf.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
:::

::: {#acdb5f95ca947ca8 .cell .markdown} Далее передадим прочитанный текст на вход функции, которая нарежет его на строки фиксированной длинны. :::

::: {#initial_id .cell .code execution_count="2" ExecuteTime="{"end_time":"2024-05-12T20:23:33.943543Z","start_time":"2024-05-12T20:23:33.936086Z"}"}

def simple_text_splitter(text: str, chunk_length: int = 200):
    chunks = [text[i:i + chunk_length] for i in range(0, len(text), chunk_length)]
    return chunks


chunks = simple_text_splitter(text)

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
::: {.output .stream .stdout} Всего чанков: 638 Первые N чанков: :::

::: {.output .execute_result execution_count="2"} ['\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ\n\n\nМы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,\nсохраняя', ' исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,\nчтя память предков, передавших нам любовь и уважение к Отечеству, веру в до', 'бро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,\nстремясь обеспечить благополучие и процветание России,\nисходя из ответственности', ' за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,\nпринимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.\n\nРАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСта', 'тья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.\n\n\nСтатья 2', '\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.\n\nСтатья 3\n\n1. Носителем суверенитета и единствен', 'ным источником власти в Российской Федерации является ее многонациональный народ.\n2. Народ осуществляет свою власть непосредственно, а также через органы государственной власти и органы местного самоу', 'правления.\n3. Высшим непосредственным выражением власти народа являются референдум и свободные выборы.\n4. Никто не может присваивать власть в Российской Федерации. Захват власти или присвоение властны', 'х полномочий преследуются по федеральному закону.\n\nСтатья 4\n\n1. Суверенитет Российской Федерации распространяется на всю ее территорию.\n2. Конституция Российской Федерации и федеральные законы имеют в', 'ерховенство на всей территории Российской Федерации.\n3. Российская Федерация обеспечивает целостность и неприкосновенность своей территории.\n\nСтатья 5\n\n1. Российская Федерация состоит из республик, кр'] ::: :::

::: {#e0c184c7aaa9d529 .cell .markdown} В данном примере реализуем примерно то же самое, что и выше, но через класс CharacterTextSplitter из библиотеки LangChain. :::

::: {#c7a98c0bec7c4234 .cell .code execution_count="3" ExecuteTime="{"end_time":"2024-05-12T20:23:34.102954Z","start_time":"2024-05-12T20:23:33.943981Z"}"}

from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=200,
    chunk_overlap=20
)

chunks = text_splitter.create_documents([text])

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
::: {.output .stream .stderr} Created a chunk of size 705, which is longer than the specified 200 Created a chunk of size 486, which is longer than the specified 200 Created a chunk of size 279, which is longer than the specified 200 Created a chunk of size 862, which is longer than the specified 200 Created a chunk of size 434, which is longer than the specified 200 Created a chunk of size 518, which is longer than the specified 200 Created a chunk of size 328, which is longer than the specified 200 Created a chunk of size 292, which is longer than the specified 200 Created a chunk of size 201, which is longer than the specified 200 Created a chunk of size 628, which is longer than the specified 200 Created a chunk of size 223, which is longer than the specified 200 Created a chunk of size 626, which is longer than the specified 200 Created a chunk of size 207, which is longer than the specified 200 Created a chunk of size 1001, which is longer than the specified 200 Created a chunk of size 312, which is longer than the specified 200 Created a chunk of size 382, which is longer than the specified 200 Created a chunk of size 239, which is longer than the specified 200 Created a chunk of size 565, which is longer than the specified 200 Created a chunk of size 296, which is longer than the specified 200 Created a chunk of size 325, which is longer than the specified 200 Created a chunk of size 246, which is longer than the specified 200 Created a chunk of size 300, which is longer than the specified 200 Created a chunk of size 371, which is longer than the specified 200 Created a chunk of size 284, which is longer than the specified 200 Created a chunk of size 308, which is longer than the specified 200 Created a chunk of size 279, which is longer than the specified 200 Created a chunk of size 647, which is longer than the specified 200 Created a chunk of size 266, which is longer than the specified 200 Created a chunk of size 632, which is longer than the specified 200 Created a chunk of size 269, which is longer than the specified 200 Created a chunk of size 448, which is longer than the specified 200 Created a chunk of size 371, which is longer than the specified 200 Created a chunk of size 815, which is longer than the specified 200 Created a chunk of size 229, which is longer than the specified 200 Created a chunk of size 371, which is longer than the specified 200 Created a chunk of size 461, which is longer than the specified 200 Created a chunk of size 792, which is longer than the specified 200 Created a chunk of size 686, which is longer than the specified 200 Created a chunk of size 418, which is longer than the specified 200 Created a chunk of size 467, which is longer than the specified 200 Created a chunk of size 292, which is longer than the specified 200 Created a chunk of size 384, which is longer than the specified 200 Created a chunk of size 339, which is longer than the specified 200 Created a chunk of size 387, which is longer than the specified 200 Created a chunk of size 260, which is longer than the specified 200 Created a chunk of size 307, which is longer than the specified 200 Created a chunk of size 589, which is longer than the specified 200 Created a chunk of size 628, which is longer than the specified 200 Created a chunk of size 415, which is longer than the specified 200 Created a chunk of size 211, which is longer than the specified 200 Created a chunk of size 723, which is longer than the specified 200 Created a chunk of size 592, which is longer than the specified 200 Created a chunk of size 10050, which is longer than the specified 200 Created a chunk of size 1047, which is longer than the specified 200 Created a chunk of size 1061, which is longer than the specified 200 Created a chunk of size 1196, which is longer than the specified 200 Created a chunk of size 727, which is longer than the specified 200 Created a chunk of size 565, which is longer than the specified 200 Created a chunk of size 426, which is longer than the specified 200 Created a chunk of size 3893, which is longer than the specified 200 Created a chunk of size 2533, which is longer than the specified 200 Created a chunk of size 239, which is longer than the specified 200 Created a chunk of size 410, which is longer than the specified 200 Created a chunk of size 1429, which is longer than the specified 200 Created a chunk of size 379, which is longer than the specified 200 Created a chunk of size 1359, which is longer than the specified 200 Created a chunk of size 1826, which is longer than the specified 200 Created a chunk of size 1446, which is longer than the specified 200 Created a chunk of size 551, which is longer than the specified 200 Created a chunk of size 215, which is longer than the specified 200 Created a chunk of size 840, which is longer than the specified 200 Created a chunk of size 1324, which is longer than the specified 200 Created a chunk of size 282, which is longer than the specified 200 Created a chunk of size 804, which is longer than the specified 200 Created a chunk of size 561, which is longer than the specified 200 Created a chunk of size 6595, which is longer than the specified 200 Created a chunk of size 587, which is longer than the specified 200 Created a chunk of size 797, which is longer than the specified 200 Created a chunk of size 316, which is longer than the specified 200 Created a chunk of size 476, which is longer than the specified 200 Created a chunk of size 290, which is longer than the specified 200 Created a chunk of size 309, which is longer than the specified 200 Created a chunk of size 322, which is longer than the specified 200 Created a chunk of size 1005, which is longer than the specified 200 Created a chunk of size 769, which is longer than the specified 200 Created a chunk of size 1719, which is longer than the specified 200 Created a chunk of size 2382, which is longer than the specified 200 Created a chunk of size 676, which is longer than the specified 200 Created a chunk of size 1184, which is longer than the specified 200 Created a chunk of size 548, which is longer than the specified 200 Created a chunk of size 453, which is longer than the specified 200 Created a chunk of size 322, which is longer than the specified 200 Created a chunk of size 795, which is longer than the specified 200 Created a chunk of size 3251, which is longer than the specified 200 Created a chunk of size 2875, which is longer than the specified 200 Created a chunk of size 391, which is longer than the specified 200 Created a chunk of size 819, which is longer than the specified 200 Created a chunk of size 1014, which is longer than the specified 200 Created a chunk of size 416, which is longer than the specified 200 Created a chunk of size 1542, which is longer than the specified 200 Created a chunk of size 1292, which is longer than the specified 200 Created a chunk of size 952, which is longer than the specified 200 Created a chunk of size 1474, which is longer than the specified 200 Created a chunk of size 1248, which is longer than the specified 200 Created a chunk of size 2517, which is longer than the specified 200 Created a chunk of size 446, which is longer than the specified 200 Created a chunk of size 3157, which is longer than the specified 200 Created a chunk of size 630, which is longer than the specified 200 Created a chunk of size 3137, which is longer than the specified 200 Created a chunk of size 455, which is longer than the specified 200 Created a chunk of size 614, which is longer than the specified 200 Created a chunk of size 782, which is longer than the specified 200 Created a chunk of size 242, which is longer than the specified 200 Created a chunk of size 459, which is longer than the specified 200 Created a chunk of size 202, which is longer than the specified 200 Created a chunk of size 5282, which is longer than the specified 200 Created a chunk of size 640, which is longer than the specified 200 Created a chunk of size 647, which is longer than the specified 200 Created a chunk of size 1012, which is longer than the specified 200 Created a chunk of size 1906, which is longer than the specified 200 Created a chunk of size 363, which is longer than the specified 200 Created a chunk of size 1119, which is longer than the specified 200 Created a chunk of size 923, which is longer than the specified 200 Created a chunk of size 399, which is longer than the specified 200 Created a chunk of size 383, which is longer than the specified 200 Created a chunk of size 947, which is longer than the specified 200 Created a chunk of size 272, which is longer than the specified 200 Created a chunk of size 580, which is longer than the specified 200 Created a chunk of size 4393, which is longer than the specified 200 :::

::: {.output .stream .stdout} Всего чанков: 265 Первые N чанков: :::

::: {.output .execute_result execution_count="3"} [Document(page_content='\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ'), Document(page_content='Мы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,\nсохраняя исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,\nчтя память предков, передавших нам любовь и уважение к Отечеству, веру в добро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,\nстремясь обеспечить благополучие и процветание России,\nисходя из ответственности за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,\nпринимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.'), Document(page_content='РАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСтатья 1'), Document(page_content='Статья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.'), Document(page_content='Статья 2\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.\n\nСтатья 3'), Document(page_content='1. Носителем суверенитета и единственным источником власти в Российской Федерации является ее многонациональный народ.\n2. Народ осуществляет свою власть непосредственно, а также через органы государственной власти и органы местного самоуправления.\n3. Высшим непосредственным выражением власти народа являются референдум и свободные выборы.\n4. Никто не может присваивать власть в Российской Федерации. Захват власти или присвоение властных полномочий преследуются по федеральному закону.'), Document(page_content='Статья 4'), Document(page_content='1. Суверенитет Российской Федерации распространяется на всю ее территорию.\n2. Конституция Российской Федерации и федеральные законы имеют верховенство на всей территории Российской Федерации.\n3. Российская Федерация обеспечивает целостность и неприкосновенность своей территории.'), Document(page_content='Статья 5'), Document(page_content='1. Российская Федерация состоит из республик, краев, областей, городов федерального значения, автономной области, автономных округов - равноправных субъектов Российской Федерации.\n2. Республика (государство) имеет свою конституцию и законодательство. Край, область, город федерального значения, автономная область, автономный округ имеет свой устав и законодательство.\n3. Федеративное устройство Российской Федерации основано на ее государственной целостности, единстве системы государственной власти, разграничении предметов ведения и полномочий между органами государственной власти Российской Федерации и органами государственной власти субъектов Российской Федерации, равноправии и самоопределении народов в Российской Федерации.\n4. Во взаимоотношениях с федеральными органами государственной власти все субъекты Российской Федерации между собой равноправны.')] ::: :::

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

::: {#2ffcf1031a9a6965 .cell .markdown}
# Рекурсивная нарезка текста на чанки с использованием LangChain

В данном Jupyter-блокноте мы исследуем метод рекурсивной нарезки текста
с помощью класса RecursiveCharacterTextSplitter из библиотеки LangChain.
Этот метод позволяет эффективно разделить текст на смысловые единицы,
такие как абзацы и предложения, сохраняя при этом их семантическую
целостность. Рекурсивная нарезка особенно полезна в случаях, когда
необходимо максимально учитывать контекстуальные и структурные границы
текста для последующих задач обработки естественного языка.
:::

::: {#6a02d4124525b8d2 .cell .markdown}
## Базовый пример рекурсивной нарезки текста

В данном примере используется текст Конституции Российской Федерации.
:::

::: {#c30e062bdc978d20 .cell .code execution_count="6" ExecuteTime="{\"end_time\":\"2024-05-12T20:24:36.817579Z\",\"start_time\":\"2024-05-12T20:24:36.815049Z\"}"}
``` python
file_path = 'constitutionrf.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
```
:::

::: {#b456c2a6925e4fb4 .cell .markdown}
Создадим объект класса `RecursiveCharacterTextSplitter` и далее
передадим на вход метода create_documents массив из текстовых
документов, после чего отобразим статистическую информацию.
:::

::: {#initial_id .cell .code execution_count="7" ExecuteTime="{\"end_time\":\"2024-05-12T20:24:36.843530Z\",\"start_time\":\"2024-05-12T20:24:36.818761Z\"}"}
``` python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

chunks = text_splitter.create_documents([text])

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stdout}
    Всего чанков: 998
    Первые N чанков:
:::

::: {.output .execute_result execution_count="7"}
    [Document(page_content='\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ'),
     Document(page_content='Мы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,'),
     Document(page_content='сохраняя исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,'),
     Document(page_content='чтя память предков, передавших нам любовь и уважение к Отечеству, веру в добро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,'),
     Document(page_content='стремясь обеспечить благополучие и процветание России,\nисходя из ответственности за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,'),
     Document(page_content='принимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.'),
     Document(page_content='РАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСтатья 1'),
     Document(page_content='Статья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.'),
     Document(page_content='Статья 2\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.\n\nСтатья 3'),
     Document(page_content='1. Носителем суверенитета и единственным источником власти в Российской Федерации является ее многонациональный народ.')]
:::
:::

::: {#15d4e258980260ea .cell .markdown}
## Нарезка текста состоящего из иероглифов

А в данном примере мы через параметр `separators` заменим разделители
текста по умолчанию на CJK разделители.
:::

::: {#c5882fe0933a5ae .cell .code execution_count="8" ExecuteTime="{\"end_time\":\"2024-05-12T20:24:36.863298Z\",\"start_time\":\"2024-05-12T20:24:36.844462Z\"}"}
``` python
text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n", "\n", " ", ".", ",",
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        ""  # Последний элемент в списке пытается делить текст на максимально маленькие части
    ],
    chunk_size=200,
    chunk_overlap=20
)

chunks = text_splitter.create_documents([text])

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stdout}
    Всего чанков: 998
    Первые N чанков:
:::

::: {.output .execute_result execution_count="8"}
    [Document(page_content='\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ'),
     Document(page_content='Мы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,'),
     Document(page_content='сохраняя исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,'),
     Document(page_content='чтя память предков, передавших нам любовь и уважение к Отечеству, веру в добро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,'),
     Document(page_content='стремясь обеспечить благополучие и процветание России,\nисходя из ответственности за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,'),
     Document(page_content='принимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.'),
     Document(page_content='РАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСтатья 1'),
     Document(page_content='Статья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.'),
     Document(page_content='Статья 2\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.\n\nСтатья 3'),
     Document(page_content='1. Носителем суверенитета и единственным источником власти в Российской Федерации является ее многонациональный народ.')]
:::
:::

::: {#5335d5993ba7d784 .cell .markdown}
## Рекурсивная нарезка JSON документов

В данном примере мы нарежем JSON-файл имеющий структуру описанную
стандартом OpenAPI.
:::

::: {#cbbade4f1d25b20f .cell .code execution_count="9" ExecuteTime="{\"end_time\":\"2024-05-12T20:24:37.408975Z\",\"start_time\":\"2024-05-12T20:24:36.863957Z\"}"}
``` python
import requests

json_url = "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v3.0/uspto.json"
json_data = requests.get(json_url).json()
```
:::

::: {#8fb7b4a34237f4e2 .cell .code execution_count="10" ExecuteTime="{\"end_time\":\"2024-05-12T20:24:37.413688Z\",\"start_time\":\"2024-05-12T20:24:37.410104Z\"}"}
``` python
from langchain_text_splitters import RecursiveJsonSplitter

json_splitter = RecursiveJsonSplitter(max_chunk_size=300)
json_chunks = json_splitter.split_json(json_data=json_data)

print(f"Всего чанков: {len(json_chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stdout}
    Всего чанков: 58
    Первые N чанков:
:::

::: {.output .execute_result execution_count="10"}
    [Document(page_content='\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ'),
     Document(page_content='Мы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,'),
     Document(page_content='сохраняя исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,'),
     Document(page_content='чтя память предков, передавших нам любовь и уважение к Отечеству, веру в добро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,'),
     Document(page_content='стремясь обеспечить благополучие и процветание России,\nисходя из ответственности за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,'),
     Document(page_content='принимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.'),
     Document(page_content='РАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСтатья 1'),
     Document(page_content='Статья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.'),
     Document(page_content='Статья 2\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.\n\nСтатья 3'),
     Document(page_content='1. Носителем суверенитета и единственным источником власти в Российской Федерации является ее многонациональный народ.')]
:::
:::

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

::: {#446f7b592b327ef5 .cell .markdown}
# Нарезка документов при помощи токенизатора

В данном юпитер-блокноте мы рассмотрим как можно при помощи библиотеки
LangChain нарезать на чанки при помощи комбинации из посимвольной
нарезки и токенизаторов.
:::

::: {#93ab778a21a9860 .cell .markdown}
## Решение без сторонних библиотек

В данном примере используется текст Конституции Российской Федерации.
:::

::: {#7a808703fde979a0 .cell .code execution_count="6" ExecuteTime="{\"end_time\":\"2024-05-12T20:25:34.469575Z\",\"start_time\":\"2024-05-12T20:25:34.467272Z\"}"}
``` python
file_path = 'constitutionrf.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
```
:::

::: {#d3003dda3adac819 .cell .markdown}
## Нарезка при помощи токенизатора TikToken

Подгрузим класс `CharacterTextSplitter`, но инициализацию выполним при
помощи метода `from_tiktoken_encoder`, данный метод сделает вызов метода
`encode` из пакета `tiktoken`, определи eos и bos токены, после чего
попытается нарезать документ таким образом, чтобы размер чанков не
выходил за указанные пределы.
:::

::: {#initial_id .cell .code execution_count="7" ExecuteTime="{\"end_time\":\"2024-05-12T20:25:34.540166Z\",\"start_time\":\"2024-05-12T20:25:34.470315Z\"}"}
``` python
from langchain_text_splitters import CharacterTextSplitter
from pprint import pprint

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    #encoding=get_encoding('cl100k_base'),  # В новых версия LangChain эту опция более недоступна
    chunk_size=200,
    chunk_overlap=20
)
chunks = text_splitter.split_text(text)

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stderr}
    Created a chunk of size 787, which is longer than the specified 200
    Created a chunk of size 514, which is longer than the specified 200
    Created a chunk of size 301, which is longer than the specified 200
    Created a chunk of size 919, which is longer than the specified 200
    Created a chunk of size 461, which is longer than the specified 200
    Created a chunk of size 557, which is longer than the specified 200
    Created a chunk of size 354, which is longer than the specified 200
    Created a chunk of size 315, which is longer than the specified 200
    Created a chunk of size 214, which is longer than the specified 200
    Created a chunk of size 675, which is longer than the specified 200
    Created a chunk of size 237, which is longer than the specified 200
    Created a chunk of size 674, which is longer than the specified 200
    Created a chunk of size 215, which is longer than the specified 200
    Created a chunk of size 1078, which is longer than the specified 200
    Created a chunk of size 333, which is longer than the specified 200
    Created a chunk of size 413, which is longer than the specified 200
    Created a chunk of size 256, which is longer than the specified 200
    Created a chunk of size 609, which is longer than the specified 200
    Created a chunk of size 315, which is longer than the specified 200
    Created a chunk of size 348, which is longer than the specified 200
    Created a chunk of size 266, which is longer than the specified 200
    Created a chunk of size 333, which is longer than the specified 200
    Created a chunk of size 402, which is longer than the specified 200
    Created a chunk of size 314, which is longer than the specified 200
    Created a chunk of size 332, which is longer than the specified 200
    Created a chunk of size 298, which is longer than the specified 200
    Created a chunk of size 707, which is longer than the specified 200
    Created a chunk of size 291, which is longer than the specified 200
    Created a chunk of size 685, which is longer than the specified 200
    Created a chunk of size 291, which is longer than the specified 200
    Created a chunk of size 474, which is longer than the specified 200
    Created a chunk of size 402, which is longer than the specified 200
    Created a chunk of size 884, which is longer than the specified 200
    Created a chunk of size 243, which is longer than the specified 200
    Created a chunk of size 398, which is longer than the specified 200
    Created a chunk of size 496, which is longer than the specified 200
    Created a chunk of size 872, which is longer than the specified 200
    Created a chunk of size 209, which is longer than the specified 200
    Created a chunk of size 762, which is longer than the specified 200
    Created a chunk of size 445, which is longer than the specified 200
    Created a chunk of size 201, which is longer than the specified 200
    Created a chunk of size 507, which is longer than the specified 200
    Created a chunk of size 309, which is longer than the specified 200
    Created a chunk of size 421, which is longer than the specified 200
    Created a chunk of size 363, which is longer than the specified 200
    Created a chunk of size 410, which is longer than the specified 200
    Created a chunk of size 276, which is longer than the specified 200
    Created a chunk of size 326, which is longer than the specified 200
    Created a chunk of size 635, which is longer than the specified 200
    Created a chunk of size 642, which is longer than the specified 200
    Created a chunk of size 452, which is longer than the specified 200
    Created a chunk of size 221, which is longer than the specified 200
    Created a chunk of size 769, which is longer than the specified 200
    Created a chunk of size 643, which is longer than the specified 200
    Created a chunk of size 10257, which is longer than the specified 200
    Created a chunk of size 1122, which is longer than the specified 200
    Created a chunk of size 1133, which is longer than the specified 200
    Created a chunk of size 1302, which is longer than the specified 200
    Created a chunk of size 783, which is longer than the specified 200
    Created a chunk of size 617, which is longer than the specified 200
    Created a chunk of size 456, which is longer than the specified 200
    Created a chunk of size 4120, which is longer than the specified 200
    Created a chunk of size 2749, which is longer than the specified 200
    Created a chunk of size 259, which is longer than the specified 200
    Created a chunk of size 444, which is longer than the specified 200
    Created a chunk of size 1549, which is longer than the specified 200
    Created a chunk of size 411, which is longer than the specified 200
    Created a chunk of size 1449, which is longer than the specified 200
    Created a chunk of size 1960, which is longer than the specified 200
    Created a chunk of size 1549, which is longer than the specified 200
    Created a chunk of size 599, which is longer than the specified 200
    Created a chunk of size 232, which is longer than the specified 200
    Created a chunk of size 899, which is longer than the specified 200
    Created a chunk of size 1409, which is longer than the specified 200
    Created a chunk of size 287, which is longer than the specified 200
    Created a chunk of size 862, which is longer than the specified 200
    Created a chunk of size 601, which is longer than the specified 200
    Created a chunk of size 6985, which is longer than the specified 200
    Created a chunk of size 631, which is longer than the specified 200
    Created a chunk of size 863, which is longer than the specified 200
    Created a chunk of size 341, which is longer than the specified 200
    Created a chunk of size 508, which is longer than the specified 200
    Created a chunk of size 312, which is longer than the specified 200
    Created a chunk of size 335, which is longer than the specified 200
    Created a chunk of size 353, which is longer than the specified 200
    Created a chunk of size 1091, which is longer than the specified 200
    Created a chunk of size 832, which is longer than the specified 200
    Created a chunk of size 1858, which is longer than the specified 200
    Created a chunk of size 2563, which is longer than the specified 200
    Created a chunk of size 660, which is longer than the specified 200
    Created a chunk of size 1249, which is longer than the specified 200
    Created a chunk of size 589, which is longer than the specified 200
    Created a chunk of size 476, which is longer than the specified 200
    Created a chunk of size 335, which is longer than the specified 200
    Created a chunk of size 841, which is longer than the specified 200
    Created a chunk of size 3499, which is longer than the specified 200
    Created a chunk of size 3005, which is longer than the specified 200
    Created a chunk of size 418, which is longer than the specified 200
    Created a chunk of size 868, which is longer than the specified 200
    Created a chunk of size 1076, which is longer than the specified 200
    Created a chunk of size 447, which is longer than the specified 200
    Created a chunk of size 1655, which is longer than the specified 200
    Created a chunk of size 1389, which is longer than the specified 200
    Created a chunk of size 1008, which is longer than the specified 200
    Created a chunk of size 1555, which is longer than the specified 200
    Created a chunk of size 1305, which is longer than the specified 200
    Created a chunk of size 2664, which is longer than the specified 200
    Created a chunk of size 478, which is longer than the specified 200
    Created a chunk of size 3346, which is longer than the specified 200
    Created a chunk of size 681, which is longer than the specified 200
    Created a chunk of size 3305, which is longer than the specified 200
    Created a chunk of size 413, which is longer than the specified 200
    Created a chunk of size 662, which is longer than the specified 200
    Created a chunk of size 830, which is longer than the specified 200
    Created a chunk of size 251, which is longer than the specified 200
    Created a chunk of size 490, which is longer than the specified 200
    Created a chunk of size 212, which is longer than the specified 200
    Created a chunk of size 5641, which is longer than the specified 200
    Created a chunk of size 704, which is longer than the specified 200
    Created a chunk of size 616, which is longer than the specified 200
    Created a chunk of size 1081, which is longer than the specified 200
    Created a chunk of size 2037, which is longer than the specified 200
    Created a chunk of size 393, which is longer than the specified 200
    Created a chunk of size 1197, which is longer than the specified 200
    Created a chunk of size 999, which is longer than the specified 200
    Created a chunk of size 437, which is longer than the specified 200
    Created a chunk of size 408, which is longer than the specified 200
    Created a chunk of size 995, which is longer than the specified 200
    Created a chunk of size 287, which is longer than the specified 200
    Created a chunk of size 628, which is longer than the specified 200
    Created a chunk of size 4651, which is longer than the specified 200
:::

::: {.output .stream .stdout}
    Всего чанков: 273
    Первые N чанков:
:::

::: {.output .execute_result execution_count="7"}
    ['\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ',
     'Мы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,\nсохраняя исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,\nчтя память предков, передавших нам любовь и уважение к Отечеству, веру в добро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,\nстремясь обеспечить благополучие и процветание России,\nисходя из ответственности за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,\nпринимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.',
     'РАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСтатья 1',
     'Статья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.',
     'Статья 2\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.\n\nСтатья 3',
     '1. Носителем суверенитета и единственным источником власти в Российской Федерации является ее многонациональный народ.\n2. Народ осуществляет свою власть непосредственно, а также через органы государственной власти и органы местного самоуправления.\n3. Высшим непосредственным выражением власти народа являются референдум и свободные выборы.\n4. Никто не может присваивать власть в Российской Федерации. Захват власти или присвоение властных полномочий преследуются по федеральному закону.',
     'Статья 4',
     '1. Суверенитет Российской Федерации распространяется на всю ее территорию.\n2. Конституция Российской Федерации и федеральные законы имеют верховенство на всей территории Российской Федерации.\n3. Российская Федерация обеспечивает целостность и неприкосновенность своей территории.',
     'Статья 5',
     '1. Российская Федерация состоит из республик, краев, областей, городов федерального значения, автономной области, автономных округов - равноправных субъектов Российской Федерации.\n2. Республика (государство) имеет свою конституцию и законодательство. Край, область, город федерального значения, автономная область, автономный округ имеет свой устав и законодательство.\n3. Федеративное устройство Российской Федерации основано на ее государственной целостности, единстве системы государственной власти, разграничении предметов ведения и полномочий между органами государственной власти Российской Федерации и органами государственной власти субъектов Российской Федерации, равноправии и самоопределении народов в Российской Федерации.\n4. Во взаимоотношениях с федеральными органами государственной власти все субъекты Российской Федерации между собой равноправны.']
:::
:::

::: {#2b71e49dd5e45006 .cell .markdown}
## Рекурсивная нарезка с помощью токенизатора TikToken

В данном примере мы используем класс рекурсивной нарезки, однако, теперь
на последней миле нарезка будет выполняться на токенизированном тексте.
:::

::: {#ee48606a6160a456 .cell .code execution_count="8" ExecuteTime="{\"end_time\":\"2024-05-12T20:25:34.629194Z\",\"start_time\":\"2024-05-12T20:25:34.540668Z\"}"}
``` python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name="gpt-4",
    chunk_size=200,
    chunk_overlap=20
)

chunks = text_splitter.split_text(text)

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stdout}
    Всего чанков: 463
    Первые N чанков:
:::

::: {.output .execute_result execution_count="8"}
    ['\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ',
     'Мы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,\nсохраняя исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,\nчтя память предков, передавших нам любовь и уважение к Отечеству, веру в добро и справедливость,',
     'возрождая суверенную государственность России и утверждая незыблемость ее демократической основы,\nстремясь обеспечить благополучие и процветание России,\nисходя из ответственности за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,\nпринимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.',
     'РАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСтатья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.\n\n\nСтатья 2',
     'Статья 2\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.\n\nСтатья 3',
     '1. Носителем суверенитета и единственным источником власти в Российской Федерации является ее многонациональный народ.\n2. Народ осуществляет свою власть непосредственно, а также через органы государственной власти и органы местного самоуправления.\n3. Высшим непосредственным выражением власти народа являются референдум и свободные выборы.',
     '4. Никто не может присваивать власть в Российской Федерации. Захват власти или присвоение властных полномочий преследуются по федеральному закону.',
     'Статья 4\n\n1. Суверенитет Российской Федерации распространяется на всю ее территорию.\n2. Конституция Российской Федерации и федеральные законы имеют верховенство на всей территории Российской Федерации.\n3. Российская Федерация обеспечивает целостность и неприкосновенность своей территории.\n\nСтатья 5',
     '1. Российская Федерация состоит из республик, краев, областей, городов федерального значения, автономной области, автономных округов - равноправных субъектов Российской Федерации.\n2. Республика (государство) имеет свою конституцию и законодательство. Край, область, город федерального значения, автономная область, автономный округ имеет свой устав и законодательство.',
     '3. Федеративное устройство Российской Федерации основано на ее государственной целостности, единстве системы государственной власти, разграничении предметов ведения и полномочий между органами государственной власти Российской Федерации и органами государственной власти субъектов Российской Федерации, равноправии и самоопределении народов в Российской Федерации.']
:::
:::

::: {#27b2ed320b63b9 .cell .markdown}
## Нарезка при помощи SentenceTransformers

В данном примере задействован токенизаторы использующий модели типа
SentenceTransformer.
:::

::: {#2f488959dc2c5a6 .cell .code execution_count="9" ExecuteTime="{\"end_time\":\"2024-05-12T20:25:36.515302Z\",\"start_time\":\"2024-05-12T20:25:34.629879Z\"}"}
``` python
from langchain_text_splitters import SentenceTransformersTokenTextSplitter

splitter = SentenceTransformersTokenTextSplitter(
    model_name="sentence-transformers/all-mpnet-base-v2",
    chunk_size=200, chunk_overlap=20
)
text_token_count = splitter.count_tokens(text=text) - 2
token_multiplier = splitter.maximum_tokens_per_chunk // text_token_count + 1
text_to_split = text * token_multiplier  # Пример использования для нарезки большого текста
print(f"Токенов в тексте для нарезки: {splitter.count_tokens(text=text_to_split)}")

chunks = splitter.split_text(text=text_to_split)

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stderr}
    /home/pasha/Documents/Repository/gpt/text-splitting/venv/lib/python3.11/site-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
      warnings.warn(
:::

::: {.output .stream .stdout}
    Токенов в тексте для нарезки: 105819
    Всего чанков: 291
    Первые N чанков:
:::

::: {.output .execute_result execution_count="9"}
    ['конституция россиискои федерации мы, многонациональныи народ россиискои федерации, соединенные общеи судьбои на своеи земле, утверждая права и свободы человека, гражданскии мир и согласие, сохраняя исторически сложившееся государственное единство, исходя из общепризнанных принципов равноправия и самоопределения народов, чтя память предков, передавших нам любовь и уважение к отечеству, веру в добро и справедливость, возрождая суверенную государственност',
     '##нную государственность россии и утверждая незыблемость ее демократическои основы, стремясь обеспечить благополучие и процветание россии, исходя из ответственности за свою родину перед нынешним и будущими поколениями, сознавая себя частью мирового сообщества, принимаем конституцию россиискои федерации. раздел первыи глава 1. основы конституционного строя статья 1 1. россииская федерация - россия есть демократическое федеративное правовое государство',
     '##ое правовое государство с республиканскои формои правления. 2. наименования россииская федерация и россия равнозначны. статья 2 человек, его права и свободы являются высшеи ценностью. признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства. статья 3 1. носителем суверенитета и единственным источником власти в россиискои федерации является ее многонациональныи народ. 2. народ осуществляет свою власть непосредственно, а также че',
     '##средственно, а также через органы государственнои власти и органы местного самоуправления. 3. высшим непосредственным выражением власти народа являются референдум и свободные выборы. 4. никто не может присваивать власть в россиискои федерации. захват власти или присвоение властных полномочии преследуются по федеральному закону. статья 4 1. суверенитет россиискои федерации распространяется на всю ее территорию. 2. конституция россиискои федерации и ф',
     '##ия россиискои федерации и федеральные законы имеют верховенство на всеи территории россиискои федерации. 3. россииская федерация обеспечивает целостность и неприкосновенность своеи территории. статья 5 1. россииская федерация состоит из республик, краев, областеи, городов федерального значения, автономнои области, автономных округов - равноправных субъектов россиискои федерации. 2. республика ( государство ) имеет свою конституцию и законодательство. краи, о',
     '##онодательство. краи, область, город федерального значения, автономная область, автономныи округ имеет свои устав и законодательство. 3. федеративное устроиство россиискои федерации основано на ее государственнои целостности, единстве системы государственнои власти, разграничении предметов ведения и полномочии между органами государственнои власти россиискои федерации и органами государственнои власти субъектов россиискои федерации, равноправии и сам',
     '##ерации, равноправии и самоопределении народов в россиискои федерации. 4. во взаимоотношениях с федеральными органами государственнои власти все субъекты россиискои федерации между собои равноправны. статья 6 1. гражданство россиискои федерации приобретается и прекращается в соответствии с федеральным законом, является единым и равным независимо от основании приобретения. 2. каждыи гражданин россиискои федерации обладает на ее территории всеми правами и свобод',
     '##ии всеми правами и свободами и несет равные обязанности, предусмотренные конституциеи россиискои федерации. 3. гражданин россиискои федерации не может быть лишен своего гражданства или права изменить его. статья 7 1. россииская федерация - социальное государство, политика которого направлена на создание условии, обеспечивающих достоиную жизнь и свободное развитие человека. 2. в россиискои федерации охраняются труд и здоровье людеи, устанавливается гарантированныи м',
     '##ивается гарантированныи минимальныи размер оплаты труда, обеспечивается государственная поддержка семьи, материнства, отцовства и детства, инвалидов и пожилых граждан, развивается система социальных служб, устанавливаются государственные пенсии, пособия и иные гарантии социальнои защиты. статья 8 1. в россиискои федерации гарантируются единство экономического пространства, свободное перемещение товаров, услуг и финансовых средств, поддержка конкуренции',
     '##в, поддержка конкуренции, свобода экономическои деятельности. 2. в россиискои федерации признаются и защищаются равным образом частная, государственная, муниципальная и иные формы собственности. статья 9 1. земля и другие природные ресурсы используются и охраняются в россиискои федерации как основа жизни и деятельности народов, проживающих на соответствующеи территории. 2. земля и другие природные ресурсы могут находиться в частнои, государственнои, м']
:::
:::

::: {#ef5a328e45e0375b .cell .markdown}
## Нарезка текста при помощи токенизатора моделей с HuggingFace

В данном примере мы у класс `CharacterTextSplitter` делаем вызов метода
`from_huggingface_tokenizer` котором на вход передаём объект
токенизатора из пакета trahsformers, что позволяет нам использовать для
нарезки текста любой токенизатор любой модели.
:::

::: {#d1d87433f6f04c0b .cell .code execution_count="10" ExecuteTime="{\"end_time\":\"2024-05-12T20:25:36.862180Z\",\"start_time\":\"2024-05-12T20:25:36.515883Z\"}"}
``` python
from transformers import GPT2TokenizerFast
from langchain_text_splitters import CharacterTextSplitter

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(
    tokenizer, chunk_size=100, chunk_overlap=0
)

chunks = text_splitter.split_text(text)

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stderr}
    Created a chunk of size 787, which is longer than the specified 100
    Created a chunk of size 191, which is longer than the specified 100
    Created a chunk of size 162, which is longer than the specified 100
    Created a chunk of size 514, which is longer than the specified 100
    Created a chunk of size 301, which is longer than the specified 100
    Created a chunk of size 919, which is longer than the specified 100
    Created a chunk of size 461, which is longer than the specified 100
    Created a chunk of size 557, which is longer than the specified 100
    Created a chunk of size 354, which is longer than the specified 100
    Created a chunk of size 315, which is longer than the specified 100
    Created a chunk of size 214, which is longer than the specified 100
    Created a chunk of size 675, which is longer than the specified 100
    Created a chunk of size 237, which is longer than the specified 100
    Created a chunk of size 674, which is longer than the specified 100
    Created a chunk of size 215, which is longer than the specified 100
    Token indices sequence length is longer than the specified maximum sequence length for this model (1078 > 1024). Running this sequence through the model will result in indexing errors
    Created a chunk of size 1078, which is longer than the specified 100
    Created a chunk of size 333, which is longer than the specified 100
    Created a chunk of size 413, which is longer than the specified 100
    Created a chunk of size 256, which is longer than the specified 100
    Created a chunk of size 609, which is longer than the specified 100
    Created a chunk of size 315, which is longer than the specified 100
    Created a chunk of size 348, which is longer than the specified 100
    Created a chunk of size 266, which is longer than the specified 100
    Created a chunk of size 333, which is longer than the specified 100
    Created a chunk of size 402, which is longer than the specified 100
    Created a chunk of size 200, which is longer than the specified 100
    Created a chunk of size 314, which is longer than the specified 100
    Created a chunk of size 332, which is longer than the specified 100
    Created a chunk of size 298, which is longer than the specified 100
    Created a chunk of size 707, which is longer than the specified 100
    Created a chunk of size 291, which is longer than the specified 100
    Created a chunk of size 150, which is longer than the specified 100
    Created a chunk of size 685, which is longer than the specified 100
    Created a chunk of size 192, which is longer than the specified 100
    Created a chunk of size 291, which is longer than the specified 100
    Created a chunk of size 474, which is longer than the specified 100
    Created a chunk of size 402, which is longer than the specified 100
    Created a chunk of size 884, which is longer than the specified 100
    Created a chunk of size 243, which is longer than the specified 100
    Created a chunk of size 398, which is longer than the specified 100
    Created a chunk of size 496, which is longer than the specified 100
    Created a chunk of size 872, which is longer than the specified 100
    Created a chunk of size 209, which is longer than the specified 100
    Created a chunk of size 762, which is longer than the specified 100
    Created a chunk of size 445, which is longer than the specified 100
    Created a chunk of size 201, which is longer than the specified 100
    Created a chunk of size 507, which is longer than the specified 100
    Created a chunk of size 309, which is longer than the specified 100
    Created a chunk of size 421, which is longer than the specified 100
    Created a chunk of size 363, which is longer than the specified 100
    Created a chunk of size 410, which is longer than the specified 100
    Created a chunk of size 276, which is longer than the specified 100
    Created a chunk of size 196, which is longer than the specified 100
    Created a chunk of size 175, which is longer than the specified 100
    Created a chunk of size 326, which is longer than the specified 100
    Created a chunk of size 635, which is longer than the specified 100
    Created a chunk of size 642, which is longer than the specified 100
    Created a chunk of size 180, which is longer than the specified 100
    Created a chunk of size 105, which is longer than the specified 100
    Created a chunk of size 452, which is longer than the specified 100
    Created a chunk of size 122, which is longer than the specified 100
    Created a chunk of size 221, which is longer than the specified 100
    Created a chunk of size 769, which is longer than the specified 100
    Created a chunk of size 643, which is longer than the specified 100
    Created a chunk of size 190, which is longer than the specified 100
    Created a chunk of size 10257, which is longer than the specified 100
    Created a chunk of size 1122, which is longer than the specified 100
    Created a chunk of size 1133, which is longer than the specified 100
    Created a chunk of size 1302, which is longer than the specified 100
    Created a chunk of size 783, which is longer than the specified 100
    Created a chunk of size 617, which is longer than the specified 100
    Created a chunk of size 456, which is longer than the specified 100
    Created a chunk of size 4120, which is longer than the specified 100
    Created a chunk of size 2749, which is longer than the specified 100
    Created a chunk of size 259, which is longer than the specified 100
    Created a chunk of size 444, which is longer than the specified 100
    Created a chunk of size 1549, which is longer than the specified 100
    Created a chunk of size 411, which is longer than the specified 100
    Created a chunk of size 1449, which is longer than the specified 100
    Created a chunk of size 1960, which is longer than the specified 100
    Created a chunk of size 1549, which is longer than the specified 100
    Created a chunk of size 599, which is longer than the specified 100
    Created a chunk of size 232, which is longer than the specified 100
    Created a chunk of size 899, which is longer than the specified 100
    Created a chunk of size 1409, which is longer than the specified 100
    Created a chunk of size 287, which is longer than the specified 100
    Created a chunk of size 862, which is longer than the specified 100
    Created a chunk of size 601, which is longer than the specified 100
    Created a chunk of size 6985, which is longer than the specified 100
    Created a chunk of size 631, which is longer than the specified 100
    Created a chunk of size 863, which is longer than the specified 100
    Created a chunk of size 341, which is longer than the specified 100
    Created a chunk of size 508, which is longer than the specified 100
    Created a chunk of size 312, which is longer than the specified 100
    Created a chunk of size 335, which is longer than the specified 100
    Created a chunk of size 353, which is longer than the specified 100
    Created a chunk of size 1091, which is longer than the specified 100
    Created a chunk of size 832, which is longer than the specified 100
    Created a chunk of size 1858, which is longer than the specified 100
    Created a chunk of size 133, which is longer than the specified 100
    Created a chunk of size 2563, which is longer than the specified 100
    Created a chunk of size 660, which is longer than the specified 100
    Created a chunk of size 1249, which is longer than the specified 100
    Created a chunk of size 589, which is longer than the specified 100
    Created a chunk of size 476, which is longer than the specified 100
    Created a chunk of size 335, which is longer than the specified 100
    Created a chunk of size 841, which is longer than the specified 100
    Created a chunk of size 3499, which is longer than the specified 100
    Created a chunk of size 3005, which is longer than the specified 100
    Created a chunk of size 418, which is longer than the specified 100
    Created a chunk of size 868, which is longer than the specified 100
    Created a chunk of size 1076, which is longer than the specified 100
    Created a chunk of size 447, which is longer than the specified 100
    Created a chunk of size 1655, which is longer than the specified 100
    Created a chunk of size 1389, which is longer than the specified 100
    Created a chunk of size 1008, which is longer than the specified 100
    Created a chunk of size 1555, which is longer than the specified 100
    Created a chunk of size 1305, which is longer than the specified 100
    Created a chunk of size 2664, which is longer than the specified 100
    Created a chunk of size 478, which is longer than the specified 100
    Created a chunk of size 3346, which is longer than the specified 100
    Created a chunk of size 681, which is longer than the specified 100
    Created a chunk of size 124, which is longer than the specified 100
    Created a chunk of size 3305, which is longer than the specified 100
    Created a chunk of size 413, which is longer than the specified 100
    Created a chunk of size 662, which is longer than the specified 100
    Created a chunk of size 830, which is longer than the specified 100
    Created a chunk of size 251, which is longer than the specified 100
    Created a chunk of size 160, which is longer than the specified 100
    Created a chunk of size 147, which is longer than the specified 100
    Created a chunk of size 490, which is longer than the specified 100
    Created a chunk of size 197, which is longer than the specified 100
    Created a chunk of size 212, which is longer than the specified 100
    Created a chunk of size 5641, which is longer than the specified 100
    Created a chunk of size 704, which is longer than the specified 100
    Created a chunk of size 616, which is longer than the specified 100
    Created a chunk of size 1081, which is longer than the specified 100
    Created a chunk of size 2037, which is longer than the specified 100
    Created a chunk of size 393, which is longer than the specified 100
    Created a chunk of size 1197, which is longer than the specified 100
    Created a chunk of size 999, which is longer than the specified 100
    Created a chunk of size 437, which is longer than the specified 100
    Created a chunk of size 101, which is longer than the specified 100
    Created a chunk of size 408, which is longer than the specified 100
    Created a chunk of size 995, which is longer than the specified 100
    Created a chunk of size 287, which is longer than the specified 100
    Created a chunk of size 628, which is longer than the specified 100
    Created a chunk of size 4651, which is longer than the specified 100
:::

::: {.output .stream .stdout}
    Всего чанков: 293
    Первые N чанков:
:::

::: {.output .execute_result execution_count="10"}
    ['\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ',
     'Мы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,\nсохраняя исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,\nчтя память предков, передавших нам любовь и уважение к Отечеству, веру в добро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,\nстремясь обеспечить благополучие и процветание России,\nисходя из ответственности за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,\nпринимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.',
     'РАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ',
     'Статья 1',
     '1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.',
     'Статья 2',
     'Человек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.',
     'Статья 3',
     '1. Носителем суверенитета и единственным источником власти в Российской Федерации является ее многонациональный народ.\n2. Народ осуществляет свою власть непосредственно, а также через органы государственной власти и органы местного самоуправления.\n3. Высшим непосредственным выражением власти народа являются референдум и свободные выборы.\n4. Никто не может присваивать власть в Российской Федерации. Захват власти или присвоение властных полномочий преследуются по федеральному закону.',
     'Статья 4']
:::
:::


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

::: {#initial_id .cell .code execution_count="1" ExecuteTime="{\"end_time\":\"2024-05-12T20:26:12.985481Z\",\"start_time\":\"2024-05-12T20:26:12.981984Z\"}" collapsed="true"}
``` python
file_path = 'constitutionrf.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
```
:::

::: {#ba4d57dad56e9bd8 .cell .code execution_count="2" ExecuteTime="{\"end_time\":\"2024-05-12T20:26:20.315538Z\",\"start_time\":\"2024-05-12T20:26:12.986145Z\"}"}
``` python
from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings import HuggingFaceEmbeddings

text_embedder = HuggingFaceEmbeddings(model_name='intfloat/multilingual-e5-large')
text_splitter = SemanticChunker(text_embedder, breakpoint_threshold_type="percentile", breakpoint_threshold_amount=95)

chunks = text_splitter.create_documents([text])

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stderr}
    /home/pasha/Documents/Repository/gpt/text-splitting/venv/lib/python3.11/site-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
      warnings.warn(
    /home/pasha/Documents/Repository/gpt/text-splitting/venv/lib/python3.11/site-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
      warnings.warn(
:::

::: {.output .stream .stdout}
    Всего чанков: 49
    Первые N чанков:
:::

::: {.output .execute_result execution_count="2"}
    [Document(page_content='\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ\n\n\nМы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,\nсохраняя исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,\nчтя память предков, передавших нам любовь и уважение к Отечеству, веру в добро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,\nстремясь обеспечить благополучие и процветание России,\nисходя из ответственности за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,\nпринимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ. РАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.'),
     Document(page_content='ОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСтатья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления. 2. Наименования Российская Федерация и Россия равнозначны. Статья 2\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства. Статья 3\n\n1. Носителем суверенитета и единственным источником власти в Российской Федерации является ее многонациональный народ. 2.'),
     Document(page_content='Народ осуществляет свою власть непосредственно, а также через органы государственной власти и органы местного самоуправления. 3. Высшим непосредственным выражением власти народа являются референдум и свободные выборы. 4. Никто не может присваивать власть в Российской Федерации. Захват власти или присвоение властных полномочий преследуются по федеральному закону. Статья 4\n\n1. Суверенитет Российской Федерации распространяется на всю ее территорию. 2. Конституция Российской Федерации и федеральные законы имеют верховенство на всей территории Российской Федерации. 3. Российская Федерация обеспечивает целостность и неприкосновенность своей территории. Статья 5\n\n1. Российская Федерация состоит из республик, краев, областей, городов федерального значения, автономной области, автономных округов - равноправных субъектов Российской Федерации. 2. Республика (государство) имеет свою конституцию и законодательство. Край, область, город федерального значения, автономная область, автономный округ имеет свой устав и законодательство. 3. Федеративное устройство Российской Федерации основано на ее государственной целостности, единстве системы государственной власти, разграничении предметов ведения и полномочий между органами государственной власти Российской Федерации и органами государственной власти субъектов Российской Федерации, равноправии и самоопределении народов в Российской Федерации. 4.'),
     Document(page_content='Во взаимоотношениях с федеральными органами государственной власти все субъекты Российской Федерации между собой равноправны. Статья 6\n\n1. Гражданство Российской Федерации приобретается и прекращается в соответствии с федеральным законом, является единым и равным независимо от оснований приобретения. 2. Каждый гражданин Российской Федерации обладает на ее территории всеми правами и свободами и несет равные обязанности, предусмотренные Конституцией Российской Федерации. 3. Гражданин Российской Федерации не может быть лишен своего гражданства или права изменить его. Статья 7\n\n1. Российская Федерация - социальное государство, политика которого направлена на создание условий, обеспечивающих достойную жизнь и свободное развитие человека. 2. В Российской Федерации охраняются труд и здоровье людей, устанавливается гарантированный минимальный размер оплаты труда, обеспечивается государственная поддержка семьи, материнства, отцовства и детства, инвалидов и пожилых граждан, развивается система социальных служб, устанавливаются государственные пенсии, пособия и иные гарантии социальной защиты. Статья 8\n\n1. В Российской Федерации гарантируются единство экономического пространства, свободное перемещение товаров, услуг и финансовых средств, поддержка конкуренции, свобода экономической деятельности. 2. В Российской Федерации признаются и защищаются равным образом частная, государственная, муниципальная и иные формы собственности. Статья 9\n\n1. Земля и другие природные ресурсы используются и охраняются в Российской Федерации как основа жизни и деятельности народов, проживающих на соответствующей территории. 2. Земля и другие природные ресурсы могут находиться в частной, государственной, муниципальной и иных формах собственности. Статья 10\n\nГосударственная власть в Российской Федерации осуществляется на основе разделения на законодательную, исполнительную и судебную. Органы законодательной, исполнительной и судебной власти самостоятельны. Статья 11\n\n1. Государственную власть в Российской Федерации осуществляют Президент Российской Федерации, Федеральное Собрание (Совет Федерации и Государственная Дума), Правительство Российской Федерации, суды Российской Федерации. 2. Государственную власть в субъектах Российской Федерации осуществляют образуемые ими органы государственной власти. 3. Разграничение предметов ведения и полномочий между органами государственной власти Российской Федерации и органами государственной власти субъектов Российской Федерации осуществляется настоящей Конституцией, Федеративным и иными договорами о разграничении предметов ведения и полномочий. Статья 12\n\nВ Российской Федерации признается и гарантируется местное самоуправление. Местное самоуправление в пределах своих полномочий самостоятельно. Органы местного самоуправления не входят в систему органов государственной власти. Статья 13\n\n1. В Российской Федерации признается идеологическое многообразие. 2. Никакая идеология не может устанавливаться в качестве государственной или обязательной. 3. В Российской Федерации признаются политическое многообразие, многопартийность. 4. Общественные объединения равны перед законом. 5. Запрещается создание и деятельность общественных объединений, цели или действия которых направлены на насильственное изменение основ конституционного строя и нарушение целостности Российской Федерации, подрыв безопасности государства, создание вооруженных формирований, разжигание социальной, расовой, национальной и религиозной розни. Статья 14\n\n1. Российская Федерация - светское государство. Никакая религия не может устанавливаться в качестве государственной или обязательной. 2. Религиозные объединения отделены от государства и равны перед законом. Статья 15\n\n1. Конституция Российской Федерации имеет высшую юридическую силу, прямое действие и применяется на всей территории Российской Федерации. Законы и иные правовые акты, принимаемые в Российской Федерации, не должны противоречить Конституции Российской Федерации. 2. Органы государственной власти, органы местного самоуправления, должностные лица, граждане и их объединения обязаны соблюдать Конституцию Российской Федерации и законы. 3.'),
     Document(page_content='Законы подлежат официальному опубликованию. Неопубликованные законы не применяются. Любые нормативные правовые акты, затрагивающие права, свободы и обязанности человека и гражданина, не могут применяться, если они не опубликованы официально для всеобщего сведения. 4. Общепризнанные принципы и нормы международного права и международные договоры Российской Федерации являются составной частью ее правовой системы. Если международным договором Российской Федерации установлены иные правила, чем предусмотренные законом, то применяются правила международного договора. Статья 16\n\n1. Положения настоящей главы Конституции составляют основы конституционного строя Российской Федерации и не могут быть изменены иначе как в порядке, установленном настоящей Конституцией. 2. Никакие другие положения настоящей Конституции не могут противоречить основам конституционного строя Российской Федерации. ГЛАВА 2. ПРАВА И СВОБОДЫ ЧЕЛОВЕКА И ГРАЖДАНИНА\n\nСтатья 17\n\n1. В Российской Федерации признаются и гарантируются права и свободы человека и гражданина согласно общепризнанным принципам и нормам международного права и в соответствии с настоящей Конституцией. 2. Основные права и свободы человека неотчуждаемы и принадлежат каждому от рождения. 3. Осуществление прав и свобод человека и гражданина не должно нарушать права и свободы других лиц. Статья 18\n\nПрава и свободы человека и гражданина являются непосредственно действующими. Они определяют смысл, содержание и применение законов, деятельность законодательной и исполнительной власти, местного самоуправления и обеспечиваются правосудием. Статья 19\n\n1. Все равны перед законом и судом.'),
     Document(page_content='2. Государство гарантирует равенство прав и свобод человека и гражданина независимо от пола, расы, национальности, языка, происхождения, имущественного и должностного положения, места жительства, отношения к религии, убеждений, принадлежности к общественным объединениям, а также других обстоятельств. Запрещаются любые формы ограничения прав граждан по признакам социальной, расовой, национальной, языковой или религиозной принадлежности. 3.'),
     Document(page_content='Мужчина и женщина имеют равные права и свободы и равные возможности для их реализации. Статья 20\n\n1. Каждый имеет право на жизнь.'),
     Document(page_content='2. Смертная казнь впредь до ее отмены может устанавливаться федеральным законом в качестве исключительной меры наказания за особо тяжкие преступления против жизни при предоставлении обвиняемому права на рассмотрение его дела судом с участием присяжных заседателей. Статья 21\n\n1.'),
     Document(page_content='Достоинство личности охраняется государством. Ничто не может быть основанием для его умаления. 2. Никто не должен подвергаться пыткам, насилию, другому жестокому или унижающему человеческое достоинство обращению или наказанию. Никто не может быть без добровольного согласия подвергнут медицинским, научным или иным опытам. Статья 22\n\n1. Каждый имеет право на свободу и личную неприкосновенность. 2. Арест, заключение под стражу и содержание под стражей допускаются только по судебному решению. До судебного решения лицо не может быть подвергнуто задержанию на срок более 48 часов. Статья 23\n\n1. Каждый имеет право на неприкосновенность частной жизни, личную и семейную тайну, защиту своей чести и доброго имени. 2. Каждый имеет право на тайну переписки, телефонных переговоров, почтовых, телеграфных и иных сообщений. Ограничение этого права допускается только на основании судебного решения. Статья 24\n\n1. Сбор, хранение, использование и распространение информации о частной жизни лица без его согласия не допускаются. 2. Органы государственной власти и органы местного самоуправления, их должностные лица обязаны обеспечить каждому возможность ознакомления с документами и материалами, непосредственно затрагивающими его права и свободы, если иное не предусмотрено законом. Статья 25\n\nЖилище неприкосновенно. Никто не вправе проникать в жилище против воли проживающих в нем лиц иначе как в случаях, установленных федеральным законом, или на основании судебного решения. Статья 26\n\n1. Каждый вправе определять и указывать свою национальную принадлежность. Никто не может быть принужден к определению и указанию своей национальной принадлежности. 2. Каждый имеет право на пользование родным языком, на свободный выбор языка общения, воспитания, обучения и творчества. Статья 27\n\n1. Каждый, кто законно находится на территории Российской Федерации, имеет право свободно передвигаться, выбирать место пребывания и жительства. 2. Каждый может свободно выезжать за пределы Российской Федерации. Гражданин Российской Федерации имеет право беспрепятственно возвращаться в Российскую Федерацию. Статья 28\n\nКаждому гарантируется свобода совести, свобода вероисповедания, включая право исповедовать индивидуально или совместно с другими любую религию или не исповедовать никакой, свободно выбирать, иметь и распространять религиозные и иные убеждения и действовать в соответствии с ними. Статья 29\n\n1. Каждому гарантируется свобода мысли и слова. 2. Не допускаются пропаганда или агитация, возбуждающие социальную, расовую, национальную или религиозную ненависть и вражду. Запрещается пропаганда социального, расового, национального, религиозного или языкового превосходства. 3. Никто не может быть принужден к выражению своих мнений и убеждений или отказу от них. 4. Каждый имеет право свободно искать, получать, передавать, производить и распространять информацию любым законным способом. Перечень сведений, составляющих государственную тайну, определяется федеральным законом. 5. Гарантируется свобода массовой информации. Цензура запрещается. Статья 30\n\n1. Каждый имеет право на объединение, включая право создавать профессиональные союзы для защиты своих интересов. Свобода деятельности общественных объединений гарантируется. 2.'),
     Document(page_content='Никто не может быть принужден к вступлению в какое-либо объединение или пребыванию в нем. Статья 31\n\nГраждане Российской Федерации имеют право собираться мирно, без оружия, проводить собрания, митинги и демонстрации, шествия и пикетирование. Статья 32\n\n1. Граждане Российской Федерации имеют право участвовать в управлении делами государства как непосредственно, так и через своих представителей. 2. Граждане Российской Федерации имеют право избирать и быть избранными в органы государственной власти и органы местного самоуправления, а также участвовать в референдуме. 3. Не имеют права избирать и быть избранными граждане, признанные судом недееспособными, а также содержащиеся в местах лишения свободы по приговору суда. 4.')]
:::
:::

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
