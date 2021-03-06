from pyplasm import *

#funzione generale che costruisce la curva
def bez_curve(controlpoints):
	return MAP(BEZIER(S1)(controlpoints))(dom1D)

# cubic cardinal con h modificato
def CUBICCARDINAL (domain,h=0.1):
	def CUBICCARDINAL0(args):
		q1_fn , q2_fn , q3_fn , q4_fn = args
		def map_fn(point):
			u=S1(point)
			u2=u*u
			u3=u2*u
			q1,q2,q3,q4=[f(point) if callable(f) else f for f in [q1_fn,q2_fn,q3_fn,q4_fn]]
			
			ret=[0.0 for i in range(len(q1))]	
			for i in range(len(ret)):
				ret[i]=(-h*u3+2*h*u2-h*u)*q1[i] +((2-h)*u3+(h-3)*u2+1)*q2[i] + ((h-2)*u3+(3-2*h)*u2+h*u)*q3[i] + (h*u3-h*u2)*q4[i]

			return ret
		return MAP(map_fn)(domain)
	return CUBICCARDINAL0

#domini 
#dom1D = GRID([10])
#dom2D = GRID([20,20])
dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D, dom1D])

#generalizzazione per la creazione di superfici
def bez_sup(curves):
	return MAP(BEZIER(S2)(curves))(dom2D)


##scheletro destro
C1dx1 = bez_curve([[0.48, 3.11,0], [0.7, 3.05,0], [0.82, 3.07,0], [1.07, 2.99,0]])

C1dx2 = bez_curve([[2.35, 2.94,0], [2.69, 4.13,0], [0.9, 4.42,0], [1.07, 2.99,0]])

C1dx3 = bez_curve([[2.35, 2.94,0], [3.78, 2.91,0], [4.33, 2.9,0], [5.51, 2.92,0]])

C1dx4 = bez_curve([[6.75, 2.89,0], [7.04, 3.92,0], [5.51, 4.32,0], [5.51, 2.92,0]])

C1dx5 = bez_curve([[6.75, 2.89,0], [8.06, 2.87,0], [7.21, 2.88,0], [8.27, 2.87,0]])

C1dx6  = SPLINE(CUBICCARDINAL(dom1D))([[8.28,2.85,0],[8.28,2.85,0],[8.3, 3.24,0],[6.2, 3.97,0],[6.2, 3.97,0]])

C1dx7 = POLYLINE([[3.53,4.01,-0.2],[5.41,3.97,-0.15]])

C1dx8 = POLYLINE([[3.53,4.01,-0.2],[0.39, 3.97,0]])

C1dx10 = bez_curve([[0.48, 3.11,0], [0.43, 3.72,0], [0.39, 3.59,0], [0.39, 3.97,0]])

C1dx11 = bez_curve([[0.39, 3.97,0], [1.29, 4.06,0], [0.98, 4.07,0], [6.2,3.97,0]])

scocca_lato_dx = STRUCT([C1dx1, C1dx2, C1dx3, C1dx4, C1dx5, C1dx6, C1dx7, C1dx8,C1dx10, C1dx11])


##scheletro sinistro

C1sx1 = bez_curve([[0.48, 3.11,-3], [0.7, 3.05,-3], [0.82, 3.07,-3], [1.07, 2.99,-3]])

C1sx2 = bez_curve([[2.35, 2.94,-3], [2.69, 4.13,-3], [0.9, 4.42,-3], [1.07, 2.99,-3]])

C1sx3 = bez_curve([[2.35, 2.94,-3], [3.78, 2.91,-3], [4.33, 2.9,-3], [5.51, 2.92,-3]])

C1sx4 = bez_curve([[6.75, 2.89,-3], [7.04, 3.92,-3], [5.51, 4.32,-3], [5.51, 2.92,-3]])

C1sx5 = bez_curve([[6.75, 2.89,-3], [8.06, 2.87,-3], [7.21, 2.88,-3], [8.27, 2.87,-3]])

C1sx6  = SPLINE(CUBICCARDINAL(dom1D))([[8.28,2.85,-3],[8.28,2.85,-3],[8.3, 3.24,-3],[6.2, 3.97,-3],[6.2, 3.97,-3]])

C1sx7 = POLYLINE([[3.53,4.01,-3+0.2],[5.5,3.97,-3+0.15]])

C1sx8 = POLYLINE([[3.53,4.01,-3+0.2],[0.39, 3.97,-3]])

C1sx10 = bez_curve([[0.48, 3.11,-3], [0.43, 3.72,-3], [0.39, 3.59,-3], [0.39, 3.97,-3]])

