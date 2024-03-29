import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Tutorial de Next',
  description: 'Criado por Caio seguindo o tutorial de Next JS da Origamid',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}