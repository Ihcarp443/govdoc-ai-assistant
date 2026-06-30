const API_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export const getChatHistory = async (userId) => {
  const response = await fetch(`${API_URL}/thread/${userId}`);

  if (!response.ok) {
    throw new Error("Failed to fetch chat history");
  }

  return response.json();
};



export const getThread = async (threadId) => {
  const response = await fetch(`${API_URL}/thread/${threadId}`);

  if (!response.ok) {
    throw new Error("Failed to fetch thread");
  }

  return response.json();
};

export const deleteChat = async (threadId, userId) => {
  const response = await fetch(`${API_URL}/thread/${threadId}/${userId}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error("Failed to delete chat");
  }

  return response.json();
};


export const getDocuments = async ( userId) => {
  console.log("Fetching documents foruserId:", userId);
  const response = await fetch(
    `${API_URL}/documents/documents?user_id=${userId}`
  );
  console.log("Document Response:", response);
  if (!response.ok) {
    throw new Error("Failed to fetch documents");
  }

  return response.json();
};
