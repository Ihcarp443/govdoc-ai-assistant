const BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export const downloadDocument = async ({
  documentId,
  format, // "pdf" | "docx"
}) => {
  try {
    const response = await fetch(`${BASE_URL}/download-document`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        document_id: documentId,
        format,
      }),
    });

    if (!response.ok) {
      throw new Error("Failed to download document");
    }

    const blob = await response.blob();

    const extension = format === "pdf" ? "pdf" : "docx";

    const url = window.URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = `document.${extension}`;

    document.body.appendChild(link);
    link.click();

    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error("Download failed:", error);
    throw error;
  }
};