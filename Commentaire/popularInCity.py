import twint

search = input("What are you searching for? ")
city = input("Where? ")

c = twint.Config()
c.Search=search
c.Near=city
c.Limit=20
c.Popular_tweets=True

twint.run.Search(c)
