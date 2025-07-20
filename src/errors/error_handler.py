from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_bad_request import HttpBadRequest
from src.errors.error_types.http_not_found import HttpNotFound
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntity

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequest, HttpNotFound, HttpUnprocessableEntity)):
        return HttpResponse(status_code=error.status_code, body={
            "errors": [{
                "title": error.name,
                "detail": error.message
            }]
        })


    return HttpResponse(status_code=500, body={
            "errors": [{
                "title": "InternalServerError",
                "detail": str(error)
            }]
        })
    