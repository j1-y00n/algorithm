-- 코드를 입력하세요
SELECT  PRODUCT_CODE, (SALES_AMOUNT * PRICE) AS SALES
FROM PRODUCT
INNER JOIN (
    SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS 'SALES_AMOUNT'
    FROM OFFLINE_SALE
    GROUP BY PRODUCT_ID
) AS RESULT
USING (PRODUCT_ID)
ORDER BY 
    SALES DESC, 
    PRODUCT_CODE;