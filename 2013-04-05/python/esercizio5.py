
#ESERCIZIO5
#gradino in 2 dimensioni
step2d = MKPOL([[[0,0],[0.54,0.36],[0.54,0.72],[0,0.72]],[[1,2,3,4]],None])


#gradino singolo in 3 dimensioni
step3d = MAP([S1,S3,S2])(PROD([step2d, Q(2)]))

#rampa di scale
ramp = STRUCT(NN(13/2)([step3d, T([1,3])([0.54,0.54-0.18])]))
ramp1 = S([2])([-0.5])(ramp)
#prova rampa
#VIEW(ramp)

stair1 = T([])([])(ramp)

stair2 = T([])([])(ramp)

stair3 = T([])([])(ramp)
