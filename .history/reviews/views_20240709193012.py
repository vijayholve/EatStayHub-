from django.shortcuts import render
from base.models import dish,Reviews,restaurants
from django import template
from django.utils import timezone
from django.template.defaulttags import register
def make_dictonery(query,list_objs):
    set_var={}
    for obj in list_objs:
        set_var[quesy.id]=time_since(query.created) 
    return set_var
        
def reviews_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    reviews_list=Reviews.objects.filter(dish=dish_obj)
    review_create={}
    for review in reviews_list:
        review_create[review.id]=time_since(review.created)
    context={"dish_obj":dish_obj,"reviews_list":reviews_list,"review_create":review_create}
    return render(request,"reviews/dish_reviews.html",context)
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
@register.filter
def time_since(value):
    now=timezone.now()
    diff=now-value
    if diff.days == 0:
        if diff.seconds >= 0 and diff.seconds < 60:
            return 'just now'
        if diff.seconds >= 60 and diff.seconds < 3600:
            minutes = diff.seconds // 60
            return f'{minutes} minutes ago'
        if diff.seconds >= 3600 and diff.seconds < 86400:
            hours = diff.seconds // 3600
            return f'{hours} hours ago'
    if diff.days == 1:
        return 'yesterday'
    if diff.days < 7:
        return f'{diff.days} days ago'
    if diff.days < 30:
        weeks = diff.days // 7
        return f'{weeks} weeks ago'
    if diff.days < 365:
        months = diff.days // 30
        return f'{months} months ago'
    years = diff.days // 365
    return f'{years} years ago'