from fastapi import FastAPI, HTTPException
from app.outputdb import contact_raw_id
from app.output_pred import contact_pred_id
from app.insert_json_data_append import insert_json_data
from app.request_infer import send_request_and_get_response, send_request_and_get_response_table
from app.db_row_count import row_count


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
    
    
@route.get("/request/{table}/all")
async def send_infer_all(table: str=None):
    table_name = "prediction_"+table
    print(table_name)
    try:
        rows = row_count(table)
        rows_per_load_cnt = 2560   
        max_load_cnt = int(rows / rows_per_load_cnt)
        print(max_load_cnt)
        for load_cnt in range(5, max_load_cnt+1): ## 혹시 모르니 1~4 까지는 시도 안하는 걸로 
            print(load_cnt)
            ## 시간 간격 10초 추기 
            response_data = send_request_and_get_response_table(table, load_cnt)
            insert_json_data(table_name, response_data)
        
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@route.get("/request/{table}/{id}")
async def send_infer(table: str=None, id: int=None):
    table_name = "prediction_{table}"
    try:
        response_data = send_request_and_get_response(table, id)
        print("response works")
        insert_json_data(table_name, response_data)
        
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))