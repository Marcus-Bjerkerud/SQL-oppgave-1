import sqlite3
import pandas as pd
import csv

def main():
    # Opprett en tilkobling til SQLite-databasen
    conn = opprett_tilkobling()

    # Opprett en tabell i databasen
    opprett_tabell(conn)

    # Last inn CSV-filen i en pandas DataFrame
    df = last_inn_csv('randoms.csv')

    # Sett inn data fra DataFrame i SQLite-tabellen
    sett_inn_data(conn, df)

    # Lukk tilkoblingen til SQLite-databasen
    conn.close()

def opprett_tilkobling():
    # Opprett en tilkobling til SQLite-databasen
    conn = sqlite3.connect('database.db')
    # Returner tilkoblingsobjektet
    return conn

def opprett_tabell(conn):
    # Opprett en ny cursor
    cursor = conn.cursor()
    # Utfør SQL-kommandoen for å opprette en ny tabell
    cursor.execute("""
        CREATE TABLE tabell (
            fname TEXT,  -- Fornavn
            ename TEXT,  -- Etternavn
            epost TEXT,  -- E-postadresse
            tlf TEXT,    -- Telefonnummer
            postnr TEXT  -- Postnummer
        )
    """)
    # Lagre endringene
    conn.commit()

def last_inn_csv(filnavn):
    # Last inn CSV-filen i en pandas DataFrame
    df = pd.read_csv(filnavn)
    # Returner DataFrame
    return df

def sett_inn_data(conn, df):
    # Sett inn data fra DataFrame i SQLite-tabellen
    df.to_sql('tabell', conn, if_exists='append', index=False)

# Kjør hovedfunksjonen
if __name__ == "__main__":
    main()