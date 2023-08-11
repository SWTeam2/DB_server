from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


# Sample function that takes parameters and returns data
def process_data(bearing: str, csv_num: int):
    # Replace this with your actual data processing logic
    data = {
        "bearing": bearing,
        "start_line": csv_num,
        "result": f"Processed data for bearing {bearing} between lines {csv_num}"
    }
    return data


# Define a Pydantic model for the request payload
class RequestPayload(BaseModel):
    bearing: str
    csv_num: int


@app.post("/process/")
async def process_request(payload: RequestPayload):
    try:
        result = process_data(
            payload.bearing, payload.csv_num)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
