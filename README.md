# 🚀 End-to-End GitOps Continuous Delivery Pipeline

## 🎯 Project Objective
"I built a complete, production-grade GitOps Delivery Pipeline for a microservices application using GitHub Actions, Helm, Argo CD, and Kubernetes (Minikube). Every application code change triggers an automated CI pipeline that builds and scans container images, updates configuration manifests in Git, and lets Argo CD automatically synchronize the changes to the cluster while continuously enforcing drift detection and self-healing."

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
# Full GitOps Pipeline Verified
