"use client"
import { useState,useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Avatar } from "@/components/ui/avatar";
import { ScrollArea } from "@/components/ui/scroll-area";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Upload, Send, Image,Sparkles,Loader2 as Loader2,User, Bot, Menu,Plus} from "lucide-react";
import AdminToolsDialog from "@/components/ui/toolDialog";
import { FileText, FileDown ,History,LogOut} from "lucide-react";
import { useRouter } from "next/navigation";
import { toast } from "sonner";
import ThreeDotsLoader from "@/components/ui/laoder";
import { Toaster } from "@/components/ui/sonner";
import {getThread} from "../Services/chat-History";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { useRef } from "react";
import { X, Paperclip } from "lucide-react";
import { sendMessage } from "../Services/sendMessage";
import { downloadDocument } from "../Services/download-doc";
import { useSearchParams } from "next/navigation";


const ChatPage = () => {
const router=useRouter()
const searchParams = useSearchParams();
const fileInputRef = useRef(null);
const [selectedFiles, setSelectedFiles] = useState([]);
const [openTools, setOpenTools] = useState(false);
const [input, setInput] = useState("");
const [userType, setUserType] = useState("");
const[isLoading,setisLoading]=useState(false)
const[userId,setUserId]=useState("")
const[threadId,setThreadId]=useState(null)
const bottomRef = useRef(null);
const [messages, setMessages] = useState([]);

const handleTextareaChange = (e) => {
  setInput(e.target.value);

  e.target.style.height = "0px";
  e.target.style.height = `${e.target.scrollHeight}px`;
};

useEffect(() => {
    setUserType(localStorage.getItem("userType"));
    setUserId(localStorage.getItem("userId"));
    setThreadId(searchParams.get("threadId") || null);
  }, []);

useEffect(()=>{
    bottomRef.current?.scrollIntoView({
        behavior:"smooth"
    });
},[messages]);

useEffect(() => {
  if (!threadId) return;
  const loadThread = async () => {
    try {
      const data = await getThread(threadId);
      console.log("data", data);

      // Convert backend state into messages
      setMessages(data.state.chat_history || []);
    } catch (err) {
      console.error(err);
    }
  };

  loadThread();
}, [threadId]);

const handleSendMessage = async () => {

  if (!input.trim() && selectedFiles.length === 0) return;
  const attachedFiles = selectedFiles.map(file => ({
    name: file.name,
    size: file.size,
    type: file.type,
  }));
  const userMessage = {
    id: Date.now().toString(),
    role: "user",
    content: input,
    files: attachedFiles,
  };
      const loadingMessage = {
      id: crypto.randomUUID(),
      role: "assistant",
      loading: true,
      content: "",
    };
  // Show user's message immediately
  setMessages((prev) => [...prev, userMessage,loadingMessage]);
  // setMessages((prev) => [...prev, loadingMessage]);
  setisLoading(true)
  setInput("");
  setSelectedFiles([]);
  const question = input;
  try {

      const response = await sendMessage({
      userId,
      threadId,
      message: question,
      files: selectedFiles,
    });
    console.log("Response from sendMessage:", response);
    const currentThreadId = threadId || response.thread_id;

    setThreadId(currentThreadId);

      setMessages(prev =>
        prev.map(msg =>
        msg.id === loadingMessage.id
        ? {
          ...msg,
          loading: false,
          content: response.answer,
          answer_type: response.answer_type,
        }
      : msg
      )
);

  } catch (error) {
    console.error(error);

    // setMessages((prev) => [
    //   ...prev,
    //   {
    //     id: (Date.now() + 2).toString(),
    //     role: "assistant",
    //     content: "Something went wrong while processing your request.",
    //     timestamp: new Date(),
    //   },
    // ]);
    setMessages(prev =>
  prev.map(msg =>
    msg.id === loadingMessage.id
      ? {
          ...msg,
          loading: false,
          content: "Something went wrong while processing your request.",
        }
      : msg
  )
);
  }
  finally{
    setisLoading(false)
  }
  
};


const handleDownload = async (content, format) => {
  try {
    await downloadDocument({
      report: content,
      fileType: format,
      fileName: `Report_${Date.now()}.${format}`,
      threadId,
      userId,
      uploadedFileName:"abc"
    });
}

catch (error) {
    console.error(error);
  }
};



const handleLogout = () => {
  localStorage.removeItem("userId");
  localStorage.removeItem("userType");

  router.push("/");
};
const isNewChat = messages.length === 0;

const renderComposer = () => (
  <div className="w-full max-w-4xl mx-auto">
    {/* Selected Files */}
    {selectedFiles.length > 0 && (
      <div className="mb-3 flex flex-wrap gap-2">
        {selectedFiles.map((file, index) => (
          <div
            key={index}
            className="flex items-center gap-2 rounded-full bg-muted px-3 py-1.5 text-sm"
          >
            <Paperclip className="h-3 w-3" />

            <span className="max-w-[220px] truncate">
              {file.name}
            </span>

            <button
              onClick={() =>
                setSelectedFiles((prev) =>
                  prev.filter((_, i) => i !== index)
                )}>
              <X className="h-3 w-3 cursor-pointer hover:text-red-500" />
            </button>
          </div>
        ))}
      </div>
    )}
  <div className="rounded-3xl border border-border bg-background px-4 py-1 shadow-sm">
   <div className="flex items-center gap-3">
    <input
      ref={fileInputRef}
      type="file"
      multiple
      disabled={isLoading}
      accept=".pdf,.doc,.docx,.png,.jpg,.jpeg"
      className="hidden"
      onChange={(e) => {
        const files = Array.from(e.target.files || []);

        setSelectedFiles(prev => {
          const existing = new Set(prev.map(f => f.name));

          return [
            ...prev,
            ...files.filter(f => !existing.has(f.name))
          ];
        });

        e.target.value = "";
      }}
    />

    <Button
      variant="ghost"
      size="icon"
      disabled={isLoading}
      className="h-10 w-10 rounded-full shrink-0"
      onClick={() => fileInputRef.current?.click()}
    >
      <Upload className="h-9 w-9" />
    </Button>

    <textarea
      disabled={isLoading}
      onChange={handleTextareaChange}
      rows={1}
      placeholder="Ask anything about your documents..."
      value={input}
      // onChange={(e) => setInput(e.target.value)}
      onKeyDown={(e) => {
        if (e.key === "Enter" && !e.shiftKey) {
          e.preventDefault();
          handleSendMessage();
        }
      }}
      className="
        flex-1
        min-h-[28px]
        max-h-40
        resize-none
        overflow-y-auto
        border-0
        bg-transparent
        px-0
        py-3
        text-md
        leading-7
        shadow-none
        outline-none
        ring-0
        focus:outline-none
        focus:ring-0
      "
    />

    <Button
      variant="ghost"
      size="sm"
      disabled={isLoading}
      className="rounded-full px-3"
      onClick={() => setOpenTools(true)}
    >
      <Sparkles className="mr-2 h-4 w-4" />
      Tools
    </Button>

    <Button
      size="icon"
      disabled={
        isLoading ||
        (!input.trim() && selectedFiles.length === 0)
      }
      className="h-9 w-9 rounded-full"
      onClick={handleSendMessage}
    >
        <Send className="h-5 w-5" />
    </Button>
  </div>
</div>
</div>
);

  return (
    <div className="h-screen w-full flex bg-background">
      <div className="flex-1 flex flex-col">
        <div className="sticky top-0 z-50  justify-between border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/80 p-4 flex items-center gap-3">
          <div className="flex items-center justify-center p-2 gap-2">
            <Avatar className="h-9 w-9 bg-primary flex items-center justify-center">
            <Bot className="h-5 w-5 text-primary-foreground" />
          </Avatar>
            <div className="font-semibold text-xl">DocuAssist</div>
          </div>
            <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="ghost" size="icon">
                    <Menu className="h-5 w-5" />
                  </Button>
                </DropdownMenuTrigger>
                
                <DropdownMenuContent align="end" className="w-48">
                
                  <DropdownMenuItem
                    className="cursor-pointer"
                    onClick={() => router.push("/history")}
                  >
                    <History className="mr-2 h-4 w-4" />
                    Chat History
                  </DropdownMenuItem>
                
                  <DropdownMenuItem
                    className="cursor-pointer text-red-600 focus:text-red-600"
                    onClick={handleLogout}
                  >
                    <LogOut className="mr-2 h-4 w-4" />
                    Logout
                  </DropdownMenuItem>
                
                </DropdownMenuContent>
              </DropdownMenu>
        </div>
        {isNewChat ? (
      <div className="flex-1 flex flex-col items-center justify-center px-6">
        <Bot className="h-16 w-16 text-primary mb-6" />

            <h1 className="text-4xl font-bold">
              DocuAssist
            </h1>
                
            <p className="text-muted-foreground mt-3 mb-10 text-center max-w-md">
              Upload your documents and ask questions, summarize content,
              analyze files, or generate professional drafts with AI.
            </p>
                
            {renderComposer()}
          </div>
        ) : (

          <>
       <ScrollArea className="flex-1 p-4">
         <div className="max-w-5xl mx-auto space-y-4">
           {messages.map((msg) => (
             <div
               key={msg.id}
               className={`flex gap-3 ${
                 msg.role === "user"
                   ? "justify-end"
                   : "justify-start"
               }`}
             >
               <div
                 className={`max-w-[75%] rounded-2xl px-4 py-3 ${
                   msg.role === "user"
                     ? "rounded-br-sm bg-primary text-primary-foreground"
                     : "rounded-bl-sm bg-slate-200 text-foreground"
                 }`}
               >
                 {/* <p className="text-sm">{msg.content}</p>    */}
                 <div
                      className={`
                        text-sm
                        leading-7
                        tracking-[0.2px]
             
                        [&_h1]:text-2xl
                        [&_h1]:font-bold
                        [&_h1]:mb-4
                      
                        [&_h2]:text-xl
                        [&_h2]:font-semibold
                        [&_h2]:mt-4
                        [&_h2]:mb-2
                      
                        [&_h3]:text-lg
                        [&_h3]:font-semibold
                      
                        [&_p]:mb-3
                      
                        [&_ul]:list-disc
                        [&_ul]:pl-6
                        [&_ul]:space-y-1
                      
                        [&_ol]:list-decimal
                        [&_ol]:pl-6
                        [&_ol]:space-y-1
                      
                        [&_li]:leading-7
                      
                        [&_strong]:font-semibold
                      
                        [&_blockquote]:border-l-4
                        [&_blockquote]:pl-4
                        [&_blockquote]:italic
                        [&_blockquote]:text-muted-foreground
                      
                        [&_code]:rounded
                        [&_code]:bg-muted
                        [&_code]:px-1.5
                        [&_code]:py-0.5
                        [&_code]:text-[0.9em]
                      
                        [&_pre]:overflow-x-auto
                        [&_pre]:rounded-lg
                        [&_pre]:bg-muted
                        [&_pre]:p-4
                      
                        [&_table]:w-full
                        [&_table]:border-collapse
                      
                        [&_th]:border
                        [&_th]:bg-muted
                        [&_th]:p-2
                        [&_th]:text-left
                      
                        [&_td]:border
                        [&_td]:p-2
                      `}
                    >
                     {msg.role === "user" ? (
                          <>
                            {msg.content && <p>{msg.content}</p>}
                                              
                            {msg.files?.length > 0 && (
                              <div className="mt-3 space-y-2">
                                {msg.files.map((file, index) => (
                                  <div
                                    key={index}
                                    className="flex items-center gap-2 rounded-md bg-white/10 px-3 py-2"
                                  >
                                    <Paperclip className="h-4 w-4" />
                                
                                    <span className="text-sm truncate">
                                      {file.name}
                                    </span>
                                  </div>
                                ))}
                              </div>
                            )}
                          </>
                        ) :
                        msg.loading ? (
                          <div className="flex justify-start">
                            <div className="rounded-2xl rounded-bl-sm bg-slate-200 px-4 py-3">
                              <ThreeDotsLoader />
                            </div>
                          </div>
                        ) : (
                          <ReactMarkdown remarkPlugins={[remarkGfm]}>
                            {msg.content}
                          </ReactMarkdown>
                        )}
                    </div>
                    {msg.role === "assistant" &&
                        msg.answer_type === "document" &&(
                          <div className="mt-4 flex flex-wrap gap-2">
                          
                            <Button
                              size="sm"
                              variant="secondary"
                              className="cursor-pointer"
                              onClick={() => handleDownload(msg.content, "pdf")}
                            >
                              <FileDown className="mr-2 h-4 w-4" />
                              Download PDF
                            </Button>
                            
                            <Button
                              size="sm"
                              variant="secondary"
                              className="cursor-pointer"
                              onClick={() =>
                                handleDownload(msg.content, "docx")
                              }
                            >
                              <FileText className="mr-2 h-4 w-4" />
                              Download Word
                            </Button>
                            
                          </div>
                      )}
               </div>   
             </div>
           ))}  

           <div ref={bottomRef} />
         </div>
       </ScrollArea>

    <div className="border-t p-4">
      {renderComposer()}
    </div>
    <Toaster richColors position="top-center" />
  </>
)}
      </div>
        <AdminToolsDialog
          open={openTools}
          onOpenChange={setOpenTools}
          role={userType}
          onSelectTool={(prompt) => {
            setInput(prompt);
            setOpenTools(false);
          }}
        />
    </div>
    
  );

};

export default ChatPage