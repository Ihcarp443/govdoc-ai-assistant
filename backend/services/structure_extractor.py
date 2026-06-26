# D:\project2\backend\services\structure_extractor.py
import json

MAX_STRUCTURE_CHARS = 15000


class StructureExtractor:

    def __init__(self, llm_provider):
        self.llm_provider = llm_provider

    def extract(self, pages, layout):
        document_text = ""

        for page in pages:
            document_text += page["text"] + "\n\n"

        document_text = document_text[:MAX_STRUCTURE_CHARS]
        prompt = f"""
You are an expert in analyzing government documents such as policies,
schemes, circulars, notifications, tenders, office memorandums,
legal orders and reports.

You are given:

1. OCR/Text extracted from the document.
2. Layout information extracted from the document.

Your task is to identify the LOGICAL STRUCTURE of the document.

Important Rules:

- Focus on the document organization.
- Do NOT return document-specific values.
- Ignore:
    • document title
    • document number
    • dates
    • addresses
    • contact details
    • signatures
    • page numbers
    • table rows
    • serial numbers
    • URLs
    • email IDs
    • monetary values

- Merge similar headings into one normalized heading.
- If headings are missing, infer them from the content.
- Preserve the natural order.

For EACH section identify:

1. order
2. heading
3. purpose
4. content_type
5. mandatory

content_type must be one of:

- paragraph
- bullet_list
- numbered_list
- table
- mixed

mandatory should be true if the section is generally expected
to appear in similar documents, otherwise false.

Return ONLY valid JSON.

Example:

{{
    "sections":[
        {{
            "order":1,
            "heading":"Introduction",
            "purpose":"Explain why the document has been issued.",
            "content_type":"paragraph",
            "mandatory":true
        }},
        {{
            "order":2,
            "heading":"Eligibility Criteria",
            "purpose":"Describe who is eligible.",
            "content_type":"bullet_list",
            "mandatory":true
        }}
    ]
}}

-----------------------
DOCUMENT LAYOUT
-----------------------

{layout}

-----------------------
DOCUMENT TEXT
-----------------------

{document_text}
"""



        response = self.llm_provider.generate(prompt)
        import re
        response = re.sub(r"^```json|```$", "", response, flags=re.MULTILINE)

        try:
            
            response = response.strip()

            return json.loads(response)

        except Exception as e:

            print("Structure extraction failed:", e)

            return {
                "sections": [],
            }