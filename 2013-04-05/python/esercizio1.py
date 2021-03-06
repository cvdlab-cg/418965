## Esercizio1 in python

#pilastri del primo piano

cilindro = T([1,2])([0.25,0.25])(CYLINDER([0.25,2.36+0.14])(36))

cilindri_riga  = STRUCT(NN(5)([cilindro,T([1])([0.5+4.7])]))
cilindri_sup = T([2,3])([0.5+9.1,0.14])(cilindro)
cilindri = STRUCT([cilindri_riga,cilindri_sup])

pil = CUBOID([0.5,0.5,2.36])

pila1 = T([1,2,3])([0.5+2.2,0.5+9.1,0.14])(pil)
pila_riga = T([2,3])([9.6,0.14])(STRUCT(NN(3)([T([1])([0.5+4.7]),pil])))
pile = STRUCT([pila1,pila_riga])

pillars0 = STRUCT([cilindri,pile])

#pilastri del secondo piano

pile_sup = STRUCT(NN(5)([pil,T([1])([5.2])]))
pile_sup2 = T([2])([9.6])(STRUCT(NN(3)([pil,T([1])([5.2])])))
cil_sup  = T([1,2])([0.5+4.7+0.5+4.7+0.5+4.7,0.5+9.1])(cilindro)
pila2 = T([1,2])([0.5+4.7+0.5+4.7+0.5+4.7+0.5+4.7,0.5+9.1])(pil)

mini_pilastro = S([1,2])([0.5,0.5])(pil)
mini_pil = T([1,2])([0.5+0.9,0.5+9.1])(mini_pilastro )

pillars1 = T([3])([0.14+2.36+0.14])(STRUCT([pile_sup,pile_sup2 ,cil_sup ,pila2, mini_pil]))


#pilastri del terzo piano

pile3 = T([2,3])([0.5+9.1,0.14+((2.36+0.14)*2)])(pile_sup)
pile31 = STRUCT([T([3])([0.14+((2.36+0.14)*2)]),pil,T([1])([0.5+4.7]),pil,T([1])([0.5+4.7+0.5+4.7+0.5+4.7]),pil])
pillars2 = STRUCT([pile3, pile31])



#pilastri del quarto piano

mini_pilastro4 = T([2,3])([0.5+9.1+0.25,0.14+((2.36+0.14)*3)])(mini_pilastro)
mini_pilastro42 = T([1,2,3])([0.5+4.7,0.5+9.1+0.25,0.14+((2.36+0.14)*3)])(mini_pilastro)
pila4 = STRUCT([T([1,2,3])([0.5+4.7+0.5+4.7,0.5+9.1,0.14+((2.36+0.14)*3)]),pil,T([1])([0.5+4.7]),pil,T([1])([0.5+4.7]),pil])
pila42 = STRUCT([T([1,3])([0.5+4.7+0.5+4.7,0.14+((2.36+0.14)*3)]),pil,T([1])([0.5+4.7+0.5+4.7]),pil])
pillars3 = STRUCT([mini_pilastro4, mini_pilastro42, pila4 ,pila42])

#struttura completa dell'esercizio1
pillars_total = STRUCT([pillars0,pillars1,pillars2,pillars3])
