# Shimla, a multi-user ssh graphical management panel

## How to install shimla on server ?

```
sudo su
```

```
apt update && apt install python3-pip
```

```
cd /root/
```

```
git clone https://github.com/PabloNoori/shimla.git
```

```
cd shimla
```


```
pip3 install -r req*.txt
```

```
python3 manage.py makemigrations
```


```
python3 manage.py migrate
```

```
sudo python3 manage.py runserver 0.0.0.0:7077
```

## How to run shimla on server ?

```
cd /root/shimla
```

```
sudo python3 manage.py runserver 0.0.0.0:7077
```


## How to Run Django Server Always ?

```
chmod +x add_my_service.sh
```

```
./add_my_service.sh
```

Test

```
sudo systemctl start shimla
sudo systemctl enable shimla
```