-- 코드를 입력하세요
SELECT MONTH, CAR_ID, RECORDS
FROM (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE MONTH(START_DATE) BETWEEN 8 AND 10
    GROUP BY CAR_ID
    HAVING COUNT(CAR_ID) >= 5
) AS NEW_CAR_ID
INNER JOIN (
    SELECT 
        CAR_ID, 
        MONTH(START_DATE) AS MONTH, 
        COUNT(CAR_ID) AS RECORDS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE MONTH(START_DATE) BETWEEN 8 AND 10
    GROUP BY MONTH(START_DATE), CAR_ID
    ORDER BY CAR_ID, START_DATE
) AS NEW_DATE 
USING(CAR_ID)
ORDER BY 
    MONTH,
    CAR_ID DESC;
    
    



# SELECT CAR_ID, START_DATE
# , COUNT(CAR_ID) AS C_M
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE MONTH(START_DATE) BETWEEN 8 AND 10
# GROUP BY MONTH(START_DATE), CAR_ID
# ORDER BY CAR_ID, START_DATE


# SELECT CAR_ID, START_DATE
# , COUNT(CAR_ID)
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE MONTH(START_DATE) BETWEEN 8 AND 10
# GROUP BY CAR_ID
# HAVING COUNT(CAR_ID) >= 5
# ORDER BY CAR_ID