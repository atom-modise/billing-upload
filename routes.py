from fastapi import File, UploadFile,APIRouter
import csv
import codecs

from app import insert, connect

router = APIRouter()

@router.get('/test-database-connection')
def database_connected():
    return {"message": connect()}


@router.post("/upload-csv")
def upload(file: UploadFile = File(...)):
    if not file:
        return {"message": "File Not Uploaded"}
    else:
        csv_reader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8-sig'))
        data = []
        for row in csv_reader:
            data.append(row)
        result = insert(data)
        return {"message": "Billing Data Uploaded", "row_count": result, "statusMessage": "success"}