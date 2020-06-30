from app import db
from models import Pet

db.drop_all()
db.create_all()


db.session.add(Pet(name='bob',species='dog',age=7,notes='good boy',photo_url='https://specials-images.forbesimg.com/imageserve/5db4c7b464b49a0007e9dfac/960x0.jpg?fit=scale'))
db.session.add(Pet(name='plain',species='dog',age=7,notes='good boy',photo_url='https://specials-images.forbesimg.com/imageserve/5db4c7b464b49a0007e9dfac/960x0.jpg?fit=scale'))
db.session.add(Pet(name='gizzard',species='dog',age=7,notes='good boy',photo_url='https://specials-images.forbesimg.com/imageserve/5db4c7b464b49a0007e9dfac/960x0.jpg?fit=scale'))
db.session.add(Pet(name='jane',species='dog',age=7,notes='good boy',photo_url='https://specials-images.forbesimg.com/imageserve/5db4c7b464b49a0007e9dfac/960x0.jpg?fit=scale'))
db.session.add(Pet(name='joe',species='dog',age=7,notes='good boy',photo_url='https://specials-images.forbesimg.com/imageserve/5db4c7b464b49a0007e9dfac/960x0.jpg?fit=scale'))

db.session.commit()