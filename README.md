## hdbresaleapi
API that takes in your posts and predicts a price with the trained random forest regressor model

### usage
either 
1. install locally and run with the command- uvicorn mlapi:app, connect with Postman to the API on port 8000
2. use hosted url https://hdbresaleapi.herokuapp.com/

### HTTP verbs | endpoints
POST | /

### post request example

{
    "flat_type":5,
    "lease_year":2000,
    "town":"WOODLANDS",
    "date": "2022-10"
}

API returns

{
    "prediction": 565767.8571428572
}
