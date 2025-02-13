SELECT
  `Certifications`,
  `Country`,
  `Eco_Friendly_Manufacturing`,
  `Market_Trend`,
  `Recycling_Programs`,
  `Sustainability_Rating`,
  `Year`
FROM
  `da-bootcamp-2023.Gloria.sust_fash_trends` ;
  SELECT
  `country`,
  `hdi_group`,
  `human_development_index__hdi_`
FROM
  `da-bootcamp-2023.Gloria.idh_reference` ;
  SELECT
  s.`Certifications`,
  s.`Country`,
  s.`Eco_Friendly_Manufacturing`,
  s.`Market_Trend`,
  s.`Recycling_Programs`,
  s.`Sustainability_Rating`,
  s.`Year`,
  i.`hdi_group`,
  i.`human_development_index__hdi_`
FROM
  `da-bootcamp-2023.Gloria.sust_fash_trends` s
JOIN
  `da-bootcamp-2023.Gloria.idh_reference` i
ON
  s.`Country` = i.`country`;
