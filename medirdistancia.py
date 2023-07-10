import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
clave = "3LTk4VxW4s0iwaqhWCn2Mrb2HKj4vhOJ"

while True:
    origen = input("Ubicación inicial: ")
    if origen.lower() in ['salir', 's']:
        break

    destino = input("Destino: ")
    if destino.lower() in ['salir', 's']:
        break

    url = main_api + urllib.parse.urlencode({"key": clave, "from": origen, "to": destino})

    json_data = requests.get(url).json()

    if json_data["info"]["statuscode"] == 0:
        print(f"Viaje desde {origen} hasta {destino}")
        print("Duración del viaje: " + json_data["route"]["formattedTime"])
        print("Kilómetros: {:.1f}".format(json_data["route"]["distance"]*1.61))

        if "fuelUsed" in json_data["route"]:
            print("Combustible utilizado (Ltr): {:.1f}".format(json_data["route"]["fuelUsed"]*3.78))
        else:
            print("Información de combustible no disponible")

        print("=============================================")

        for maniobra in json_data["route"]["legs"][0]["maneuvers"]:
            print(maniobra["narrative"])

    else:
        print("Error al obtener datos. Por favor, verifica las ciudades ingresadas e intenta nuevamente.")
