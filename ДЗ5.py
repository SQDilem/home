import sqlite3
conn = sqlite3.connect("Blog.db")
cursore = conn.cursor()

cursore.execute('''
CREATE TABLE IF NOT EXISTS rubrics(
  id INTEGER PRIMARY KEY,
  name TEXT); 
'''  )

cursore.execute('''
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY, 
  full_name TEXT, 
  birth_date DATE, 
  role TEXT, 
  registration_date DATE); 
''')

cursore.execute('''
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY,
  rubric_id INTEGER,
  user_id INTEGER,
  text TEXT, 
  FOREIGN KEY  (rubric_id) REFERENCES rubrics(id),
  FOREIGN KEY  (user_id) REFERENCES users(id)); 
''') 

conn.commit()

rublics_data = [
  ('1', 'Technology'),
  ('2', 'Travel'),
  ('3', 'Food'),
  ('4', 'Lifesryle'),
  ('5', 'Fasion'),
]
cursore.executemany('INSERT INTO rubrics (id, name) VALUES (?, ?);', rublics_data) 


users_data = [
  (1, 'John Doe', '1990-05-15', 'author', '2023-01-10'),
  (2, 'Jane Smith', '1905-09-20', 'reader', '2022-08-05'),
  (3, 'Alexsander Black', '2000-07-05', 'admin', '2023-03-18'),
  (4, 'Emily Brown', '2001-11-27', 'reader', '2021-12-02'),
  (5, 'Michel Wilson', '1980-07-30', 'author', '2021-12-02'),
]
cursore.executemany('INSERT INTO users (id, full_name, birth_date, role, registration_date) VALUES (?,?,?,?,?)', users_data)

posts_data = [
  (1, 1, 1, 'Summer Fasion'),
  (2, 2, 3, 'A Journey the Montains'),
  (3, 3, 1, 'Hello, World!'),
  (4, 4, 4, 'Balancing Worlk and Hobbies'),
  (5, 5, 2, 'Exploring the Latest Tech Trends'),
]
cursore.executemany('INSERT INTO posts (id, rubric_id, user_id, text) VALUES (?,?,?,?)', posts_data)
conn.commit()
conn.close()
  