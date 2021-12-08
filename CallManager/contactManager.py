import time
import contactService
import random

contactService.do_setup()

class ContactManager:
    
    def __init__(self):
        self.contact_service = contactService
        #list of contacts getting fetched from a db
        self.contactQueue = [x[0] for x in contactService.get_all_contacts_only()]
        self.personQueue = []        
        
        
    def joinPersonQueue(self,name):
        self.personQueue.append([name,len(self.personQueue)])
        return "Your position in queue is {}".format(len(self.personQueue))
        
    def make_call(self,contact,name):
        print(self.contactQueue)
        print(self.personQueue)
        print("Person {} is going to make a call to {} ".format(name[0],contact))
        self.personQueue.remove(name)
        
        
        callDuration = random.randint(1,10)
        time.sleep(callDuration)
        print("Done with the call lasted for ",callDuration)
        
        #when erson is done with call we should be able to assign him new number
        for x in self.personQueue:
            x[1] = x[1]-1
        self.personQueue.append([name[0],len(self.personQueue)])
        print("Person {} your new position in the queue is {} ".format(name[0],len(self.personQueue)))
        print(self.personQueue)
        
        
        
        
        
    
    
    