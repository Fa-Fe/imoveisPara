from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

geolocator = Nominatim(user_agent="localiza.py")

def obter_coordenadas(endereco):
    try:
        localizacao = geolocator.geocode(endereco)
        if localizacao:
            return (localizacao.latitude, localizacao.longitude)
        else:
            return None, None
        
    except GeocoderTimedOut:
        time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente
        return obter_coordenadas(endereco)

endereço_teste = "RUA FERNANDO FERRARI, 408 - Santa Luzia, Pará, Brasil"
latitude, longitude = obter_coordenadas(endereço_teste)
if latitude and longitude:
    print(f"Endereço: {endereço_teste}")
    print(latitude, longitude)
else:
    print(f"Não foi possível obter as coordenadas para o endereço: {endereço_teste}")

link_google_maps = f"https://www.google.com/maps?q={latitude},{longitude}"
print(f"Link do Google Maps: {link_google_maps}")