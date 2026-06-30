const BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export const getChatHistory = async (userId) => {
  const response = await fetch(`${BASE_URL}/api/chat-history/${userId}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error("Failed to fetch chat history");
  }

  return response.json();
};