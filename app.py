from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
# Database Configuration
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{username}:{password}@{hostname}/{databasename}".format(
    username="Timi1234",
    password="Your Pythonanywhere database password",
    hostname="Timi1234.mysql.pythonanywhere-services.com",
    databasename="Timi1234$databasename"
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/api', methods=['GET','POST'])
def create_person():
    try:
        name = request.args.get('name')

        # Check if the name parameter is provided and is a string
        if not name:
            return jsonify({'error': 'Name query parameter is required'}), 400
        elif not isinstance(name, str) or name.isnumeric():
            return jsonify({'error': 'Name should be a non-numeric string'}), 400

        # Check if the name already exists in the database
        existing_person = Person.query.filter_by(name=name).first()
        if existing_person:
            return jsonify({'error': 'Name already exists in the database'}), 400

        # If the name is unique and not numeric, create a new person
        person = Person(name=name)
        db.session.add(person)
        db.session.commit()
        return jsonify({'message': 'Person created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
   
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get(user_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify({'id': person.id, 'name': person.name})

@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    name = request.json.get('name')
    if not name:
        return jsonify({'error': 'Name field is required'}), 400

    person = Person.query.get(user_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    person.name = name
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'})

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get(user_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
