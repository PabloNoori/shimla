# Shimla, a multi-user ssh graphical management panel

## How to install shimla on server ?

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
python3 manage.py runserver 0.0.0.0:9999
```

## How to run shimla on server ?

```
cd /root/shimla
```

```
python3 manage.py runserver 0.0.0.0:9999
```