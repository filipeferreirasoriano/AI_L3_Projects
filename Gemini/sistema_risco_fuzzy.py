# sistema_risco_fuzzy.py
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt # Opcional, para visualização

# --------------------------------------------------------------------------
# 1. DEFINIÇÃO DAS VARIÁVEIS (ANTECEDENTES E CONSEQUENTE)
# --------------------------------------------------------------------------

# Universos de discurso
u_0_10 = np.arange(0, 11, 1)  # Para a maioria das variáveis (0-10)
u_risco = np.arange(0, 101, 1) # Para o Nível de Risco do Projeto (0-100)

# Variáveis de Entrada (Antecedentes)
ee = ctrl.Antecedent(u_0_10, 'experiencia_equipe')
cp = ctrl.Antecedent(u_0_10, 'complexidade_projeto')
cr = ctrl.Antecedent(u_0_10, 'clareza_requisitos')
tu = ctrl.Antecedent(u_0_10, 'tecnologia_utilizada')
tp = ctrl.Antecedent(u_0_10, 'tamanho_projeto')
od = ctrl.Antecedent(u_0_10, 'orcamento_disponivel')
pp = ctrl.Antecedent(u_0_10, 'prazo_projeto')
qc = ctrl.Antecedent(u_0_10, 'qualidade_comunicacao')
dr = ctrl.Antecedent(u_0_10, 'disponibilidade_recursos')
ni = ctrl.Antecedent(u_0_10, 'nivel_inovacao')
de = ctrl.Antecedent(u_0_10, 'dependencias_externas')
sg = ctrl.Antecedent(u_0_10, 'suporte_alta_gestao')
mp = ctrl.Antecedent(u_0_10, 'maturidade_processos')
pt = ctrl.Antecedent(u_0_10, 'planejamento_testes')
cs = ctrl.Antecedent(u_0_10, 'criticidade_seguranca')

# Variável de Saída (Consequente)
nrp = ctrl.Consequent(u_risco, 'nivel_risco_projeto')

# --------------------------------------------------------------------------
# 2. DEFINIÇÃO DOS CONJUNTOS FUZZY (FUNÇÕES DE PERTINÊNCIA)
# --------------------------------------------------------------------------

# Experiência da Equipe (EE)
ee['Baixa'] = fuzz.trimf(ee.universe, [0, 0, 5])
ee['Media'] = fuzz.trimf(ee.universe, [2, 5, 8])
ee['Alta'] = fuzz.trimf(ee.universe, [5, 10, 10])

# Complexidade do Projeto (CP)
cp['Baixa'] = fuzz.trimf(cp.universe, [0, 0, 5])
cp['Media'] = fuzz.trimf(cp.universe, [2, 5, 8])
cp['Alta'] = fuzz.trimf(cp.universe, [5, 10, 10])

# Clareza dos Requisitos (CR)
cr['Baixa'] = fuzz.trimf(cr.universe, [0, 0, 5]) # Pouco Claros
cr['Media'] = fuzz.trimf(cr.universe, [2, 5, 8]) # Razoavelmente Claros
cr['Alta'] = fuzz.trimf(cr.universe, [5, 10, 10]) # Muito Claros

# Tecnologia Utilizada (TU)
tu['Nova'] = fuzz.trimf(tu.universe, [0, 0, 5])
tu['Conhecida'] = fuzz.trimf(tu.universe, [2, 5, 8])
tu['Dominada'] = fuzz.trimf(tu.universe, [5, 10, 10])

# Tamanho do Projeto (TP)
tp['Pequeno'] = fuzz.trimf(tp.universe, [0, 0, 5])
tp['Medio'] = fuzz.trimf(tp.universe, [2, 5, 8])
tp['Grande'] = fuzz.trimf(tp.universe, [5, 10, 10])

# Orçamento Disponível (OD)
od['Insuficiente'] = fuzz.trimf(od.universe, [0, 0, 5])
od['Adequado'] = fuzz.trimf(od.universe, [2, 5, 8])
od['Confortavel'] = fuzz.trimf(od.universe, [5, 10, 10])

# Prazo do Projeto (PP)
pp['Apertado'] = fuzz.trimf(pp.universe, [0, 0, 5])
pp['Realista'] = fuzz.trimf(pp.universe, [2, 5, 8])
pp['Flexivel'] = fuzz.trimf(pp.universe, [5, 10, 10])

# Qualidade da Comunicação (QC)
qc['Ruim'] = fuzz.trimf(qc.universe, [0, 0, 5])
qc['Regular'] = fuzz.trimf(qc.universe, [2, 5, 8])
qc['Boa'] = fuzz.trimf(qc.universe, [5, 10, 10])

# Disponibilidade de Recursos (DR)
dr['Baixa'] = fuzz.trimf(dr.universe, [0, 0, 5])
dr['Media'] = fuzz.trimf(dr.universe, [2, 5, 8])
dr['Alta'] = fuzz.trimf(dr.universe, [5, 10, 10])

# Nível de Inovação (NI)
ni['Baixo'] = fuzz.trimf(ni.universe, [0, 0, 5])
ni['Medio'] = fuzz.trimf(ni.universe, [2, 5, 8])
ni['Alto'] = fuzz.trimf(ni.universe, [5, 10, 10])

# Dependências Externas (DE)
de['Baixa'] = fuzz.trimf(de.universe, [0, 0, 5])
de['Media'] = fuzz.trimf(de.universe, [2, 5, 8])
de['Alta'] = fuzz.trimf(de.universe, [5, 10, 10])

# Suporte da Alta Gestão (SG)
sg['Baixo'] = fuzz.trimf(sg.universe, [0, 0, 5])
sg['Medio'] = fuzz.trimf(sg.universe, [2, 5, 8])
sg['Alto'] = fuzz.trimf(sg.universe, [5, 10, 10])

# Maturidade dos Processos (MP)
mp['Baixa'] = fuzz.trimf(mp.universe, [0, 0, 5])
mp['Media'] = fuzz.trimf(mp.universe, [2, 5, 8])
mp['Alta'] = fuzz.trimf(mp.universe, [5, 10, 10])

# Planejamento de Testes (PT)
pt['Insuficiente'] = fuzz.trimf(pt.universe, [0, 0, 5])
pt['Adequado'] = fuzz.trimf(pt.universe, [2, 5, 8])
pt['Abrangente'] = fuzz.trimf(pt.universe, [5, 10, 10])

# Criticidade da Segurança (CS)
cs['Baixa'] = fuzz.trimf(cs.universe, [0, 0, 5])
cs['Media'] = fuzz.trimf(cs.universe, [2, 5,