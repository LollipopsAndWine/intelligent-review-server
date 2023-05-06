from fastapi import FastAPI, Request
from api.jsonEditor.views import app as json_editor_api
from api.rule.views import app as rule_api
from api.task.views import app as task_api
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(json_editor_api, prefix="/json_editor", tags=["json_editor"],
                   responses={404: {"description": "Not found"}})
app.include_router(rule_api, prefix="/rule", tags=["rule"],
                   responses={404: {"description": "Not found"}})
app.include_router(task_api, prefix="/task", tags=["task"],
                   responses={404: {"description": "Not found"}})


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # you probably want some kind of logging here
        # session.close()
        print(e)
        return JSONResponse(content={'data': None, "code": 400, 'status': '0', 'text': e.args, 'token': None}, status_code=200)


# app.middleware('http')(catch_exceptions_middleware)
app.add_middleware(
    CORSMiddleware,
    # 允许跨域的源列表，例如 ["http://www.example.org"] 等等，["*"] 表示允许任何源
    allow_origins=["*"],
    # 跨域请求是否支持 cookie，默认是 False，如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
    allow_credentials=False,
    # 允许跨域请求的 HTTP 方法列表，默认是 ["GET"]
    allow_methods=["*"],
    # 允许跨域请求的 HTTP 请求头列表，默认是 []，可以使用 ["*"] 表示允许所有的请求头
    # 当然 Accept、Accept-Language、Content-Language 以及 Content-Type 总之被允许的
    allow_headers=["*"],
    # 可以被浏览器访问的响应头, 默认是 []，一般很少指定
    # expose_headers=["*"]
    # 设定浏览器缓存 CORS 响应的最长时间，单位是秒。默认为 600，一般也很少指定
    # max_age=1000
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", port=8088)
