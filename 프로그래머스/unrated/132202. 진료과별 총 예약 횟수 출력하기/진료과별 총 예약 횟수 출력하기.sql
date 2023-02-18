-- 코드를 입력하세요
SELECT
    MCDP_CD AS '진료과코드', COUNT('진료과코드') AS '5월예약건수'
FROM 
    APPOINTMENT
WHERE
    DATE_FORMAT(APNT_YMD, "%Y-%m") = '2022-05'
GROUP BY
    MCDP_CD
ORDER BY
    5월예약건수,
    진료과코드;






# SELECT 
#     MCDP_CD AS '진료과코드', 
#     COUNT(MCDP_CD) AS '5월예약건수',
#     APNT_YMD
# FROM 
#     APPOINTMENT
# where
#     DATE_FORMAT(APNT_YMD, "%Y-%m") = '2022-05'
#     # YEAR(APNT_YMD) = 2022
#     # AND MONTH(APNT_YMD) = 05
#     AND APNT_CNCL_YN = 'N'
# # GROUP BY 
# #     MCDP_CD

# ORDER BY
#     '5월예약건수',
#     '진료과코드';