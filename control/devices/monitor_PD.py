from sys import argv

m = 0.001658
c = -2.202

def V2P(V, m= 0.001658, c= -2.202):
	return (V-c)/m

def P2V(P, m= 0.001658, c= -2.202):
	return m*P+c

if __name__ == "__main__":
	V = float(argv[1])
	print("{} V PD signal corresponds to {:.5g} mW EDFA power".format(V, V2P(V)))
