with a as(
SELECT
block_time AS “time”,
nft_token_id AS “ape id”,
original_amount AS “sale price”
FROM nft.trades
WHERE original_currency = ‘ETH’
AND nft_contract_address = (‘\xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d’)::bytea
ORDER BY block_time DESC)
select *
from (
select “ape id” , max(“time”) as “last sale”
from a
group by “ape id”
) b
join a on a.“ape id” = b.“ape id”
where a.“time” = b.“last sale” (e