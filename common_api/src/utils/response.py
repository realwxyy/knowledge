from flask import make_response, jsonify

INVALID_FIELD_NAME_SENT_422 = {
    "http_code": 422,
    "code": 422,
    "message": "Invalid fields found"
}

INVALID_INPUT_422 = {
    "http_code": 422,
    "code": 422,
    "message": "Missing parameters"
}

BAD_REQUEST_400 = {
    "http_code": 400,
    "code": 400,
    "message": "Bad request"
}

SERVER_ERROR_500 = {
    "http_code": 500,
    "code": 500,
    "message": "Server error"
}

SERVER_ERROR_404 = {
    "http_code": 404,
    "code": 404,
    "message": "Resource not found"
}

UNAUTHORIZED_403 = {
    "http_code": 403,
    "code": 403,
    "message": "You are not authorized"
}

SUCCESS_200 = {
    'http_code': 200,
    'code': 200,
}

SUCCESS_201 = {
    'http_code': 201,
    'code': 200,
    "message": "add success"
}
SUCCESS_204 = {
    'http_code': 204,
    'code': 204
}


def response_with(response, value=None, message=None,
                  error=None, headers={}, pagination=None):
    result = {}
    if value is not None:
        result.update({'data': value})
    print(message)
    if message is not None:
        result.update({'message': message})

    result.update({'code': response['code']})

    if error is not None:
        result.update({'errors': error})

    if pagination is not None:
        result.update({'pagination': pagination})

    headers.update({'Access-Control-Allow-Origin': '*'})
    headers.update({'server': 'Flask REST API'})

    return make_response(jsonify(result), response['http_code'], headers)


def resp_succ(data={}):
    return response_with(SUCCESS_200, data)


def resp_not_found(data={}):
    return response_with(SERVER_ERROR_404, data)


def resp_fail(data={}, message='失败'):
    return response_with(BAD_REQUEST_400, data, message)


def resp_err(data={}, message='失败'):
    return response_with(SERVER_ERROR_500, data, message)
