import requests

# lista de urls de imagenes
urls = [
	'https://url.org/img/img1.png',
	'https://url.org/img/img2.png',
]
# recorrer la lista y descargar las imagenes una a una y guardarlas en la carpeta (avisar cuando se daecargue cada imagen)
for i in range(len(urls)):
	url = urls[i]
	nombre_local_imagen = '0' + str(i + 1) + 'd.png'
	imagen = requests.get(url).content
	with open(nombre_local_imagen, 'wb') as handler:
		handler.write(imagen)
	print('Imagen descargada: ', nombre_local_imagen)

