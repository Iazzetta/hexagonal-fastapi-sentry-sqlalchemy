from fastapi.responses import JSONResponse

def response_not_found(model: str, err: any):
    return JSONResponse(content = {'data': f'Não foi possível encontrar {model}'}, status_code = 404)

def response_error(model: str, err: any):
    return JSONResponse(content = {'data': f'Ocorreu um problema: {model}'}, status_code = 500)


def response_success(response: any):
    return JSONResponse(content = {'data': response}, status_code = 200)