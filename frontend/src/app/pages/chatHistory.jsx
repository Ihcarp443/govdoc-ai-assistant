"use client"
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/cards";
import { Separator } from "@/components/ui/separator";
import { FileText, Image as  Plus, Clock, File, } from "lucide-react";
import { useEffect, useState } from "react";
import { getChatHistory } from "../Services/get-chat-History";
import { Trash2 } from "lucide-react";
import { useRouter } from "next/navigation";
import { HistoryCardSkeleton } from "@/components/ui/historyCardSkelton";
import { deleteChat } from "../Services/delete-chat";
const ChatHistory = () => {
  const router = useRouter();
  // const [histories, setHistories] = useState([]);
const [loading, setLoading] = useState(false);
const[userId,setUserId]=useState("")


  const histories = [
    { id: "1", name: "Marketing Strategy", date: new Date(), time: "3:45 PM", documents: ["strategy.pdf"], preview: "Summarize the Q4 goals..." },
    { id: "2", name: "Technical Documentation", date: new Date(), time: "1:20 PM", documents: ["docs.pdf", "api.pdf"], preview: "How does the API work..." },
    { id: "3", name: "Legal Documents", date: new Date(), time: "10:30 AM", documents: ["agreement.pdf"], preview: "What are the clauses..." }
  ];

// useEffect(() => {
//     const id = localStorage.getItem("userId");
//     setUserId(id);
//   }, []);

const fetchHistory = async () => {
  // if (!userId) return;
  // setLoading(true);

  // try {
  //   // const data = await getChatHistory(userId);
  //   // setHistories(data);
  // } catch (err) {
  //   console.error(err);
  // } finally {
  //   setLoading(false);
  // }
};


const handleDelete = async (threadId) => {
  // try {
  //   await deleteChatThread({
  //     user_id: userId,
  //     thread_id: threadId,
  //   });

  //   // Reload history
  //   fetchHistory();
  // } catch (err) {
  //   console.error(err);
  // }
};

useEffect(() => {
  //   setLoading(true)
  // fetchHistory();
}, [userId]);

  return (
    <div className="h-screen w-full bg-background">
      <div className="h-full max-w-7xl mx-auto p-6">
        <div className="mb-6 flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-2">Chat History</h1>
            <p className="text-muted-foreground">View and manage your document conversations</p>
          </div>
          <Button className={"cursor-pointer"} onClick={() => router.push("/chat")}>
            <Plus className="h-4 w-4 mr-2" />
            New Chat
          </Button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {loading
            ? Array.from({ length: 3 }).map((_, index) => (
                <HistoryCardSkeleton key={index} />
              ))
            : histories.map((history) => (
            <Card 
            key={history.id}
             className="p-5 hover:shadow-lg transition-shadow cursor-pointer"
              onClick={() =>
                router.push(`/chat?threadId=${history.id}`)
              }>
              <div className="flex items-start justify-between mb-3">
                <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center">
                  <FileText className="h-6 w-6 text-primary" />
                </div>
                <div className="text-right">
                  <div className="flex items-center gap-1 text-xs text-muted-foreground">
                    <Clock className="h-3 w-3" />
                    {history.time}
                  </div>
                </div>
              </div>
              
              <h3 className="font-semibold text-lg mb-2 text-foreground">{history.name}</h3>
              <p className="text-sm text-muted-foreground mb-4 line-clamp-2">{history.preview}</p>
              
              <Separator className="mb-3" />
              
              <div className="space-y-2 justify-between flex">
                <div>
                <div className="text-xs font-medium text-muted-foreground">Documents ({history.documents.length})</div>
                <div className="flex flex-wrap gap-2 mt-2">
                  {history.documents.map((doc, idx) => (
                    <div key={idx} className="flex items-center gap-1 text-xs bg-muted px-2 py-1 rounded">
                      <File className="h-3 w-3" />
                      {doc}
                    </div>
                  ))}
                </div>
                </div>
                  <Button
                     size="icon"
                     variant="ghost"
                     onClick={(e) => {
                       e.stopPropagation();
                       handleDelete(history.id); // or history.thread_id
                     }}
                     className="cursor-pointer text-red-500 hover:bg-red-100 hover:text-red-700 dark:hover:bg-red-950 transition-colors"
                   >
                     <Trash2 className="h-5 w-5" />
                   </Button>
              </div>
            </Card>
          ))}
        </div>



{/* 
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {histories.map((history) => (
            <Card key={history.id} className="p-5 hover:shadow-lg transition-shadow cursor-pointer">
              <div className="flex items-start justify-between mb-3">
                <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center">
                  <FileText className="h-6 w-6 text-primary" />
                </div>
                <div className="text-right">
                  <div className="flex items-center gap-1 text-xs text-muted-foreground">
                    <Clock className="h-3 w-3" />
                    {history.time}
                  </div>
                </div>
              </div>
              
              <h3 className="font-semibold text-lg mb-2 text-foreground">{history.name}</h3>
              <p className="text-sm text-muted-foreground mb-4 line-clamp-2">{history.preview}</p>
              
              <Separator className="mb-3" />
              
              <div className="space-y-2">
                <div className="text-xs font-medium text-muted-foreground">Documents ({history.documents.length})</div>
                <div className="flex flex-wrap gap-2">
                  {history.documents.map((doc, idx) => (
                    <div key={idx} className="flex items-center gap-1 text-xs bg-muted px-2 py-1 rounded">
                      <File className="h-3 w-3" />
                      {doc}
                    </div>
                  ))}
                </div>
              </div>
            </Card>
          ))}
        </div> */}
      </div>
    </div>
  );
};

export default ChatHistory