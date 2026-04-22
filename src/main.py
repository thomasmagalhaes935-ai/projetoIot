from machine import Pin, ADC, PWM
import time 


potenciometro = ADC(Pin(34))
potenciometro.atten(ADC.ATTN_11DB)

botao_regar = Pin(33, Pin.IN, Pin.PULL_UP)
valor_regar = 0
estado_anterior_botao = 1

def verificar_botao(valor_regar, estado_anterior_botao):
    estado_atual = botao_regar.value()
    if estado_anterior_botao == 1 and estado_atual == 0:
        valor_regar + 500
        print("Regando a planta!")
        
    return valor_regar, estado_atual



pwm_r = PWM(Pin(4))
pwm_g = PWM(Pin(5))
pwm_b = PWM(Pin(18))

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

cores = [
       (100, 0, 0),   #vermelho
       (100, 50, 0),  #laranja
       (0, 100, 0),   #verde 
       (0, 0, 100),   #azul
       (100, 0, 100) #roxo
]

def set_color(r, g, b):
    pwm_r.duty_u16(int(r*65535/100))
    pwm_g.duty_u16(int(g*65535/100))
    pwm_b.duty_u16(int(b*65535/100))


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
    
def atualizar_led(estado_da_planta):
    if estado_da_planta == "SECO_CRITICO":
        set_color(100, 0, 0) 
    elif estado_da_planta == "SECO":
        set_color(100, 50, 0)
    elif estado_da_planta == "IDEAL":
        set_color(0, 100, 0)
    elif estado_da_planta == "UMIDO":
        set_color(0, 0, 100)
    else: 
        set_color(100, 0, 100)


while True: 
    valor_umidade = ler_umidade()
    estado_da_planta = determinar_estado(valor_umidade)
    print("UMIDADE: ", valor_umidade)
    print("ESTADO: ", estado_da_planta)
    atualizar_led(estado_da_planta)
    time.sleep(1)



