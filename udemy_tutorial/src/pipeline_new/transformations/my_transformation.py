import dlt
@dlt.table(
    name = "demo"
)
def demo():
    return spark.range(100)