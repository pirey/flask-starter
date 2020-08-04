import json
from werkzeug.exceptions import HTTPException
from marshmallow import ValidationError

from app.logger import logger


def init(app, api):
    """Common API Routes"""
    @app.route('/ping')
    def index():
        logger.info('Testing log output - OK')
        return {'message': 'pong'}

    # TODO proper custom error handling
    # the code below doesn't work as expected

    #  @app.errorhandler(ValidationError)
    #  def handle_validation_error(e):
    #      return e.messages, 422
    #
    #  @app.errorhandler(HTTPException)
    #  def handle_exception(e):
    #      """Return JSON instead of HTML for HTTP errors."""
    #
    #      logger.exception('Something went wrong')
    #
    #      # start with the correct headers and status code from the error
    #      response = e.get_response()
    #      # replace the body with JSON
    #      response.data = json.dumps({
    #          "code": e.code,
    #          "name": e.name,
    #          "description": e.description,
    #      })
    #      response.content_type = "application/json"
    #      return response
