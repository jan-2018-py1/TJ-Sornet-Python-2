class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_num = None

class Hospital(object):
    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
    def admit(self, new_patient):
        # admit new patient
        if len(self.patients) >= self.capacity:
            print "We're sorry but the hospital is full."
        else:
            self.patients.insert(len(self.patients), new_patient)
            self.patients[len(self.patients)-1].bed_num = self.patients[len(self.patients)-1].id
            print "Admission complete!"
            print "Patient ID: ", self.patients[len(self.patients)-1].id
            print "Patient Name: ", self.patients[len(self.patients)-1].name
            print "Allergies: ", self.patients[len(self.patients)-1].allergies
            print "Bed Number: ", self.patients[len(self.patients)-1].bed_num
            print "------------"
    def discharge(self, patient_name):
        # discharge patient - look up by name
        for i in range(0, len(self.patients)):
            if self.patients[i].name == patient_name:
                print "Patient Name -", self.patients[i].name, "- removed"
                self.patients.pop(i)
                print "Patient List:"
                self.info()
                break
    def info(self):
        for i in range(0, len(self.patients)):
            print "Patient ID: ", self.patients[i].id
            print "Patient Name: ", self.patients[i].name
            print "Allergies: ", self.patients[i].allergies
            print "Bed Number: ", self.patients[i].bed_num
            print "------------"

patient1 = Patient(1, "TJ", "Peanut")
patient2 = Patient(2, "Frances", "Egg")
patient3 = Patient(3, "Vincent", "Fish")
patient4 = Patient(4, "Lucas", "Chicken")

kaiser = Hospital("Kaiser", 3)
kaiser.admit(patient1)
kaiser.admit(patient2)
kaiser.admit(patient3)
kaiser.admit(patient4)
kaiser.discharge("TJ")

    