#ESERCIZIO4



#finestra colorata
wind1 = COLOR(GREEN)(R([2,3])(PI/2)(CUBOID([10.15,1.5,0.25])))

wind1T = T([1,2,3])([0.25,0.25,8.14])(wind1)

wind2 = COLOR(BLACK)(R([2,3])(PI/2)(CUBOID([4.7,1.5,0.25])))

wind21 = T([1,2,3])([10.9,0.25,2.5+0.5])(wind2)
wind22 = T([3])([2.5+0.14])(wind21)
wind23 = T([3])([2.5])(wind22)

windows = STRUCT([wind1T,wind21,wind22,wind23])

#prova di finestre colorate
#VIEW(windows)

#prova totale
#build = STRUCT([pillars_total, floors, vert_partitions, windows])
#VIEW(build)

