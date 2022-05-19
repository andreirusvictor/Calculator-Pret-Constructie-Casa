# variabile introduse de catre utilizator:
st
tmp
su

# variabile stocate intr-o baza de date:
reg_h
fin
arh
st_topo
geo
com_ag
cu_avz
st_geo
topo
ie
isan
it



def suprafata_construita():
    sc = su * 1.2
    return sc


def cost_teren():
    cost_tr = st * tmp
    return cost_tr


def cost_proiect_arhitectura():
    pr_arh = sc * arh
    return pr_arh


def cost_casa_la_rosu():
    casa_rosu = sc * arh + reg_h
    return casa_rosu

def cost_casa_la_cheie():
    casa_la_cheie = sc * (arh + reg_h + fin)
    return casa_la_cheie

def cu_avize():
    return cu_avz

def cost_studiu_geotehnic():
    return st_geo

def cost_ridicare_topo():
    return topo

def cost_ac():
    ac = casa_cheie * 0.05
    return ac

def cost_instalatii_electrice():
    cost_ie = sc x ie
    return cost_ie


def cost_instalatii_sanitare():
    cost_is = sc x isan
    return cost_is

def cost_instalatii_termice():
    cost_it = sc x it
    return cost_it

def valoare_comision_agentie():
    val_ag = com_ag / 100 * cost_tr
    return val_ag

def cost_verificare_topo():
    return st_topo

def cost_notar():
    cost_notar = cost_tr / 100
    return cost_notar

def cost_aviz_geotehnic():
    return geo

def cost_total():
    cost_total = cost_tr + pr_arh + casa_cheie + cu_avz + st_geo _ topo + ac + ut_curent + ut_gaz + ut_ac + val_ag + cost_st_topo + cost_notar + cost_aviz_gt
    return cost_total

