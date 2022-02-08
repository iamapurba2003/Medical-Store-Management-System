from database import db

# Talking to Database
cur = db.cursor()

# Stock of Medicines
Medicines = [
    ('Etodizem', 350, 'A Very Effective Medicine for Liver', 250),
    ('Allelovir', 200, 'Removes Pain from Stomach Ache', 300),
    ('Estropiride', 300, 'Gas Removal  -- But Takes Time', 100),
    ('Amoxicillin', 600, 'Used to Treat Variety of Bacterial Infections', 600),
    ('Flucloxacillin', 550, 'Treats Skin Infections', 200),
    ('Balsalazide', 340, 'Used to Treat mild to moderate Ulcerative Collitis', 700),
    ('Nexpro RD40', 520, 'Relieves Acidity & Gastric Pains', 400),
    ('Banzel', 250, 'Medicines to treat Seizures', 550),
    ('Metrozil 600', 254, 'Cures Abdominal Pain', 630),
    ('UniEnzyme', 360, 'Helps in Proper Digestion', 960)
]

# Queries
Queries = [
    ("CREATE TABLE IF NOT EXISTS medicines(name VARCHAR(50), price BIGINT, description VARCHAR(60), quantity INT(10))"),
    # ("CREATE TABLE IF NOT EXISTS account(user_name VARCHAR(60), password VARCHAR(50), name VARCHAR(30))")
]

Query = "INSERT INTO medicines(name, price, description, quantity) VALUES (%s, %s, %s, %s)"


# Execution of Queries
for val in Queries:
    cur.execute(val)

# Inserted Medicines into Table 
# cur.executemany(Query, Medicines)
# db.commit()

# cur.execute("SHOW TABLES")
# for x in cur:print(x)


def main():
    pass


# Driver Code
if __name__ == "__main__":
    main()


"""
I want to add an Additional Feature of Inserting Medicines, but that's still Experimental. Will apply at last 
"""