from searchtweets import load_credentials, gen_request_parameters, collect_results
from wordcloud import WordCloud, STOPWORDS

if __name__ == "__main__":

    palavra = input("Digite uma palavra para a qual deseja criar uma nuvem de palavras do Twitter\n")
    if len(palavra.split()) == 1:
        LIMIT = 100  #quantidade máxima de tweets

        stopwords = set(STOPWORDS)
        stopwords.update(["e", "mas", "http", "https", "é", "que", "de", "não",
                          "o", "pra", "para", "da", "rt"])

        arquivo = open("C:/workspace/nuvem-twitter/relatorioTwitter.txt", "w", encoding="utf-8")

        search_args = load_credentials("config.yaml",
                                       yaml_key="search_tweets",
                                       env_overwrite=False)

        query = gen_request_parameters(f"{palavra} lang:pt", results_per_call=LIMIT, granularity=None)

        tweets = collect_results(query,
                                 max_tweets=LIMIT,
                                 result_stream_args=search_args)

        for tweet in tweets:
            datas = tweet['data']

        for data in datas:
            arquivo.write(data["text"])

        arquivo.close()

        relatorioTwitter = open("C:/workspace/nuvem-twitter/relatorioTwitter.txt", "r", encoding="utf-8")
        texto = relatorioTwitter.read()

        twitterCloud = WordCloud(stopwords=stopwords,
                                 background_color="black",
                                 width=1400, height=600).generate(texto)

        twitterCloud.to_file("C:/workspace/nuvem-twitter/imagemTwitter.png")

        print("Imagem gerada! Acesse em C:/workspace/nuvem-twitter/nuvem-palavras/")
    else:
        print("Quantidade incorreta de palavras!")
