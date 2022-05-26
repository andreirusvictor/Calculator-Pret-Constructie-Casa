from flask import Flask, render_template, request
import psycopg2


app = Flask('calculator')


# Ia din baza de date toate intrariile din tabela pentru tabela specificata
def select(cursor, tabela):
    cursor.execute(f'SELECT * FROM {tabela};')

    # fetchall returneaza o lista de intrari, de exemplu pentru tabela (ID, DESCRIERE, VALOARE)
    # returneaza (1, 'Arhitectura simpla', 200), asa ca le convertim la un dictionar
    # pentru a intelege ce inseamna fiecare valoare
    rows = cursor.fetchall()

    rezultat = list()
    for row in rows:
        rezultat.append(
            dict(id=row[0], descriere=row[1], valoare=row[2])
        )

    return rezultat

# aducem valorile completate in campurile formularului si le pasam variabilelor definite pentru efectuarea calculelor:
def costuri():
    st = int(request.form.get('suprafata_teren'))
    tmp = int(request.form.get('pret_teren'))
    su = int(request.form.get('suprafata_casa'))

    reg_h = int(request.form.get('regim_inaltime'))
    fin = int(request.form.get('nivel_finisare'))
    arh = int(request.form.get('arhitectura'))
    st_topo = int(request.form.get('verificare_topografica'))
    geo = int(request.form.get('verificare_geologica'))
    com_ag = float(request.form.get('comision'))

    sc = su * 1.2
    cost_tr = st * tmp
    pr_arh = sc * arh
    casa_rosu = sc * arh + reg_h
    casa_cheie = sc * (arh + reg_h + fin)

    cu_avz = 400
    st_geo = 200
    topo = 400

    ac = casa_cheie * 0.05

    ut_curent = 1200
    ut_gaz = 1200
    ut_ac = 600

    cost_ie = sc * 16
    cost_is = sc * 33
    cost_it = sc * 22

    val_ag = com_ag / 100 * cost_tr

    cost_notar = cost_tr / 100

    cost_total = cost_tr + pr_arh + casa_cheie + cu_avz + st_geo + topo + ac + ut_curent + ut_gaz + ut_ac + st_topo + cost_notar + geo

    return [
        dict(descriere="Suprafata construita", valoare=sc),
        dict(descriere="Cost teren", valoare=cost_tr),
        dict(descriere="Cost proiect arhitectura", valoare=pr_arh),
        dict(descriere="Cost construire casa la rosu", valoare=casa_rosu),
        dict(descriere="Cost construire casa la cheie", valoare=casa_cheie),
        dict(descriere="Cost certificat urbanism + avize", valoare=cu_avz),
        dict(descriere="Cost studio geotehnic", valoare=st_geo),
        dict(descriere="Cost ridicare topografica", valoare=topo),
        dict(descriere="Cost autorizatie de constructie", valoare=ac),
        dict(descriere="Cost utilitati curent", valoare=ut_curent),
        dict(descriere="Cost utilitati gaz", valoare=ut_gaz),
        dict(descriere="Cost utilitati apa/canal", valoare=ut_ac),
        dict(descriere="Cost instalatii electrice", valoare=cost_ie),
        dict(descriere="Cost instalatii sanitare", valoare=cost_is),
        dict(descriere="Cost instalatii termice", valoare=cost_it),
        dict(descriere="Valoare comision agentie", valoare=val_ag),
        dict(descriere="Cost topograf verificare teren", valoare=st_topo),
        dict(descriere="Cost notariale cumparare teren", valoare=cost_notar),
        dict(descriere="Cost aviz geotehnic preliminar", valoare=geo),
        dict(descriere="Cost total", valoare=cost_total),
    ]


@app.route('/')
def first_page():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres",

    )
    cursor = conn.cursor()

    return render_template(
        'first_page.html',
        title='Formular de calcul',

        # Trimitem variabilele necesare randarii template-ului, selectand toate datele
        # necesare calculului, din toate tabelele existente
        regimuri_inaltime=select(cursor, 'regim_inaltime'),
        niveluri_finisare=select(cursor, 'nivel_finisare'),
        niveluri_arhitectura=select(cursor, 'nivel_arhitectura'),
        verificare_topografica=select(cursor, 'verificare_topografica'),
        verificare_geologica=select(cursor, 'verificare_geologica'),
        comision_agentie=select(cursor, 'comision_agentie'),
    )


@app.route('/second_page/', methods=('POST',))
def second_page():

    # Functia costuri returneaza o lista cu toate costurile necesare construite casei,
    # in forma (descriere="Tipul costului", valoare="Valoarea costului". Trimitem aceasta lista
    # template-ului, pentru a le afisa.
    return render_template(
        'second_page.html',
        valori=costuri()
    )


if __name__ == '__main__':
    app.run(debug=True)