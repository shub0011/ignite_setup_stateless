# ignite_setup_stateless

Follow these steps


-  - install eksctl 
-  - install kubectl 



```sh
eksctl create cluster --name ignitecluster --nodes 2 --nodes-min 1 --nodes-max 4

```
Now check the cluster and the service by using commands

```sh

eksctl get cluster -n ignitecluster

kubectl get svc

```
create namespace
```sh
kubectl create namespace ignite
```
create service
```sh
kubectl create -f service.yaml
```
create service name
```sh
kubectl create sa ignite -n ignite
```
create cluster role
```sh
kubectl create -f cluster-role.yaml
```
create node configuration 
```sh
kubectl create configmap ignite-config -n ignite --from-file=node-configuration.xml
```

Create the StatefulSet by running the following command:
```sh

  kubectl create -f statefulset.yaml
  ```

Check if the pods were deployed correctly:
```sh

kubectl get pods -n ignite
```
Check if the ignite were deployed correctly (eg):
```sh
kubectl logs ignite-cluster-5b69557db6-lcglw -n ignite
```
Since you are using persistence, you must activate the cluster after it is started. To do that, connect to one of the pods:
```sh
kubectl exec -it <pod_name> -n ignite -- /bin/bash
```
Execute the following command:
```sh
/opt/ignite/apache-ignite/bin/control.sh --set-state ACTIVE --yes

```

scale the cluster 
```sh
kubectl scale sts ignite-cluster --replicas=3 -n ignite
```
Get the public IP of the service:
```sh
$ kubectl describe svc ignite-service -n ignite
Name:                     ignite-service
Namespace:                ignite
Labels:                   app=ignite
Annotations:              <none>
Selector:                 app=ignite
Type:                     LoadBalancer
IP:                       10.0.144.19
LoadBalancer Ingress:     13.86.186.145
Port:                     rest  8080/TCP
TargetPort:               8080/TCP
NodePort:                 rest  31912/TCP
Endpoints:                10.244.1.5:8080
Port:                     thinclients  10800/TCP
TargetPort:               10800/TCP
NodePort:                 thinclients  31345/TCP
Endpoints:                10.244.1.5:10800
Session Affinity:         None
External Traffic Policy:  Cluster
```

# Connecting to REST API
Connect to the cluster’s REST API as follows:
```sh
$ curl http://13.86.186.145:8080/ignite?cmd=version
{"successStatus":0,"error":null,"response":"2.10.0","sessionToken":null}
```



# to test the persistence

To start the test create a new environment ( to use python3) Follow this steps .

```sh
python3 -m venv /path/to/new/virtual/environment

source venv/bin/activate

pip3 install -r requirements.txt

```

and then run 
```sh
python3 test_scipt.py
```

and then 
```sh
python3 test_script_2.py
```
