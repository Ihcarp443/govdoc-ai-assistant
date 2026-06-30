export default function ThreeDotsLoader() {
  return (
    <div className="flex items-center gap-1 px-2 py-1">
      <span
        className="h-2 w-2 rounded-full bg-primary animate-dot-wave"
        style={{ animationDelay: "0s" }}
      />
      <span
        className="h-2 w-2 rounded-full bg-primary animate-dot-wave"
        style={{ animationDelay: "0.15s" }}
      />
      <span
        className="h-2 w-2 rounded-full bg-primary animate-dot-wave"
        style={{ animationDelay: "0.3s" }}
      />
    </div>
  );
}