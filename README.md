# MindPlan - Smart AI Based Calendar

MindPlan is a personal productivity assistant that tracks your activity on Windows, logs application usage, and provides insights via an API. This backend is designed to serve a React frontend for visualizing usage and generating AI-driven calendar recommendations.

---

## 🎯 Project Scope

- Track user activity on Windows: apps, window titles, start/end times.
- Store activity logs in a local SQLite database.
- Provide API endpoints to serve activity data for frontend visualization.
- Lay the foundation for AI-driven calendar recommendations based on user habits.
- Modular and extensible architecture for future features and cross-platform support.

## 📦 Dependencies

- annotated-types
- anyio
- click
- colorama
- fastapi
- greenlet
- h11
- idna
- psutil
- pydantic
- pydantic_core
- pywin32
- sniffio
- SQLAlchemy
- starlette
- typing-inspection
- typing_extensions
- uvicorn

## ⚡ Features

- Track active apps and window titles on Windows.
- Log start time, end time, and duration of usage per app.
- Serve activity data via API endpoints.

## 📝 Updating the README

- Fixed UnicodeEncodeError on Windows when writing README.
- Resolved tracker crash when DB table did not exist.
