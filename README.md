# cloudProject

# Images Used
[Hadoop Namenode](https://hub.docker.com/layers/bde2020/hadoop-namenode/2.0.0-hadoop3.2.1-java8/images/sha256-51ad9293ec52083c5003ef0aaab00c3dd7d6335ddf495cc1257f97a272cab4c0?context=explore)

[Hadoop Datanode](https://hub.docker.com/layers/bde2020/hadoop-datanode/2.0.0-hadoop3.2.1-java8/images/sha256-ddf6e9ad55af4f73d2ccb6da31d9e3331ffb94d5f046126db4f40aa348d484bf?context=explore)

[Apache Spark](https://hub.docker.com/layers/bitnami/spark/3/images/sha256-e60f9146bdce100cf518746117f84d659d352dc0fc4c0af552e05a935f5d2ae1?context=explore)

[Jupyter Notebook](https://hub.docker.com/r/jupyter/datascience-notebook)

[Sonarscanner](https://hub.docker.com/r/newtmitch/sonar-scanner)

[SonarQube](https://hub.docker.com/_/sonarqube)

# In Kubernetes Cloud Shell

this can be accessed in gcp by going to kubernetes engine>creating a cluster>connect>run in cloud shell 

git clone https://github.com/gam81/cloudProject

cd cloudProject

minikube start

kubectl apply -f yamls/sonar-deployment.yaml

kubectl apply -f yamls/sonar-service.yaml

kubectl apply -f yamls/spark-deployment.yaml

kubectl apply -f yamls/spark-service.yaml

kubectl apply -f yamls/namenode-deployment.yaml

kubectl apply -f yamls/namenode-service.yaml

kubectl apply -f yamls/datanode-deployment.yaml

kubectl apply -f yamls/jupyter-deployment.yaml

kubectl apply -f yamls/jupyter-service.yaml


It may take some time for the IPs to finish assigning.

Go to "External IP Addresses" in google cloud platform. Type the following command in your terminal:

kubectl get service -o wide

Then reserve the IPs that appear here in google cloud. This makes them able to be connected through the program.

Replace the empty IP slots after the local variable check in the gui.py with these IPs in order to connect to them through GCP. Run as "gui.py false" to connect non-locally.

