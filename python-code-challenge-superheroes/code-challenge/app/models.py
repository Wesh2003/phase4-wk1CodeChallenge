from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heros'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String)
    super_name = db.Column(db.String)
    strength =  db.Column(db.Integer)


    powers = db.relationship('Power', backref='hero')
    heropowers = db.relationship('HeroPower', backref='hero')

    serialize_rules = ('-powers.hero',)

    def __repr__(self):
        return f'<Hero {self.title} for {self.platform}>'

class Power(db.Model):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)

    hero_id = db.Column(db.Integer, db.ForeignKey('heros.id'))
    
    heropowers = db.relationship('HeroPower', backref='hero')

    serialize_rules = ('-hero.powers', '-heropower.powers',)

    def __repr__(self):
        return f'<Power ({self.id}) of {self.game}: {self.score}/10>'

class HeroPower(db.Model):
    __tablename__ = 'heropowers'

    id = db.Column(db.Integer, primary_key=True)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_id = db.Column(db.Integer, db.ForeignKey('heros.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    serialize_rules = ('-powers.heropower',)