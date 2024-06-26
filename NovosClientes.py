import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import joblib
#Carregando dados
dados = pd.DataFrame({
    'maiorAtraso': [...],
    'percentualProtestos': [...],
    'titulosEmAberto': [...],
    'valorSolicitado': [...],
    'percentualRisco': [...],
    'periodoBalanco': [...],
    "passivoCirculante": [...],
    "totalAtivo": [...],
    "endividamento":[...],
    "duplicatasAReceber":[...],
    "faturamentoBruto":[...],
    "margemBruta":[...],
    "capitalSocial":[...],
    "empresa_MeEppMei":[...],
    "scorePontualidade":[...],
    "limiteEmpresaAnaliseCredito":[...],
    "valorAprovado":[...],
    'status': [...]
})

# Separando os dados em features e rótulo
features = dados.drop('status', axis=1)
saida = dados['status']

# Utilizando o metodo sample do Pandas para embaralhar os dados e dividir em conjuntos de treinamento e teste
train_data = dados.sample(frac=0.8, random_state=42)  # 80% dos dados para treinamento
test_data = dados.drop(train_data.index)  # O restante dos dados para teste

# Visualizando os conjuntos de treinamento e teste
print("Conjunto de Treinamento:")
print(train_data)
print("\nConjunto de Teste:")
print(test_data)

# Dividindo os dados em conjuntos de treinamento e teste
features_train, features_test, saida_train, saida_test = train_test_split(features, saida, test_size=0.2, random_state=42)

# Pré-processamento de dados: Normalização
scaler = StandardScaler()
features_train_scaled = scaler.fit_transform(features_train)
features_test_scaled = scaler.transform(features_test)

# Treinamento do modelo SVM
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')  # Usando um kernel RBF
svm_model.fit(features_train_scaled, saida_train)

# Salvar o modelo SVM treinado
joblib.dump(svm_model, 'svm_model.pkl')

# Predições
saida_pred = svm_model.predict(features_test_scaled)

# Avaliação do modelo
print("Relatório de Classificação:")
print(classification_report(saida_test, saida_pred))

#Como seria possível indicar o grupo desse cliente sem ter que refazer todos os grupos?
#Assim:

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Carregar o modelo SVM previamente treinado
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')  # Por exemplo, usando um kernel RBF


#o que é kernel RBF: O kernel RBF (Radial Basis Function) é um dos tipos de kernel mais comuns usados em algoritmos de
# máquinas de vetor de suporte (SVM). O SVM é um algoritmo de aprendizado supervisionado usado para classificação e regressão.

# Carregar os dados do novo cliente e prepará-los
novo_cliente = pd.DataFrame({
    'maiorAtraso': [10],
    'percentualProtestos': [0.2],
    'titulosEmAberto': [2],
    'valorSolicitado': [15000],
    'percentualRisco': [0.3],
    'periodoBalanco': [12],
    'passivoCirculante': [5000],
    'totalAtivo': [20000],
    'endividamento': [0.25],
    'duplicatasAReceber': [3000],
    'faturamentoBruto': [50000],
    'margemBruta': [0.35],
    'capitalSocial': [10000],
    'empresa_MeEppMei': [1],
    'scorePontualidade': [700],
    'limiteEmpresaAnaliseCredito': [20000]
})

# Aplicar pré-processamento de dados (normalização)
scaler = StandardScaler()
novo_cliente_scaled = scaler.fit_transform(novo_cliente)

# Carregar o modelo SVM previamente treinado
# Ajustar o modelo SVM com os dados do novo cliente
svm_model.fit(features_train_scaled, saida_train)

# Prever o grupo de crédito do novo cliente
previsao_grupo_credito = svm_model.predict(novo_cliente_scaled)

# Atribuir o cliente ao grupo correspondente com base na previsão do modelo
if previsao_grupo_credito == 'Microcrédito':
    grupo_credito = 'Microcrédito'
else:
    grupo_credito = 'Crédito para Grandes Negócios'

# Tomar decisões com base na previsão (exemplo: estabelecer limite de crédito)
limite_de_credito = 5000 if grupo_credito == 'Microcrédito' else 20000

# Exibir resultados
print("Grupo de Crédito:", grupo_credito)
print("Limite de Crédito:", limite_de_credito)

