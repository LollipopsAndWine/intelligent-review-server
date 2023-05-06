# coding: utf-8
from pathlib import Path
from datetime import datetime
from loguru import logger

log_path = "./log"  # str(Path(__file__).parent.parent / "log")
if not Path(log_path).exists():
    Path(log_path).mkdir(parents=True, exist_ok=True)

log_file = '{0}/err_{1}.log'.format(log_path, datetime.now().strftime('%Y-%m-%d'))

logger.add(log_file, rotation="00:00", retention="10 days", enqueue=True, delay=True)
