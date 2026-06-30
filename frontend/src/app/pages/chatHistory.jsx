"use client"
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/cards";
import { Separator } from "@/components/ui/separator";
import { FileText, Image as  Plus, Clock, File, } from "lucide-react";
import { useEffect, useState } from "react";
import { getChatHistory } from "../Services/chat-History";
import {
  Trash2,
  Download,
} from "lucide-react";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import downloadDocument from "../Services/download-doc";
import { useRouter } from "next/navigation";
import { HistoryCardSkeleton } from "@/components/ui/historyCardSkelton";
// import { Badge } from "@/components/ui/badge";
import { deleteChat } from "../Services/delete-chat";
// import { downloadDocument } from "../Services/get-document";
import { getDocuments } from "../Services/chat-History";
const ChatHistory = () => {
  const router = useRouter();
  // const [histories, setHistories] = useState([]);
  const [loading, setLoading] = useState(false);
  const[userId,setUserId]=useState("")
  const [documents, setDocuments] = useState([]);
  const [histories, setHistories] = useState([]);
  const [dialogOpen, setDialogOpen] = useState(false);
  const [selectedThreadDocuments, setSelectedThreadDocuments] = useState([]);

useEffect(() => {
    const id = localStorage.getItem("userId");
    setUserId(id);
    console.log("User ID from localStorage:", id);
  }, []);


const documentsByThread = documents.reduce((acc, doc) => {
  if (!acc[doc.thread_id]) {
    acc[doc.thread_id] = [];
  }

  acc[doc.thread_id].push(doc);

  return acc;
}, {});

useEffect(() => {
  if (!userId) return;
  const loadData = async () => {
    setLoading(true);

    try {
      const [threadRes, documentRes] = await Promise.all([
        getChatHistory(userId),
        getDocuments(userId),
      ]);
      console.log("Thread Response:", threadRes);
      console.log("Document Response:", documentRes);
      setHistories(threadRes.threads || []);
      setDocuments(documentRes.documents || []);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  loadData();
}, [userId]);
// const threadDocuments = documentsByThread[history.thread_id] || [];
const handleDelete = async (threadId) => {
  try {
    await deleteChat(threadId, userId);

    setHistories((prev) =>
      prev.filter((item) => item.thread_id !== threadId)
    );
    setDocuments(prev =>
  prev.filter(doc => doc.thread_id !== threadId)
);
  } catch (err) {
    console.error(err);
  }
};

  const openDocumentsDialog = (docs) => {
    setSelectedThreadDocuments(docs);
    setDialogOpen(true);
  };


  return (
    <div className="h-screen w-full bg-background">
      <div className="h-full max-w-7xl mx-auto p-6">
        <div className="mb-6 flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-2">Chat History</h1>
            <p className="text-muted-foreground">View and manage your document conversations</p>
          </div>
          {/* onClick={() => router.push(`/chat?threadId=${history.thread_id} */}
          <Button className={"cursor-pointer"} onClick={() => router.push("/chat")}>
            <Plus className="h-4 w-4 mr-2" />
            New Chat
          </Button>
        </div>

<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {loading ? (
          Array.from({ length: 3 }).map((_, index) => (
            <HistoryCardSkeleton key={index} />
          ))
        ) : histories.length === 0 ? (
          <div className="col-span-full flex flex-col items-center justify-center py-20">
            <FileText className="h-12 w-12 text-muted-foreground mb-4" />
        
            <h2 className="text-xl font-semibold">
              No chat history
            </h2>
        
            <p className="text-muted-foreground mt-2">
              Start a new conversation to see it here.
            </p>
        
            <Button
              className="mt-6"
              onClick={() => router.push("/chat")}
            >
              <Plus className="h-4 w-4 mr-2" />
              New Chat
            </Button>
          </div>
        ) : (histories.map((history) => {
              const threadDocuments =
              documentsByThread[history.thread_id] || [];
              return(
            <Card 
            key={history.thread_id}
             className="p-5 hover:shadow-lg transition-shadow cursor-pointer"
              onClick={() =>
                router.push(`/chat?threadId=${history.thread_id}`)
              }>
              <div className="flex items-start justify-between mb-3">
                <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center">
                  <FileText className="h-6 w-6 text-primary" />
                </div>
                <div className="text-right">
                  <div className="text-xs text-muted-foreground">
                        {new Date(history.created_at).toLocaleDateString([], {
                          dateStyle: "medium",
                        })}
                      </div>
                      
                      <div className="text-xs text-muted-foreground">
                        {new Date(history.created_at).toLocaleTimeString([], {
                          hour: "2-digit",
                          minute: "2-digit",
                        })}
                      </div>
                </div>
              </div>
              
              <h3 className="font-semibold text-lg mb-2 text-foreground">{history.title}</h3>
              <p className="text-sm text-muted-foreground mb-4 line-clamp-2">{threadDocuments.length} document(s) attached</p>
              
              <Separator className="mb-3" />
              
              <div className="space-y-2 justify-between flex">
                <div>
                <div className="text-xs font-medium text-muted-foreground">Documents ({threadDocuments.length})</div>
                <div className="flex flex-wrap gap-2 mt-2">
  <div className="flex flex-wrap gap-2 mt-2">
  {threadDocuments.slice(0, 3).map((doc) => (
    <div
      key={doc.document_id}
      className="flex items-center gap-1 text-xs bg-muted px-2 py-1 rounded"
      onClick={(e) => {
                        e.stopPropagation();
                        openDocumentsDialog(threadDocuments);
      }}
    >
      <File className="h-3 w-3" />

      <span className="truncate max-w-[120px]"  >
        {doc.display_name}
      </span>
    </div>
  ))}
</div>

              {threadDocuments.length > 3 && (
                <div className="mt-2 text-xs text-muted-foreground0 cursor-pointer hover:underline" onClick={(e) => {
                        e.stopPropagation();
                        openDocumentsDialog(threadDocuments);
                      }}>
                  +{threadDocuments.length - 3} more
                </div>
              )}
                </div>
                </div>
                  <Button
                     size="icon"
                     variant="ghost"
                     onClick={(e) => {
                       e.stopPropagation();
                       handleDelete(history.thread_id) // or history.thread_id
                     }}
                     className="cursor-pointer text-red-500 hover:bg-red-100 hover:text-red-700 dark:hover:bg-red-950 transition-colors"
                   >
                     <Trash2 className="h-5 w-5" />
                   </Button>
              </div>
            </Card>
            )}))}
        </div>

      </div>
  <Dialog open={dialogOpen} onOpenChange={setDialogOpen} className="max-w-7xl">
    <DialogContent className="!max-w-[60vw] w-[60vw] p-6">
    <DialogHeader>
      <DialogTitle className="text-xl font-semibold">
        Documents
      </DialogTitle>
    </DialogHeader>

    <div className="rounded-lg border overflow-hidden">
      <Table>
        <TableHeader>
          <TableRow className="bg-muted/40">
            <TableHead className="w-[38%]">Document</TableHead>
            <TableHead className="w-[12%]">Type</TableHead>
            <TableHead className="w-[16%]">Origin</TableHead>
            <TableHead className="w-[22%]">Created</TableHead>
            <TableHead className="w-[12%] text-center">
              Action
            </TableHead>
          </TableRow>
        </TableHeader>

        <TableBody>
          {selectedThreadDocuments.map((doc) => (
            <TableRow
              key={doc.document_id}
              className="hover:bg-muted/40 transition-colors"
            >
              {/* Document */}
              <TableCell className="py-4">
                <div className="flex items-center gap-3">
                  <div className="flex h-9 w-9 items-center justify-center rounded-md bg-muted">
                    <File className="h-4 w-4 text-muted-foreground" />
                  </div>

                  <span className="break-all font-medium">
                    {doc.display_name}
                  </span>
                </div>
              </TableCell>

              {/* File Type */}
              <TableCell className="py-4">
                {doc.file_type || "N/A"}
              </TableCell>

              {/* Origin */}
              <TableCell className="py-4">
                {doc.origin === "upload" ? (
                  <span className="inline-flex items-center rounded-full bg-emerald-100 px-3 py-1 text-xs font-medium text-emerald-700">
                    Uploaded
                  </span>
                ) : (
                  <span className="inline-flex items-center rounded-full bg-blue-100 px-3 py-1 text-xs font-medium text-blue-700">
                    Generated
                  </span>
                )}
              </TableCell>

              {/* Created */}
              <TableCell className="py-4 text-muted-foreground">
                {new Date(doc.created_at).toLocaleString()}
              </TableCell>

              {/* Action */}
              <TableCell className="py-4 text-center">
                <Button
                  size="icon"
                  variant="ghost"
                  className="hover:bg-primary/10"
                  onClick={() =>
                    downloadFile(doc.document_id, doc.display_name)
                  }
                >
                  <Download className="h-4 w-4" />
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  </DialogContent>
</Dialog>
    </div>
  );
};


export default ChatHistory;