# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Irmafeatures(models.Model):
    datetime = models.DateTimeField(db_column='DateTime', primary_key=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='Lon', blank=True, null=True)  # Field name made lowercase.
    wind = models.BigIntegerField(db_column='Wind', blank=True, null=True)  # Field name made lowercase.
    pressure = models.BigIntegerField(db_column='Pressure', blank=True, null=True)  # Field name made lowercase.
    p_mean = models.FloatField(blank=True, null=True)
    p_min = models.FloatField(blank=True, null=True)
    p_max = models.FloatField(blank=True, null=True)
    p_var = models.FloatField(blank=True, null=True)
    p_std = models.FloatField(blank=True, null=True)
    p_sum = models.FloatField(blank=True, null=True)
    p_count = models.IntegerField(blank=True, null=True)
    storm_type = models.TextField(db_column='Storm Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'irmaFeatures'


class Kloutids(models.Model):
    screen_name = models.CharField(max_length=250)
    klout_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'kloutIDs'


class Precpsirma(models.Model):
    datetime = models.DateTimeField(db_column='DateTime', primary_key=True)  # Field name made lowercase.
    mean = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    var = models.FloatField(blank=True, null=True)
    std = models.FloatField(blank=True, null=True)
    sum = models.FloatField(blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'precpsIrma'


class Tweetcoords(models.Model):
    tweet_id = models.CharField(primary_key=True, max_length=100)
    created_at = models.DateTimeField()
    text = models.TextField(blank=True, null=True)
    user_id = models.CharField(max_length=100)
    coordinates = models.TextField(blank=True, null=True)
    location_coordinates = models.TextField(blank=True, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    place_id = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    hashtags = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweetCoords'


class Tweetfeatures(models.Model):
    tweet_id = models.CharField(primary_key=True, max_length=100)
    has_image = models.IntegerField(blank=True, null=True)
    has_hashtags = models.IntegerField(blank=True, null=True)
    has_url = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweetFeatures'


class Tweetirmatimes(models.Model):
    tweet_id = models.CharField(primary_key=True, max_length=40)
    irmatime = models.DateTimeField(db_column='irmaTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tweetIrmaTimes'
        unique_together = (('tweet_id', 'irmatime'),)


class Tweetscores(models.Model):
    tweetid = models.CharField(db_column='tweetID', primary_key=True, max_length=100)  # Field name made lowercase.
    tweetscore = models.FloatField(db_column='tweetScore')  # Field name made lowercase.
    textscore = models.FloatField(db_column='textScore')  # Field name made lowercase.
    imagescore = models.FloatField(db_column='imageScore')  # Field name made lowercase.
    gisscore = models.FloatField(db_column='gisScore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tweetScores'


class Twitterusers(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    screen_name = models.CharField(max_length=100)
    location = models.TextField(blank=True, null=True)
    verified = models.IntegerField()
    followers_count = models.IntegerField()
    friends_count = models.IntegerField()
    statuses_count = models.IntegerField()
    created_at = models.DateTimeField()
    klout_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'twitterUsers'
