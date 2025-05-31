class Processo:
  def __init__(self, nome, duracao):
    self.nome = nome
    self.duracao = duracao
    self.tempo = 0
    self.tempo_finalizacao = 0
    self.tempo_retorno = 0
    self.tempo_chegada = 0
    self.tempo_resposta = 0
    self.inicio = -1
    self.fim = False
    
class RoundRobin:
    def __init__(self, quantum):
        self.quantum = quantum
        self.processos = []
        self.tempo_chegada_processos = []
        self.qtd_processos = 0
        self.tempo_duracao = 0
        self.tempo_atual = 0

        
    def add_processo(self, nome, duracao, horario_chegada):
        processo = Processo(nome, duracao)
        processo.tempo_chegada = horario_chegada
        self.tempo_chegada_processos.append(horario_chegada)
        self.processos.append(processo)
        self.qtd_processos += 1
        self.tempo_duracao += duracao
        
    def executar(self):
        tempo_ate_quantum = 1
        fila = self.processos.copy()
        processos_finalizados = []
        while fila:
            processo = fila.pop(0)
            if processo.inicio == -1:
                processo.inicio = self.tempo_atual
                processo.tempoRes = self.tempo_atual
            while tempo_ate_quantum <= self.quantum and processo.tempo < processo.duracao:
                self.validacao_insercao_processo_tempo_atual()
                processo.tempo += 1
                self.tempo_atual += 1
                tempo_ate_quantum += 1
                print(f"Processo {processo.nome} executando. Tempo atual: {self.tempo_atual}. Tempo de execucao: {processo.duracao}. Tempo de execucao restante: {processo.duracao - processo.tempo}. Tempo de chegada: {processo.tempo_chegada}")
            tempo_ate_quantum = 1
            if processo.tempo >= processo.duracao:
                processo.fim = True
                processo.tempo_finalizacao = self.tempo_atual
                processo.tempo_retorno = processo.tempo_finalizacao - processo.tempo_chegada
                processo.tempo_resposta = processo.inicio - processo.tempo_chegada
                processos_finalizados.append(processo)
            else:
                fila.append(processo)
        self.listar_processos_finalizados(processos_finalizados)

    def validacao_insercao_processo_tempo_atual(self):
        while self.tempo_chegada_processos and self.tempo_chegada_processos[0] <= self.tempo_atual:
            print(f"Novo processo inserido no tempo {self.tempo_atual}.")
            self.tempo_chegada_processos.pop(0)
        
    def listar_processos_finalizados(self, processos_finalizados):
        processos_finalizados.sort(key=lambda x: x.nome)
        tempo_medio_retorno = sum(p.tempo_resposta for p in processos_finalizados) / len(processos_finalizados)
        print("Processos Finalizados:")
        print("-" * 20)
        for process in processos_finalizados:
            self.listar_dados(process)
        print(f"Tempo medio de resposta: {tempo_medio_retorno:.2f}")
        print("-" * 20)
    def listar_dados(self, process: Processo):
        
        print(f"Processo: {process.nome}")
        print(f"Chegada: {process.tempo_chegada}")
        print(f"Comeca em: {process.inicio}")
        print(f"Tempo de Execucaoo: {process.duracao}")
        print(f"Tempo de Fim: {process.tempo_finalizacao}")
        print(f"Tempo de Resposta: {process.tempo_resposta}")
        print(f"Tempo de Espera: {process.tempo_retorno}")
        print(f"Tempo de Retorno: {process.tempo_retorno}")
        print("-" * 20)
        
                
round_robin_1 = RoundRobin(2)
round_robin_1.add_processo("P1", 5, 0)                   
round_robin_1.add_processo("P2", 3, 1)                   
round_robin_1.add_processo("P3", 8, 2)      
round_robin_1.add_processo("P4", 3, 3)      
round_robin_1.executar()     
        
round_robin_2 = RoundRobin(2)
round_robin_2.add_processo("P1", 5, 0)                   
round_robin_2.add_processo("P2", 3, 1)                   
round_robin_2.add_processo("P3", 6, 2)      
round_robin_2.executar() 
                      
