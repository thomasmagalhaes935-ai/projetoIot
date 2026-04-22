from machine import Pin, ADC, PWM
import time 

potenciometro = ADC(Pin(34))
potenciometro.atten(ADC.ATTN_11DB)

botao_regar = Pin(33, Pin.IN, Pin.PULL_UP)
estado_anterior_botao = 1

umidade_atual = potenciometro.read() 


def verificar_botao(estado_anterior):
    estado_atual = botao_regar.value()
    adicionar_agua = 0

    if estado_anterior == 1 and estado_atual == 0:
        adicionar_agua = 500
        print("Regando a planta!")

    return adicionar_agua, estado_atual


def calcular_secagem(clima):
    base = 30
    variacao = int((4095 - clima) / 100)
    return base + variacao


pwm_r = PWM(Pin(4))
pwm_g = PWM(Pin(5))
pwm_b = PWM(Pin(18))

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

def set_color(r, g, b):
    pwm_r.duty(int(r * 1023 / 100))
    pwm_g.duty(int(g * 1023 / 100))
    pwm_b.duty(int(b * 1023 / 100))


def determinar_estado(valor_umidade):
    if valor_umidade < 800:
        return "SECO_CRITICO"
    elif valor_umidade < 1500: 
        return "SECO"
    elif valor_umidade < 3000:
        return "IDEAL"
    elif valor_umidade < 3800:
        return "UMIDO"
    else:
        return "EXCESSO"
    

def atualizar_led(estado):
    if estado == "SECO_CRITICO":
        set_color(100, 0, 0) 
    elif estado == "SECO":
        set_color(100, 50, 0)
    elif estado == "IDEAL":
        set_color(0, 100, 0)
    elif estado == "UMIDO":
        set_color(0, 0, 100)
    else: 
        set_color(100, 0, 100)


while True:
    agua_adicionada, estado_anterior_botao = verificar_botao(estado_anterior_botao)

    umidade_atual += agua_adicionada

    clima_base = potenciometro.read()
    umidade_atual -= calcular_secagem(clima_base)

    if umidade_atual < 0:
        umidade_atual = 0
    elif umidade_atual > 4095:
        umidade_atual = 4095

    estado_da_planta = determinar_estado(umidade_atual)

    print(" Umidade:", umidade_atual)
    print(" Estado:", estado_da_planta)

    atualizar_led(estado_da_planta)

    time.sleep(1)