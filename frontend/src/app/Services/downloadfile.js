const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;
    
export const handleDownload = async (documentId, displayName, filePath) => {
  try {
    const url = `${BASE_URL}/documents/download?file_path=${encodeURIComponent(
      filePath
    )}`;

    const response = await fetch(url);

    if (!response.ok) {
      throw new Error("Failed to download file");
    }

    const blob = await response.blob();

    const downloadUrl = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = downloadUrl;
    a.download = displayName || "downloaded_file"; 

    document.body.appendChild(a);
    a.click();

    a.remove();
    window.URL.revokeObjectURL(downloadUrl);
  } catch (error) {
    console.error("Download failed:", error);
  }
};