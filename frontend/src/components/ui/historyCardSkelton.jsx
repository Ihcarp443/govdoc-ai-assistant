import { Skeleton } from "@/components/ui/skeleton";
import { Separator } from "@/components/ui/separator";
import { Card } from "@/components/ui/cards";
const HistoryCardSkeleton = () => {
  return (
    <Card className="p-5">
      <div className="flex items-start justify-between mb-3">
        <Skeleton className="h-12 w-12 rounded-lg" />

        <div className="flex flex-col items-end gap-2">
          <Skeleton className="h-3 w-16" />
        </div>
      </div>

      <Skeleton className="h-6 w-3/4 mb-2" />
      <Skeleton className="h-4 w-full mb-1" />
      <Skeleton className="h-4 w-2/3 mb-4" />

      <Separator className="mb-3" />

      <Skeleton className="h-3 w-24 mb-2" />

      <div className="flex flex-wrap gap-2">
        <Skeleton className="h-6 w-24 rounded-md" />
        <Skeleton className="h-6 w-20 rounded-md" />
      </div>
    </Card>
  );
};

export {HistoryCardSkeleton}