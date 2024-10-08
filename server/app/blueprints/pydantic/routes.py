from app import bcrypt, db
from flask import flash, render_template, request

from . import bp
from .forms import SignupForm
from .models import PydanticAccount


@bp.route("/create-account", methods=["GET", "POST"])
def create_account():
    form = SignupForm(request.form)
    if request.method == "GET":
        return render_template("pydantic/create_account.html", form=form)

    if request.method == "POST" and form.validate():
        account = None
        try:
            email = form.email.data
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

            account = PydanticAccount(email=email, password=hashed_password)
            db.session.add(account)
            db.session.commit()
            flash("A new account is created.")
        except Exception:
            db.session.rollback()

    return render_template("pydantic/create_account.html", form=form)
