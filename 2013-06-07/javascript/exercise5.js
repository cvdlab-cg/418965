var domain = DOMAIN([[0,20],[0,21]])([80,80])

var domain_home = DOMAIN([[-3.6,0],[0,21]])([10,10]) 

var height  = function(dominio){
		var x = dominio[0];
		var y = dominio[1];
		var z = SIN(x*y)*COS(x*y);

		//parte semi pianeggiante + parte montuosa
		if(x<= 10) dz = x*y*Math.random()/500; 
		else dz = x*y*Math.random()/100;
		return [x, y, dz+z];
}

var model = COLOR([139/255,69/255,19/255])(STRUCT([MAP(height)(domain), domain_home]))

var lake1 = T([0,1])([2*PI,6*PI])(DISK(PI/2)([12,1]))

var lake2 = T([0,1])([2*PI,2*PI])(DISK(PI)([12,1]))

var lake = STRUCT([COLOR([0,180,120]), EXTRUDE([0.5]), lake2, lake1])

//funzione di supporto -> circonferenza con bezier
var cerchio = function(r, h){
			var cerchio0 = function(v){
			return [r*COS(v[0]), r*SIN(v[0]), h];
			}
		return cerchio0;
	}

var cono = function(r, h1, h2){
		function cono0(l){
			var domain_cono = PROD1x1([INTERVALS(2*PI)(l[0]), INTERVALS(1)(l[1])]);
			var c = cerchio(r, h1);
			var base = T([2])([h1])(DISK(r)([12,12]));
			var s = MAP(BEZIER(S1)([c, [0, 0, h1+h2]]))(domain_cono);
			return STRUCT([s, base]);
			}
		return cono0;
	}

var trunk = function(r, h, d){
		var c = CYL_SURFACE([r,h])([d,1]);
		var d1 = DISK([r])([d,1]);
		var d2 = T([2])([h])(DISK([r])([d,1]));
		return STRUCT([c,d1,d2])
	}


var albero =  function(r1,h1,h2,r2){

		var tronco = COLOR([60/255,30/255,10/255])(trunk(r1,h1,12))
		var corpo = COLOR([0,130/255,0])(cono(r2,h1,h2)([12,1]))
		var albero0 = STRUCT([tronco, corpo])
		return STRUCT([S([0,1,2])([0.05,0.05,0.05])(albero0)])
	}


var forest = function (subset){

		var array = [];
		var xi = subset[0]; //con xi<xf
		var xf = subset[1];
		var yi = subset[2]; //con yi<yf
		var yf = subset[3];

		for (var i=xi; i<= xf; i+=0.25){
			for (var j=yi; j<= yf; j+=0.25){

			var r1 = 1*(Math.random()+1)
			var h1 = 3*(Math.random()+1)
			var h2 = 5*(Math.random()+1)
			var r2 = 2*(Math.random()+1)
			array = array.concat(T([0,1,2])([i,j,((SIN(i*j)*COS(i*j))+(i*j/100))])(T([0,1])([0.05,0.05])(albero(r1,h1,h2,r2))))
			
			}
		}

		return STRUCT(array.slice(0));
}

var f = forest([0,1,0,1]);

var f2 = forest([0,1,4*PI-1,4*PI+1]);

var forests = STRUCT([f,f2]);

var settlement = function(subset){

		var array = [];
		var xi = subset[0]; //con xi<xf
		var xf = subset[1];
		var yi = subset[2]; //con yi<yf
		var yf = subset[3];


		for (var i=xi; i<= xf; i++){
			for (var j=yi; j<= yf; j++){

			var x = 0.25*(Math.random()+1)
			var y = 0.4*(Math.random()+0.5)
			var z = 0.35*(Math.random()+1)
			array = array.concat(T([0,1])([i-x-0.1,j+0.05])(CUBOID([x,y,z])))
			}
		}
			return STRUCT(array.slice(0));
	}

var complex_home1 = settlement([-3,0,0.1,7]);

var complex_home2 = settlement([-3,0,14,20]);

var complex_home = COLOR([255,0,0])(STRUCT([complex_home1,complex_home2]))

DRAW(model)

DRAW(lake)

DRAW(forests)

DRAW(complex_home)

//strade

var orizzontal = function (xi, xf) {
	
	var array = [];

	for (i=xi; i<=xf; i+=1.1){
		array = array.concat(T([0])([i])(CUBOID([0.25,8,0.001])))
	}
	return STRUCT(array.slice(0));

}

var street_orizontal = orizzontal(-3.05,-0.8)

	
var vertical = function (yi,yf){
	var array = [];
	for (i=yi; i<=yf; i+=1.05){
		array = array.concat(T([0,1])([-3.5,i])(CUBOID([3.4,0.125,0.001])))
	}
	return STRUCT(array.slice(0));
}

var street_vertical = vertical(0.7,8)

var street1 = COLOR([0,0,0])(STRUCT([street_vertical,street_orizontal]))

var street_con = COLOR([0,0,0])(T([1])([5])(street_orizontal))

var street = STRUCT([street1, T([1])([13])(street1), street_con])

DRAW(street)

