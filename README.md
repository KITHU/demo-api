[![Build Status](https://travis-ci.org/KITHU/demo-api.svg?branch=main)](https://travis-ci.org/KITHU/demo-api)
[![Coverage Status](https://coveralls.io/repos/github/KITHU/demo-api/badge.svg?branch=develop)](https://coveralls.io/github/KITHU/demo-api?branch=develop)

# **demo-api**
### **API Documentation**
- Click [here](https://tranquil-spire-14325.herokuapp.com) to view swagger API documentation

## **Endpoints:**
### Register

`POST /api/v1/auth/register/`

Example request body:
``` 
{
    "username":"njeru",
    "email":"njeru@gmail.com",
    "password":"1234"
}

```

### Login
`POST /api/v1/auth/login/`

Example request body:
``` 
{
    "email":"njeru@gmail.com",
    "password":"1234"
}
```
### Social Auth

`POST /api/v1/auth/google/`

Example request body:
``` 
{
    "auth_token":google auth token
}

```
## **Customer Profile**
### update customer info
`PATCH /api/v1/profile/id/`

Example request body:
``` 
{
    "country_code": "254",
    "phone_no":"771866678"
}
```
Authentication required

### Retrieve a customers
`GET /api/v1/profile/id/`

Authentication required, return a single customers

### List all customers
`GET /api/v1/profile/`

Authentication required, return all customers

## **Orders**
### create an order
`POST /api/v1/orders/create/`

Example request body:
``` 
{
    "item_name": "delmonte apple",
    "amount": 205.00,
    "customer": 2
}
```
Authentication required, returns order object and also sends an sms to the customer if they have a valid phone number

### Retrieve an order
`GET /api/v1/orders/id/`

Authentication isn't required, return a single order

### List all orders
`GET /api/v1/order/`

Authentication isn't required, return a list of orders