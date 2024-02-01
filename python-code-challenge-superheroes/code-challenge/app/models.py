from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at=  db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())

    # powers = db.relationship('Power', backref='hero')
    heropowers = db.relationship('HeroPower', backref='hero')

    # serialize_rules = ('-heropowers.hero',)

    def __repr__(self):
        return f'<Hero {self.name} for {self.super_name}>'

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name=  db.Column(db.String)
    description = db.Column(db.String)
    created_at=  db.Column(db.DateTime(), default=db.func.now())
    updated_at=  db.Column(db.DateTime(), onupdate=db.func.now())
    
    heropowers = db.relationship('HeroPower', backref='power')

    # serialize_rules = ('-heropowers.power',)

    def __repr__(self):
        return f'<Power ({self.id}) of {self.name}: {self.description}/10>'

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'heropowers'
    id = db.Column(db.Integer, primary_key=True)
    strength=  db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    # serialize_rules = ('-powers.heropower', '-heroes.heropower')

    def __repr__(self):
        return f"{self.strength} {self.hero_id}"