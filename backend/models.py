# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Academic(models.Model):
    academicresearchid = models.AutoField(db_column='academicResearchID', primary_key=True)  # Field name made lowercase.
    museumid = models.ForeignKey('Museum', models.DO_NOTHING, db_column='museumID')  # Field name made lowercase.
    academicresearchtime = models.CharField(db_column='academicResearchTime', max_length=45)  # Field name made lowercase.
    academicresearchtitle = models.CharField(db_column='academicResearchTitle', max_length=45)  # Field name made lowercase.
    academicresearchlink = models.CharField(db_column='academicResearchLink', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'academic'


class Collection(models.Model):
    collectionid = models.AutoField(db_column='CollectionID', primary_key=True)  # Field name made lowercase.
    museumid = models.ForeignKey('Museum', models.DO_NOTHING, db_column='museumID')  # Field name made lowercase.
    collectionname = models.CharField(db_column='collectionName', max_length=45)  # Field name made lowercase.
    collectionintroduction = models.TextField(db_column='collectionIntroduction', blank=True, null=True)  # Field name made lowercase.
    collection_age = models.TextField(blank=True, null=True)
    collectionimage = models.TextField(db_column='collectionImage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collection'


class Education(models.Model):
    educationid = models.AutoField(db_column='educationID', primary_key=True)  # Field name made lowercase.
    museumid = models.ForeignKey('Museum', models.DO_NOTHING, db_column='museumID')  # Field name made lowercase.
    educationname = models.CharField(db_column='educationName', max_length=45)  # Field name made lowercase.
    educationlink = models.CharField(db_column='educationLink', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'education'


class Exhibition(models.Model):
    exhibitionid = models.AutoField(db_column='exhibitionID', primary_key=True)  # Field name made lowercase.
    museumid = models.ForeignKey('Museum', models.DO_NOTHING, db_column='museumID')  # Field name made lowercase.
    exhibitiontime = models.CharField(db_column='exhibitionTime', max_length=128, blank=True, null=True)  # Field name made lowercase.
    exhibitiontheme = models.CharField(db_column='exhibitionTheme', max_length=128, blank=True, null=True)  # Field name made lowercase.
    exhibitionintroduction = models.TextField(db_column='exhibitionIntroduction', blank=True, null=True)  # Field name made lowercase.
    exhibitionlocation = models.TextField(db_column='exhibitionLocation', blank=True, null=True)  # Field name made lowercase.
    exhibitiontel = models.TextField(db_column='exhibitionTel', blank=True, null=True)  # Field name made lowercase.
    exhibitionthinglist = models.TextField(db_column='exhibitionThingList', blank=True, null=True)  # Field name made lowercase.
    exhibition_picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exhibition'


class Explanation(models.Model):
    explanationid = models.AutoField(db_column='explanationID', primary_key=True)  # Field name made lowercase.
    explanationname = models.CharField(db_column='explanationName', max_length=45)  # Field name made lowercase.
    explainerid = models.IntegerField(db_column='explainerID')  # Field name made lowercase.
    explanationtime = models.IntegerField(db_column='explanationTime')  # Field name made lowercase.
    explanationlanguage = models.TextField(db_column='explanationLanguage')  # Field name made lowercase.
    recommendedtime = models.FloatField(db_column='recommendedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'explanation'


class Museum(models.Model):
    museumid = models.PositiveIntegerField(db_column='museumID', primary_key=True)  # Field name made lowercase.
    museumname = models.CharField(db_column='museumName', max_length=45)  # Field name made lowercase.
    introduction = models.TextField(blank=True, null=True)
    opentime = models.TextField(blank=True, null=True)
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=45, blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    museum_introduction = models.TextField(blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    annual_visits = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)
    admission_fee = models.TextField(blank=True, null=True)
    building_time = models.CharField(max_length=45, blank=True, null=True)
    collection_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'museum'


class Museumnews(models.Model):
    newsid = models.AutoField(db_column='newsID', primary_key=True)  # Field name made lowercase.
    museumid = models.ForeignKey(Museum, models.DO_NOTHING, db_column='museumID')  # Field name made lowercase.
    newstitle = models.CharField(db_column='newsTitle', max_length=45)  # Field name made lowercase.
    newstime = models.DateField(db_column='newsTime')  # Field name made lowercase.
    newsmaintext = models.TextField()
    positive_negative = models.CharField(db_column='positive/negative', max_length=45)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'museumnews'


class Museumrank(models.Model):
    museumid = models.ForeignKey(Museum, models.DO_NOTHING, db_column='museumID', primary_key=True)  # Field name made lowercase.
    rank1 = models.PositiveIntegerField(unique=True)
    rank2 = models.PositiveIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'museumrank'
        unique_together = (('museumid', 'rank1', 'rank2'),)


class Usercomments(models.Model):
    commentid = models.AutoField(db_column='commentID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    museumid = models.ForeignKey(Museum, models.DO_NOTHING, db_column='museumID')  # Field name made lowercase.
    comment = models.TextField()
    sentianalysis_environment = models.PositiveIntegerField(db_column='sentiAnalysis_environment')  # Field name made lowercase.
    sentianalysis_exhibit = models.IntegerField(db_column='sentiAnalysis_exhibit')  # Field name made lowercase.
    sentianalysis_service = models.IntegerField(db_column='sentiAnalysis_service')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usercomments'


class Userroles(models.Model):
    userroles = models.CharField(db_column='userRoles', primary_key=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userroles'


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)
    idcard = models.CharField(db_column='IDcard', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.TextField()
    userrole = models.ForeignKey(Userroles, models.DO_NOTHING, db_column='userRole')  # Field name made lowercase.
    usercreatedate = models.DateTimeField(db_column='userCreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
