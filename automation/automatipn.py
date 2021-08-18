from os import replace
import re
from faker import Faker

fake = Faker('en_US')

# opening the file

with open('assets/potentialcontacts.txt', 'r') as file:
    content = file.read()

extracting_phone_numbers = re.findall(r'\d{3}.\d{3}.\d{4}|\d{3}.\d{4}',content)

for phone in extracting_phone_numbers:
    if len(phone) == 10:
        new_phone = phone.split('-').sorted(key=int)
        final_phone = '-'.join(new_phone)
        
        
        with open('assets/phone_numbers.txt','a') as file:
        
           file.write(final_phone)


    if len(phone) == 7:
        new_phone = phone.split('-').sorted(key=int)
        final_phone = '-'.join(new_phone)
    with open('assets/phone_numbers.txt','a') as file:
        
           file.write(final_phone)

extracting_email = re.findall(r'[\w\.-]+@[\w\.-]+',content)

for email in extracting_email: 

    with open('assets/emails.txt','a') as file:
        
           file.write(email)

## testing 


content = ""

for _ in range(100):
    content += fake.paragraph()
    content += fake.email()
    content += fake.address()
    content += fake.phone_number()
    content += fake.word()

with open('contacts.txt', 'w+') as file:
    file.write(content)


if __name__ == "__main__":

   print(extracting_phone_numbers)
   print(extracting_email)
   print(final_phone)
 