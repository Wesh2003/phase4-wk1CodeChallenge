#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api= Api(app)
migrate = Migrate(app, db)

db.init_app(app)

class Index(Resource):
    def index(self):
        return "Index for Hero/Power API"

api.add_resource(Index, '/')


class HeroData(Resource): 
    def get(self):
        all_heroes= Hero.query.all()
        print("====================================================")
        print(all_heroes)
        hero_dict= [hero.to_dict() for hero in all_heroes]
        response= make_response(jsonify(hero_dict), 200)
        return response

api.add_resource(HeroData, '/heroes')

class HeroByID(Resource):
    def get_hero_by_id(self, id):
        hero = Hero.query.filter_by(id=id).first()
        hero_dict = hero.to_dict()

        response = make_response(
            jsonify(hero_dict),
            200
        )
        return response 

api.add_resource(HeroByID, '/heroes/<int:id>')

class PowerData(Resource):
    def get_powers(self):
        all_powers = Power.query.all()

        power_dict= [power.to_dict() for power in all_powers]
        response = make_response(
            jsonify(power_dict),
            200
        )
        return response

api.add_resource(PowerData,'/powers')


class PowerByID(Resource):
    def get_power_by_id(self, id):
        power = Power.query.filter_by(id=id).first()

        power_dict = power.to_dict()

        response = make_response(
            jsonify(power_dict),
            200
        )

        return response

api.add_resource(PowerByID, '/powers/<int:id>')


class HeroPowers(Resource):
    def post_hero_powers(self):
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

api.add_resource(HeroPowers, "/hero_powers", methods=["POST"])

class PowersUpdate(Resource):
    def update_power_by_id(self, id):
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

api.add_resource(PowersUpdate, "/powers/<int:id>", methods=["PATCH"])




if __name__ == '__main__':
    app.run(port=5550)
