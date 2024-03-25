### **"Swagger Petstore" API autotesting**

1. Link: *https://petstore.swagger.io/*
2. Basis for writing autotests: *Pytest*, *Requests*
3. Test report: *Allure*

**Pytest setup:**
````
pip install pytest
````

**Requests setup:**
````
pip install requests
````

**Faker setup:**
````
pip install Faker
````

**Running autotests:**
````
pytest -v
````

**Test report Allure:**
````
pip install allure-pytest
````
````
pytest tests --alluredir=allure_results
````
````
allure serve allure_results
````
