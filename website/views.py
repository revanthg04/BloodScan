from flask import Blueprint, render_template, request, flash, jsonify, url_for,redirect
from flask_login import login_required, current_user
from .models import Hr,User, Diagnosis, Diet
from . import db
import joblib, os
from sklearn.preprocessing import LabelEncoder
import pandas as pd

label_encoder = LabelEncoder()
script_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(script_dir, 'models', 'x.pkl')
model = joblib.load(model_path)


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/update-profile', methods=['POST'])
@login_required
def update_profile():
    if request.method == 'POST':
        age = request.form.get('age')
        gender = request.form.get('gender')
        medical_conditions = request.form.get('medical_conditions')

        
        user = User.query.get(current_user.id)

        if user.hr:
            
            user.hr.age = age
            user.hr.gender = gender
            user.hr.medical_conditions = medical_conditions
        else:
            
            hr = Hr(age=age, gender=gender, medical_conditions=medical_conditions, user=user)
            db.session.add(hr)
        db.session.commit()

        
        flash('Profile updated successfully!', category='success')
        return redirect(url_for('views.home'))  

    
    flash('Failed to update profile. Please try again.', category='error')
    return redirect(url_for('views.update_profile'))


@views.route('/delete-profile', methods=['POST'])
@login_required
def delete_profile():
    user = User.query.get(current_user.id)
    if user.has_profile():
        db.session.delete(user.hr)
        db.session.commit()
        flash('Profile deleted successfully!', category='success')
    else:
        flash('No profile data to delete.', category='error')
    return redirect(url_for('views.home'))

