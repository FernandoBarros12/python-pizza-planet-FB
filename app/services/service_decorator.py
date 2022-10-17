from flask import jsonify
import functools


def service_decorator(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        entity, error = func(*args, **kwargs)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    return decorator
