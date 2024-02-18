from datetime import datetime, timedelta

# Data ostatnich laboratoriów
data_laboratoria = datetime(2024, 2, 10)

# Data kolokwium
data_kolokwium = datetime(2024, 3, 5)

# Dzisiejsza data
dzis = datetime.now()

# Obliczanie różnicy między datami
dni_od_laboratoriow = (dzis - data_laboratoria).days
dni_do_kolokwium = (data_kolokwium - dzis).days

# Przedstawienie wyniku w czytelny sposób
print("Od ostatnich laboratoriów minęło {} dni.".format(dni_od_laboratoriow))
print("Do kolejnego kolokwium pozostało {} dni.".format(dni_do_kolokwium))
