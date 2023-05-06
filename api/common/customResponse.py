from fastapi import status
from fastapi.responses import JSONResponse, Response
from typing import Union


def resp(data: Union[list, dict, str] = "", code=200, msg="success", status_code=status.HTTP_200_OK) -> Response:
    return JSONResponse(
        status_code=status_code,
        content={
            'code': code,
            'message': msg,
            'data': data,
        }
    )
