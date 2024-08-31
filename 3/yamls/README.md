## Kubernetes YAMLS

### Folder Structure

In the `yamls` folder, you will find the following Kubernetes manifests:

- `Deployment.yaml`: Defines the Deployment for the Flask application.
- `Service.yaml`: Defines the Service that exposes the application.
- `Ingress.yaml`: Defines the Ingress for external access.

### Deploying to Kubernetes using Minikube
```sh
minikube start
```
1. **Apply the Deployment**

   ```sh
kubectl apply -f yamls/
```
2. **Add the Minikube IP to your /etc/hosts file for local DNS resolution**
   ```sh
MINIKUBE_IP=$(minikube ip)
echo "$MINIKUBE_IP rickandmorty.local" | sudo tee -a /etc/hosts
```
3. **Verify the deployment, service, and ingress**
   ```sh
kubectl get deployments
kubectl get services
kubectl get ingress
```
4. **Access the application using the Ingress host**
   ```sh
curl http://rickandmorty.local/characters
curl http://rickandmorty.local/healthcheck
```

