# Q4) Hospital Management System:
# Design a system to manage patients, doctors, appointments, and medical records. 
# Implement classes for patients, doctors, appointments, medical staff, and scheduling.


class Patient:
    def __init__(self, name, patient_id, age):
        self.name = name
        self.patient_id = patient_id
        self.age = age

    def printData(self):
        print(f"Patient {self.patient_id}: {self.name}, Age: {self.age}")


class Doctor:
    def __init__(self, name, doctor_id, specialty):
        self.name = name
        self.doctor_id = doctor_id
        self.specialty = specialty

    def printData(self):
        print(f"Doctor {self.doctor_id}: {self.name}, Specialty: {self.specialty}")


class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def printData(self):
        print(f"Appointment: {self.date} at {self.time} | Patient: {self.patient.name} | Doctor: {self.doctor.name}")


class MedicalRecord:
    def __init__(self, patient):
        self.patient = patient
        self.records = []

    def add_record(self, description):
        self.records.append(description)
        print(f"Record added for {self.patient.name}: {description}")

    def printRecords(self):
        print(f"\nMedical Records for {self.patient.name}:")
        if not self.records:
            print("No records found.")
            return
        for i, rec in enumerate(self.records, 1):
            print(f"{i}. {rec}")


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
        print(f"Appointment scheduled for {appointment.patient.name} with {appointment.doctor.name} on {appointment.date} at {appointment.time}")

    def show_appointments(self):
        print("\nAll Appointments:")
        if not self.appointments:
            print("No appointments scheduled.")
            return
        for appt in self.appointments:
            appt.printData()


hospital = Hospital()

#Add patients
p1 = Patient("Suhana", 101, 30)
p2 = Patient("Aman", 102, 25)
hospital.add_patient(p1)
hospital.add_patient(p2)

#Add doctors
d1 = Doctor("Dr. Rihana", 201, "Cardiologist")
d2 = Doctor("Dr. Mirasab", 202, "Dermatologist")
hospital.add_doctor(d1)
hospital.add_doctor(d2)

#Schedule appointments
a1 = Appointment(p1, d1, "2025-09-25", "10:00 AM")
a2 = Appointment(p2, d2, "2025-09-26", "11:00 AM")
hospital.schedule_appointment(a1)
hospital.schedule_appointment(a2)

#Add medical records
mr1 = MedicalRecord(p1)
mr1.add_record("Blood Pressure: Normal")
mr1.add_record("Prescribed medication: Amlodipine")

mr2 = MedicalRecord(p2)
mr2.add_record("Skin Allergy treatment given")

#Show appointments
hospital.show_appointments()

#Show medical records
mr1.printRecords()
mr2.printRecords()
