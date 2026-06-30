export const sendMessage = async ({
    message,
    files,
    threadId,
    userId
}) => {

    let uploadedFiles = [];

    if (files.length > 0) {

        const formData = new FormData();

        files.forEach(file => {
            formData.append("files", file);
        });

        formData.append("thread_id", threadId);
        formData.append("user_id", userId);

        const uploadResponse = await fetch(
            "/api/upload",
            {
                method: "POST",
                body: formData
            }
        );

        uploadedFiles = await uploadResponse.json();
    }

    const questionResponse = await fetch(
        "/api/chat",
        {
            method: "POST",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                user_id:userId,
                thread_id:threadId,
                question:message,
                uploaded_files:uploadedFiles
            })
        }
    );

    return questionResponse.json();
}