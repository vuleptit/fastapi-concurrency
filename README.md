# FastAPI Cocurrency

# ASGI (Async Server Gateway Interface)

- Là bản nâng cấp của WSGI
- Hỗ trợ thêm
  - async + await
  - WebSocket
  - HTTP/2
  - Long-live connection
  - High cocurrency (event loop)

- Flow:
  ```
  Client
      ↓
  Uvicorn (ASGI server)
      ↓
  FastAPI (ASGI app)
  ```
