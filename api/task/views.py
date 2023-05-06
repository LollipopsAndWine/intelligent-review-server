import json
from fastapi import APIRouter, Depends
from ..common.customResponse import resp
from .param_schema import ManyAidpDataParam, StartReviewParam
from sqlalchemy.orm import Session
from ..common.database import get_db
from .models import AdipTask
from api.rule.models import Rules
from ..common.http_client import hc
from .utils import findValByKey, equation, is_in, is_contains, lg, lt, before, after, f_equation

app = APIRouter()


@app.get("/aidp_task")
def search_rule(project_id, data_key, project_name, db: Session = Depends(get_db)):
    print(project_id, data_key, project_name)
    my_aidp_task = AdipTask(
        project_id=project_id,
        project_name=project_name,
        data_key=data_key
    )
    db.add(my_aidp_task)
    db.commit()
    return resp()


@app.get("/aidp_info", response_model=ManyAidpDataParam)
def search_rule(keyword, db: Session = Depends(get_db)):
    my_aidp_task = db.query(AdipTask).filter(AdipTask.project_name.like(f"%{keyword}%")).order_by(
        AdipTask.project_name).all()
    from collections import defaultdict
    data = defaultdict(lambda: [])
    for i in my_aidp_task:
        data[i.project_name].append(i)
    return {
        "code": 200,
        "data": data
    }


@app.get("/aidp_data")
def search_rule(project_id, data_key, db: Session = Depends(get_db)):
    url = f'http://192.168.1.205:8001/api/machining/demoV1?project_id={project_id}&data_key={data_key}'
    rep = hc.request_api("GET", url)
    print(rep.status_code)
    print(rep.text)
    ret = rep.json()

    return resp(data=json.dumps(ret["data"]["data"], ensure_ascii=False))


@app.post("/start")
def start_review(param: StartReviewParam, db: Session = Depends(get_db)):
    rule_id = param.rule_id
    base_data = param.base_data
    # print(rule_id)
    print(base_data)
    result = dict()
    select_rule = {
        "=": equation,
        "in": is_in,
        "contains": is_contains,
        ">": lg,
        "<": lt,
        "早于": before,
        "晚于": after,
        "=:f": f_equation
    }
    my_rule = db.query(Rules).filter(Rules.id == rule_id).first()
    rule_config = json.loads(my_rule.rule_config)
    for item in rule_config:
        print(item)
        left_key = item["leftField"].split(":")[1]
        right_key = item["rightField"].split(":")[1]
        rule = item["rule"]
        print(findValByKey(left_key, base_data))
        print(findValByKey(right_key, base_data))
        print("++++++++++++++++++++++++++end")
        left_value = findValByKey(left_key, base_data)
        right_value = findValByKey(right_key, base_data)
        ret = select_rule.get(rule)(left_value, right_value) if left_value and right_value else False
        result.update({f"{left_key} {rule.split(':')[0]} {right_key}": {"result": ret, "show_data": f"{left_value} {rule.split(':')[0]} {right_value}"}})
    print(result)
    return resp(data=result)
