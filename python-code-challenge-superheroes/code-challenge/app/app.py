#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return "Index for Hero/Power API"

@app.route('/heroes')
def heroes():

    heroes = []
    for hero in Hero.query.all():
        hero_dict = {
            "name": hero.name,
            "super_name": hero.super_name,
            "strength": hero.strength,
        }
        heroes.append(hero_dict)

    response = make_response(
        jsonify(heroes),
        200
    )

    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/heroes/<int:id>')
def hero_by_id(id):
    hero = Hero.query.filter_by(id=id).first()

    hero_dict = hero.to_dict()

    response = make_response(
        jsonify(hero_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/powers')
def heroes():

    powers = []
    for power in Power.query.all():
        power_dict = {
            "description": power.description,
        }
        heroes.append(power_dict)

    response = make_response(
        jsonify(powers),
        200
    )

    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/powers/<int:id>')
def power_by_id(id):
    power = Power.query.filter_by(id=id).first()

    power_dict = power.to_dict()

    response = make_response(
        jsonify(power_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response



@app.route('/hero_powers', methods=['POST'])
def post_hero_powers():
    new_hero_power = HeroPower(
            strength=request.form.get("strength"),
            power_id=request.form.get("power_id"),
            hero_id=request.form.get("hero_id"),
        )

    db.session.add(new_hero_power)
    db.session.commit()

    hero_power_dict = new_hero_power.to_dict()

    response = make_response(
            jsonify(hero_power_dict),
            201
        )

    return response

@app.route('/powers/<int:id>', methods=['PATCH'])
def power_by_id(id):
    power = Power.query.filter_by(id=id).first()

    for attr in request.form:
        setattr(power, attr, request.form.get(attr))

    db.session.add(power)
    db.session.commit()

    power_dict = power.to_dict()

    response = make_response(
        jsonify(power_dict),
            200
            )

    return response



if __name__ == '__main__':
    app.run(port=5555)
