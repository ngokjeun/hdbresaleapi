from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import datetime as dt


app = FastAPI()

class ScoringItem(BaseModel):
    flat_type: int
    lease_year: int
    town: str
    date: str #YYYY-MM

with open('rfr.pkl', 'rb') as f:
    model = pickle.load(f)

@app.post("/")
async def scoring_endpoint(item: ScoringItem):
    
    date = item.dict()['date']
    town_select = item.dict()['town'].upper()
    year_select = item.dict()['lease_year']
    flat_select = item.dict()['flat_type']

    ordinal_date = dt.datetime.toordinal(pd.to_datetime(date, format='%Y-%m'))
    town_select_list = [0] * 26

    town_list = ['month', 'town', 'flat_type', 'block', 'street_name', 'storey_range',
       'floor_area_sqm', 'flat_model', 'lease_commence_date',
       'remaining_lease', 'resale_price', 'Month', 'year', 'flat_kind',
       'town_ANG MO KIO', 'town_BEDOK', 'town_BISHAN', 'town_BUKIT BATOK',
       'town_BUKIT MERAH', 'town_BUKIT PANJANG', 'town_BUKIT TIMAH',
       'town_CENTRAL AREA', 'town_CHOA CHU KANG', 'town_CLEMENTI',
       'town_GEYLANG', 'town_HOUGANG', 'town_JURONG EAST', 'town_JURONG WEST',
       'town_KALLANG/WHAMPOA', 'town_MARINE PARADE', 'town_PASIR RIS',
       'town_PUNGGOL', 'town_QUEENSTOWN', 'town_SEMBAWANG', 'town_SENGKANG',
       'town_SERANGOON', 'town_TAMPINES', 'town_TOA PAYOH', 'town_WOODLANDS',
       'town_YISHUN', 'sale_date']

    for i in town_list:
         if town_select in i:
             t_index = town_list.index(i) - 14
             town_select_list = town_select_list[:t_index]+[1]+town_select_list[t_index+1:]

    user_list = [[year_select, flat_select, ordinal_date] + town_select_list]

    yhat = model.predict(user_list)

    return {'prediction': float(yhat)}
