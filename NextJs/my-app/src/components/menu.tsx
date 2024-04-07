import Link from 'next/link'

export default function Menu () {
    return (
        <div>
          <ul>
            <li><Link href="/" prefetch={true}>Menu</Link></li>
            <li><Link href="/sobre" prefetch={true}>Sobre</Link></li>
            <li><Link href="/contato" prefetch={true}>Contato</Link></li>
          </ul>
        </div>
    )
}