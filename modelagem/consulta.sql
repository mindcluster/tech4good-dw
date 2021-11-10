/* - A cooperativa está interessada em conhecer a evolução da produção dos itens ovos de galinha, ovos de codorna e quantidade de frangos e de peixes abatidos. 
Essa informação é especialmente útil para avaliar se os mercadinhos correm algum risco de sofrer desabastecimento. 
É importante que essa informação apresente os valores dos excedentes de cada mês ao longo do ano;*/

SELECT * FROM tech4good.FACTPRODUCTION WHERE ITEM_ID IN (1, 2, 3, 11) order by DATE_ID;