C1sx11 = bez_curve([[0.39, 3.97,-3], [1.29, 4.06,-3], [0.98, 4.07,-3], [6.2,3.97,-3]])

scocca_lato_sx = STRUCT([C1sx1, C1sx2, C1sx3, C1sx4, C1sx5, C1sx6, C1sx7, C1sx8, C1sx10, C1sx11])

##scheletro anteriore

C1an1 = bez_curve([[8.27, 2.87,0],[8.7,2.87,-1.5],[8.7,2.87,-1.5],[8.27, 2.87,-3]])

C1an2 = bez_curve([[8.27, 3.24,0],[8.7,3.24,-1.5],[8.7,3.24,-1.5],[8.27, 3.24,-3]])

C1an3 = SPLINE(CUBICCARDINAL(dom1D))([[5.51,3.97,0],[5.51,3.97,0],[5.41,3.97,-0.15],[4.5,4.6,-0.3],[4.5,4.6,-3+0.3],[5.51,3.97,-3+0.15],[5.41,3.97,-3],[5.41,3.97,-3]])

C1an4 = SPLINE(CUBICCARDINAL(dom1D))([[5.41,3.97,-0.15],[5.41,3.97,-0.15],[8.5,3.24,-1.5+0.15],[8.5,3.24,-1.5-0.15],[5.51,3.97,-3+0.15],[5.51,3.97,-3+0.15]])

C1an5 = bez_curve([[5.41,3.97,-0.15],[6,3.97,-0.15],[6,3.97,-3+0.15],[5.51,3.97,-3+0.15]])
scocca_ant = STRUCT([C1an1, C1an2, C1an3,C1an4,C1an5])

##scheletro tetto

C1te1 = SPLINE(CUBICCARDINAL(dom1D))([[3.53,4.01,0],[3.53,4.01,0],[3.53,4.01,-0.2],[3.5,4.6,-0.4],[3.5,4.6,-3+0.2+0.2], [3.53,4.01,-3+0.2],[3.53,4.01,-3+0.2],[3.53,4.01,-3],[3.53,4.01,-3]])

C1te2 = POLYLINE([[3.5,4.6,-3+0.2+0.2],[4.5,4.6,-3+0.3]])

C1te3 = POLYLINE([[3.5,4.6,-0.2-0.2],[4.5,4.6,-0.3]])

scocca_tetto = STRUCT([C1te1,C1te2,C1te3])

##scheletro posteriore

C1pos1 = SPLINE(CUBICCARDINAL(dom1D))([[3.5,4.6,-3+0.2+0.2],[3.5,4.6,-3+0.2+0.2],[0.39, 3.97,-3],[0.39, 3.97,-3]])

C1pos2 = SPLINE(CUBICCARDINAL(dom1D))([[3.5,4.6,-0.2-0.2],[3.5,4.6,-0.2-0.2],[0.39, 3.97,0],[0.39, 3.97,0]])

C1pos3 = bez_curve([[1.55,3.97,-0.9],[1,3.97,-0.9],[1,3.97,-3+0.9],[1.55,3.97,-3+0.9]])

C1pos4 = POLYLINE([[1.55,3.97,-0.9],[3.5,4.6,-0.2-0.2]])

C1pos5 = POLYLINE([[1.55,3.97,-3+0.9],[3.5,4.6,-3+0.2+0.2]])

C1pos6 = SPLINE(CUBICCARDINAL(dom1D))([[0.48, 3.11,0],[0.48, 3.11,0],[0.48, 3.11,-0.2],[0.48, 3.4,-0.2], [0.48, 3.4,-3+0.2],[0.48, 3.11,-3+0.2],[0.48, 3.11,-3],[0.48, 3.11,-3]])

C1pos7 = SPLINE(CUBICCARDINAL(dom1D))([[0.39, 3.97,0],[0.39, 3.97,0],[0.39, 3.97,-1.5],[0.39, 3.97,-3],[0.39, 3.97,-3]])

C1pos8 = POLYLINE([[1.55,3.97,-0.9],[0.39,3.97,0]])

C1pos9 = POLYLINE([[1.55,3.97,-3+0.9], [0.39,3.97,-3]])

scocca_post = STRUCT([C1pos1, C1pos2, C1pos3, C1pos4, C1pos5, C1pos6, C1pos7,C1pos8, C1pos9])

scocca0 = STRUCT([scocca_lato_dx, scocca_lato_sx, scocca_ant, scocca_tetto, scocca_post])

# funzione che centra nel centro la struttura
centroide = T([1,2,3])([-SIZE([1])(scocca0)[0]/2, -SIZE([2])(scocca0)[0]/2-1.9, SIZE([3])(scocca0)[0]/2])

scocca = centroide(scocca0)

VIEW(scocca)



