from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class RequestParams(BaseModel):
    bearing: str
    csv_num: int

@app.get("/process/")
async def process_request(params: RequestParams):
    try:
        result = {
            "bearing": params.bearing,
            "start_line": params.csv_num,
            "result": f"Processed data for bearing {params.bearing} between lines {params.csv_num}"
        }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
