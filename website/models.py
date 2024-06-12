from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    hr = db.relationship('Hr', backref='user', uselist=False)
    diagnosis = db.relationship('Diagnosis', backref='user', uselist=False)
    diet = db.relationship('Diet', backref='user', uselist=False)
    def has_profile(self):
        return hasattr(self, 'hr') and self.hr is not None
    def has_diagnosis(self):
        return hasattr(self, 'diagnosis') and self.diagnosis is not None
    def has_diet(self):
        return hasattr(self, 'diet') and self.diet is not None
    


class Hr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))  # Assuming string data type for gender
    medical_conditions = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Diagnosis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10))
    age_at_diagnosis = db.Column(db.String(30))
    idh1 = db.Column(db.String(20))
    tp53 = db.Column(db.String(20))
    atrx = db.Column(db.String(20))
    pten = db.Column(db.String(20))
    egfr = db.Column(db.String(20))
    cic = db.Column(db.String(20))
    muc16 = db.Column(db.String(20))
    pik3ca = db.Column(db.String(20))
    nf1 = db.Column(db.String(20))
    pik3r1 = db.Column(db.String(20))
    fubp1 = db.Column(db.String(20))
    rb1 = db.Column(db.String(20))
    notch1 = db.Column(db.String(20))
    bcor = db.Column(db.String(20))
    csmd3 = db.Column(db.String(20))
    smarca4 = db.Column(db.String(20))
    grin2a = db.Column(db.String(20))
    idh2 = db.Column(db.String(20))
    fat4 = db.Column(db.String(20))
    pdgfra = db.Column(db.String(20))
    predictions = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_item = db.Column(db.String(150))
    calories = db.Column(db.Integer)
    exercise = db.Column(db.String(50))
    calories_burned = db.Column(db.Integer)
    net_calories = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


