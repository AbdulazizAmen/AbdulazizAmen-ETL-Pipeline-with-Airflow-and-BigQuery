ALTER TABLE
  `gcp-project-386421.recipe_staging_dataset.dataset_udang` ADD COLUMN
IF NOT EXISTS Main_Ingredient STRING;
CREATE OR REPLACE TABLE
  `gcp-project-386421.recipe_dataset.D_dataset_udang` AS
SELECT
  IFNULL(Main_Ingredient,
    'Udang') AS Main_Ingredient,
  Title AS Recipe_Title,
  Ingredients,
  Steps,
  Loves,
  URL
FROM
  `gcp-project-386421.recipe_staging_dataset.dataset_udang`;