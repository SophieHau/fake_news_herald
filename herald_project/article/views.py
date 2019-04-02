from django.shortcuts import render
from .models import *
from comment.models import *
from django.utils import timezone

def show_articles(request):
	return render(request, 'index.html', {
			'articles': Article.objects.order_by('pub_date'),
		})

def show_article(request, article_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		comment = request.POST.get('user_comment')
		new_user = User(name=username)
		new_user.save()
		new_comment = Comment(
			user=User.objects.get(id=new_user.id), 
			article=Article.objects.get(id=article_id),
			text=comment,
			pub_date=timezone.now()
			)
		new_comment.save()

	return render(request, 'article.html', {
			'article': Article.objects.get(id=article_id),
		})


