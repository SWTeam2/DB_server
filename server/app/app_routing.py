from fastapi import FastAPI, HTTPException
from app.outputdb import contact_raw_id

app = FastAPI()


@app.get("/data/{table}/{id}")
async def get_data_request(table: str=None, id: int=None):
    try:
        result = contact_raw_id(table, id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
