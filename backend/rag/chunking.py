# from langchain_text_splitters import RecursiveCharacterTextSplitter
# import uuid
# import re


# # document=[{'page': 1, 'source': 'ocr', 'image_path': 'backend/data/pages\\page_1.png', 'word_count': 23, 'text': 'PARL WAR8\nDesiRn bY Stott Rogers\nFor XBOX Live Arcade PSN and WIIWare\nRating CID+\nShion Daie: /BD\nARU HAR8\n1)47\n0\nSearch'}, {'page': 2, 'source': 'ocr', 'image_path': 'backend/data/pages\\page_2.png', 'word_count': 353, 'text': 'Nlew tab\n२+ Settings\nPrivac :\n१० page\nG0\n\n0age-d0c/30291084#4\nHCLTech\nbed\nSave to Drive\nHarvcst Moon the sloic animals of  Ihc Far Side" and thc stcam-\nmccts mecha Dcth tcch by way of Drian Despain and Mcch Wamor.\nFarms are created to bc cxtremely customizable but of\nmanagcable sizes to\nallow players to travel from onc cnd Io Ihe olher within thc gamc play\nscssi0n\nPlayers can cuslomizc crops, buildings dcfenscs\nRandoml y gencrated world elements on six different farm maps and sIx\nWeather conditions (Summer Wintcr Spring Fall Tornlado and Rain )\ncreaic a\ndepth nol SceD on any othcr action siratepy zame\nGame Experience:\n4\nRound" ofgame playl is broken up inio Tve " Phases\nBuying Planting\nDefending Boss and Setling\nBuying\ntheir ACME mail order catalog Ine player can purchase\nsced and farning cquipment for use in Ihe Planting phase Ncw vegetables\ncquipment, fentilizer irrigation defense systems (fences from\nwooden to laser beam) and even weapons and "special" items can be bought\nas the gane progresses. You can even eventually build and upgradc your\nown robotic death suit! (which can double as a Iraclor combine)\nPlanting\nA farcr must lend to his crops and Ihe player is no different\nDuring this phasc thc player moves aboul a JD isometric dynamic farm. The\nland must be tilled, Ihe vegelables must be watered and Ihe guidance missile\ndclense systems must bc clecled\n% cclionl, Iending and placemient is\nimportant Io victory Crops are also affected by seasons\nDefending - Initially armed with\nyou must defend your crops from\nthe attacks of vengeful farn animals and Ihcir mechanized death suits They\nwill Iry to ruin your crops and destroy your land in an attempi Io drive you\noul of business Or\nmight just Iry Io kill you outrighi The right\ndcfenses and\nittlc skill will\nyou from "buying the furm\nfour " rounds" the player squares of against onc of thc main\nanimals ( Pig Cow Chicken, elc, .  Jin\nlight to the finisn Il Maclonald\nPARI TAR8\n"4"18704\n0\nSearch\npdf\npunk\nUsing\nforming\nCrup\nven\nhoc.\nthcy\nKccp\n09>>\nEvcry'}, {'page': 3, 'source': 'pdf_text', 'image_path': 'backend/data/pages\\page_3.png', 'word_count': 450, 'text': '1 \nSample PDF \n \nCreated for testing PDFObject \n \nThis PDF is three pages long. Three long pages. Or three short pages if \nyou’re optimistic. Is it the same as saying “three long minutes”, knowing \nthat all minutes are the same duration, and one cannot possibly be longer \nthan the other? If these pages are all the same size, can one possibly be \nlonger than the other? \n \nI digress. Here’s some Latin. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec \nodio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum \nimperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris \nmassa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per \nconubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero.  \n \nSed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem \nat dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. \nMorbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia \naliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh.  \n \nQuisque volutpat condimentum velit. Class aptent taciti sociosqu ad litora torquent per conubia \nnostra, per inceptos himenaeos. Nam nec ante. Sed lacinia, urna non tincidunt mattis, tortor neque \nadipiscing diam, a cursus ipsum ante quis turpis. Nulla facilisi. Ut fringilla. Suspendisse potenti. \nNunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam. Etiam ultrices.  \n \nSuspendisse in justo eu magna luctus suscipit. Sed lectus. Integer euismod lacus luctus magna. \nQuisque cursus, metus vitae pharetra auctor, sem massa mattis sem, at interdum magna augue \neget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; \nMorbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. In vel mi sit amet augue congue \nelementum. Morbi in ipsum sit amet pede facilisis laoreet. Donec lacus nunc, viverra nec, blandit \nvel, egestas et, augue. Vestibulum tincidunt malesuada tellus. Ut ultrices ultrices enim. Curabitur \nsit amet mauris.  \n \nMorbi in dui quis est pulvinar ullamcorper. Nulla facilisi. Integer lacinia sollicitudin massa. Cras \nmetus. Sed aliquet risus a tortor. Integer id quam. Morbi mi. Quisque nisl felis, venenatis tristique, \ndignissim in, ultrices sit amet, augue. Proin sodales libero eget ante. Nulla quam. Aenean laoreet. \nVestibulum nisi lectus, commodo ac, facilisis ac, ultricies eu, pede. Ut orci risus, accumsan \nporttitor, cursus quis, aliquet eget, justo. Sed pretium blandit orci.  \n \nUt eu diam at pede suscipit sodales. Aenean lectus elit, fermentum non, convallis id, sagittis at, \nneque. Nullam mauris orci, aliquet et, iaculis et, viverra vitae, ligula. Nulla ut felis in purus \naliquam imperdiet. Maecenas aliquet mollis lectus. Vivamus consectetuer risus et tortor. Lorem'}, {'page': 4, 'source': 'pdf_text', 'image_path': 'backend/data/pages\\page_4.png', 'word_count': 528, 'text': '2 \nipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante \ndapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. \nPraesent mauris.  \n \nFusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class \naptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur \nsodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean \nquam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem.  \n \nProin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, \nmassa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper \nvel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. Class aptent taciti \nsociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec ante. Sed lacinia, \nurna non tincidunt mattis, tortor neque adipiscing diam, a cursus ipsum ante quis turpis. Nulla \nfacilisi. Ut fringilla. Suspendisse potenti.  \n \nNunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam. Etiam ultrices. \nSuspendisse in justo eu magna luctus suscipit. Sed lectus. Integer euismod lacus luctus magna. \nQuisque cursus, metus vitae pharetra auctor, sem massa mattis sem, at interdum magna augue \neget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; \nMorbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. In vel mi sit amet augue congue \nelementum. Morbi in ipsum sit amet pede facilisis laoreet.  \n \nDonec lacus nunc, viverra nec, blandit vel, egestas et, augue. Vestibulum tincidunt malesuada \ntellus. Ut ultrices ultrices enim. Curabitur sit amet mauris. Morbi in dui quis est pulvinar \nullamcorper. Nulla facilisi. Integer lacinia sollicitudin massa. Cras metus. Sed aliquet risus a \ntortor. Integer id quam. Morbi mi.  \n \nLorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed \ncursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis \nipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum \nlacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per \ninceptos himenaeos. Curabitur sodales ligula in libero.  \n \nSed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem \nat dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. \nMorbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia \naliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh.  \n \nQuisque volutpat condimentum velit. Class aptent taciti sociosqu ad litora torquent per conubia \nnostra, per inceptos himenaeos. Nam nec ante. Sed lacinia, urna non tincidunt mattis, tortor neque \nadipiscing diam, a cursus ipsum ante quis turpis. Nulla facilisi. Ut fringilla. Suspendisse potenti. \nNunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam. Etiam ultrices.  \n \nSuspendisse in justo eu magna luctus suscipit. Sed lectus. Integer euismod lacus luctus magna. \nQuisque cursus, metus vitae pharetra auctor, sem massa mattis sem, at interdum magna augue \neget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; \nMorbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. In vel mi sit amet augue congue'}, {'page': 5, 'source': 'pdf_text', 'image_path': 'backend/data/pages\\page_5.png', 'word_count': 389, 'text': '3 \nelementum. Morbi in ipsum sit amet pede facilisis laoreet. Donec lacus nunc, viverra nec, blandit \nvel, egestas et, augue. Vestibulum tincidunt malesuada tellus. Ut ultrices ultrices enim. Curabitur \nsit amet mauris.  \n \nMorbi in dui quis est pulvinar ullamcorper. Nulla facilisi. Integer lacinia sollicitudin massa. Cras \nmetus. Sed aliquet risus a tortor. Integer id quam. Morbi mi. Quisque nisl felis, venenatis tristique, \ndignissim in, ultrices sit amet, augue. Proin sodales libero eget ante. Nulla quam. Aenean laoreet. \nVestibulum nisi lectus, commodo ac, facilisis ac, ultricies eu, pede. Ut orci risus, accumsan \nporttitor, cursus quis, aliquet eget, justo. Sed pretium blandit orci.  \n \nUt eu diam at pede suscipit sodales. Aenean lectus elit, fermentum non, convallis id, sagittis at, \nneque. Nullam mauris orci, aliquet et, iaculis et, viverra vitae, ligula. Nulla ut felis in purus \naliquam imperdiet. Maecenas aliquet mollis lectus. Vivamus consectetuer risus et tortor. Lorem \nipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante \ndapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. \nPraesent mauris.  \n \nFusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class \naptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur \nsodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean \nquam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem.  \n \nProin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, \nmassa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper \nvel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. Class aptent taciti \nsociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec ante. Sed lacinia, \nurna non tincidunt mattis, tortor neque adipiscing diam, a cursus ipsum ante quis turpis. Nulla \nfacilisi. Ut fringilla. Suspendisse potenti.  \n \nNunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam. Etiam ultrices. \nSuspendisse in justo eu magna luctus suscipit. Sed lectus. Integer euismod lacus luctus magna. \nQuisque cursus, metus vitae pharetra auctor, sem massa mattis sem, at interdum magna augue \neget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; \nMorbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. In vel mi sit amet augue congue \nelementum. Morbi in ipsum sit amet pede facilisis laoreet.'}]


