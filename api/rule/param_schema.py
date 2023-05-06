from pydantic import BaseModel
from typing import List


class SaveSchemaParam(BaseModel):
    rule_name: str
    rule_config: list


class RuleParam(BaseModel):
    id: int
    rule_name: str

    class Config:
        orm_mode = True


class ManyRuleParam(BaseModel):
    data: List[RuleParam]


class SearchParam(BaseModel):
    keyword: str
