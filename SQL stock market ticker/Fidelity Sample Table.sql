WITH fidelity AS (
    SELECT * FROM (VALUES
        ('GME', '100', '20,000')
        ('AMC', '75',   '1,000')
    ) AS titles(
        symbol, shares, totalValue
    )
)

SELECT * FROM fidelity;