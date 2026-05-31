# CSC & Upcloud Web Deployment Prototypes - FastAPI Todo App

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://github.com/tiangolo/fastapi)
[![Rahti](https://img.shields.io/badge/CSC_Rahti-Container_Cloud-blue?style=for-the-badge)](https://rahti.csc.fi)
[![Pukki](https://img.shields.io/badge/CSC_Pukki-Managed_DB_Cluster-orange?style=for-the-badge)](https://pukki.csc.fi)
[![cPouta](https://img.shields.io/badge/CSC_cPouta-IaaS_Cloud-purple?style=for-the-badge)](https://research.csc.fi/cpouta)
[![UpCloud](https://img.shields.io/badge/UpCloud-Commercial_IaaS-darkgreen?style=for-the-badge&logo=upcloud)](https://upcloud.com)

This repository serves as the practical application prototype for the project **"Web deployment prototypes with CSC and Upcloud"**.

It adapts and extends an open-source framework originally built by [borys25ol/fastapi-todo-example-app](https://github.com/borys25ol/fastapi-todo-example-app.git) to implement a decoupled, production-ready backend Todo application, which is used here to systematically evaluate various cloud infrastructure capabilities.

---

### 🛠️ Technology Stack

- **Framework:** FastAPI (Python)
- **Database Tools:** SQLAlchemy & Alembic (Migrations)
- **Target Drivers:** SQLite (Phase V1), PostgreSQL (Phases V2-V4)
- **Containerization:** Docker & OpenShift S2I Pipelines

---

## 🚀 Project Deployment Roadmap

To systematically evaluate cloud deployment strategies, this project is structured into three iterative phases:

### 📍 Phase V1: Standalone Cloud Deployment (Current)

- **Objective:** Establish the core compute container environment and verify standalone network accessibility.
- **Infrastructure:** **CSC Rahti (Container Cloud)** via Source-to-Image (S2I) build mechanism.
- **Database:** Embedded standalone **SQLite** (`todo.db`) for isolated container health and initial API verification.

### ⏳ Phase V2: Managed Cloud Database Integration

- **Objective:** Separate state from compute to achieves "Compute-and-Data Separation".
- **Infrastructure:** **CSC Rahti** (Compute in Containers) + **CSC Pukki** (Managed PostgreSQL Cluster).

### ⏳ Phase V3: Infrastructure Evolution to IaaS

- **Objective:** Performance benchmarking between Platform-as-a-Service (Rahti) and Infrastructure-as-a-Service (cPouta Ubuntu VMs).
- **Sub-Phase V3.1:** All-in-One Architecture (FastAPI App & PostgreSQL coupled locally inside cPouta VM).
- **Sub-Phase V3.2:** Cloud-Native Disaggregated Architecture (cPouta VM compute node remote-routing to CSC Pukki DB).

### ⏳ Phase V4: Hybrid Multi-Cloud Topology 
- **Infrastructure:** **UpCloud** (VM) + **CSC Pukki** (Cross-Cloud DB Connectivity)

---

## 🌐 Web Routes & API Interaction

- **API Interactive Dashboard (Swagger UI):** Automatically generated and available directly at the root path `/` (e.g., `http://127.0.0.1:8000/` or assigned public Rahti Route URL).
- **System Health Gateway:** Available at `/api/v1/status`.

## Project structure

Files related to application are in the `main` directory.
Application parts are:

```text
main
├── __init__.py
├── api
│   ├── __init__.py
│   └── v1
│       ├── __init__.py
│       ├── router.py
│       └── routes
│           ├── __init__.py
│           ├── status.py
│           ├── tasks.py
│           └── user.py
├── app.py
├── core
│   ├── __init__.py
│   ├── config.py
│   ├── dependencies.py
│   ├── exceptions.py
│   ├── logging.py
│   ├── security.py
│   └── settings
│       ├── __init__.py
│       ├── app.py
│       └── base.py
├── db
│   ├── __init__.py
│   ├── base.py
│   ├── base_class.py
│   ├── migrations
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       └── dfb75cfbf652_create_tables.py
│   ├── repositories
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── tasks.py
│   │   └── users.py
│   └── session.py
├── models
│   ├── __init__.py
│   ├── task.py
│   └── user.py
├── schemas
│   ├── __init__.py
│   ├── response.py
│   ├── status.py
│   ├── tasks.py
│   └── user.py
├── services
│   ├── __init__.py
│   └── user.py
└── utils
    ├── __init__.py
    └── tasks.py
```
