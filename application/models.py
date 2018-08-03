from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    address = db.Column(db.String(45), index=True, unique=False)
    
    def __init__(self, notes):
        self.notes = notes

    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return '<Data %r>' % self.notes  % self.address