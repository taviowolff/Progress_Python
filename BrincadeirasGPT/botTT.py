import tweepy

# Adicione suas credenciais aqui
consumer_key = "SUA_CHAVE_DE_API"
consumer_secret = "SEU_SEGREDO_DE_API"
access_token = "SEU_TOKEN_DE_ACESSO"
access_token_secret = "SEU_SEGREDO_DE_TOKEN_DE_ACESSO"

# Autentica-se com as credenciais
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Publica um tweet
api.update_status("Olá, mundo!")

# Obtém os últimos 20 tweets do seu feed de notícias
public_tweets = api.home_timeline()
for tweet in public_tweets:
  print(tweet.text)
