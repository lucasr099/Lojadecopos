console.log("APP.JSX ESTÁ SENDO RENDERIZADO!");


import { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  async function sendMessage() {
    console.log("BOTÃO CLIKADO. message =", message);

  if (!message.trim()) return;

  try {
    const res = await axios.post(
      "http://127.0.0.1:8000/chat/",
      { message },
      { headers: { "Content-Type": "application/json" } }
    );

    console.log("RESPOSTA DO SERVER:", res.data);

    setResponse(res.data.response);

  } catch (err) {
    console.log("ERRO:", err);
    setResponse("Erro ao falar com o servidor.");
  }
}


  return (
    <div style={{ padding: 40, fontFamily: "Arial" }}>
      <h1>Bot Loja Copos</h1>

      <textarea
        value={message}
        onChange={e => setMessage(e.target.value)}
        placeholder="Pergunte algo sobre o estoque..."
        style={{ width: "100%", height: 120, marginBottom: 20 }}
      />

      <button onClick={sendMessage} style={{
        padding: "10px 20px",
        fontSize: 18,
        cursor: "pointer"
      }}>
        Enviar
      </button>

      <h2>Resposta:</h2>
      <div style={{
        background: "#f0f0f0",
        padding: 20,
        borderRadius: 8,
        minHeight: 100
      }}>
        {response}
      </div>
    </div>
  );
}

export default App;

