class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_num = "none"





class Hospital(object):
    def __init__(self, name, capacity):
        self.patientslist =[]
        self.name = name
        self.capacity = capacity
    def admit(self, patient, bed_num):
        if len(self.patientslist)>=self.capacity:
            print "The hospital is full."
        else:
            self.patientslist.append(patient)
            patient.bed_num = bed_num
        return self
    def discharge(self, patient):
        for i in range(0,len(self.patientslist)):
            if self.patientslist[i].name == patient:
                self.patientslist[i].bed_num = "none"
                self.patientslist.pop(i)
                break
        return self
    def info(self):
        for i in range(0,len(self.patientslist)):
            print self.patientslist[i].name, self.patientslist[i].id, self.patientslist[i].allergies, self.patientslist[i].bed_num

hos1 = Hospital("Kaiser", 10)
p1 = Patient(123,"johnnie","cat")
p2 = Patient(245,"Thihn","dog")
p3 = Patient(654,"james","peach")
p4 = Patient(3,"ryan","peanut")



hos1.admit(p1,1).admit(p2,2).admit(p3,3).discharge("james").info()

