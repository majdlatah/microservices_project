# Microservices Project

The project includes a simple implementation of pizza-delivery microservices.

We used Connexion framework to implement our REST API.

These microsevices were delpoyed on our local Ubuntu 14.04 Server, which runs an MySQL database.

| Customer Service  | Order Service | Menu Service | 
| ------------- | ------------- |-------------  |
| Find Customer | Create Order  | Find Food |
| Delete Customer | Order Status  | Delete Food |

REST APIs:

Find Customer: http://localhost:5000/api/customer/<customer-id>

Delete Customer: curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/customer/<customer-id>

Create Order: curl -d '{"cid":"<customer-id>","pizza":"<pizza-id>"}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/order

Order Status: http://localhost:5000/api/order/<order-id>

Find Food: http://localhost:5000/api/customer/<food-id>

Delete Food: curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/food/<food-id>




