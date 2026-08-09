# 🚀 End-to-End GitOps Continuous Delivery Pipeline

## 🎯 Project Objective
Build a lightweight multi-service web application (Frontend + Backend) and deploy it to Kubernetes using a modern **GitOps Continuous Delivery** pipeline powered by Argo CD, Helm, GitHub Actions, and Trivy.

---

## 🏗️ Architecture & Workflow Overview
1. **Developer**: Pushes code to the `gitops-app-code` GitHub repository.
2. **GitHub Actions (CI)**: 
   - Builds Docker images for Frontend and Backend services.
   - Scans images for vulnerabilities using **Trivy**.
   - Pushes verified images to GitHub Container Registry (GHCR).
   - Automatically updates the image tags in the `gitops-manifests` repository.
3. **Argo CD (GitOps CD)**:
   - Continuously monitors the `gitops-manifests` repository.
   - Detects changes and automatically reconciles the state in the **Kubernetes Cluster**.
4. **Kubernetes & Helm**:
   - Deploys application workloads via customized Helm charts.

---

## 🛠️ Tech Stack
- **Application**: HTML/Nginx (Frontend), Python/Flask (Backend)
- **Containerization**: Docker
- **Container Registry**: GitHub Container Registry (GHCR)
- **CI & Security**: GitHub Actions, Trivy
- **Orchestration & Packaging**: Kubernetes (Minikube), Helm
- **GitOps CD**: Argo CD

---

## 📁 Repository Structure
- `gitops-app-code`: Source code, Dockerfiles, and GitHub Actions workflows.
- `gitops-manifests`: Helm charts and Argo CD application manifests.
