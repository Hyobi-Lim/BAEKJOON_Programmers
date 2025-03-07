-- 코드를 작성해주세요
SELECT DISTINCT CASE
                    WHEN 'Front End' IN (SELECT CATEGORY
                                         FROM SKILLCODES
                                         JOIN DEVELOPERS A ON SKILLCODES.CODE&DEVELOPERS.SKILL_CODE=SKILLCODES.CODE
                                         WHERE A.ID=ID)
                    AND 'Python' IN (SELECT NAME
                                     FROM SKILLCODES
                                     JOIN DEVELOPERS A ON SKILLCODES.CODE&DEVELOPERS.SKILL_CODE=SKILLCODES.CODE
                                     WHERE A.ID=ID)
                    THEN 'A'
                    WHEN 'C#' IN (SELECT NAME
                                  FROM SKILLCODES
                                  JOIN DEVELOPERS A ON SKILLCODES.CODE&DEVELOPERS.SKILL_CODE=SKILLCODES.CODE
                                  WHERE A.ID=ID)
                    THEN 'B'
                    WHEN 'Front End' IN (SELECT CATEGORY
                                         FROM SKILLCODES
                                         JOIN DEVELOPERS A ON SKILLCODES.CODE&DEVELOPERS.SKILL_CODE=SKILLCODES.CODE
                                         WHERE A.ID=ID)
                    AND 'Python' NOT IN (SELECT NAME
                                         FROM SKILLCODES
                                         JOIN DEVELOPERS A ON SKILLCODES.CODE&DEVELOPERS.SKILL_CODE=SKILLCODES.CODE
                                         WHERE A.ID=ID)
                    THEN 'C'
                    END GRADE,ID,EMAIL
FROM SKILLCODES
JOIN DEVELOPERS ON SKILLCODES.CODE&DEVELOPERS.SKILL_CODE=SKILLCODES.CODE
HAVING GRADE IS NOT NULL
ORDER BY GRADE,ID;