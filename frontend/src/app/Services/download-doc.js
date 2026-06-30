const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export const downloadDocument = async ({
  report,
  fileType,
  fileName,
  threadId,
  userId,
  uploadedFileName,
}) => {
  const response = await fetch(`${BASE_URL}/export`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      report: report,
      file_type: fileType,
      thread_id: threadId,
      user_id: userId,
      uploaded_file_name: uploadedFileName,
      file_name: fileName,
    }),
  });
if (!response.ok) {
  const err = await response.json();
  console.error("Export Error:", err);
  throw new Error(err.detail || "Export failed");
}

  const blob = await response.blob();

  // Get filename from backend if available
  const disposition = response.headers.get("Content-Disposition");
  let downloadName = fileName;

  if (disposition) {
    const match = disposition.match(/filename="?([^"]+)"?/);
    if (match) {
      downloadName = match[1];
    }
  }

  const url = window.URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = downloadName;

  document.body.appendChild(a);
  a.click();
  a.remove();

  window.URL.revokeObjectURL(url);
};