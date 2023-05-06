from pydantic import BaseModel, validator
from typing import List, Union


class AidpDataParam(BaseModel):
    project_id: int
    project_name: str
    data_key: str

    class Config:
        orm_mode = True


class ManyAidpDataParam(BaseModel):
    data: dict[str, List[AidpDataParam]]


class StartReviewParam(BaseModel):
    rule_id: int
    base_data: Union[dict, List]
