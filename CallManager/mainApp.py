from contactManager import ContactManager
import random


contactMgr = ContactManager()
print(contactMgr.joinPersonQueue("rakesh"))
print(contactMgr.joinPersonQueue("ranjan"))
print(contactMgr.joinPersonQueue("user99"))
print(contactMgr.joinPersonQueue("user212"))
print(contactMgr.joinPersonQueue("user50"))

print("-------------START CALLS-----------")

#currently 5 users can make calls to contacts, the contact is random and duration is random
for x in contactMgr.personQueue[:]:
    print("----SART A CALL-----")
    number = contactMgr.contactQueue[random.randint(0,4)]
    contactMgr.make_call(number,x)
    print("----END-----")

print(contactMgr.contactQueue)