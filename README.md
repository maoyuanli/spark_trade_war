# About
An example of transforming and manipulating data in Spark.

Utilizes tweets stream and nltk to analyze the mainstream media sentiment on the US - China Trade War. 

# How to use
Please use your own credentials for Twitter and Quandl APIs and save them as "token.json" in the project root folder.
(just like the sample_token.json)

If use docker:
* docker build -t tradewar .
* docker run -it -p 8888:8888 tradewar bash
* jupyter lab --ip=0.0.0.0 --allow-root