# Projet Kubernetes PoC – Cloud-K8s-Poc

## Présentation

Ce projet est un **Proof of Concept** (PoC) de déploiement d’une application web critique sur un cluster Kubernetes.  
Il a pour objectif de démontrer :

- La séparation et sécurisation des composants via Kubernetes (ConfigMap, RBAC, NetworkPolicy)
- L’autoscaling automatique grâce au HPA (Horizontal Pod Autoscaler)
- L’exposition de l’application par un Service
- La supervision du cluster (optionnelle avec Grafana)

## Fonctionnalités de l’application

- API REST Python (Flask) avec 2 endpoints :
  - `/read_db` : lecture de la base SQLite, retourne la liste des utilisateurs
  - `/cpu_load` : simule une charge CPU élevée pendant 3 minutes (test du scaling)
- Utilisation d’un **ConfigMap** pour la configuration (chemin BDD)
- Base SQLite intégrée dans l’image Docker

## Déploiement Kubernetes

### Prérequis

- Docker Desktop lancé
- Minikube installé et démarré
- kubectl prêt (fourni avec Minikube)

### Étapes à suivre

#### 1. Démarrer Minikube

```bash
minikube start
```

#### 2. Passer le shell en mode Docker Minikube

```bash
eval $(minikube docker-env)
```

#### 3. Construire l’image dans Minikube

Depuis le dossier app/ :

```bash
minikube image build -t flask-sqlite-api:latest .
```

#### 4. Déployer les fichiers Kubernetes

Depuis le dossier k8s/ :

```bash
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f grafana.yaml
kubectl apply -f hpa.yaml
kubectl apply -f networkpolicy.yaml
kubectl apply -f rbac.yaml
kubectl apply -f service.yaml
```

#### 5. Activer le metrics-server pour le HPA

```bash
minikube addons enable metrics-server
```

#### 6. Vérifier le fonctionnement

- Pods en running :
  ```bash
  kubectl get pods
  ```
- Accès à l’application :
  ```bash
  minikube service flask-sqlite-api
  ```
- HPA et scaling :
  ```bash
  kubectl get hpa
  ```
