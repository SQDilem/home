import sqlite3  

conn = sqlite3.connect("MyContacts.db")
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS Contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone_number TEXT,
    email TEXT
  ); 
''')

contact_data = [
  ('John Doe', '+123123123', 'john.doe@mail.ru'), 
  ('Jane Smith', '+1987659782', 'jane.smith@gmail.com'),
  ('Micheal Johnson', '+198765466', 'micheal.johnson@example.com'),
  ('Sarah Williams', '+198765432', 'sarah.williams@example.com'), 
  ('David Brown', '+198766632', 'david.brown@example.com'), 
]

cursor.executemany('INSERT INTO Contacts (name, phone_number, email) VALUES (?,?,?)', contact_data)

conn.commit()

cursor.execute('SELECT * FROM Contacts')
all_contacts = cursor.fetchall()
print ('All contacts:')
for contact in all_contacts: 
  print (contact)

cursor.execute('SELECT name, phone_number FROM Contacts WHERE phone_number LIKE "+1%"') 
contacts_with_country_code = cursor.fetchall() 
print ("\nContacts with country code +1:")
for contact in contacts_with_country_code:
  print (contact)

cursor.execute('SELECT * FROM Contants WHERE email LIKE "%gmail%"')
gmail_contacts = cursor.fetchall()
print ("\nGmail contacts:")
for contact in gmail_contacts:
  print (contact)

update_id = 1 
new_name = 'Updated Name'
new_phone_number = '+99999999'
cursor.execute('DELETE FROM Contacts SET name = ?, phone_numder = ?, WHERE id = ?', (new_name, new_phone_number))
conn.commit()
  
delete_id = 3 
cursor.execute('DELET FROM Contacts WHERE id = ?', (delete_id,))
conn.commit()

conn.close()
