from django.http import Http404
from django.shortcuts import render
from .models import Tweetcoords, Twitterusers

def index(request):
	return render(request, 'filter/index.html')

def filter(request):
	allTweets = Tweetcoords.objects.all()
	context = {
		'allTweets' : allTweets[:300],
	}
	return render(request, 'filter/filter.html', context)


def details(request, tweetID):
	try:
		tweet = Tweetcoords.objects.get(tweet_id = tweetID)
		user = Twitterusers.objects.get(user_id = tweet.user_id)
	except Tweetcoords.DoesNotExist as identifier:
		raise Http404('Tweet does not exist.')
	context = {
		'tweet' : tweet,
		'user' : user,
	}
	return render(request, 'filter/details.html', context)