import copy
import json
from fastapi import APIRouter, Depends
from ..common.customResponse import resp
from .param_schema import SaveSchemaParam, ManyRuleParam
from sqlalchemy.orm import Session
from ..common.database import get_db
from .models import Rules


app = APIRouter()


@app.post("/save_rule")
def save_rule(param: SaveSchemaParam, db: Session = Depends(get_db)):
    rule_name = param.rule_name
    rule_config = param.rule_config
    my_rule = Rules(
        rule_name=rule_name,
        rule_config=json.dumps(rule_config, ensure_ascii=False)
    )
    db.add(my_rule)
    db.commit()
    return resp()


@app.get("/rules", response_model=ManyRuleParam)
def get_rule(db: Session = Depends(get_db)):
    my_rule = db.query(Rules).all()
    return {
        "code": 200,
        "data": my_rule
    }


@app.get("/search_rule", response_model=ManyRuleParam)
def search_rule(keyword, db: Session = Depends(get_db)):
    my_rule = db.query(Rules).filter(Rules.rule_name.like(f"%{keyword}%")).all()
    return {
        "code": 200,
        "data": my_rule
    }


@app.get("/rule_detail")
def get_rule(id, db: Session = Depends(get_db)):
    my_rule = db.query(Rules).filter(Rules.id == id).first()
    rule_config = json.loads(my_rule.rule_config)
    sn = []
    rc_value = []
    for item in copy.deepcopy(rule_config):
        item.pop('rule', None)
        tem_v = list(item.values())
        for v in tem_v:
            sn.append(str(v).split(":")[0])
        rc_value.extend(tem_v)

    data_filter = list(set(sn))
    data = [
        {
            "name": item,
            "des": item,
            "symbolSize": 65,
            "category": 0,
            "itemStyle": {
                "emphasis": {
                    "color": '#af9369'
                },
            },
        } for item in list(set(sn))
    ]

    for item in rc_value:
        name = f'{str(item).split(":")[1]}({str(item).split(":")[0]})'
        if name not in data_filter:
            data.append({
                "name": name,
                "des": item,
                "symbolSize": 50,
                "category": 1,
                "itemStyle": {
                    "emphasis": {
                        "color": '#B6996E'
                    },
                },
            })
            data_filter.append(name)

    links = [{
        "source": f'{str(item["leftField"]).split(":")[1]}({str(item["leftField"]).split(":")[0]})',
        "target": f'{str(item["rightField"]).split(":")[1]}({str(item["rightField"]).split(":")[0]})',
        "name": "",
        "label": {"show": True, "formatter": item["rule"], "fontSize": 12}
    } for item in rule_config]

    links.extend([{
        "source": str(item).split(":")[0],
        "target": f'{str(item).split(":")[1]}({str(item).split(":")[0]})',
        "name": "",
        "label": {}
    } for item in rc_value])

    return resp(data={
        "data": data,
        "links": links
    })



