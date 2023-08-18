from fastapi import FastAPI, HTTPException
from app.outputdb import contact_raw_id
from app.output_pred import contact_pred_id


route = FastAPI()


@route.get("/data/{table}/{id}")
async def get_data_request(table: str=None, id: int=None):
    try:
        result = contact_raw_id(table, id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.get("/output/{table}/{pred_id}")
async def get_data_request(table: str=None, pred_id: int=None):
    try:
        result = contact_pred_id(table, pred_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))