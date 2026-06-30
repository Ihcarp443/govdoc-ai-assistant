"use client";

import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";
import { FileText,FilePen,SearchCheck } from "lucide-react";
const AdminToolsDialog = ({open,onOpenChange,onSelectTool,role}) => {


      const toolOptions = [
      {
        title: "Summarize",
        roles: ["public", "admin"],
        icon: FileText,
        color:
"border-blue-200 bg-blue-50 text-blue-700 hover:bg-blue-100 dark:border-blue-900 dark:bg-blue-950/30 dark:text-blue-300",
        prompt:
          "Summarize this document in concise bullet points highlighting the important information.",
      },
      {
        title: "Draft Reply",
        roles: ["public", "admin"],
        icon: FilePen,
       color:
"border-green-200 bg-green-50 text-green-700 hover:bg-green-100 dark:border-green-900 dark:bg-green-950/30 dark:text-green-300",
        prompt:
          "Draft a professional response based on the uploaded document.",
      },
      {
        title: "Analyze Document",
        roles: ["public", "admin"],
        icon: SearchCheck,
       color:
"border-purple-200 bg-purple-50 text-purple-700 hover:bg-purple-100 dark:border-purple-900 dark:bg-purple-950/30 dark:text-purple-300",
        prompt:
          "Analyze this document and identify important clauses, risks, key insights and recommendations.",
      },
    ];
    
    role="public"
    const visibleTools = toolOptions.filter((tool) =>
    tool.roles.includes(role)
    );

  return (

   <Dialog open={open} onOpenChange={onOpenChange}>
  <DialogContent className="sm:max-w-2xl">
      <DialogTitle className="text-xl font-semibold flex justify-center items-center">
        AI Tools
      </DialogTitle>
     <div className="flex justify-between gap-3 mt-6">
     {visibleTools.map((tool) => {
    const Icon = tool.icon;

    return (
      <button
        key={tool.id}
        onClick={() => onSelectTool(tool.prompt)}
        className={`cursor-pointer flex items-center gap-3 rounded-lg border px-5 py-2 text-left transition-all hover:shadow-md ${tool.color}`}
      >
        <div className="flex h-7 w-7 items-center justify-center rounded-lg">
          <Icon className="h-4 w-4" />
        </div>

        <h3 className="font-medium">{tool.title}</h3>
      </button>
    );
  })}
    </div>
    <DialogHeader>
    

      <DialogDescription asChild>
        <div className="mt-3 rounded-lg  bg-muted/30 p-4">
          <h4 className="font-semibold text-foreground mb-2">
            Instructions
          </h4>

          <ul className="list-disc space-y-1 pl-5 text-sm text-muted-foreground">
            <li>Upload a PDF, DOCX or image before using any AI tool.</li>
            <li>Select one of the tools above.</li>
            <li>You can edit the prompt before sending it.</li>
            <li>Some tools work best with well-formatted documents.</li>
          </ul>
        </div>
      </DialogDescription>
    </DialogHeader>

    {/* <div className="flex justify-between gap-3 mt-6">
      {toolOptions.map((tool) => {
        const Icon = tool.icon;

        return (
          <button
            key={tool.title}
            onClick={() => onSelectTool(tool.prompt)}
            className={`flex items-center gap-3 rounded-lg border px-5 p-y-4  text-left transition-all hover:shadow-md hover:scale-[1.02] ${tool.color}`}
          >
            <div className="flex h-7 w-7 items-center justify-center rounded-lg">
              <Icon className="h-4 w-4" />
            </div>

            <div>
              <h3 className="font-medium">
                {tool.title}
              </h3>
            </div>
          </button>
        );
      })}
    </div> */}
  </DialogContent>
</Dialog>
  );
};

export default AdminToolsDialog;