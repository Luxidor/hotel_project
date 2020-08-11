class Guest:
    def __init__(self, name, id, card_num, phone_num):
        self.name = name
        self.id =  id
        self.card_num = card_num
        self.phone_num =  phone_num
        
    def __str__(self):
        return "name: " + self.name + ", card number: " + self.card_num + ", phone number: " + self.phone_num + ", id: " + str(self.id)


