# Patient

* id - db.column(db.Integer, primary_key=True)
* name - db.column(db.String(50))
* sex - db.column(db.String(2))
* idnum - db.column(db.Integer)
* phone - db.column(db.Integer)
* addr - db.column(db.String(100))
* images = db.relationship("Image", back_populates="patient", cascade="all")
* records = db.relationship("MedRecord", back_populates="patient", cascade="all")
* clinics = db.relationship("Clinic", back_populates="patient", cascade="all")



# Image

* id - db.column(db.Integer, primary_key=True)
* description - db.column(db.String(100))
* filename - db.column(db.String(64))
* timestamp - db.column(db.DateTime, default=datetime.utcnow, index=True)
* patient-id   - db.column(db.Integer, db.ForeignKey("patient.id"))
* patient = db.relationship("Patient", back_populates="images")



# MedRecord

* id - db.column(db.Integer, primary_key=True)
* patient-description - db.column(db.String(500))
* lis-description - db.column(db.String(500))
* pacs-description - db.column(db.String(500))
* patient-id - db.column(db.Integer, db.ForeignKey("patient.id"))
* patient = db.relationship("Patient", back_populates="records")



# Clinic

* id -db.column(db.Integer, primary_key=True)
* init-clinic - db.column(db.String(1000))
* doc-clinic - db.column(db.String(1000))
* patient-id - db.column(db.Integer, db.ForeignKey("patient.id"))
* patient = db.relationship("Patient", back_populates="clinics")



# ~~Report~~

* ~~id - db.column(db.Integer, primary_key=True)~~
* ~~patient-id  - db.column(db.Integer, db.ForeignKey("patient.id"))~~







```
# Raw SQL in via SQLALchemy
# https://stackoverflow.com/questions/17972020/how-to-execute-raw-sql-in-flask-sqlalchemy-app
"""
1. Retrieve user input pNum;
    ```
    pNum = request.form.get("patientNum")
    ```
2. Query patient info includes name, sex, id, phone, and address, etc. 
   by pNum via db.engine.execute('xxx')
   ```
   info = db.engine.execute("SELECT name, sex, id, phone, addr FROM xxx WHERE p-num = pNum")
   ```
3. Pass the query result back to the PatientInfo() form class, 
   and set each field with the corresponding result data 
   patientInfo.patientName.data = info[0]
   patientInfo.patientSex.data = info[1]
   patientInfo.patientID.data = info[2]
   patientInfo.patientPhone.data = info[3]
   patientInfo.patientAddr.data = info[4] 
"""
```