I have created the model for products, and routes as required, I have also added a middleware logger, that logs the response time in the required format. 
For testing I have made a sample products.json, with some sample computer parts as products. for the time being, im just using sqlite to keep the database transactions simple, mostly because of the time crunch. 
To run it, simply run the command ```python manage.py runserver```, I have already performed the migrations, so you dont have to first migrate. To use the task to import the data, we use ```python manage.py import_products```, this imports all the data from the products.json file

## UPDATE:
First run ```pip install -r requirements.txt``` to install the required packages.
I have made it so that there are no more trailing slashes, and when the list is empty, it returns 204 instead of 404 by overriding the get method, i have also written a couple of tests, which can be run using ```python manage.py test```
I have also added a new command to erase all the products from the database, to make it easier to test with custom data, to run which, just do ```python manage.py clear_products```
I have tried to make it so that the data formats are exactly what were told in the file.
You can also run it usinv uvicorn, by simply running ```uvicorn appscrip.asgi:application --reload```
## Screenshots: 
1. GET all products![image](https://github.com/user-attachments/assets/82dcbd56-decc-4ee4-ad38-b6d53cdcc25d)
2. GET single product ![image](https://github.com/user-attachments/assets/960f640d-3833-4f90-a3e0-792e0764122e)
3. POST new product ![image](https://github.com/user-attachments/assets/a1a39793-c480-46a7-9438-7784ddbc9469)
4. PUT update product ![image](https://github.com/user-attachments/assets/97049bad-0cfa-47db-a639-4391cee60479)
5. DELETE product via id ![image](https://github.com/user-attachments/assets/fe702e73-8503-4e8c-8568-8772a708857d)
6. Logging ![image](https://github.com/user-attachments/assets/ac4a3d81-92cf-4e03-936a-6cb6ed87078e)
