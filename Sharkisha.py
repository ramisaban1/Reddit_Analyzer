import praw

def getComments(keyword):
    try:
        print('connecting to reddit')
        reddit = praw.Reddit(client_id='***********',
                             client_secret='****************',
                             password='******',
                             user_agent='iBot',
                             username='*******')
        print('Jankins')
        subreddit=reddit.subreddit(keyword)
        for submission in subreddit.hot(limit=20):
            for top_level_comment in submission.comments:
                if ('python' in top_level_comment.body):
                    print('Title: ', submission.title)
                    print(top_level_comment.body)
                    print('***************************************************')                
    except Exception as e:
        print (e)



print('PUPPY')



getComments('python')
