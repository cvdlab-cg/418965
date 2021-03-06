##esercizio2.py

#definizione della funzione GRID
GRID = COMP([INSR(PROD),AA(QUOTE)])

#pavimento del primo piano -> floor0

sector01 = GRID([[0.5+2.2+0.5],[-0.5-9.1,0.5+1.8+0.5],[0.14]])
sector02 = GRID([[-0.5-2.2,0.5+2+0.5+4.7+0.5+4.7+0.5],[-0.5-3.6,1.7+1.5+0.5+1.8+0.5+1.8+0.5],[0.14]])
sector03 = GRID([[-0.5-2.2-0.5-2-0.5-4.7-0.5-4.7-0.5,0.6],[-0.5-3.6-1.7,1.5],[0.14]])
sector04 = GRID([[-0.5-2.2-0.5-2-0.5-4.7-0.5-4.7-0.5,1.9],[-0.5-3.6-1.7-1.5,0.5+1.8+0.5+1.8+0.5],[0.14]])
sector05 = GRID([[-0.5-2.2,0.5+1.2+0.5],[-0.5-3.6+0.7,0.7],[0.14]])
#settori circolari del pavimento
sector06 = T([1,2])([0.5+2.2+0.5+2+0.5+4.7+0.5+4.7+0.5+1.9,-2.55+0.5+9.1+0.5+1.8+0.5])(CYLINDER([2.55,0.14])(36))
sector07 = T([1,2])([-1.1+0.5+2.2+0.5+1.2+0.5,0.5+3.6-0.7])(CYLINDER([1.1,0.14])(36))

floor0 = STRUCT([sector01,sector02,sector03,sector04,sector05,sector06,sector07])

# pavimento del secondo piano -> floor1

sector11 = GRID([[0.25,-0.25-0.9,1.3+0.5+2+((0.5+4.7)*3)+0.5],[-0.5,9.1],[0.14]])
sector12 = GRID([[0.5+1.7+0.5+0.5+2+0.5,-4.7-0.5-0.5,4.2+0.5+4.7+0.5],[-0.5-9.1-0.25-0.25,1.8],[0.14]])
sector13 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1-0.25-0.25-1.8,+0.5],[0.14]])
sector14 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1,0.5],[0.14]])
sector15 = GRID([[((0.5+4.7)*4)+0.5],[0.5],[0.14]])

balcone = T([1,2])([-2.2,0.5+9.1+0.3])(CUBOID([2.2,2,0.14]))

floor1 = T([3])([2.36+0.14])(STRUCT([sector11,sector12,sector13, sector14, sector15, balcone]))

# pavimento del terzo piano -> floor2

sector21 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1-0.5-1.8,0.5],[0.14]])
sector22 = GRID([[0.5,-2.2-0.5-2-0.5-3.3,1.4+0.5+4.7+0.5+4.7+0.5],[-0.5-9.1-0.25,0.25+1.8],[0.14]])
sector23 = GRID([[0.5+0.9+0.25,-1.05-0.5-2,0.5],[-0.5-9.1,0.25],[0.14]])
sector24 = GRID([[0.5,-0.9,1.3+0.5+2+0.5+4.7+0.5+4.7+0.5+4.7+0.5],[-0.5-9.1-0.25,0.25],[0.14]])

#perimetro e Q del pavimento poligonale
poligono = MKPOL([[[10.4,0.5],[10.4+0.5+4.7+0.5+4.7+0.5,0.5],[10.4+0.5+4.7+0.5+4.7+0.5,0.5+9.1+0.25],[10.4-1.9,0.5+9.1+0.25]],[[1,2,3,4]],None])
sector25 = PROD([poligono,Q(0.14)])

sector26 = GRID([[((0.5+4.7)*4)+0.5],[+0.5],[0.14]])
sector27 = GRID([[0.25],[-0.5,9.1],[0.14]])

floor2 = T([3])([(2.36+0.14)*2])(STRUCT([sector21,sector22,sector23,sector24,sector25,sector26,sector27]))

# pavimento del quarto piano -> floor3

sector31 = GRID([[((0.5+4.7)*4)+0.5],[0.5+9.1+0.25+0.25],[0.14]])
sector32 = GRID([[0.5+1.7+0.5+0.5+2+0.5+4.7+0.5,-4.7-0.5-0.5,+4.2+0.5],[-0.5-9.1-0.25,0.25+1.8],[0.14]])
sector33 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1-0.25-0.25-1.8,+0.5],[0.14]])

floor3 = T([3])([(2.36+0.14)*3])(STRUCT([sector31,sector32,sector33]))

# pavimento del quinto piano -> floor4

sector41 = GRID([[((0.5+4.7)*4)+0.5],[0.5],[0.14]])
sector42 = GRID([[0.5,-4.7-0.5-4.7,((0.5+4.7)*2)+0.5],[-0.5,+9.1],[0.14]])
sector43 = GRID([[((0.5+4.7)*4)+0.5],[-0.5-9.1,0.5+1.8+0.5],[0.14]])

floor4 = T([3])([(2.36+0.14)*4])(STRUCT([sector41,sector42,sector43]))


#pavimento completo
floors = STRUCT([floor0,floor1,floor2,floor3,floor4])


#prova di VIEW dell'edificio parziale (esercizio1+esercizio2)
#build = STRUCT([floors, pillars_total])
#VIEW(build)











