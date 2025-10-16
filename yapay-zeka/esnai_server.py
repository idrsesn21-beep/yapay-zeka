# ESNAI Cloud v1.0 — Text-only (TTS opsiyonel)
# Flask API + GPT4All (lokal açık kaynak LLM). Ücretsiz/bağımsız.
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

APP_PORT = int(os.getenv("PORT", "10000"))
MODEL_NAME = os.getenv("ESNAI_MODEL", "orca-mini-3b-gguf2-q4_0.gguf")
MAX_TOKENS_DEFAULT = int(os.getenv("ESNAI_MAX_TOKENS", "300"))

app = Flask(__name__)
CORS(app)

_llm = None
def load_llm():
    global _llm
    if _llm is not None:
        return _llm
    try:
        from gpt4all import GPT4All
        _llm = GPT4All(MODEL_NAME)
        return _llm
    except Exception as e:
        print("[ESNAI] LLM yüklenemedi:", e)
        return None

@app.get("/health")
def health():
    ok = load_llm() is not None
    return jsonify({"ok": ok, "model": MODEL_NAME})

@app.post("/story")
def story():
    """Body JSON:
    {
      "prompt": "6-8 yaş çocuklar için cesaret temalı kısa hikaye",
      "max_tokens": 220,
      "temperature": 0.8
    }"""
    llm = load_llm()
    if llm is None:
        return jsonify({"error":"LLM not loaded"}), 500

    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "6-8 yaş için nazik bir anlatımla kısa hikaye (100-150 kelime). Tema: cesaret.")
    max_tokens = int(data.get("max_tokens", MAX_TOKENS_DEFAULT))
    temperature = float(data.get("temperature", 0.8))

    system = "Türkçe yaz. 6-8 yaş için uygundur. Pozitif, güvenli, öğretici ve nazik ol."
    full = f"{system}\nKONU: {prompt}\nHİKAYE:"
    try:
        text = llm.generate(full, max_tokens=max_tokens, temp=temperature)
        return jsonify({"text": text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print(f"[ESNAI] Server starting on 0.0.0.0:{APP_PORT} — model={MODEL_NAME}")
    app.run(host="0.0.0.0", port=APP_PORT, debug=False)
