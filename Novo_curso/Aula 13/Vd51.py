RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade = int(input('a quantos Km/h o carro está? ')) # definir a velocidade do carro
local_carro = int(input('Em que Km na estrada o carro está? ')) # definir posição do carro

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1


print(vel_carro_pass_radar_1) 
print(carro_multado_radar_1)
print(carro_passou_radar_1)
# verificando o valor das variáveis 

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')