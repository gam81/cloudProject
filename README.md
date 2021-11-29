# cloudProject

# In Kubernetes Cloud Shell

this can be accessed in gcp by going to kubernetes engine>creating a cluster>connect>run in cloud shell 

git clone https://github.com/erikpitt/cs1660-project.git

cd cs1660-project

kubectl apply -f yamls/sonar-deployment.yaml

kubectl apply -f yamls/sonar-service.yaml

kubectl apply -f yamls/spark-deployment.yaml

kubectl apply -f yamls/spark-service.yaml

kubectl apply -f yamls/namenode-deployment.yaml

kubectl apply -f yamls/namenode-service.yaml

kubectl apply -f yamls/datanode-deployment.yaml

kubectl apply -f yamls/jupyter-deployment.yaml

kubectl apply -f yamls/jupyter-service.yaml
