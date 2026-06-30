const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export const downloadDocument = async ({
    markdown,
    fileType,
    fileName
}) => {

    const response = await fetch(
        `${BASE_URL}/export`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                markdown,
                file_type: fileType,
                file_name: fileName
            })
        }
    );

    if (!response.ok) {
        throw new Error("Export failed");
    }

    const blob = await response.blob();

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;
    a.download = fileName;

    document.body.appendChild(a);

    a.click();

    a.remove();

    window.URL.revokeObjectURL(url);
};