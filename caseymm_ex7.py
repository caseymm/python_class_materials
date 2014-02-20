class Elevator:
    def __init__(self):
        self.floor = 1
        self.num_pass = 0
        self.door_open = False
    def get_floor(self):
        return self.floor
    def get_num_pass(self):
        return self.num_pass
    def get_door(self):
        return self.door_open
    def __str__(self):
        return "floor=" + str(self.floor) + ", passengers=" + str(self.num_pass) + ", door open=" + str(self.door_open)
    
    def call_to_floor(self, newfloor):
        self.door_open = False
        self.floor = newfloor       
    def enter_pass(self, num):
        self.door_open = True
        self.num_pass = self.num_pass + num
    def exit_pass(self, num):
        self.door_open = True
        self.num_pass = self.num_pass - num
        
e = Elevator()
print e
e.call_to_floor(9)
print e
e.enter_pass(3)
print e
e.call_to_floor(4)
print e
e.exit_pass(1)
print e
