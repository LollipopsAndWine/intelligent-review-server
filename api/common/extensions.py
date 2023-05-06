import os
import re
import yaml
from urllib import parse
from pathlib import Path

if 'PREFIX' in os.environ and os.environ['PREFIX']:
    config_path = os.path.join(os.environ['PREFIX'], "share/aimp/static/config/base_config.yaml")
else:
    config_path = Path(__file__).parent.parent / "static/config/base_config.yaml"


class ConfigMap(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def configMap():
    with open(str(config_path), mode='r', encoding='utf-8') as fd:
        data = yaml.load(fd, Loader=yaml.FullLoader)
        _config = data.get(data.get("run_config"))
        # _config["LAST_METADATA_PATH"] = os.path.expanduser(_config["LAST_METADATA_PATH"])
    inst = ConfigMap()
    for k, v in _config.items():
        inst[k] = v

    return inst


def parse_uri(database_uri):
    search_ret = re.search("://.*?:(.*)@", database_uri)
    password = search_ret.group(1)
    new_password = parse.quote_plus(password)
    new_database_uri = database_uri.replace(password, new_password)

    return new_database_uri


def nestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from nestedDictValues(v)
    else:
      yield v
