import pandas as pd
from scripts.module.helpers.GCSHelpers import GCSHelpers


class BitcoinDataTransformation:
    def __init__(
            self,
            csv_file: str,
    ) -> None:
        self.csv_file = csv_file

    def transform_data(self, output_file_location):
        """
        :return:
        """
        print("processs the data")
        df_ = pd.DataFrame()
        df = pd.DataFrame()
        result = pd.DataFrame(columns=['buying_date','buy_price','selling_date','sell_price', 'roi_percentage'])
        result.to_csv(output_file_location, encoding='utf-8', sep=',',)

        chunks = pd.read_csv(filepath_or_buffer=self.csv_file, delimiter=',', chunksize=10, low_memory=True)
        for chunk in chunks:
            chunk['EndTimestamp'] = chunk['Timestamp']
            df_ = df_.append(chunk)
            df_['Timestamp'] = df_['Timestamp'].astype('int64')
            df = df.append(
                pd.merge(
                    df_.assign(temp=1),
                    chunk.assign(temp=1),
                    on="temp",
                    how="outer",
                ).query("EndTimestamp_y - Timestamp_x > 86400 and High_y > Low_x")
                .sort_values(by='EndTimestamp_y', ascending=False)
            )
            print(df)
            result = df
            result['buying_date'] = pd.to_datetime(result['Timestamp_x'], unit='s')
            result['buy_price'] = result['Low_x']
            result['selling_date'] = pd.to_datetime(result['EndTimestamp_y'], unit='s')
            result['sell_price'] = result['High_y']
            result['roi_percentage'] = result['High_y'] - result['Low_x'] / 100
            result = result[['buying_date', 'buy_price', 'selling_date', 'sell_price', 'roi_percentage']]
            result = result.drop_duplicates(subset=['buying_date'], keep='first')
            print(f"result = {result}")
            result.to_csv(output_file_location, mode='a', encoding='utf-8', sep=',', index=False, header=False)

        return result


if __name__ == '__main__':
    import os

    local_file = GCSHelpers.download_file_from_gcs_by_url(
        file_path=os.environ['LOCAL_FILE_PATH'],
        url=os.environ['URL_FILE']
    )
    transform = BitcoinDataTransformation(os.environ['LOCAL_FILE_PATH'])
    transform.transform_data(output_file_location=os.environ['OUTPUT_FILE_PATH'])
