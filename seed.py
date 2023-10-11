from db import db
# This file is for initial seeding of the database.
# Import the models you want above and then create your objects/data
# inside the create_data function below. You must create an object with
# your model then append each object to the data_to_save variable to be saved.


def create_data():
    data_to_save = []
    # Add your data in between the start and end comments below.
    # Before sure to append each object you want to save to data_to_save.
    # Ex: data_to_save.append(my_object_here)
    ### Start ###

    ### End ###
    db.session.bulk_save_objects(data_to_save)
    db.session.commit()
