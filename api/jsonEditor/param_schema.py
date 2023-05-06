import json
from pydantic import BaseModel, validator
from datetime import datetime
from typing import List, Union
from .utils import get_keys


class SaveSchemaParam(BaseModel):
    schema_name: str
    json_schema: Union[dict, list]


class ResponseSchema(BaseModel):
    id: int
    schema_name: str
    json_schema: str
    is_delete: bool
    create_time: datetime
    update_time: datetime

    class Config:
        orm_mode = True

    @validator('json_schema')
    def json_to_dict(cls, v):
        temp_v = json.loads(v)
        print(temp_v)
        print(get_keys(temp_v, reset=1))
        temp_key = [item for item in list(set(get_keys(temp_v, reset=1))) if item]
        print(temp_key)
        return {
            "schema_key": temp_key,
            "data": temp_v
        }

    @validator('create_time')
    def format_time1(cls, v):
        return v.strftime('%Y-%m-%d %H:%M:%S')

    @validator('update_time')
    def format_time2(cls, v):
        return v.strftime('%Y-%m-%d %H:%M:%S')


class ManyResponseSchema(BaseModel):
    data: List[ResponseSchema]
