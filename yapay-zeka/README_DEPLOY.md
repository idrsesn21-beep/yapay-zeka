# ESNAI Cloud v1.0 — Ücretsiz, Bağımsız Metin Üretim Sunucusu

Bu paket, **GPT vb. dış API olmadan**, açık kaynak LLM (GPT4All) ile çalışan **metin üretim** sunucusudur.
Varsayılan model: `orca-mini-3b-gguf2-q4_0.gguf` (küçük, ücretsiz).

> v1 = Metin. (TTS/Video v2–v3’te eklenecek.)

---

## 1) Dosyalar
- `esnai_server.py` → Flask API
- `requirements.txt` → Python bağımlılıkları
- `Procfile` → (Railway/Heroku uyumlu başlatma komutu)
- `render.yaml` → Render.com için tek tık deploy ayarı
- `web/index.html` → Basit test istemcisi

---

## 2) Lokal Çalıştırma (PC)
```bash
pip install -r requirements.txt
python esnai_server.py
```
Sunucu: `http://127.0.0.1:10000`
Test: `web/index.html` dosyasını tarayıcıda açın → URL alanına `http://127.0.0.1:10000` yazın → “Metin üret”.

> İlk istekte GPT4All modeli indirir (ücretsiz).

---

## 3) Cloud’a Kurulum (Seçenekler)

### A) Render.com (Önerilen, ücretsiz plan)
1. GitHub’ta yeni repo aç → bu dosyaları push et.
2. https://render.com → “New” → “Web Service” → repo’nu seç.
3. Environment: **Python**
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python esnai_server.py`
6. Deploy → Sana `https://esnai-xxx.onrender.com` gibi bir adres verir.
7. `web/index.html`’de bu adresi yazıp test et.

> `render.yaml` dosyası varsa “Blueprint” ile tek adımda da kurulur.

### B) Railway.app (kolay)
1. https://railway.app → New Project → “Deploy from GitHub”.
2. `Procfile` zaten `web: python esnai_server.py` yazıyor → otomatik algılar.
3. Domain oluşunca `web/index.html` ile test et.

### C) Replit (en hızlı prototip)
1. https://replit.com → Python Repl oluştur.
2. Bu 4 dosyayı yükle: `esnai_server.py`, `requirements.txt`, `web/index.html`, `Procfile`
3. Shell: `pip install -r requirements.txt`
4. Run → public URL ile çalışır.

---

## 4) API Kullanımı

### 4.1 Sağlık
`GET /health` → `{ ok: true, model: "..." }`

### 4.2 Metin Üretimi
`POST /story`
```json
{"prompt":"6-8 yaş için cesaret temalı kısa hikaye","max_tokens":260,"temperature":0.8}
```
Yanıt:
```json
{"text":"...metin..."}
```

---

## 5) Ortam Değişkenleri (opsiyonel)
- `PORT` (varsayılan 10000)
- `ESNAI_MODEL` (varsayılan `orca-mini-3b-gguf2-q4_0.gguf`)
- `ESNAI_MAX_TOKENS` (varsayılan 300)

> Daha büyük modeller için sunucuda RAM/CPU gerekebilir.

---

## 6) Sonraki Adımlar
- v2: **TTS (Coqui)** modülü, `/tts` endpoint
- v3: **Görsel/Video** pipeline (AnimateDiff / MoviePy)
- ESN IA Studio → ESNAI Cloud API ile konuşacak (GPT yerine).

Bilal, bu senin **kendi yapay zekan** için temel taştır. ESNAI’yi buradan büyütüyoruz.
