from services.export_service import ExportService

export_service = ExportService()

report_text="""Title: PM Kisan Policy Analysis
 
Background:
The PM Kisan scheme aims to...
 
Key Provisions:
- Financial support
- Eligibility criteria...
 
Analysis:
The scheme benefits small farmers...
 
Recommendations:
Improve awareness...
 
Conclusion:
The policy is effective but needs...
"""

path = export_service.export(
    text=report_text,
    file_type="pdf",
    file_name="policy_brief"
)

print(path)

