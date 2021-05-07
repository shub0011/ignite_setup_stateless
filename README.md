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
