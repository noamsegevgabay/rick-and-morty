## Kubernetes YAMLS

### Folder Structure

In the `yamls` folder, you will find the following Kubernetes manifests:

- `Deployment.yaml`: Defines the Deployment for the Flask application.
- `Service.yaml`: Defines the Service that exposes the application.
- `Ingress.yaml`: Defines the Ingress for external access.

### Deploying to Kubernetes using Minikube
```bash
minikube start
```
 **Apply the Deployment**

   ```bash
kubectl apply -f yamls/
```
**Add the Minikube IP to your /etc/hosts file for local DNS resolution**
```bash
MINIKUBE_IP=$(minikube ip)
echo "$MINIKUBE_IP rickandmorty.local" | sudo tee -a /etc/hosts
```
 **Verify the deployment, service, and ingress**
```bash
kubectl get deployments
kubectl get services
kubectl get ingress
```
**Access the application using the Ingress host**
```bash
curl http://rickandmorty.local/characters
curl http://rickandmorty.local/healthcheck
```

