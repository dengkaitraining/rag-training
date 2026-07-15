### Google Gemini API - curl
```bash
   curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
    -H 'Content-Type: application/json' \
    -H 'X-goog-api-key: {API_KEY}' \
    -X POST \
    -d '{
      "contents": [
        {
             "parts": [
            {
              "text": "請描述 Taiwan 這個國家的特色"
            }
          ]
        }
      ]
    }'
```
### Local Ollama API - curl
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2:latest",
  "messages": [
    { "role": "system", "content": "請描述 Taiwan 這個國家的特色" }
  ]
}'
```