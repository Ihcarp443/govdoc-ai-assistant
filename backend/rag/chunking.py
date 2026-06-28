import uuid
import re

from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkingService:

    def __init__(
        self,
        chunk_size=900,
        chunk_overlap=150
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                "; ",
                ", ",
                " "
            ]
        )

    # --------------------------------------------------------

    def clean_text(self, text):

        text = re.sub(r"\r", "", text)

        text = re.sub(r"\n{3,}", "\n\n", text)

        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()

    # --------------------------------------------------------

    def merge_pages(self, document):

        merged = ""

        page_offsets = []

        current_offset = 0

        for page in document["pages"]:

            text = page["text"]

            if page["source"] == "ocr":
                text = self.clean_text(text)

            marker = f"\n\n<<<PAGE_{page['page']}>>>\n\n"

            merged += marker

            current_offset += len(marker)

            page_offsets.append({
                "page": page["page"],
                "source": page["source"],
                "start": current_offset
            })

            merged += text

            current_offset += len(text)

        return merged, page_offsets

    # --------------------------------------------------------

    def find_pages(self, start, end, page_offsets):

        pages = []

        sources = []

        for i in range(len(page_offsets)):

            page_start = page_offsets[i]["start"]

            if i < len(page_offsets)-1:
                page_end = page_offsets[i+1]["start"]
            else:
                page_end = float("inf")

            if start < page_end and end > page_start:

                pages.append(page_offsets[i]["page"])

                sources.append(page_offsets[i]["source"])

        return pages, list(set(sources))

    # --------------------------------------------------------

    def create_chunks(self, document):

        merged_text, page_offsets = self.merge_pages(document)

        docs = self.splitter.create_documents([merged_text])
        d_type=document["metadata"]["document_type"]
        # for k,v in document.items():
        #     print(f"{k}: {v}")
        #     print("-------------------------------------------------")
        chunks = []

        cursor = 0

        for index, doc in enumerate(docs):

            text = doc.page_content.strip()

            start = merged_text.find(text, cursor)

            if start == -1:
                start = cursor

            end = start + len(text)

            cursor = end

            pages, sources = self.find_pages(
                start,
                end,
                page_offsets
            )

            text = re.sub(
                r"<<<PAGE_\d+>>>",
                "",
                text
            )

            text = re.sub(
                r"<<<PAGE_\d+>>>",
                "",
                text
            )

            chunks.append({

                "chunk_id": str(uuid.uuid4()),

                "document_id": document["document_id"],

                "filename": document["filename"],

                "document_type": d_type,

                "chunk_index": index,

                "text": text.strip(),

                "pages": pages,

                "sources": sources,

                "word_count": len(text.split()),

                "char_count": len(text),

                "char_start": start,

                "char_end": end

            })
        print(f"\nTotal Chunks Created: {len(chunks)}")
        print("="*50)
        for chunk in chunks:
            print(f"Chunk ID: {chunk['chunk_id']}")
            print(f"Document ID: {chunk['document_id']}")
            print(f"Filename: {chunk['filename']}")
            print(f"Document Type: {chunk['document_type']}")
            print(f"Chunk Index: {chunk['chunk_index']}")
            print(f"Pages: {chunk['pages']}")
            print(f"Sources: {chunk['sources']}")
            print(f"Word Count: {chunk['word_count']}")
            print(f"Char Count: {chunk['char_count']}")
            print(f"Char Start: {chunk['char_start']}")
            print(f"Char End: {chunk['char_end']}")
            print("-"*50)
        return chunks
