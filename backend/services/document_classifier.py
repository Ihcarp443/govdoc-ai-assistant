class DocumentClassifier:

    def __init__(self, llm_provider):

        self.llm = llm_provider

    def classify(self, pages):

        document_text = "\n".join(
            page["text"]
            for page in pages[:3]
        )
        prompt = f"""
You are an expert government document classifier.

Classify the document into EXACTLY ONE category.

Categories:

Policy: Defines rules, objectives, guidelines, or framework for governance or implementation.

Circular: Official communication issued to departments/offices providing instructions, clarification, or information.

Notification: Official announcement of a decision, rule, appointment, amendment, or regulation.

Legal Record: Court orders, judgments, legal proceedings, acts, regulations, or legal documentation.

Tender: Procurement-related document inviting bids, quotations, or proposals.

Report: Analytical, investigative, progress, audit, survey, or status report.

Scheme Guidelines: Document explaining eligibility, benefits, implementation process, and procedures of a government scheme.

Office Memorandum: Internal government communication regarding administrative decisions, procedures, or policies.

Other: Does not clearly belong to any of the above categories.

Document:
{document_text[:8000]}

Return ONLY the category name.
"""

        result = self.llm.generate(prompt)

        return result.strip()