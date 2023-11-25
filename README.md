
# Haalarimerkki-inventaariosovellus

Sovelluksella käyttäjä voi pitää kirjaa haalarimerkkien myynnistä ja saatavuudesta. Sovellus on tarkoitettu merkkien myyjän käytettäväksi. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

## Sovelluksen ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan kaikista saatavilla olevista merkeistä ja niiden määrän.
- Käyttäjä voi luoda uusia haalarimerkkejä.
- Käyttäjä voi lisätä jo olemassa olevan haalarimerkin määrää.
- Käyttäjä voi muokata luomansa merkin hintaa, nimeä, suunnittelijaa, tilauspaikkaa, (ehkä kuvaa). Käyttäjä voi myös poistaa merkin.
- Käyttäjä voi etsiä merkkejä nimen perusteella.
- Käyttäjä voi rajata merkkejä eri suodattimilla kuten hinta, tilauspaikka, suunnittelija.
- Ylläpitäjä voi muokata ja poistaa tietokantoja / käyttäjiä.
- Ylläpitäjä voi luoda salaisen tietokannan ja määrittää, keillä käyttäjillä on pääsy alueelle.
- Merkkien myyntihistoria. (Mahdollisuus poistaa merkkejä ja "myydä" merkkejä)

### Jatkokehitys?
- Hintahistoria


## Sovelluksen asennus

Kloonaa tai lataa tämä repositio koneellesi esim komennolla:

```bash
git clone https://github.com/t0ffe/tkt-tsoha.git
```


Asenna riippuvuudet komennolla:

```bash
pip install -r requirements.txt
```

## Käyttö

Aloita sovellus komennolla:

```bash
flask run
```

Sovellus on käytettävissä oletusarvoisesti selaimella osositteessa [http://127.0.0.1:5000](http://127.0.0.1:5000)
