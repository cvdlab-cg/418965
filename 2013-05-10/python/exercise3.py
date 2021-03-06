
cerchione = DIFF([CYLINDER([0.45,0.2])(100),CYLINDER([0.35,0.2])(100)])

gomma = S([3])([1.5])(TORUS([0.6,0.4])([36,36]))

raggio = CUBOID([0.01,0.35,0.01])

raggi = STRUCT(NN(20)([raggio, ROTN([PI/10,[0,0,1]])]))

ruotadx = STRUCT([cerchione, T(3)(0.2-0.005)(raggi), T([3])([0.1])(COLOR(BLACK)(gomma))])

ruotasx = STRUCT([cerchione, T(3)(-0.005)(raggi), T([3])([0.1])(COLOR(BLACK)(gomma))])

ruota11 = T([1,2,3])([1.73,3.26,-0.1])(ruotadx) 

# funzione composta per traslare e dimensionare le ruote anteriori
pos = COMP([S([1,2])([0.95,0.95]),T([1,2])([4.75,0.1])])

ruota12 = pos(ruota11)

ruota21 = T([1,2,3])([1.73,3.26,-0.1-3])(ruotasx)

ruota22 = pos(ruota21)

ruote0 = STRUCT([ruota11, ruota12, ruota21, ruota22])

ruote = T([1,2,3])([-4.1,-2.8,1.5])(ruote0)

VIEW(STRUCT([ruote,scocca]))



