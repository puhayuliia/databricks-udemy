from pyspark import pipelines as dp

@dp.table()
def main():
  return spark.range(100)