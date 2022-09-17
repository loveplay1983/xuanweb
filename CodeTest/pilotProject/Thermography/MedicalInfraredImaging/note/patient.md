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



