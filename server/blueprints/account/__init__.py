from flask import Blueprint

bp = Blueprint(
    "account_bp",
    __name__,
    template_folder="templates",
)

from . import routes  # noqa: F401
