import urllib.request
import json

# Haetaan säädataa netistä
url = "https://api.openweathermap.org/data/2.5/weather?q=Helsinki&units=metric&mode=JSON&APPID=ff64c247a136f706923d1ee0d55d71e2"
data = urllib.request.urlopen(url).read()
# Muutetaan tekstiksi
output = data.decode('utf-8')

# Kaunistetaan tulostelua varten
json_formatted_str = json.dumps(output, indent=2)
print(json_formatted_str)

# Kirjoitetaan tiedostoon
with open("weather.json", "w") as my_file:
    my_file.write(output)

# Parsitaan kentistä tietoja ulos
saa = json.loads(data)
# print(saa)
print(saa['name'])
print(saa['weather'][0]['description'])
print(saa['main']['temp'])
print(saa['main']['humidity'])
print(saa['main']['humidity'])
