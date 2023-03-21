create conda enviroment
```bash
    conda create -n insurance python=3.8 -y
```
activate env
```bash
    conda activate insurance
```
create a requirements.txt
install the requirements
```bash
pip install -r requirements.txt
```

```bash
    git init
```

```bash
    dvc init
```

```bash
dvc add data_given/insurance.csv
```

git commit -m "first commit"


check the metrics diff
```bash
dvc metrics diff
```

install django in conda enviroment
```bash
conda install -c anaconda django
```

create a django project 
```bash 
django-admin startproject webapp
```

create a application inside a webapp django project
```bash
python manage.py startapp Ipp(Insurance Premium Prediction)
```

run the application 
```bash
python manage.py runserver
```



