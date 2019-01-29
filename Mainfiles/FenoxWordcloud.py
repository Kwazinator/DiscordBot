from wordcloud import WordCloud, STOPWORDS


def dochannel(channelname):
    #comment_words = ' '
    stopwords = set(STOPWORDS)

    with open(channelname, 'r') as myfile:
        data = myfile.read()

    wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=stopwords,
                          min_font_size=10).generate(data)
    savedfile = channelname + '.png'
    wordcloud.to_file(savedfile)