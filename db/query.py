import datetime

from pytz import UTC

from db.models import User, Blog, Topic


# Test 1 passed +
def create():
    u1 = User.objects.create(first_name='u1', last_name='u1')
    u1.save()
    u2 = User.objects.create(first_name='u2', last_name='u2')
    u2.save()
    u3 = User.objects.create(first_name='u3', last_name='u3')
    u3.save()

    blog1 = Blog.objects.create(title='blog1', author=u1)
    blog1.save()
    blog2 = Blog.objects.create(title='blog2', author=u1)
    blog2.save()

    blog1.subscribers.add(u1, u2)
    blog2.subscribers.add(u2)
    # blog1.save()
    # blog2.save()

    topic1 = Topic.objects.create(title='topic1', blog=blog1, author=u1)
    topic1.save()

    topic2 = Topic.objects.create(title='topic2_content', blog=blog1, author=u3,
                                  created=datetime(year=2017, month=1, day=1, tzinfo=UTC))
    topic2.save()

    topic1.likes.add(u1, u2, u3)
    # topic1.save()
    return


# Test 2 passed ++
def edit_all():
    User.objects.all().update(first_name='uu1')
    return


# Test 3 passed +++
def edit_u1_u2():
    User.objects.filter(first_name__in=['u1', 'u2']).update(first_name='uu1')
    return


# Test 4 passed ++++
# удалить пользователя с first_name u1 (функция delete_u1)
def delete_u1():
    User.objects.filter(first_name='u1').delete()
    return


# Test 5 not passed -----
# отписать пользователя с first_name u2 от блогов--------------------------
def unsubscribe_u2_from_blogs():
    # Blog.objects.filter(subscribers__user_name='u2').subscribers.remove()
    return


# Test 6 passed ++++++
# Найти топики у которых дата создания больше 2018-01-01------------------
def get_topic_created_grated():
    return Topic.objects.filter(created__gt=datetime(year=2018, month=1, day=1, tzinfo=UTC))


# Test 7 passed +++++++
def get_topic_title_ended():
    return Topic.objects.filter(title__endswith='content')


# Test 8 passed ++++++++
def get_user_with_limit():
    return User.objects.all().order_by('-id')[:2]


# Test 9 not passed ---------
def get_topic_count():
    return


# Test 10 not passed ----------
def get_avg_topic_count():
    return


# Test 11 not passed -----------
def get_blog_that_have_more_than_one_topic():
    return


# Test 12 passed ++++++++++++
def get_topic_by_u1():
    return Topic.objects.filter(author__first_name='u1')


# Test 13 passed +++++++++++++
def get_user_that_dont_have_blog():
    return User.objects.filter(blog__isnull=True).order_by('pk')


# Test 14 not passed --------------
def get_topic_that_like_all_us():
    return


# Test 15 passed +++++++++++++++
def get_topic_that_dont_have_like():
    return Topic.objects.filter(likes__isnull=True)


    # import db.query
    #
    # def db_view(request):
    #     my_lines = []
    #     result = db.query.get_topic_that_dont_have_like()
    #     my_lines.append("Ready")
    #     return render(request, 'db_view.html', context={'my_lines': my_lines})
