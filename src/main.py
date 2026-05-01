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