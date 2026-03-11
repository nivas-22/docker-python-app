

### Build the Images

## Normal Dockerfile

```bash
docker build -t python-app .
```

---

## Multi-stage Dockerfile

```copy
docker build -f Dockerfile.multi -t python-app-multi .
```

---

## Run the Container

```bash
docker run -p 5000:5000 python-app
```

# Open browser:

```copy
http://localhost:5000
```

## Response:

```json
{
  "message": "Welcome to Docker Python App 🚀",
  "python_version": "3.11",
  "server_time": "2026-03-11 12:30:00"
}
```
---

