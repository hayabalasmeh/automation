from os import replace
import re
from faker import Faker

fake = Faker('en_US')

# opening the file

with open('assets/potentialcontacts.txt', 'r') as file:
    content = file.read()

extracting_phone_numbers = re.findall(r'\d{3}.\d{3}.\d{4}|\d{3}.\d{4}',content)


# Duplicate:
numbers = []
for phone in extracting_phone_numbers:

    if phone not in numbers:
         
        numbers.append(phone) 

for phone in numbers:
        
            if len(phone) == 12:
                
                new_phone =re.sub('\.','-',phone)
                temp_1= re.sub('\)','-',new_phone)
                temp = temp_1.split('-')
                # print(temp)
                temp.sort(key=int)
                # print(temp)
                final_phone = '-'.join(temp)
                print(final_phone)
                with open('assets/phone_numbers.txt','a') as file:
                     file.write(f'{final_phone}\n')
                
for phone in numbers:
    
        with open('assets/phone_numbers.txt','a') as file:
            if len(phone) == 7:
                
                new_phone =re.sub('\.','-',phone)
                temp_1= re.sub('\)','-',new_phone)
                temp = temp_1.split('-')
                temp.sort(key=int)
                final_phone = '-'.join(temp)

          
            #     new_phone = re.sub('\.','-',phone).split('-').sorted(key=int)
            #     final_phone = '-'.join(new_phone)
            
                print(final_phone)
                
                file.write(f'206-{final_phone}\n')
                

extracting_email = re.findall(r'[\w\.-]+@[\w\.-]+',content)

# Duplicate:
emails = []
for email in extracting_email:

    if email not in emails:
         
        emails.append(email) 

for email in emails: 

    with open('assets/emails.txt','a') as file:
        
           file.write(f'{email}\n')

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
     print(list)
     print(extracting_phone_numbers[1])
   