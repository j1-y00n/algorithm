-- 코드를 입력하세요
SELECT CART_ID
FROM (
    SELECT CART_ID, NAME
    FROM CART_PRODUCTS
    WHERE NAME IN ('MILK', 'Yogurt')
    GROUP BY CART_ID, NAME    
) AS new
GROUP BY CART_ID
HAVING COUNT(*) >= 2
ORDER BY CART_ID;