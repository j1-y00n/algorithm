-- 코드를 입력하세요
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS
LEFT JOIN ANIMAL_INS USING (ANIMAL_ID)
WHERE ANIMAL_INS.DATETIME IS NULL
ORDER BY ANIMAL_ID;