@views.route('/submit_diagnosis', methods=['POST'])
@login_required                     
def submit_diagnosis():
    if request.method == 'POST':
        
        gender = request.form.get('gender')
        age_at_diagnosis = request.form.get('years')
        idh1 = request.form.get('idh1')
        tp53 = request.form.get('tp53')
        atrx = request.form.get('atrx')
        pten = request.form.get('pten')
        egfr = request.form.get('egfr')
        cic = request.form.get('cic')
        muc16 = request.form.get('muc16')
        pik3ca = request.form.get('pik3ca')
        nf1 = request.form.get('nf1')
        pik3r1 = request.form.get('pik3r1')
        fubp1 = request.form.get('fubp1')
        rb1 = request.form.get('rb1')
        notch1 = request.form.get('notch1')
        bcor = request.form.get('bcor')
        csmd3 = request.form.get('csmd3')
        smarca4 = request.form.get('smarca4')
        grin2a = request.form.get('grin2a')
        idh2 = request.form.get('idh2')
        fat4 = request.form.get('fat4')
        pdgfra = request.form.get('pdgfra')

        user1 = User.query.get(current_user.id)


        
        diagnosis = Diagnosis(gender=gender,
            age_at_diagnosis=age_at_diagnosis,
            idh1=idh1,
            tp53=tp53,
            atrx=atrx,
            pten=pten,
            egfr=egfr,
            cic=cic,
            muc16=muc16,
            pik3ca=pik3ca,
            nf1=nf1,
            pik3r1=pik3r1,
            fubp1=fubp1,
            rb1=rb1,
            notch1=notch1,
            bcor=bcor,
            csmd3=csmd3,
            smarca4=smarca4,
            grin2a=grin2a,
            idh2=idh2,
            fat4=fat4,
            pdgfra=pdgfra,
            user = user1)

       
        db.session.add(diagnosis)
        db.session.commit()

        db.session.add(diagnosis)
        db.session.commit()
        new_data = {
            'Gender': [gender],
            'Age_at_diagnosis': [age_at_diagnosis],
            'IDH1_MUTATED': [idh1 == 'MUTATED'],
            'IDH1_NOT_MUTATED': [idh1 != 'MUTATED'],
            'TP53_MUTATED': [tp53 == 'MUTATED'],
            'TP53_NOT_MUTATED': [tp53 != 'MUTATED'],
            'ATRX_MUTATED': [atrx == 'MUTATED'],
            'ATRX_NOT_MUTATED': [atrx != 'MUTATED'],
            'PTEN_MUTATED': [pten == 'MUTATED'],
            'PTEN_NOT_MUTATED': [pten != 'MUTATED'],
            'EGFR_MUTATED': [egfr == 'MUTATED'],
            'EGFR_NOT_MUTATED': [egfr != 'MUTATED'],
            'CIC_MUTATED': [cic == 'MUTATED'],
            'CIC_NOT_MUTATED': [cic != 'MUTATED'],
            'MUC16_MUTATED': [muc16 == 'MUTATED'],
            'MUC16_NOT_MUTATED': [muc16 != 'MUTATED'],
            'PIK3CA_MUTATED': [pik3ca == 'MUTATED'],
            'PIK3CA_NOT_MUTATED': [pik3ca != 'MUTATED'],
            'NF1_MUTATED': [nf1 == 'MUTATED'],
            'NF1_NOT_MUTATED': [nf1 != 'MUTATED'],
            'PIK3R1_MUTATED': [pik3r1 == 'MUTATED'],
            'PIK3R1_NOT_MUTATED': [pik3r1 != 'MUTATED'],
            'FUBP1_MUTATED': [fubp1 == 'MUTATED'],
            'FUBP1_NOT_MUTATED': [fubp1 != 'MUTATED'],
            'RB1_MUTATED': [rb1 == 'MUTATED'],
            'RB1_NOT_MUTATED': [rb1 != 'MUTATED'],
            'NOTCH1_MUTATED': [notch1 == 'MUTATED'],
            'NOTCH1_NOT_MUTATED': [notch1 != 'MUTATED'],
            'BCOR_MUTATED': [bcor == 'MUTATED'],
            'BCOR_NOT_MUTATED': [bcor != 'MUTATED'],
            'CSMD3_MUTATED': [csmd3 == 'MUTATED'],
            'CSMD3_NOT_MUTATED': [csmd3 != 'MUTATED'],
            'SMARCA4_MUTATED': [smarca4 == 'MUTATED'],
            'SMARCA4_NOT_MUTATED': [smarca4 != 'MUTATED'],
            'GRIN2A_MUTATED': [grin2a == 'MUTATED'],
            'GRIN2A_NOT_MUTATED': [grin2a != 'MUTATED'],
            'IDH2_MUTATED': [idh2 == 'MUTATED'],
            'IDH2_NOT_MUTATED': [idh2 != 'MUTATED'],
            'FAT4_MUTATED': [fat4 == 'MUTATED'],
            'FAT4_NOT_MUTATED': [fat4 != 'MUTATED'],
            'PDGFRA_MUTATED': [pdgfra == 'MUTATED'],
            'PDGFRA_NOT_MUTATED': [pdgfra != 'MUTATED']
            }
        new_data['Gender'] = label_encoder.fit_transform(new_data['Gender'])
        
        new_datas = pd.DataFrame.from_dict(new_data)
        predictions = model.predict(new_datas)
        user1.diagnosis.predictions = predictions
        flash('Diagnosis submitted successfully!', 'success')
        return redirect(url_for('views.home'))  

    
    flash('Failed to submit diagnosis. Please try again.', category='error')
    return redirect(url_for('views.submit_diagnosis'))


@views.route('/delete-diagnosis', methods=['POST'])
@login_required                     
def delete_diagnosis():
    user = User.query.get(current_user.id)
    if user.has_diagnosis():
        db.session.delete(user.diagnosis)
        db.session.commit()
        flash('Profile deleted successfully!', category='success')
    else:
        flash('No profile data to delete.', category='error')
    return redirect(url_for('views.home'))

@views.route('/submit_diet', methods=['POST'])
@login_required
def submit_diet():
     if request.method == 'POST':
        food_item = request.form.get('food_item')
        calories = int(request.form.get('calories'))
        exercise = request.form.get('exercise')
        calories_burned = int(request.form.get('calories_burned'))
        calorie_difference = calories - calories_burned
        new_diet_entry = Diet(food_item=food_item,
                              calories=calories,
                              exercise=exercise,
                              calories_burned=calories_burned,
                              net_calories = calorie_difference,
                              user=current_user)
        db.session.add(new_diet_entry)
        db.session.commit()
        flash('Diet updated', category='success')
        return redirect(url_for('views.home'))
@views.route('/delete-diet', methods=['POST'])
@login_required
def delete_diet():
    user = User.query.get(current_user.id)
    if user.has_diet():
        db.session.delete(user.diet)
        db.session.commit()
        flash('Profile deleted successfully!', category='success')
    else:
        flash('No profile data to delete.', category='error')
    return redirect(url_for('views.home'))