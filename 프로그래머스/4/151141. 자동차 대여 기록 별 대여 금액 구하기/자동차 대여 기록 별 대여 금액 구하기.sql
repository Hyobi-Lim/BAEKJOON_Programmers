-- 코드를 입력하세요
SELECT HISTORY_ID, CASE
                    WHEN DATEDIFF(END_DATE,START_DATE)+1>=90 THEN FLOOR((DATEDIFF(END_DATE,START_DATE)+1)*DAILY_FEE*(100-(SELECT DISCOUNT_RATE
                                                                                                                          FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                                                                                          WHERE CAR_TYPE='트럭' AND DURATION_TYPE='90일 이상'))/100)
                    WHEN DATEDIFF(END_DATE,START_DATE)+1>=30 THEN FLOOR((DATEDIFF(END_DATE,START_DATE)+1)*DAILY_FEE*(100-(SELECT DISCOUNT_RATE
                                                                                                                          FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                                                                                          WHERE CAR_TYPE='트럭' AND DURATION_TYPE='30일 이상'))/100)
                    WHEN DATEDIFF(END_DATE,START_DATE)+1>=7 THEN FLOOR((DATEDIFF(END_DATE,START_DATE)+1)*DAILY_FEE*(100-(SELECT DISCOUNT_RATE
                                                                                                                         FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                                                                                         WHERE CAR_TYPE='트럭' AND DURATION_TYPE='7일 이상'))/100)
                    ELSE (DATEDIFF(END_DATE,START_DATE)+1)*DAILY_FEE
                    END FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A
JOIN CAR_RENTAL_COMPANY_CAR B ON A.CAR_ID=B.CAR_ID
WHERE CAR_TYPE='트럭'
ORDER BY FEE DESC, HISTORY_ID DESC;