print('=== Cadastro de Tarefa ===')
titulo = input('Título da tarefa: ')
prioridade = int(input('Prioridade (1 a 5): '))
prazo_horas = float(input('Prazo estimado em horas: '))
resposta_urgencia = input('A tarefa é urgente? (sim/não): ')
urgente = resposta_urgencia == 'sim'
fator_esforco = 1.2
esforco_estimado = prazo_horas * fator_esforco

prioridade_alta = prioridade >= 4
prioritaria = prioridade_alta or urgente

print('\n=== Resumo da Tarefa ===')
print(f'Título: {titulo}')
print(f'Prioridade: {prioridade}')
print(f'Prazo informado: {prazo_horas:.2f} horas')
print(f'Esforço estimado: {esforco_estimado:.2f} horas')
print(f'Urgente: {urgente}')
print(f'Prioridade alta: {prioridade_alta}')
print(f'Deve ser tratada como prioritária: {prioritaria}')