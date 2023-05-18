ALTER TABLE
  `gcp-project-386421.recipe_staging_dataset.dataset_ikan` ADD COLUMN
IF NOT EXISTS Main_Ingredient STRING;
CREATE OR REPLACE TABLE
  `gcp-project-386421.recipe_dataset.D_dataset_ikan` AS
SELECT
  IFNULL(Main_Ingredient,
    'Ikan') AS Main_Ingredient,
  Title AS Recipe_Title,
  Ingredients,
  Steps,
  Loves,
  URL
FROM
  `gcp-project-386421.recipe_staging_dataset.dataset_ikan`;