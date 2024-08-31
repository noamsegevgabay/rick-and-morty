# Rick and Morty Flask App - CI/CD Workflow

This README provides details on the GitHub Actions workflow used for deploying and testing the Rick and Morty Flask application on a Kubernetes cluster using Kind.

## Workflow Overview

The GitHub Actions workflow automates the deployment and testing of the Flask application. It includes steps for creating a Kubernetes cluster, deploying the application using Helm, testing the application endpoints, and cleaning up the cluster.

## Workflow Configuration

### `name: Deploy and Test Application`

The workflow is triggered on `push` to the `main` branch and on `pull_request` events.

### Jobs

#### `deploy-and-test`

**Runs on**: `ubuntu-latest`

**Steps**:

1. **Checkout code**
   ```bash
   uses: actions/checkout@v2
Checks out the repository code.

Install Kind

bash
Copy code
run: |
  curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
  chmod +x ./kind
  sudo mv ./kind /usr/local/bin/kind
Downloads and installs Kind for creating a Kubernetes cluster.

Create Kubernetes cluster

bash
Copy code
run: kind create cluster --wait 5m
Creates a Kubernetes cluster using Kind and waits for 5 minutes.

Wait for Kubernetes API

bash
Copy code
run: |
  for i in {1..10}; do
    kubectl cluster-info && break || sleep 10;
  done
Waits for the Kubernetes API to be accessible.

Install kubectl

bash
Copy code
run: |
  curl -LO "https://dl.k8s.io/release/v1.24.0/bin/linux/amd64/kubectl"
  chmod +x ./kubectl
  sudo mv ./kubectl /usr/local/bin/kubectl
Downloads and installs kubectl for interacting with the Kubernetes cluster.

Install Helm

bash
Copy code
run: |
  curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
Downloads and installs Helm for managing Kubernetes applications.

Deploy application with Helm

bash
Copy code
run: |
  helm upgrade --install flask-app ./4/helm/flask-app --wait
Deploys the Flask application using Helm.

Wait for application to be ready

bash
Copy code
run: |
  kubectl rollout status deployment/flask-app
Waits for the Flask application deployment to be rolled out successfully.

Port Forwarding

bash
Copy code
run: |
  kubectl port-forward svc/flask-app 8080:80 &
Sets up port forwarding to access the application locally.

Test application endpoints

bash
Copy code
run: |
  curl http://localhost:8080/healthcheck
  curl http://localhost:8080/characters
Tests the /healthcheck and /characters endpoints of the application.

Delete Kind cluster

bash
Copy code
run: kind delete cluster
Deletes the Kind Kubernetes cluster after testing.

Usage
To use this workflow, ensure that:

The repository has the required Helm chart for deploying the application.
The workflow file is located in the .github/workflows/ directory of your repository.
The workflow will automatically run on pushes to the main branch and on pull requests, deploying and testing the Flask application in a Kubernetes cluster.

sql
Copy code

Feel free to copy and paste this into your `README.md` file.
