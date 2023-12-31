
# Haalarimerkki-inventaariosovellus

Sovelluksella käyttäjä voi pitää kirjaa haalarimerkkien myynnistä ja saatavuudesta. Sovellus on tarkoitettu merkkien myyjän käytettäväksi. Jokainen käyttäjä on Myyjä tai Asiakas.

## Sovelluksen ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan kaikista saatavilla olevista merkeistä ja niiden määrän.
- Käyttäjä voi luoda uusia haalarimerkkejä.
- Käyttäjä voi lisätä jo olemassa olevan haalarimerkin määrää.
- Käyttäjä voi muokata luomansa merkin hintaa, nimeä.
- Käyttäjä voi poistaa merkin.


### Jatkokehitys?
- Käyttäjä voi etsiä merkkejä nimen perusteella.
- Käyttäjä voi rajata merkkejä eri suodattimilla kuten hinta, tilauspaikka, suunnittelija.
- Ylläpitäjä voi muokata ja poistaa tietokantoja / käyttäjiä.
- Ylläpitäjä voi luoda salaisen tietokannan ja määrittää, keillä käyttäjillä on pääsy alueelle.
- Merkkien myyntihistoria. (Mahdollisuus poistaa merkkejä ja "myydä" merkkejä)
-Käyttäjä voi muokata luomansa merkin suunnittelijaa, tilauspaikkaa, (ehkä kuvaa).
- Hintahistoria


## Sovelluksen asennus

1. Kloonaa tämä repositio koneellesi esim komennolla:

```bash
git clone https://github.com/t0ffe/tkt-tsoha.git
```

2. Mene juurihakemistoon ja aja:

```bash
echo -e "DATABASE_URL=postgresql+psycopg2://\nSECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(16))')" > .env
```
se luo `.env` tiedoston ja asettaa sinne ympäristömuuttujat `DATABASE_URL` ja `SECRET_KEY`. 
###### Jos tietokantayhteys ei toimi saatat joutua muokkaamaan `DATABASE_URL`:in arvoa. Voit kokeilla `postgresql:///user` 

3. Aktivoi virtuaaliympäristö komennnoilla:

```bash
python3 -m venv venv
source venv/bin/activate
```

ja asenna riippuvuudet komennolla:

```bash
pip install -r requirements.txt
```
4. Asenna PostgreSQL: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

5. Määritä tietokannan skeema komennolla:

```bash
psql -f schema.sql
```
Schema:
![schema.png](schema.png "Tietokanta jonka yllä oleva schema luo")


## Käyttö

Aloita sovellus komennolla:

```bash
flask run
```

Sovellus on käytettävissä oletusarvoisesti selaimella osoitteessa [http://127.0.0.1:5000](http://127.0.0.1:5000)
