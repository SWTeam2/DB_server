from fastapi import FastAPI, HTTPException
from app.outputdb import contact_raw_id
from app.outputdb import contact_raw
from app.output_pred import contact_pred

app = FastAPI()


@app.get("/data/")
async def get_data_request(table: str=None, id: str=None, csv_num: str=None):
    try:
        if id == None:
            result = contact_raw_id(table, id)

        if csv_num == None:
            result = contact_raw(table, csv_num)

        else:
            result = contact_pred(table, id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/infer/")
async def post_prediction_request(table: str=None, pred_id: str=None):
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @app.get("/data/")
# async def get_data_request(table: str=None, csv_num: str=None, pred_id: str=None):
#     try:
#         if pred_id == None:
#             result = contact_raw_id(table, csv_num)
#         else:
#             result = contact_pred(table, pred_id)
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))