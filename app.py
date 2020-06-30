from flask import Flask, render_template, flash, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///flask_wtforms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """Renders home page"""

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)

@app.route('/pets/<int:id>', methods=['GET', 'POST'])
def pet_page(id):
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        
        db.session.commit()
        return redirect(f'/pets/{id}')
    
    else:
        return render_template('edit_pet.html', form=form, pet=pet)

@app.route('/pets/new', methods=['GET','POST'])
def add_new_pet():
    form = PetForm()
    
    if form.validate_on_submit():
        # pet.name = form.name.data
        # pet.species = form.species.data
        # pet.age = form.age.data
        # pet.photo_url = form.photo_url.data
        # pet.notes = form.notes.data
        # import pdb;pdb.set_trace()
        data = {key:val for key,val in form.data.items() if key != 'csrf_token'}
        pet = Pet(**data)
        
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template('add_pet.html', form=form)

@app.route('/pets/<int:id>/adopt', methods= ['POST'])
def update_availability(id):
    pet = Pet.query.get_or_404(id)
    pet.available = False
    db.session.add(pet)
    db.session.commit()
    return redirect('/')


@app.route('/pets/<int:id>/delete', methods= ['POST'])
def remove_pet(id):
    Pet.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/')