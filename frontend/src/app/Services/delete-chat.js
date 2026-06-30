export const deleteChat = async ({ user_id, thread_id }) => {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/chat/delete-thread`,
    {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user_id,
        thread_id,
      }),
    }
  );

  if (!response.ok) {
    throw new Error("Failed to delete thread");
  }

  return response.json();
};