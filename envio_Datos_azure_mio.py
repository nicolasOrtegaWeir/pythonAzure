import time
from azure.iot.device import IoTHubDeviceClient, Message

connection_string = "HostName=PruebaParaDiferentesPC.azure-devices.net;DeviceId=Python04;SharedAccessKey=TOr+sdRHoPnpMPFNv3pPIG86uWZiKLZRZsBupJtBJZU="

msj = '{{"ContadorArriba": {contador_arriba},"ContadorAbajo: {contador_abajo}}}'

client = IoTHubDeviceClient.create_from_connection_string(connection_string)

def envio_de_datos():
    try:
        print("Enviando mensajes, Ctrl-C para terminar envío")
        contador_arriba = 50
        contador_abajo = 50
        while True:
            mensaje_formateado = msj.format(contador_arriba = contador_arriba, contador_abajo = contador_abajo)
            contador_arriba = contador_arriba + 1
            if (contador_arriba == 101):
                contador_arriba = 50
            contador_abajo = contador_abajo - 1
            if (contador_abajo == -1):
                contador_abajo = 50
            mensaje = Message(mensaje_formateado)
            
            print("Enviando mensaje: {}".format(mensaje))
            client.send_message(mensaje)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Envío terminado")

if __name__ == '__main__':
    print("Enviando mensajes!")
    envio_de_datos()
