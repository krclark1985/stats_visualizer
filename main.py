from typing import List, Any
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import math_methods
from rich import print
from rich.traceback import install
install()  # Automatically improves traceback


# defines the data model for the request body in the POST method;
# accepts any data type which is later validated with valid_input_check() method
class DataSet(BaseModel):
    data_input: List[Any]


# initializes FastAPI app
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("[bold green]We're live![/bold green]")

# takes data set as input (as a list of float values),
# calls math methods sequentially to calculate various
# statistical measures, and builds a dictionary of them
# step by step; returns dictionary of calculated measures
@app.post("/calculate-stats")
def calculate_stats(data_set: DataSet):
    default_dict = {
        'min': 0.0,
        'q1': 0.0,
        'median': 0.0,
        'q3': 0.0,
        'max': 0.0,
        'range': 0.0,
        'iqr': 0.0,
        'mean': 0.0,
        'mode': [],
        'outliers': []
    }

    try: 
        solutions_dict = {
            'min': 0.0,
            'q1': 0.0,
            'median': 0.0,
            'q3': 0.0,
            'max': 0.0,
            'range': 0.0,
            'iqr': 0.0,
            'mean': 0.0,
            'mode': [],
            'outliers': []
        }

        # encodes DataSet object data_set into JSON encodable object,
        # then extracts data set input list from this object; then
        # sorts new_data_set for use in subsequent math_methods
        new_data_set = jsonable_encoder(data_set)
        new_data_set = new_data_set["data_input"]

        if valid_input_check(new_data_set) == False:
            return jsonable_encoder(default_dict)

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
    
    except Exception as e:
        print("[bold red]An error has occurred:[/bold red]", e)

        # Catch-all error
        return jsonable_encoder(default_dict)

# checks to ensure that input data set contains at least 2 values,
# and that it does not contain any non-numeric values; returns False
# if data set is invalid, and True if valid
def valid_input_check(input_data_set):
    if empty_data_check(input_data_set) == False:
        print("[bold red]Data set must contain more than one value[/bold red]")
        return False
    if non_numeric_check(input_data_set) == False:
        print ("[bold red]Data set contains non-numeric values; please input numeric values only[/bold red]")
        return False
    return True

def empty_data_check(input_data_set):
    if len(input_data_set) < 2:
        return False
    else:
        True

def non_numeric_check(input_data_set):
    for data in input_data_set:
        if not isinstance(data, (int, float, complex)):
            return False
    return True

'''
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
'''