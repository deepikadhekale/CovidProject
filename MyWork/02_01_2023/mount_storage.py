# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "  3a2c0b4f-a9e7-4b91-be86-0d835427136c",
           "fs.azure.account.oauth2.client.secret": "3EQ8Q~jC8_j-gCnV7QImXDY4OIuF1YdefD5MZc1U",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/55d19ae4-2bda-40c1-a5a9-125fea481e8d/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@covidreportingdldeep.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportingdldeep/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@covidreportingdldeep.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportingdldeep/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@covidreportingdldeep.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportingdldeep/lookup",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/covidreportingdldeep/lookup")


# COMMAND ----------


