from .expect import fish_detect
from fastapi import File, UploadFile
from fastapi import APIRouter, Depends
from .aws.bucket import *
import json 

router = APIRouter()


@router.post("/")
async def infer(file: UploadFile = File()):
    content = await file.read()
    filename = f"{file.filename}.jpg"
    with open(filename, "wb") as fp:
        fp.write(content)
        post_bucket(content,filename)

    result = fish_detect(filename)
    with open("api/endpoints/data.json", 'r') as file:
        fish_data = json.load(file)
        for data in fish_data:
            if data["pk"] == result:
                data["url"] = "https://svj-deepblue.s3.ap-northeast-2.amazonaws.com/" + filename 
                return data
