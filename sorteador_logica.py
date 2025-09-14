import json
import random

tunagem = ["Offroad", "Rally", "Pista", "Rua", "Drift", "Sleeper"]
traducao_grupos = {
    'Buggies': 'BUGGIES',
    'Muscle Clássico': 'CLASSIC MUSCLE',
    'Carros Clássicos de Corrida': 'CLASSIC RACERS',
    'Rally Clássico': 'CLASSIC RALLY',
    'Carros Esportivos Clássicos': 'CLASSIC SPORTS CARS',
    'Carros Cult': 'CULT CARS',
    'Carros de Drift': 'DRIFT CARS',
    'Brinquedos de Pista Extremos': 'EXTREME TRACK TOYS',
    'Carros de GT': 'GT CARS',
    'Hot Hatches': 'HOT HATCH',
    'Hipercarros': 'HYPERCAR',
    'Muscle Moderno': 'MODERN MUSCLE',
    'Rally Moderno': 'MODERN RALLY',
    'Carros Esportivos Modernos': 'MODERN SPORTS CARS',
    'Supercarros Modernos': 'MODERN SUPERCARS',
    'Fora de Estrada': 'OFFROAD',
    'Picapes e 4x4': "PICK-UP & 4X4'S",
    'Monstros do Rally': 'RALLY MONSTERS',
    'Clássicos Raros': 'RARE CLASSICS',
    'Hot Hatches Retrô': 'RETRO HOT HATCH',
    'Muscle Retrô': 'RETRO MUSCLE',
    'Rally Retrô': 'RETRO RALLY',
    'Sedãs Retrô': 'RETRO SALOONS',
    'Carros Esportivos Retrôs': 'RETRO SPORTS CARS',
    'Supercarros Retrô': 'RETRO SUPERCARS',
    'Hot Rods e Personalizados': 'RODS AND CUSTOMS',
    'Heróis dos Utilitários Esportivos': 'SPORT UTILITY HEROES',
    'Super GT': 'SUPER GT',
    'Super Hot Hatches': 'SUPER HOT HATCH',
    'Supersedãs': 'SUPER SALOONS',
    'Carros de Pista': 'TRACK TOYS',
    'Picapes': 'TRUCKS',
    'Buggies Ilimitados': 'UNLIMITED BUGGIES',
    'Offroad Ilimitado': 'UNLIMITED OFFROAD',
    'UTVs': "UTV'S",
    'Vans e Utilitários': 'VANS AND UTILITY',
    'Carros Antigos de Corrida': 'VINTAGE RACERS',
}

def sortear_carro(filtro_grupo):

    with open('carros.json', 'r') as lista_carros:
        carros = json.load(lista_carros)
    
    filtros_ingles = [traducao_grupos[f] for f in filtro_grupo]

    carros_filtrados = []

    for carro in carros:
        if not filtros_ingles:
            carros_filtrados = carros
        else:
            for carro in carros: 
                if carro['Group'] in filtros_ingles:         
                    carros_filtrados.append(carro)

    if carros_filtrados:
        carro_sorteado = random.choice(carros_filtrados)
        tunagem_sorteada = random.choice(tunagem)
        return {
            'carro': carro_sorteado,
            'tunagem': tunagem_sorteada
        }
    else:
        return {
            'carro': "Nenhum carro encontrado neste filtro.",
            'tunagem': None
        }