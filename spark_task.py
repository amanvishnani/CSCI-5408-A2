from pyspark import SparkConf, SparkContext

try:
    sc
except Exception as e:
    sc = None
    conf = SparkConf().setAppName("Assignment2")
    sc = SparkContext(conf=conf)

keywords = ["education", "canada", "university", "dalhousie", "expensive", "faculty", "graduate"]
bigram_keywords = ["good school", "bad school", "computer science"]


def bigrams(wordList):
    new_words = []
    for i in range(len(wordList) - 1):
        new_words.append((wordList[i], wordList[i + 1]))
    return new_words


fileRDD = sc.textFile('file:///home/ubuntu/output.txt')

sentences = fileRDD.map(lambda sentence: sentence.lower())
sentences_word = sentences.map(lambda line: line.split(" ")).cache()

# Pipeline 1
words = sentences_word.flatMap(lambda x: x)
filtered_word = words.filter(lambda word: word in keywords)

# Pipeline 2
bigram_words = sentences_word.flatMap(lambda s: bigrams(s))
bigram_words = bigram_words.map(lambda word_tuple: " ".join([word_tuple[0], word_tuple[1]]))
bigram_words = bigram_words.filter(lambda word: word in bigram_keywords)

# Concatenate
final_words = filtered_word.union(bigram_words)
final_word_count = final_words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

final_word_count.cache()
final_word_count.saveAsTextFile("/root/spark_output")
final_word_count.collect()
