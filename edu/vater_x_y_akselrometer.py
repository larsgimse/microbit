# elektronisk vater
# akselerometeret i microbit leser verdi mellom -1024 og 1024 og er i vater naar aksen har verdien 0
#
# for aa bruke LED displayet maa vi gjoere om verdien fra akselrometeret til verdier mellom 0 og 4
# til dette lager vi to funksjoner xakse(verdi) og yxakse(verdi)

from microbit import*

lysstyrke = 9 #lysstyrken paa LED kan sette mellom 1 og 9 der 9 er sterkest og 0 er av

def xakse(x_acc):
    x = 0
    if x_acc > -500: #verdien er mindre enn -500 x=0+1 
        x = x + 1
    if x_acc > -200: #verdien er mindre enn -200 x=1+1
        x = x + 1
    if x_acc > 200: #verdien er storre enn 200 x=2+1
        x = x + 1
    if x_acc > 500: #verdien er storre enn 500 x=3+1
        x = x + 1
    return x
    
def yakse(y_acc):
    y = 0
    if y_acc > -500: #verdien er mindre enn -500 y=0+1
        y = y + 1
    if y_acc > -200: #verdien er mindre enn -200 y=1+1
        y = y + 1
    if y_acc > 200: #verdien er mindre enn 200 y=2+1
        y = y + 1
    if y_acc > 500: #verdien er mindre enn 500 y=3+1
        y = y + 1
    return y
    

while True:
    display.clear() #renser skjermen mellom hver loop
    x_display = xakse(accelerometer.get_x()) #setter x_display til xakse verdi i forhold til akselerometeret
    y_display = yakse(accelerometer.get_y()) #setter y_display til xakse verdi i forhold til akselerometeret
    
    display.set_pixel(x_display, y_display, lysstyrke) #skrur paa aktuell LED basert paa x_display, y_display og lysstyrke
    
    print(x_display, y_display) #skriver verdien paa skjermen i program som stoetter dette, eks. MU 
