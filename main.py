from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import math_methods

# Define the data model for the request
# body in the POST method
class DataSet(BaseModel):
    data_input: List[float]


# Initialize FastAPI app
app = FastAPI()

# Takes data set as input (as a list of float values),
# calls math methods sequentially to calculate various
# statistical measures, and builds a dictionary of them
# step by step; returns dictionary of calculated measures
@app.post("/calculate-stats/")
def calculate_stats(data_set: DataSet):
    solutions_dict = {'min': 0.0,
                      'q1': 0.0,
                      'median': 0.0,
                      'q3': 0.0,
                      'max': 0.0,
                      'range': 0.0,
                      'iqr': 0.0,
                      'mean': 0.0,
                      'mode': [],
                      'outliers': []}
    
    # Encodes DataSet object data_set into JSON encodable object,
    # then extracts data set input list from new_data_set; then
    # sorts new_data_set for use in subsequent math_methods
    new_data_set = jsonable_encoder(data_set)
    new_data_set = new_data_set["data_input"]
    new_data_set.sort()

    solutions_dict['min'] = new_data_set[0]
    solutions_dict['max'] = new_data_set[-1]
    solutions_dict['range'] = new_data_set[-1] - new_data_set[0]
    solutions_dict['mean'] = math_methods.mean(new_data_set)
    solutions_dict['mode'] = math_methods.mode(new_data_set)
    five_number_summary_dict = math_methods.five_num_summary_dict(new_data_set)
    solutions_dict['q1'] = five_number_summary_dict['q1']
    solutions_dict['median'] = five_number_summary_dict['median']
    solutions_dict['q3'] = five_number_summary_dict['q3']
    solutions_dict['iqr'] = five_number_summary_dict['q3'] - five_number_summary_dict['q1']
    solutions_dict['outliers'] = math_methods.outliers(new_data_set)

    return solutions_dict


'''
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
'''