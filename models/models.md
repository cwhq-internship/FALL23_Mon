# Getting started making database models


## Simple example
When creating a model for the first time you will need to create the file in the models folder. You will need to import db from db as shown below. You can access all the standard SQLAlchemy column data types. Be sure to create or reset the database in order for the model to generate a new table. The example below is a very basic model for getting started. This can be used as a starter template when making new models.
```
from db import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    is_active = db.Column(db.Boolean)
    email = db.Column(db.String)
```

## Making Relations

### One to One
Sometimes one model has a relationship to another. An example in this case would be a user and a pet. Lets assume for now each user has a relationship to only one pet. You can show that
```
from db import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    pet = db.relationship('Pet', backref='user', lazy=True, uselist=False)

class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    weight = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=True)
```

### One to Many
Using the same example as above lets assume a user has many pets. We can take the above code and tweak the user model a bit to show that a user can have multiple pets.
```
from db import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    pets = db.relationship('Pet', backref='user', lazy=True)

class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    weight = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=True)
```

### Many To Many
- TODO 

## How to query data?
In order to query data you will need to make sure you have db imported towards the top of your blueprints or app.py like this `from db import db`. Next you will need to import your models into that same file. Using the examples listed above it may look like this `from models.your_filename import Pet`.

Additional Resources
- A list of all the available datatypes that SQLAlchemy has to offer can be located [here](https://docs.sqlalchemy.org/en/14/core/type_basics.html). You can access those datatypes the same way you currently access them which is `db.NameOfDataTypeHere` another example is `db.String` used in the above examples.
- If you want to learn more about Flask SQLAlchemy you can visit the docs [here](https://flask-sqlalchemy.palletsprojects.com).