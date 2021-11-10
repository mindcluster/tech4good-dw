# Projeto Tech for Good - Dataware House

<img alt="Arquitetura da Solução" src="./arquitetura/DW Fome Zero.drawio.png">

<details>
<summary>Desafio</summary>
Dentre os 17 objetivos interconectados apresentados pela ONU, um deles 
trata de assunto ligado a agricultura e sustentabilidade. Esse tema tem relação 
direta com o Brasil, considerando o expressivo tamanho territorial do país e o 
momento de destaque ocupado pelo Agronegócio que apresenta cada vez maior importância na composição do PIB brasileiro. 

Apesar da evolução crescente do Agronegócio nacional, o Brasil concentra 
uma expressiva quantidade de pessoas pobres morando na zona rural.

Se antecipando ao objetivo 2 da ONU, “Fome zero e Agricultura 
Sustentável”, a Embrapa apresentou em 2011 um programa, denominado 
Sisteminha, com o objetivo de capacitar o cidadão do campo a ter auto 
suficiência em termos de produção alimentar de qualidade. O “sisteminha” da 
embrapa é composto por um conjunto de 15 fontes de produção de alimentos 
integradas, que permite sustentabilidade alimentar ao seu usuário. A lista de 
fontes de produção de alimentos é apresentada abaixo e sua respectiva 
indicação é ilustrada em imagem adaptada do artigo da embrapa, conforme 
segue:

  1) Produção de peixes, 
  2) Produção de ovos de galinhas; 
  3) Produção de frangos de corte; 
  4) Produção de minhocas; 
  5) Produção vegetal (carboidratos, hortaliças, chás e temperos; frutíferas e 
madeireiras);
  6) Produção de composto; 
  7) Produção de ovos de codorna; 
  8) Produção de porquinhos da Índia; 
  9) Aquaponia; 
  10)Produção de larvas de moscas; 
  11)Produção de ruminantes; 
  12)Produção de suínos; 
  13)Biodigestor; 
  14)Sistema de tratamento de água potável; 
  15)Carvoaria artesanal.

Provocação da Disciplina: O time de arquitetos da ong “FIAP 
Agriculturando com tecnologia” foi contratada para realizar uma consultoria 
tecnológica para medir o desempenho produtivo de uma cooperativa de 
produtores rurais que implementam o Sisteminha em suas propriedades.

A cooperativa é composta por um total de 1008 produtores ruais, dotados, 
cada qual, de um aplicativo mobile desenvolvido pela própria cooperativa que 
permite submeter a produção diária de: ovos de galinha, ovos de codorna e
quantidade de frangos e de peixes abatidos. Para utilizar o aplicativo, o agricultor deve realizar um cadastro contendo seus dados pessoais e informações da 12 propriedade rural, como por exemplo: tamanho da área de trabalho da propriedade.

O aplicativo da cooperativa permite também que ao agricultor informe a 
quantidade excedente dos itens produzidos. Essa informação é útil para que a 
cooperativa organize uma operação logística de coleta da produção excedente 
de cada agricultor para que seja então direcionada para um de muitos 
mercadinhos da cooperativa. A parte proporcional da venda realizada pelos 
mercadinhos retorna em dinheiro para cada agricultor.
O grupo deve aplicar os conceitos de um DW que permitam o 
armazenamento e análise dos dados produzidos pelos agricultores da
cooperativa. Realize as entregas 1 e 2 e participe da entrega de uma solução 
tecnológica que deve contribuir para a melhoria da vida de milhares de pessoas
</details>

## Entrega 1 – Arquitetura de Fluxo de dados do DW:
Desenhe uma arquitetura de fluxo de dados para o projeto do DW. Considere extrações da parte Back-end do Sistema mobile da cooperativa. Considere, no projeto de arquitetura, mecanismos que garantam a qualidade dos dados.

## Entrega 2 – Modelagem Dimensional:
Faça a MODELAGEM DIMENSIONAL de um DATA MART para armazenar os dados coletados pelo aplicativo da cooperativa que permita responder a perguntas de negócio (forneça para cada item a consulta SQL correspondente):

Estudo do comportamento do agricultor:

- A cooperativa está interessada em conhecer a evolução da produção dos itens ovos de galinha, ovos de codorna e quantidade de frangos e de peixes abatidos. Essa informação é especialmente útil para avaliar se os mercadinhos correm algum risco de sofrer desabastecimento. É importante que essa informação apresente os valores dos excedentes de cada mês ao longo do ano;
- A cooperativa está interessada em conhecer a lista dos 10 agricultores que produzem menos, considerando cada tipo de alimento, para apoia-los com treinamentos para melhorarem seu desempenho. 
- A cooperativa também está interessada em conhecer a lista dos 10 agricultores que mais produzem, considerando cada tipo de alimento, para identificar eventuais melhorias no processo de produção de alimentos que possa ser replicada aos demais agricultores;

## Estrutura do projeto

- [Arquitetura](./arquitetura/)

Arquitetura do projeto de DW com nosso diagrama de fluxo de dados desenhado pelo time de arquitetos da ong “FIAP Agriculturando com tecnologia”.

- [Modelagem](./modelagem/)

Scripts para criar e popular o banco de dados do projeto de DW. 

- [BI](./bi/)

Visualização dos dados no aplicativo Power BI.


## Extra: Dashboard

<img src="./bi/dashboard powerbi.png" alt="dashboard" width="700">

Acesso ao Dashboard: [PowerBI](./bi/Dashboard.pbix)

## Grupo
- Felipe Toscano da Silva – RM 81515
- Gabriel Siqueira Petillo – RM 81238
- Giovanna Marinho Pereira de Godoy – RM 80534
- Jean Jacques Nascimento Barros – RM 81524
- Vinicius Mota Pereira Silva – RM 80101
