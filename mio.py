#import requests
import	json


data={}

with open("./mi.json") as file:
	data = json.load(file)

thislist=[]
dicfinal={}

for xd in data["response"]:
	thisdict = {}
	thisdict["id"]=	xd["id"]
	thisdict["success_nodes"]= xd["success_nodes"]
	#thisdict["name"]=xd["summary_fields"]["unified_job_template"]["name"]
	thisdict["posicion"] = xd["posicion"]
	#thislist["lista_padres"] = []
	thislist.append(thisdict)
dicfinal["response"]= thislist
#print(json.dumps(dicfinal, indent=4))

#Lista de Hijos 
listaHijos = [item["id"]for item in dicfinal["response"] if len(item["success_nodes"])==0 ]

#print(listaHijos)

#for i in dicfinal:
#	for j in i["success_nodes"]:
lista_nodos = dicfinal["response"]
print(dicfinal["response"][0]["id"]) # dicfinal["response"] lista de diccionarios
node_set = set()
node_hijos_set = set()
nodes_ids = {node["id"] for node in dicfinal["response"]}
#nodos_hijos = [node_hijos_set.add(node["success_nodes"]) for node in dicfinal["response"]]
for i in lista_nodos:
	for j in i["success_nodes"]:
		node_hijos_set.add(j)


print(nodes_ids)
print(node_hijos_set)
id_nodo_padre = nodes_ids - node_hijos_set
print("Soy el padre", id_nodo_padre)


#hijos_padres = [nodo["success_nodes"] for nodo in lista_nodos if nodo["id"]==list(id_nodo_padre)[0]] 
#print(hijos_padres)


def hijos_nodo(nodo_padre):
	lista_hijos_response=[]
	lista_hijos = [nodo["success_nodes"] for nodo in lista_nodos if nodo["id"]==nodo_padre]
	lista_hijos_response.append(lista_hijos[0])
	if lista_hijos==[[]]:
		print("acabo")
	else:
		#print(lista_hijos)
		for i in lista_hijos[0]:
			
			lista_hijos_response.append(hijos_nodo(i))
	return lista_hijos_response
#print(hijos_nodo(lista_nodos, 3))
lista_hijos = []
lista_hijos = hijos_nodo(0)

print(lista_hijos)
print('-----')
print(lista_hijos[0])
print('-----')
print(lista_hijos[1][0])
print(lista_hijos[2][0])
print('-----')
print(lista_hijos[1][1][0])
print(lista_hijos[2][1][0])
print(lista_hijos[2][2][0])
print('-----')
print(lista_hijos[1][1][1][0])
print(lista_hijos[2][1][1][0])
print(lista_hijos[2][1][2][0])

def niveles(lista_padres, nodo_padre):
	cont = 0
