import os
from dotenv import load_dotenv
import tweepy

# .envファイルの内容を読み込む
load_dotenv()

# tweepyのドキュメントに合わせた変数名なので、この名前でなくても良い
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# タイムラインの取得
# public_tweets = api.home_timeline()
# print(public_tweets)
# for tweet in public_tweets:
#     print(tweet.text)

# # 自分のアカウント情報を取得
# me = api.me()
# # 作成日時
# print("アカウントの作成日時：" + str(me.created_at))
# # プロフィール
# print("プロフィール：" + me.description)
# # フォロワー数
# print("フォロワー数：" + str(me.followers_count))
# # フォロー数
# print("フォロー数：" + str(me.friends_count))
# # リンクしたURL
# print("リンクしたURL：" + str(me.url))
# # フォロワー20件
# print("フォロワー20件：" + str(me.followers()))
# # フォロワー1件目のアカウント作成日時
# print("フォロワー1件目のアカウント作成日時：" + str(me.followers()[0].created_at))

# # 特定のユーザー情報を取得
# user = api.get_user("@yousuck2020")
# # フォロワー数
# print(user.followers_count)

# 自動ツイート
# api.update_status("テスト")
# api.update_with_media(status="テスト。", filename="1.jpg")

# 自動いいねとリツイート（tweet_idは）
# tweet_id = "1443132650084986881"
# api.create_favorite(tweet_id)
# api.retweet(tweet_id)

# 検索した投稿全てにいいねを付ける
# posts = api.search(q="Python", count=30)
# for post in posts:
#     tweet_id = post.id
#     api.create_favorite(tweet_id)