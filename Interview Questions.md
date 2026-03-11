### Interview Question

1. What is the difference between container and virtual machine?
2. What is the role of the Docker daemon?
3. Explain Docker image layers.
4. Difference between docker run vs docker start.
5. Explain -p vs -P.
6. Difference between CMD and ENTRYPOINT.
7. Why containers lose data without volumes?
8. Bind mounts vs volumes.
9. Explain Docker bridge network.
10. How do containers communicate?
11. Why multi-stage builds are important?
12. How do you reduce Docker image size?
13. Where are Docker logs stored?
14. How do you monitor container performance?
15. How do you reduce Docker image size?

---

# 1. What is the difference between a Container and a Virtual Machine?
   
| Feature      | Container             | Virtual Machine   |
| ------------ | --------------------- | ----------------- |
| OS           | Shares host OS kernel | Has its own OS    |
| Startup time | Seconds               | Minutes           |
| Size         | Lightweight (MBs)     | Heavy (GBs)       |
| Performance  | Near native           | Slight overhead   |
| Isolation    | Process-level         | Full OS isolation |

# Virtual Machine

Hardware
   ↓
Host OS
   ↓
Hypervisor
   ↓
Guest OS
   ↓
Application

# Docker Container

Hardware
   ↓
Host OS
   ↓
Docker Engine
   ↓
Containers
   ↓
Applications

Containers are faster because they reuse the host OS kernel.

---

# 2. What is the role of the Docker Daemon?

The Docker daemon (dockerd) is the background service responsible for managing:

- Containers
- Images
- Networks
- Volumes

It listens for API requests from the Docker CLI and executes them.

Example

When you run:

```bash
docker run nginx
```
The flow is:

```copy
Docker CLI → Docker Daemon → Create Container → Start Container
```

---

# 3. Explain Docker Image Layers

A Docker image is built using layered filesystems.

Each instruction in a Dockerfile creates a new layer.

Example Dockerfile:

```copy
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

Layers created:

```copy
Layer 1 → Base image
Layer 2 → WORKDIR
Layer 3 → Copy requirements
Layer 4 → Install dependencies
Layer 5 → Copy application
```
Benefits:

- Faster builds (layer caching)
- Reusability
- Smaller downloads

Check layers:

```copy
docker history IMAGE_NAME
```
---

# 4. Difference between docker run and docker start

| Command      | Purpose                      |
| ------------ | ---------------------------- |
| docker run   | Creates + starts a container |
| docker start | Starts an existing container |

Example

Create container:

```copy
docker run -d nginx
```
Start stopped container:

```copy
docker start CONTAINER_ID
```

---

# 5. Explain -p vs -P

-p (Manual Port Mapping)

```copy
docker run -p 8080:80 nginx
```
Meaning:

```copy
Host Port → 8080
Container Port → 80
```
Access via:

```
http://localhost:8080
```
-P (Random Port Mapping)

```bash
docker run -P nginx
```
Docker automatically assigns a host port.

Check mapping:

```bash
docker port CONTAINER_ID
```
---

# 6. Difference between CMD and ENTRYPOINT

| CMD                      | ENTRYPOINT                |
| ------------------------ | ------------------------- |
| Default command          | Main executable           |
| Can be overridden easily | Harder to override        |
| Provides arguments       | Defines container program |


Example

```copy
CMD ["python", "app.py"]
```
ENTRYPOINT example:

```copy
ENTRYPOINT ["python"]
CMD ["app.py"]
```

Run:

```
docker run image script.py
```

Output command becomes:

```
python script.py
```
---

# 7. Why containers lose data without volumes?

Containers are ephemeral.

When a container is deleted:

```
Container filesystem → destroyed
```
Any data inside the container is lost.

Example:
```
Database inside container
Container removed
Database lost
```

Solution → Volumes

---

# 8. Bind Mounts vs Volumes

| Feature            | Volume          | Bind Mount    |
| ------------------ | --------------- | ------------- |
| Managed by Docker  | Yes             | No            |
| Host path required | No              | Yes           |
| Portable           | Yes             | Less portable |
| Best for           | Production data | Development   |

Volume Example
```
docker volume create mydata
```

Run container:
```
docker run -v mydata:/data nginx
```
Bind Mount Example

```copy
docker run -v $(pwd):/app python
```

---

# 9. Explain Docker Bridge Network

Bridge network is the default Docker network.

It allows containers to communicate using internal IP addresses.

List networks:

```
docker network ls
```
Example:

```
bridge
host
none
```

Create custom bridge network:

```bash

docker network create mynetwork
```
Run containers inside network:

```bash
docker run -d --network mynetwork nginx
```
---

# 10. How do containers communicate?

Three main ways:

1. Same Network

Containers inside the same network can communicate using container names.

Example:
```
backend → database
```

2. Port Mapping

Expose container service to host.

```
docker run -p 8080:80 nginx
```
3. Docker DNS

Docker automatically provides DNS resolution for container names.

Example:

```
http://database:5432
```
---

# 11. Why Multi-Stage Builds are Important?

Multi-stage builds reduce image size by separating:

```
Build environment
Runtime environment
```
Example:

```dockerfile
FROM node:20 AS builder
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```
Benefits:

- Smaller images
- Better security
- Faster deployments

---


# 12. How do you reduce Docker image size?

Best practices:

1. Use smaller base images

```copy
python:3.11-slim
node:alpine
```
2. Use multi-stage builds

3. Remove unnecessary files

4. Use .dockerignore

Example .dockerignore:

```
node_modules
.git
*.log
```
---

# 13. Where are Docker logs stored?

By default Docker stores logs in:

```
/var/lib/docker/containers/<container-id>/
```
View logs:

```
docker logs CONTAINER_ID
```
Follow logs:
```
docker logs -f CONTAINER_ID
```

---

# 14. How do you monitor container performance?

Docker provides monitoring commands.

CPU & Memory usage

```
docker stats
```
Example output:

```
CONTAINER   CPU %   MEM USAGE
nginx       1.2%    25MB
```
Check running processes

```
docker top CONTAINER_ID
```
---

# 16. How do you debug a failing container?

Steps:

1. Check logs
```
docker logs CONTAINER_ID
```

2. Inspect container
```
docker inspect CONTAINER_ID
```

3. Enter container
```
docker exec -it CONTAINER_ID bash
```
---

17. What is Docker Build Cache?

Docker caches layers to speed up builds.

If instructions haven't changed, Docker reuses previous layers.

Example:
```
COPY requirements.txt
RUN pip install
```

If requirements.txt doesn't change, the layer is reused.

---
