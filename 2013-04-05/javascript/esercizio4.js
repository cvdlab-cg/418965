
//esercizio4

//finestra colorata di rosso
var wind1 = COLOR([10,0,0])(R([1,2])(PI/2)(CUBOID([10.15,1.5,0.25])))

var wind1T = T([0,1,2])([0.25,0.25,8.14])(wind1)

var wind2 = COLOR([0,0,0])(R([1,2])(PI/2)(CUBOID([4.7,1.5,0.25])))

var wind21 = T([0,1,2])([10.9,0.25,2.5+0.5])(wind2)
var wind22 = T([2])([2.5+0.14])(wind21)
var wind23 = T([2])([2.5])(wind22)

var windows = STRUCT([wind1T,wind21,wind22,wind23])

//prova di finestre colorate
//DRAW(windows)

//prova totale
//var build = STRUCT([pillars_total, floors, vert_partitions, east_color])
//DRAW(build)


