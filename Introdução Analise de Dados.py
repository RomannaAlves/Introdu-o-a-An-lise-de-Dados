#!/usr/bin/env python
# coding: utf-8

# # Introdução a Análise de Dados
# 
# ### Como funciona um Projeto de Análise de Dados?
# 
# Os projetos de Análise de Dados são na verdade Desafios das Empresas
# 
# ### Desafio
# 
# - Empresa Vende Bermudas
# - 5 Lojas
# - Está querendo aumentar as vendas
# - O que fazer?
# - Informações Disponíveis: Base de Vendas

# ### Passo 1 - Trazer sua base de dados para o Python e ver o que tem nela

# In[4]:


import pandas as pd

tabela = pd.read_excel("Vendas.xlsx")
display(tabela)


# ### Passo 2 - Pegar um panorama geral sobre a sua base de dados

# In[5]:


faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)


# ### Passo 3 - Começar sua análise Top -> Down

# In[7]:


#faturamento por loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
display(faturamento_por_loja)


# ### Passo 4 - Entrar no detalhe pra entender

# In[8]:


#faturamento por produto da loja Iguatemi Campinas
faturamento_por_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(faturamento_por_produto)


# In[ ]:


# o diferencial da loja Iguatemi Campinas é a Bermuda Liso
#Propostas: sugerir que as outras lojas vendam a Bermuda Liso para aumentar o seu faturamento

