from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.db_connection import connect_db, insert_data, disconnect_db 


app = FastAPI()

# Sample function that takes parameters and returns data
def process_data(bearing: str, start_line: int, end_line: int):
    # Replace this with your actual data processing logic
    data = {
        "bearing": bearing,
        "start_line": start_line,
        "end_line": end_line,
        "result": f"Processed data for bearing {bearing} between lines {start_line} and {end_line}"
    }
    return data

# Define a Pydantic model for the request payload
class RequestPayload(BaseModel):
    bearing: str
    start_line: int
    end_line: int

@app.post("/process/")
async def process_request(payload: RequestPayload):
    try:
        result = process_data(payload.bearing, payload.start_line, payload.end_line)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
