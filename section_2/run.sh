docker build . -t zalora
(docker stop zalora ; docker rm zalora) > /dev/null 2>&1
docker run -it -d --rm \
  --name=zalora \
  -e LOCAL_FILE_PATH=/usr/local/bitcoin/data/bitcoin.csv \
  -e OUTPUT_FILE_PATH=/usr/local/bitcoin/result/result.csv \
  -e URL_FILE=https://storage.googleapis.com/zalora-interview-data/bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv \
  -v $PWD:/usr/local/bitcoin \
  zalora