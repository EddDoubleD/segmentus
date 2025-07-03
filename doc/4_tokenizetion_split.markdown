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
