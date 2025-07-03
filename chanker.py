from enum import Enum
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_text_splitters import HTMLHeaderTextSplitter, MarkdownHeaderTextSplitter, RecursiveJsonSplitter
from transformers import GPT2TokenizerFast
from langchain_text_splitters import SentenceTransformersTokenTextSplitter

class SplitterAlgorithm(Enum):
    FIXED_LENGTH = 1
    RECURSIVE_CHARACTER = 2
    HTML_HEADER = 3
    MARKDOWN_HEADER = 4
    SENTENCE_TRANSFORMERS = 5
    HUGGINGFACE_TOKENIZER = 6

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def split_text(text, algorithm, **kwargs):
    if algorithm == SplitterAlgorithm.FIXED_LENGTH:
        chunk_length = kwargs.get('chunk_length', 200)
        chunks = [text[i:i + chunk_length] for i in range(0, len(text), chunk_length)]
        return chunks

    elif algorithm == SplitterAlgorithm.RECURSIVE_CHARACTER:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=kwargs.get('chunk_size', 200),
            chunk_overlap=kwargs.get('chunk_overlap', 20)
        )
        return text_splitter.create_documents([text])

    elif algorithm == SplitterAlgorithm.HTML_HEADER:
        headers_to_split_on = kwargs.get('headers_to_split_on', [("h1", "Header 1"), ("h2", "Header 2"), ("h3", "Header 3")])
        html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
        return html_splitter.split_text(text)

    elif algorithm == SplitterAlgorithm.MARKDOWN_HEADER:
        headers_to_split_on = kwargs.get('headers_to_split_on', [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")])
        markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
        return markdown_splitter.split_text(text)

    elif algorithm == SplitterAlgorithm.SENTENCE_TRANSFORMERS:
        splitter = SentenceTransformersTokenTextSplitter(
            model_name=kwargs.get('model_name', "sentence-transformers/all-mpnet-base-v2"),
            chunk_size=kwargs.get('chunk_size', 200),
            chunk_overlap=kwargs.get('chunk_overlap', 20)
        )
        return splitter.split_text(text)

    elif algorithm == SplitterAlgorithm.HUGGINGFACE_TOKENIZER:
        tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
        text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(
            tokenizer,
            chunk_size=kwargs.get('chunk_size', 100),
            chunk_overlap=kwargs.get('chunk_overlap', 0)
        )
        return text_splitter.split_text(text)

    else:
        raise ValueError("Unsupported algorithm")

