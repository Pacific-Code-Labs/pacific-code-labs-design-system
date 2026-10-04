import { useId, type ReactNode } from "react";
import { Button } from "./ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "./ui/dialog";
export { Button };
export function Skeleton({ label }: { label: string }) {
  return (
    <div aria-busy="true" aria-label={label} className="space-y-6">
      <div className="h-10 w-1/3 rounded-xl bg-muted animate-pulse" />
      <div className="grid sm:grid-cols-3 gap-4">
        {[1, 2, 3].map((i) => (
          <div key={i} className="h-28 rounded-2xl bg-muted animate-pulse" />
        ))}
      </div>
      <div className="h-72 rounded-2xl bg-muted animate-pulse" />
    </div>
  );
}
export function Drawer({
  open,
  title,
  description,
  onClose,
  children,
}: {
  open: boolean;
  title: string;
  description: string;
  onClose: () => void;
  children: ReactNode;
}) {
  return (
    <Dialog
      open={open}
      onOpenChange={(v) => {
        if (!v) onClose();
      }}
    >
      <DialogContent className="!left-auto !right-0 !top-0 !translate-x-0 !translate-y-0 h-dvh max-w-xl rounded-none flex flex-col p-0">
        <DialogHeader className="p-6 border-b">
          <DialogTitle>{title}</DialogTitle>
          <DialogDescription>{description}</DialogDescription>
        </DialogHeader>
        <div className="overflow-y-auto p-6 flex-1">{children}</div>
      </DialogContent>
    </Dialog>
  );
}

export function LanguageFlag({ language }: { language: "es" | "en" }) {
  const clip = useId();
  return (
    <svg width="24" height="18" viewBox="0 0 30 20" aria-hidden="true">
      <defs>
        <clipPath id={clip}>
          <rect width="30" height="20" rx="2" />
        </clipPath>
      </defs>
      <g clipPath={`url(#${clip})`}>
        <rect width="30" height="20" fill="white" />
        {language === "es" ? (
          <>
            <path d="M0 0H30V3.33H0ZM0 16.67H30V20H0Z" fill="#002b7f" />
            <rect y="6.67" width="30" height="6.66" fill="#ce1126" />
          </>
        ) : (
          <>
            {[0, 2, 4, 6, 8, 10, 12].map((i) => (
              <rect
                key={i}
                y={(i * 20) / 13}
                width="30"
                height={20 / 13}
                fill="#b22234"
              />
            ))}
            <rect width="12" height={(7 * 20) / 13} fill="#3c3b6e" />
            {Array.from({ length: 9 }, (_, row) =>
              Array.from({ length: row % 2 ? 5 : 6 }, (_, col) => (
                <circle
                  key={`${row}-${col}`}
                  cx={1 + col * 2 + (row % 2 ? 1 : 0)}
                  cy={0.8 + row * 1.15}
                  r=".35"
                  fill="white"
                />
              )),
            )}
          </>
        )}
      </g>
      <rect
        x=".5"
        y=".5"
        width="29"
        height="19"
        rx="2"
        fill="none"
        stroke="currentColor"
        strokeOpacity=".15"
      />
    </svg>
  );
}
