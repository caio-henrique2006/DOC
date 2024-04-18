import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";
import Menu from "@/components/menu";

export const metadata: Metadata = {
  title: "Tutorial de Next",
  description: "Criado por Caio seguindo o tutorial de Next JS da Origamid",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>
        <Menu />
        {children}
      </body>
    </html>
  );
}
