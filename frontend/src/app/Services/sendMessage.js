import { useState } from "react";
export const sendMessage = async ({
    message,
    files,
    threadId,
    userId
}) => {
    const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;
    let uploadedPaths = [];
    let thread = threadId;

    if (files.length > 0) {

        const formData = new FormData();

        files.forEach(file => {
            formData.append("files", file);
            formData.append("filenames", file.name);
        });

        formData.append("thread_id", thread);
        formData.append("user_id", userId);

        const uploadResponse = await fetch(`${API_BASE_URL}/upload`, {
              method: "POST",
              body: formData,
            });

        const uploadData = await uploadResponse.json();
        thread=uploadData.thread_id;
        uploadedPaths = uploadData.paths;
    }


    const questionResponse = await fetch(`${API_BASE_URL}/chat`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message,
            thread_id: thread,
            user_id: userId,
            input_type: "text",
            paths: uploadedPaths,
          }),
        });

    return questionResponse.json();
};