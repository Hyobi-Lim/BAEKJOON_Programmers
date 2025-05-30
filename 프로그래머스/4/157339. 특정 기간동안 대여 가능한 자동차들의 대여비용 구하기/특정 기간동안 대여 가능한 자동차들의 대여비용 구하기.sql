-- 코드를 입력하세요
SELECT CAR_ID, A.CAR_TYPE, FLOOR(DAILY_FEE*((100-DISCOUNT_RATE)/100)*30) FEE
FROM CAR_RENTAL_COMPANY_CAR A
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN B ON A.CAR_TYPE=B.CAR_TYPE AND DURATION_TYPE='30일 이상'
WHERE (A.CAR_TYPE='세단' OR  A.CAR_TYPE='SUV') AND 
        CAR_ID NOT IN (SELECT CAR_ID
                       FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                       WHERE END_DATE>='2022-11-01' AND START_DATE<='2022-12-01')
        AND FLOOR(DAILY_FEE*((100-DISCOUNT_RATE)/100)*30) BETWEEN 500000 AND 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC;