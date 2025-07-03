import argparse

from chanker import SplitterAlgorithm, split_text, read_text


def main():
    parser = argparse.ArgumentParser(description="Text chunking tool")
    parser.add_argument("file_path", type=str, help="Path to the input text file")
    parser.add_argument("algorithm", type=str, choices=["fixed_length", "recursive_character", "html_header", "markdown_header", "sentence_transformers", "huggingface_tokenizer"], help="Chunking algorithm to use")
    parser.add_argument("--chunk_size", type=int, default=200, help="Size of each chunk (for some algorithms)")
    parser.add_argument("--chunk_overlap", type=int, default=20, help="Overlap between chunks (for some algorithms)")
    parser.add_argument("--model_name", type=str, default="sentence-transformers/all-mpnet-base-v2", help="Model name for sentence transformers (if applicable)")

    args = parser.parse_args()

    text = read_text(args.file_path)
    algorithm = SplitterAlgorithm[args.algorithm.upper()]

    chunks = split_text(text, algorithm, chunk_size=args.chunk_size, chunk_overlap=args.chunk_overlap, model_name=args.model_name)

    print(f"Всего чанков: {len(chunks)}")
    print("Первые N чанков:")
    for i, chunk in enumerate(chunks[:10]):
        print(f"{i + 1}: {chunk}")

if __name__ == "__main__":
    main()

