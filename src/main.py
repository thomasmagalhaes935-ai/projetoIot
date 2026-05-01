import machine
import time

print("Teste")

POT_PIN = 34
BOTAO_REGAR_PIN = 33
BOTAO_SELECAO_PIN = 26 

LED_R_PIN = 4
LED_G_PIN = 5
LED_B_PIN = 18

PINOS_LEDS_PLANTAS = [12, 13, 14, 27] 
PWM_FREQ = 1000

potenciometro = machine.ADC(machine.Pin(POT_PIN))
potenciometro.atten(machine.ADC.ATTN_11DB)

btn_regar = machine.Pin(BOTAO_REGAR_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
btn_selecao = machine.Pin(BOTAO_SELECAO_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

pwm_r = machine.PWM(machine.Pin(LED_R_PIN))
pwm_g = machine.PWM(machine.Pin(LED_G_PIN))
pwm_b = machine.PWM(machine.Pin(LED_B_PIN))

pwm_r.freq(PWM_FREQ)
pwm_g.freq(PWM_FREQ)
pwm_b.freq(PWM_FREQ)

leds_selecao = [machine.Pin(p, machine.Pin.OUT) for p in PINOS_LEDS_PLANTAS]

plantas = [
    {"nome": "Cacto", "umidade": 2600, "taxa_base": 5, "rega": 600, "ultima_rega": 0},
    {"nome": "Suculenta", "umidade": 2600, "taxa_base": 15, "rega": 800, "ultima_rega": 0},
    {"nome": "Samambaia", "umidade": 2600, "taxa_base": 50, "rega": 1200, "ultima_rega": 0},
    {"nome": "Horta", "umidade": 2600, "taxa_base": 30, "rega": 1000, "ultima_rega": 0}
]

planta_focada = 0
ultimo_update = time.ticks_ms()
intervalo_log = 1000
led_alerta_estado = True
ultimo_pisca = 0
intervalo_pisca = 500

last_btn_states = [1, 1] 
debounce_delay = 50 

def interpretar_clima(valor):
    if valor < 800:
         return "Muito Seco (Crítico)"
    elif valor < 1500: 
        return "Seco"
    elif valor < 2700: 
        return "Normal/Ideal"
    elif valor < 3600: 
        return "Umido"
    else: 
        return "Muito Úmido"

def determinar_estado(valor):
    if valor < 900: 
        return "SECO_CRITICO"
    elif valor < 1600: 
        return "SECO"
    elif valor < 2900: 
        return "IDEAL"
    elif valor < 3600: 
        return "UMIDO"
    else: 
        return "EXCESSO"

def set_color(r, g, b):
    pwm_r.duty(int(r * 1023 / 100))
    pwm_g.duty(int(g * 1023 / 100))
    pwm_b.duty(int(b * 1023 / 100))

def atualizar_led_rgb(estado):
    if estado == "SECO_CRITICO": 
        set_color(100, 0, 0)
    elif estado == "SECO": 
        set_color(100, 40, 0)
    elif estado == "IDEAL": 
        set_color(0, 100, 0)
    elif estado == "UMIDO": 
        set_color(0, 0, 100)
    else: 
        set_color(100, 0, 100)