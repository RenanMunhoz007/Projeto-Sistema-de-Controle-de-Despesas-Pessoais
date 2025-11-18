# Sistema de Controle de Despesas Pessoais

## Descrição do Projeto
Este projeto tem como objetivo criar um sistema simples para controlar finanças pessoais.  
O sistema permitirá registrar receitas e despesas, organizar categorias e definir um orçamento mensal.  
Além disso, será possível gerar alertas quando certos limites forem ultrapassados.

## Estrutura Planejada de Classes

### 1. Categoria
Representa a categoria relacionada a uma receita ou despesa.  
Atributos:
- nome  
- tipo (RECEITA ou DESPESA)  
- limite_mes  
- descricao  

### 2. Transacao (classe base)
Classe base que representa qualquer tipo de movimentação financeira.  
Atributos:
- valor  
- categoria  
- data  
- descricao  
- forma_pagamento  

### 3. Receita 
Representa uma transação de entrada de dinheiro.

### 4. Despesa 
Representa uma transação de saída de dinheiro.

### 5. Orcamento Mes
Representa o orçamento de um mês específico.  
Atributos:
- ano  
- mes  
- definir_orcamento  
- definir_valor  

### 6. Alerta
Representa um alerta relacionado ao orçamento ou gastos.  
Atributos:
- mensagem  
- tipo  
- data  

### 7. Config
Representa as configurações gerais do sistema.  
Atributos:
- valor_minimo_alerta  
- mes_comparativos  
- meta_economia  
