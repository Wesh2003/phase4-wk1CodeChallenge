from faker import Faker
from random import choice

from app import app
from models import db, Power, Hero, HeroPower

# db.init_app(app)

fake = Faker()

with app.app_context():

    Power.query.delete()
    Hero.query.delete()
    HeroPower.query.delete()

    fake = Faker()

    db.session.add_all([
        Power( name= "super strength", description= "gives the wielder super-human strengths" ),
        Power( name= "flight", description= "gives the wielder the ability to fly through the skies at supersonic speed" ),
        Power( name= "super human senses", description= "allows the wielder to use her senses at a super-human level" ),
        Power( name= "elasticity", description= "can stretch the human body to extreme lengths" )
    ])

    db.session.commit()

    db.session.add_all([
        Hero( name= "Kamala Khan", super_name= "Ms. Marvel" ),
        Hero( name= "Doreen Green", super_name= "Squirrel Girl" ),
        Hero( name= "Gwen Stacy", super_name= "Spider-Gwen" ),
        Hero( name= "Janet Van Dyne", super_name= "The Wasp" ),
        Hero( name= "Wanda Maximoff", super_name= "Scarlet Witch" ),
        Hero( name= "Carol Danvers", super_name= "Captain Marvel" ),
        Hero( name= "Jean Grey", super_name= "Dark Phoenix" ),
        Hero( name= "Ororo Munroe", super_name= "Storm" ),
        Hero( name= "Kitty Pryde", super_name= "Shadowcat" ),
        Hero( name= "Elektra Natchios", super_name= "Elektra" )
    ])

    db.session.commit()

    hero= Hero.query.all()
    power= Power.query.all()

    for i in range(10):
      strength= ['Weak', 'Strong', 'Average']
      rand_hero= choice(hero)
      rand_power= choice(power)

      new_hero_power= HeroPower(strength= choice(strength), hero_id= rand_hero.id,  power_id= rand_power.id)
      db.session.add(new_hero_power)
      db.session.commit()







# puts "🦸‍♀️ Seeding powers..."
# Power.create([
#   { name: "super strength", description: "gives the wielder super-human strengths" },
#   { name: "flight", description: "gives the wielder the ability to fly through the skies at supersonic speed" },
#   { name: "super human senses", description: "allows the wielder to use her senses at a super-human level" },
#   { name: "elasticity", description: "can stretch the human body to extreme lengths" }
# ])

# puts "🦸‍♀️ Seeding heroes..."
# Hero.create([
#   { name: "Kamala Khan", super_name: "Ms. Marvel" },
#   { name: "Doreen Green", super_name: "Squirrel Girl" },
#   { name: "Gwen Stacy", super_name: "Spider-Gwen" },
#   { name: "Janet Van Dyne", super_name: "The Wasp" },
#   { name: "Wanda Maximoff", super_name: "Scarlet Witch" },
#   { name: "Carol Danvers", super_name: "Captain Marvel" },
#   { name: "Jean Grey", super_name: "Dark Phoenix" },
#   { name: "Ororo Munroe", super_name: "Storm" },
#   { name: "Kitty Pryde", super_name: "Shadowcat" },
#   { name: "Elektra Natchios", super_name: "Elektra" }
# ])

# puts "🦸‍♀️ Adding powers to heroes..."

# strengths = ["Strong", "Weak", "Average"]
# Hero.all.each do |hero|
#   rand(1..3).times do
#     # get a random power
#     power = Power.find(Power.pluck(:id).sample)

#     HeroPower.create!(hero_id: hero.id, power_id: power.id, strength: strengths.sample)
#   end
# end

# puts "🦸‍♀️ Done seeding!"
