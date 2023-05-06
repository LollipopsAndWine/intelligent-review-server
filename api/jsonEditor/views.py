import json
from fastapi import APIRouter, Depends
from ..common.customResponse import resp
from .param_schema import SaveSchemaParam, ManyResponseSchema
from sqlalchemy.orm import Session
from ..common.database import get_db
from .models import JsonSchema


app = APIRouter()


@app.post("/save_schema")
def save_schema(param: SaveSchemaParam, db: Session = Depends(get_db)):
    schema_name = param.schema_name
    json_schema = param.json_schema
    my_js = JsonSchema(
        schema_name=schema_name,
        json_schema=json.dumps(json_schema, ensure_ascii=False)
    )
    db.add(my_js)
    db.commit()
    return resp()


@app.get("/schema", response_model=ManyResponseSchema)
def get_schema(db: Session = Depends(get_db)):
    ret = db.query(JsonSchema).all()
    return {
        "code": 200,
        "data": ret
    }
