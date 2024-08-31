## Kubernetes Deployment

### Folder Structure

In the `yamls` folder, you will find the following Kubernetes manifests:

- `Deployment.yaml`: Defines the Deployment for the Flask application.
- `Service.yaml`: Defines the Service that exposes the application.
- `Ingress.yaml`: Defines the Ingress for external access.

### Deploying to Kubernetes

1. **Apply the Deployment**

   ```sh
   kubectl apply -f yamls/Deployment.yaml
