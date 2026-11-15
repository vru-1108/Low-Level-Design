class Room:
    def __init__(self, number: str, floor: int):
        self.number = number
        self.floor = floor

class Appointment:
    def __init__(self, doctor, patient, room: Room, time: str):
        self.doctor = doctor
        self.patient = patient
        self.room = room
        self.time = time
        doctor.add_appointment(self)
        patient.add_appointment(self)

class Doctor:
    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization
        self.appointments = []

    def add_appointment(self, appt: Appointment):
        self.appointments.append(appt)

    def get_patients(self):
        seen = set()
        result = []
        for appt in self.appointments:
            if id(appt.patient) not in seen:
                seen.add(id(appt.patient))
                result.append(appt.patient)
        return result

class Patient:
    def __init__(self, name: str):
        self.name = name
        self.appointments = []

    def add_appointment(self, appt: Appointment):
        self.appointments.append(appt)

    def get_doctors(self):
        seen = set()
        result = []
        for appt in self.appointments:
            if id(appt.doctor) not in seen:
                seen.add(id(appt.doctor))
                result.append(appt.doctor)
        return result

# Usage
dr_smith = Doctor("Dr. Smith", "Cardiology")
dr_patel = Doctor("Dr. Patel", "Neurology")

alice = Patient("Alice")
bob = Patient("Bob")

room_101 = Room("101", 1)
room_205 = Room("205", 2)

Appointment(dr_smith, alice, room_101, "9:00 AM")
Appointment(dr_smith, bob, room_101, "10:00 AM")
Appointment(dr_patel, alice, room_205, "2:00 PM")

print(f"{dr_smith.name}'s patients:")
for p in dr_smith.get_patients():
    print(f"  - {p.name}")

print(f"{alice.name}'s doctors:")
for d in alice.get_doctors():
    print(f"  - {d.name} ({d.specialization})")

print(f"{dr_smith.name}'s schedule:")
for a in dr_smith.appointments:
    print(f"  - {a.time} with {a.patient.name} in Room {a.room.number}")