# class ChunkingService:

#     def __init__(self):

#         self.splitter = RecursiveCharacterTextSplitter(
#             chunk_size=1000,
#             chunk_overlap=200
#         ) 

#     def clean_text(self,text: str):
#         text = re.sub(r'\n+', ' ', text)

#         text = re.sub(r'\s+', ' ', text)

#         return text.strip()

#     def create_chunks(self, document):

#         final_chunks = []
#         for page in document['pages']:

#             if not page["text"].strip():
#                 continue
            
            
#             if page["source"] == "ocr":
#                 text=self.clean_text(page["text"])
#             else:
#                 text=page["text"]

#             chunks = self.splitter.split_text(
#                 text
#             )
#             for idx, chunk in enumerate(chunks):
            
#                 final_chunks.append({
#                     "chunk_id": str(uuid.uuid4()),
#                     "document_id": document["document_id"],
#                     "filename": document["filename"],
#                     "document_type": document["metadata"]["document_type"],
#                     "word_count": len(chunk.split()),
#                     "char_count": len(chunk),
#                     "page": page["page"],
#                     "source": page["source"],
#                     "chunk_index": idx,
#                     "text": chunk
#                 })
#         return final_chunks

# # chunking_service = ChunkingService()


# # chunks = chunking_service.create_chunks(document)

# # print(chunks)
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