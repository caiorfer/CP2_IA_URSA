Está sem dados no momento mas a logica está ai

# Análise de Crédito Automatizada

Este projeto visa automatizar o processo de análise de crédito para determinar a qual grupo um cliente pertence com base em suas características financeiras.

## Descrição do Projeto

O objetivo deste projeto é desenvolver um sistema de classificação que atribua automaticamente clientes novos a grupos de microcrédito ou crédito para grandes negócios com base em suas características financeiras. O sistema utiliza um modelo de Máquina de Vetor de Suporte (SVM) treinado com dados históricos de clientes.

## Funcionalidades

- Carregamento e pré-processamento de dados.
- Treinamento de um modelo SVM com kernel RBF.
- Previsão do grupo de crédito para um novo cliente.
- Atribuição de limite de crédito com base na previsão do modelo.

## Arquivos do Projeto

- `train_model.py`: Script para treinar o modelo SVM com os dados históricos.
- `predict_new_customer.py`: Script para prever o grupo de crédito de um novo cliente.
- `svm_model.pkl`: Arquivo contendo o modelo SVM treinado.
- `data/`: Pasta contendo os dados históricos dos clientes.

## Tecnologias Utilizadas

- Python
- Pandas
- Scikit-learn
- Joblib
