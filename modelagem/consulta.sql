/* - A cooperativa está interessada em conhecer a evolução da produção dos itens ovos de galinha, ovos de codorna 
e quantidade de frangos e de peixes abatidos. Essa informação é especialmente útil para avaliar se os mercadinhos 
correm algum risco de sofrer desabastecimento. É importante que essa informação apresente os valores dos excedentes
de cada mês ao longo do ano;*/

SELECT 
    I.NAME, 
    D.MONTH,
    SUM(FP.QTD_EXCESS) AS EXCESS
FROM
    FACTPRODUCTION AS FP,
    ITEM AS I,
    DATE AS D
WHERE
    ITEM_ID IN (1 , 2, 3, 11)
	AND FP.ITEM_ID = I.ID
	AND FP.DATE_ID = D.ID
GROUP BY 
	I.NAME, D.MONTH;

/*- A cooperativa está interessada em conhecer a lista dos 10 agricultores que produzem menos, considerando cada tipo de alimento, 
para apoia-los com treinamentos para melhorarem seu desempenho. */

SELECT 
    I.NAME AS PRODUCT, 
    P.NAME AS PRODUCER,
    SUM(FP.QTD_PRODUCT) AS QTD
FROM
    FACTPRODUCTION AS FP,
    ITEM AS I,
    PRODUCER AS P
WHERE
    FP.ITEM_ID = I.ID
	AND FP.PRODUCER_ID = P.ID
GROUP BY PRODUCT, PRODUCER
ORDER BY QTD ASC, I.NAME
LIMIT 10;

/*- A cooperativa também está interessada em conhecer a lista dos 10 agricultores que mais produzem, considerando cada tipo de alimento, 
para identificar eventuais melhorias no processo de produção de alimentos que possa ser replicada aos demais agricultores;*/

SELECT
    I.NAME AS PRODUCT, 
    P.NAME AS PRODUCER,
    SUM(FP.QTD_PRODUCT) AS QTD
FROM
    FACTPRODUCTION AS FP,
    ITEM AS I,
    PRODUCER AS P
WHERE
    FP.ITEM_ID = I.ID
	AND FP.PRODUCER_ID = P.ID
GROUP BY PRODUCT, PRODUCER
ORDER BY QTD DESC
LIMIT 10;