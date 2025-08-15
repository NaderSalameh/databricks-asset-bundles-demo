# test_datetime_utils.py
import datetime
from utils.datetime_utils import timestamp_to_date_col


def test_timestamp_to_date_col(spark):

    # create dataframe with a known timestamp column using datetime object
    data = [(datetime.datetime(2025, 4, 10, 10, 30, 0),)]
    schema = "ride_timestamp timestamp"
    df = spark.createDataFrame(data, schema=schema)
    
    # use the utility to add a date column
    result_df = timestamp_to_date_col(spark, df, "ride_timestamp", "ride_date")
    
    # assert that the extracted date matches the expected value
    row = result_df.select("ride_date").first()

    expected_date = datetime.date(2025, 4, 10)  # expected: 2025-04-10

    assert row["ride_date"] == expected_date