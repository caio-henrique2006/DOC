'use client'
import { useState } from 'react';

export default function ImcPage() {

    const [peso, setPeso] = useState("");
    const [altura, setAltura] = useState("");
    const [resultado, setResultado] = useState("");

    function calc () {
        console.log(peso, altura);
    }

    return (
        <main>
            <p>Peso:</p>
            <input type="text" id="peso" onChange={(e) => {setPeso(e.currentTarget.value)}} />
            <p>Altura:</p>
            <input type="text" id="altura" onChange={(e) => {setAltura(e.currentTarget.value)}} />
            <button onClick={calc}>Calcular</button>
        </main>
    )
}