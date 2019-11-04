keywords = ["education", "canada", "university", "dalhousie", "expensive", "faculty", "graduate", "good-school", "bad-school", "computer-science"]
bigram_keywords = [("good school", "good-school"), ("bad school", "bad-school"),
                   ("computer science", "computer-science")]


def replaceWords(sentence):
    for m, n in bigram_keywords:
        sentence = sentence.replace(m, n)
    return sentence


# Read file
fileRDD = sc.textFile('file:///home/ubuntu/output.txt')


sentences = fileRDD.map(lambda sentence: sentence.lower()).map(replaceWords)
words = sentences.flatMap(lambda line: line.lower().split(" "))

filtered_word = words.filter(lambda word: word in keywords)
filtered_word_count = filtered_word.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
filtered_word_count.collect()
