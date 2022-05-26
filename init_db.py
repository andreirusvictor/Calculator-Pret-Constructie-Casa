import psycopg2


    conn=psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres",

)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE regim_inaltime (
        id SERIAL PRIMARY KEY,
        descriere TEXT NOT NULL,
        valoare INTEGER NOT NULL
    );
    
    CREATE TABLE nivel_finisare (
        id SERIAL PRIMARY KEY,
        descriere TEXT NOT NULL,
        valoare INTEGER NOT NULL
    );
    
    CREATE TABLE nivel_arhitectura (
        id SERIAL PRIMARY KEY,
        descriere TEXT NOT NULL,
        valoare INTEGER NOT NULL
    );
    
    CREATE TABLE verificare_topografica (
        id SERIAL PRIMARY KEY,
        descriere TEXT NOT NULL,
        valoare INTEGER NOT NULL
    );
    
    CREATE TABLE verificare_geologica (
        id SERIAL PRIMARY KEY,
        descriere TEXT NOT NULL,
        valoare INTEGER NOT NULL
    );
    
    CREATE TABLE comision_agentie (
        id SERIAL PRIMARY KEY,
        descriere TEXT NOT NULL,
        valoare FLOAT NOT NULL
    );
    
    INSERT INTO regim_inaltime VALUES 
        (1, 'Parter si cel putin un etaj sau mansarda', 200),
        (2, 'Parter', 400);
        
    INSERT INTO nivel_finisare VALUES 
        (1, 'Ieftin', 180),
        (2, 'Mediu', 200),
        (3, 'Peste mediu', 245),
        (4, 'Lux', 285);
    
    INSERT INTO nivel_arhitectura VALUES
        (1, 'Arhitectura simpla', 230),
        (2, 'Arhitectura de complexitate media', 260),
        (3, 'Arhitectura complexa', 290);
        
    INSERT INTO verificare_topografica VALUES 
        (1, 'Da', 200),
        (2, 'Nu', 0);

    INSERT INTO verificare_geologica VALUES 
        (1, 'Da', 200),
        (2, 'Nu', 0);
    
    INSERT INTO comision_agentie VALUES 
        (1, 'Nu', 0),
        (2, '1%', 1),
        (3, '1.5%', 1.5),
        (4, '2%', 2),
        (5, '3%', 3);
    """
)

conn.commit()
conn.close()
