# CPG-105
Diabetic Retinopathy Analysis Site
----------

Clone the project:
```bash
git clone https://github.com/ToxicityMax/CPG-105.git
cd CPG-105
```

Set up your environment:
```bash
pip install -r requirements.txt
```

The essentials:
```bash
cd src/
python manage.py makemigrations
python manage.py migrate 
```
Make a admin user:
```bash
python manage.py createsuperuser
```
Change Path of model in src/ml/utils.py:
```python
MODEL_PATH = "/path/to/CPG-105/src/static/modelsave.h5"
```

Start server:
```
python manage.py runserver
```
