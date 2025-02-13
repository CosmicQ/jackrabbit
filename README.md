# Jackrabbit

Jackrabbit is a mock-up of a ride-sharing app designed for self-learning with Kubernetes, microservices, and DevOps practices. This project demonstrates how to build, deploy, and manage a cloud-native application using modern technologies.

### **Technologies Used**
- **Frontend**: React (or Flask for simplicity)
- **Backend**: Python (Flask/FastAPI)
- **Database**: PostgreSQL
- **Caching**: Redis
- **Reverse Proxy**: Nginx
- **Infrastructure as Code**: Terraform
- **Containerization**: Docker
- **Orchestration**: Kubernetes (via Helm & YAML)
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus, Grafana, Loki

### **Features**
- User registration and ride requests
- Display driver availability and locations
- Persistent storage using PostgreSQL
- Fast access to driver locations via Redis
- Kubernetes-based deployment with Helm
- Continuous delivery pipeline using GitHub Actions
- Monitoring setup with Prometheus and Grafana
- Logging with Loki

---

### **Getting Started**

#### **Prerequisites**
- [Docker](https://www.docker.com/get-started)
- [Kubernetes](https://kubernetes.io/docs/setup/)
- [Helm](https://helm.sh/docs/intro/install/)
- [Terraform](https://www.terraform.io/docs)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [GitHub Actions](https://docs.github.com/en/actions)

#### **Setup**
1. **Clone the repo**:
```
   bash
   git clone https://github.com/yourusername/jackrabbit.git
   cd jackrabbit
```
2. **Set up Kubernetes (local or cloud-based cluster)**:
    If using a local setup, Minikube is a good option.

3. **Deploy with Helm**:

    Add the necessary Helm charts and deploy using:
```
  helm install jackrabbit ./helm/ride-share
```

4. **Deploy infrastructure with Terraform**:
```
  terraform init
  terraform apply
```

5. **Run the CI/CD pipeline**: 
GitHub Actions will automatically build and deploy the app whenever code is pushed.

Local Development

To run the project locally (without Kubernetes):

    Build Docker images for frontend and backend.

    docker-compose up --build

Monitoring

    Access the Prometheus and Grafana dashboards to monitor the app.
    Check logs via Loki for debugging.

---

Contributing

Feel free to open issues, submit PRs, or raise any questions. This is a personal learning project, and contributions are always welcome!

---

License

This project is open-source and licensed under the MIT License.
