# Dynamic Traffic Routing System with Kubernetes

This repository provides a step-by-step guide on creating a dynamic traffic routing system using Kubernetes, Nginx Ingress, Python, and Redis. The following is the recommended order for creating resources:

1. **Prerequisites**:
   - Ensure that Docker Desktop is installed and Kubernetes is enabled.
   - Install `kubectl` for managing Kubernetes clusters.

2. **Deploy Nginx Ingress Controller**:
   - Deploy the Nginx Ingress Controller using Helm:

     ```shell
     kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.0.0/deploy/static/provider/cloud/deploy.yaml
     kubectl get pods -n ingress-nginx
     ```

3. **Build and Deploy the Authentication Service**:
   
   **/auth-service** Contains the Authentication application.
   - Build a Docker image for the authentication service and push it to your local Docker registry or public registery.
   - Update the image name in **01_auth-service-deployment.yaml** file
   - Run auth-service deployment and Service by
     
     ```
     kubectl apply -f 01_auth-service-deployment.yaml
     kubectl apply -f 02_auth-service-service.yaml
     ```
   
4. **Set Up Redis for Pod-to-Name Mapping**:
   Running up Redis Deployment and Service
   
   ```
   kubectl apply -f 03_redis-deployment.yaml
   kubectl apply -f 04_redis-service.yaml
   ```
6. **Dynamic Routing with Nginx Ingress**:
   Running an Ingress resource for dynamic routing using Lua annotations.
   
   ```
   kubectl apply -f 05_auth_ingress.yaml
   ```
7. **Create Pods for Dynamic Routing**:
   Deploy pods for dynamic routing. These pods should return static pages with their names and insert key-value pairs in the Redis database.
   
   ```
   kubectl apply -f 06_dynamic-pods-deployment.yaml
   kubectl apply -f 07_dynamic-pods-service.yaml
   ```
