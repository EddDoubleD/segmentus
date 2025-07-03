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

::: {#55eb8474d4ccd12d .cell .markdown}
# Нарезка чанков фиксированной длинны

В данном блокноте мы рассмотрим два самых базовых метода нарезки текста
н чанки, первый из них будет резать входной текст на стройки
фиксированной длинны.
:::

::: {#bf8351aff2175441 .cell .markdown}
## Решение без сторонних библиотек

В данном примере используется текст Конституции Российской Федерации.
:::

::: {#dad600d4afe24240 .cell .code execution_count="1" ExecuteTime="{\"end_time\":\"2024-05-12T20:23:33.935491Z\",\"start_time\":\"2024-05-12T20:23:33.931807Z\"}"}
``` python
file_path = 'constitutionrf.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
```
:::

::: {#acdb5f95ca947ca8 .cell .markdown}
Далее передадим прочитанный текст на вход функции, которая нарежет его
на строки фиксированной длинны.
:::

::: {#initial_id .cell .code execution_count="2" ExecuteTime="{\"end_time\":\"2024-05-12T20:23:33.943543Z\",\"start_time\":\"2024-05-12T20:23:33.936086Z\"}"}
``` python
def simple_text_splitter(text: str, chunk_length: int = 200):
    chunks = [text[i:i + chunk_length] for i in range(0, len(text), chunk_length)]
    return chunks


chunks = simple_text_splitter(text)

print(f"Всего чанков: {len(chunks)}")
print("Первые N чанков:")
chunks[:10]
```

::: {.output .stream .stdout}
    Всего чанков: 638
    Первые N чанков:
:::

::: {.output .execute_result execution_count="2"}
    ['\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ\n\n\nМы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,\nсохраняя',
     ' исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,\nчтя память предков, передавших нам любовь и уважение к Отечеству, веру в до',
     'бро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,\nстремясь обеспечить благополучие и процветание России,\nисходя из ответственности',
     ' за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,\nпринимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.\n\nРАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСта',
     'тья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.\n\n\nСтатья 2',
     '\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.\n\nСтатья 3\n\n1. Носителем суверенитета и единствен',
     'ным источником власти в Российской Федерации является ее многонациональный народ.\n2. Народ осуществляет свою власть непосредственно, а также через органы государственной власти и органы местного самоу',
     'правления.\n3. Высшим непосредственным выражением власти народа являются референдум и свободные выборы.\n4. Никто не может присваивать власть в Российской Федерации. Захват власти или присвоение властны',
     'х полномочий преследуются по федеральному закону.\n\nСтатья 4\n\n1. Суверенитет Российской Федерации распространяется на всю ее территорию.\n2. Конституция Российской Федерации и федеральные законы имеют в',
     'ерховенство на всей территории Российской Федерации.\n3. Российская Федерация обеспечивает целостность и неприкосновенность своей территории.\n\nСтатья 5\n\n1. Российская Федерация состоит из республик, кр']
:::
:::

::: {#e0c184c7aaa9d529 .cell .markdown}
В данном примере реализуем примерно то же самое, что и выше, но через
класс `CharacterTextSplitter` из библиотеки LangChain.
:::

::: {#c7a98c0bec7c4234 .cell .code execution_count="3" ExecuteTime="{\"end_time\":\"2024-05-12T20:23:34.102954Z\",\"start_time\":\"2024-05-12T20:23:33.943981Z\"}"}
``` python
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
```

::: {.output .stream .stderr}
    Created a chunk of size 705, which is longer than the specified 200
    Created a chunk of size 486, which is longer than the specified 200
    Created a chunk of size 279, which is longer than the specified 200
    Created a chunk of size 862, which is longer than the specified 200
    Created a chunk of size 434, which is longer than the specified 200
    Created a chunk of size 518, which is longer than the specified 200
    Created a chunk of size 328, which is longer than the specified 200
    Created a chunk of size 292, which is longer than the specified 200
    Created a chunk of size 201, which is longer than the specified 200
    Created a chunk of size 628, which is longer than the specified 200
    Created a chunk of size 223, which is longer than the specified 200
    Created a chunk of size 626, which is longer than the specified 200
    Created a chunk of size 207, which is longer than the specified 200
    Created a chunk of size 1001, which is longer than the specified 200
    Created a chunk of size 312, which is longer than the specified 200
    Created a chunk of size 382, which is longer than the specified 200
    Created a chunk of size 239, which is longer than the specified 200
    Created a chunk of size 565, which is longer than the specified 200
    Created a chunk of size 296, which is longer than the specified 200
    Created a chunk of size 325, which is longer than the specified 200
    Created a chunk of size 246, which is longer than the specified 200
    Created a chunk of size 300, which is longer than the specified 200
    Created a chunk of size 371, which is longer than the specified 200
    Created a chunk of size 284, which is longer than the specified 200
    Created a chunk of size 308, which is longer than the specified 200
    Created a chunk of size 279, which is longer than the specified 200
    Created a chunk of size 647, which is longer than the specified 200
    Created a chunk of size 266, which is longer than the specified 200
    Created a chunk of size 632, which is longer than the specified 200
    Created a chunk of size 269, which is longer than the specified 200
    Created a chunk of size 448, which is longer than the specified 200
    Created a chunk of size 371, which is longer than the specified 200
    Created a chunk of size 815, which is longer than the specified 200
    Created a chunk of size 229, which is longer than the specified 200
    Created a chunk of size 371, which is longer than the specified 200
    Created a chunk of size 461, which is longer than the specified 200
    Created a chunk of size 792, which is longer than the specified 200
    Created a chunk of size 686, which is longer than the specified 200
    Created a chunk of size 418, which is longer than the specified 200
    Created a chunk of size 467, which is longer than the specified 200
    Created a chunk of size 292, which is longer than the specified 200
    Created a chunk of size 384, which is longer than the specified 200
    Created a chunk of size 339, which is longer than the specified 200
    Created a chunk of size 387, which is longer than the specified 200
    Created a chunk of size 260, which is longer than the specified 200
    Created a chunk of size 307, which is longer than the specified 200
    Created a chunk of size 589, which is longer than the specified 200
    Created a chunk of size 628, which is longer than the specified 200
    Created a chunk of size 415, which is longer than the specified 200
    Created a chunk of size 211, which is longer than the specified 200
    Created a chunk of size 723, which is longer than the specified 200
    Created a chunk of size 592, which is longer than the specified 200
    Created a chunk of size 10050, which is longer than the specified 200
    Created a chunk of size 1047, which is longer than the specified 200
    Created a chunk of size 1061, which is longer than the specified 200
    Created a chunk of size 1196, which is longer than the specified 200
    Created a chunk of size 727, which is longer than the specified 200
    Created a chunk of size 565, which is longer than the specified 200
    Created a chunk of size 426, which is longer than the specified 200
    Created a chunk of size 3893, which is longer than the specified 200
    Created a chunk of size 2533, which is longer than the specified 200
    Created a chunk of size 239, which is longer than the specified 200
    Created a chunk of size 410, which is longer than the specified 200
    Created a chunk of size 1429, which is longer than the specified 200
    Created a chunk of size 379, which is longer than the specified 200
    Created a chunk of size 1359, which is longer than the specified 200
    Created a chunk of size 1826, which is longer than the specified 200
    Created a chunk of size 1446, which is longer than the specified 200
    Created a chunk of size 551, which is longer than the specified 200
    Created a chunk of size 215, which is longer than the specified 200
    Created a chunk of size 840, which is longer than the specified 200
    Created a chunk of size 1324, which is longer than the specified 200
    Created a chunk of size 282, which is longer than the specified 200
    Created a chunk of size 804, which is longer than the specified 200
    Created a chunk of size 561, which is longer than the specified 200
    Created a chunk of size 6595, which is longer than the specified 200
    Created a chunk of size 587, which is longer than the specified 200
    Created a chunk of size 797, which is longer than the specified 200
    Created a chunk of size 316, which is longer than the specified 200
    Created a chunk of size 476, which is longer than the specified 200
    Created a chunk of size 290, which is longer than the specified 200
    Created a chunk of size 309, which is longer than the specified 200
    Created a chunk of size 322, which is longer than the specified 200
    Created a chunk of size 1005, which is longer than the specified 200
    Created a chunk of size 769, which is longer than the specified 200
    Created a chunk of size 1719, which is longer than the specified 200
    Created a chunk of size 2382, which is longer than the specified 200
    Created a chunk of size 676, which is longer than the specified 200
    Created a chunk of size 1184, which is longer than the specified 200
    Created a chunk of size 548, which is longer than the specified 200
    Created a chunk of size 453, which is longer than the specified 200
    Created a chunk of size 322, which is longer than the specified 200
    Created a chunk of size 795, which is longer than the specified 200
    Created a chunk of size 3251, which is longer than the specified 200
    Created a chunk of size 2875, which is longer than the specified 200
    Created a chunk of size 391, which is longer than the specified 200
    Created a chunk of size 819, which is longer than the specified 200
    Created a chunk of size 1014, which is longer than the specified 200
    Created a chunk of size 416, which is longer than the specified 200
    Created a chunk of size 1542, which is longer than the specified 200
    Created a chunk of size 1292, which is longer than the specified 200
    Created a chunk of size 952, which is longer than the specified 200
    Created a chunk of size 1474, which is longer than the specified 200
    Created a chunk of size 1248, which is longer than the specified 200
    Created a chunk of size 2517, which is longer than the specified 200
    Created a chunk of size 446, which is longer than the specified 200
    Created a chunk of size 3157, which is longer than the specified 200
    Created a chunk of size 630, which is longer than the specified 200
    Created a chunk of size 3137, which is longer than the specified 200
    Created a chunk of size 455, which is longer than the specified 200
    Created a chunk of size 614, which is longer than the specified 200
    Created a chunk of size 782, which is longer than the specified 200
    Created a chunk of size 242, which is longer than the specified 200
    Created a chunk of size 459, which is longer than the specified 200
    Created a chunk of size 202, which is longer than the specified 200
    Created a chunk of size 5282, which is longer than the specified 200
    Created a chunk of size 640, which is longer than the specified 200
    Created a chunk of size 647, which is longer than the specified 200
    Created a chunk of size 1012, which is longer than the specified 200
    Created a chunk of size 1906, which is longer than the specified 200
    Created a chunk of size 363, which is longer than the specified 200
    Created a chunk of size 1119, which is longer than the specified 200
    Created a chunk of size 923, which is longer than the specified 200
    Created a chunk of size 399, which is longer than the specified 200
    Created a chunk of size 383, which is longer than the specified 200
    Created a chunk of size 947, which is longer than the specified 200
    Created a chunk of size 272, which is longer than the specified 200
    Created a chunk of size 580, which is longer than the specified 200
    Created a chunk of size 4393, which is longer than the specified 200
:::

::: {.output .stream .stdout}
    Всего чанков: 265
    Первые N чанков:
:::

::: {.output .execute_result execution_count="3"}
    [Document(page_content='\ufeffКОНСТИТУЦИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ'),
     Document(page_content='Мы, многонациональный народ Российской Федерации,\nсоединенные общей судьбой на своей земле,\nутверждая права и свободы человека, гражданский мир и согласие,\nсохраняя исторически сложившееся государственное единство,\nисходя из общепризнанных принципов равноправия и самоопределения народов,\nчтя память предков, передавших нам любовь и уважение к Отечеству, веру в добро и справедливость,\nвозрождая суверенную государственность России и утверждая незыблемость ее демократической основы,\nстремясь обеспечить благополучие и процветание России,\nисходя из ответственности за свою Родину перед нынешним и будущими поколениями,\nсознавая себя частью мирового сообщества,\nпринимаем КОНСТИТУЦИЮ РОССИЙСКОЙ ФЕДЕРАЦИИ.'),
     Document(page_content='РАЗДЕЛ ПЕРВЫЙ\n\nГЛАВА 1.\nОСНОВЫ КОНСТИТУЦИОННОГО СТРОЯ\n\nСтатья 1'),
     Document(page_content='Статья 1\n\n1. Российская Федерация - Россия есть демократическое федеративное правовое государство с республиканской формой правления.\n2. Наименования Российская Федерация и Россия равнозначны.'),
     Document(page_content='Статья 2\n\nЧеловек, его права и свободы являются высшей ценностью. Признание, соблюдение и защита прав и свобод человека и гражданина - обязанность государства.\n\nСтатья 3'),
     Document(page_content='1. Носителем суверенитета и единственным источником власти в Российской Федерации является ее многонациональный народ.\n2. Народ осуществляет свою власть непосредственно, а также через органы государственной власти и органы местного самоуправления.\n3. Высшим непосредственным выражением власти народа являются референдум и свободные выборы.\n4. Никто не может присваивать власть в Российской Федерации. Захват власти или присвоение властных полномочий преследуются по федеральному закону.'),
     Document(page_content='Статья 4'),
     Document(page_content='1. Суверенитет Российской Федерации распространяется на всю ее территорию.\n2. Конституция Российской Федерации и федеральные законы имеют верховенство на всей территории Российской Федерации.\n3. Российская Федерация обеспечивает целостность и неприкосновенность своей территории.'),
     Document(page_content='Статья 5'),
     Document(page_content='1. Российская Федерация состоит из республик, краев, областей, городов федерального значения, автономной области, автономных округов - равноправных субъектов Российской Федерации.\n2. Республика (государство) имеет свою конституцию и законодательство. Край, область, город федерального значения, автономная область, автономный округ имеет свой устав и законодательство.\n3. Федеративное устройство Российской Федерации основано на ее государственной целостности, единстве системы государственной власти, разграничении предметов ведения и полномочий между органами государственной власти Российской Федерации и органами государственной власти субъектов Российской Федерации, равноправии и самоопределении народов в Российской Федерации.\n4. Во взаимоотношениях с федеральными органами государственной власти все субъекты Российской Федерации между собой равноправны.')]
:::
:::
