from db.models import User, Blog, Topic
import datetime
# from django.util import datetime

# from django.db.models import Q


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
    topic2 = Topic.objects.create(title='topic2_content', blog=blog1, author=u3, created='2017-01-01')
    topic2.save()

    topic1.likes.add(u1, u2, u3)
    # topic1.save()
    return


def edit_all():
    User.objects.all().update(first_name='uu1')
    return


def edit_u1_u2():
    User.objects.filter(first_name__in=['u1', 'u2']).update(first_name='uu1')
    return


# удалить пользователя с first_name u1 (функция delete_u1)
def delete_u1():
    User.objects.filter(first_name='u1').delete()
    return

# отписать пользователя с first_name u2 от блогов--------------------------
def unsubscribe_u2_from_blogs():
    Blog.objects.filter(subscribers__user_name='u2').subscribers.remove()
    return

# Найти топики у которых дата создания больше 2018-01-01------------------
def get_topic_created_grated():
    topics = Topic.objects.filter(created__gt=datetime.date(2018, 1, 1))
    return


def get_topic_title_ended():
    return


def get_u_with_limit():
    return


def get_topic_count():
    return


def get_avg_topic_count():
    return


def get_blog_that_have_more_than_one_topic():
    return


def get_topic_by_u1():
    return


def get_u_that_dont_have_blog():
    return


def get_topic_that_like_all_us():
    return


def get_topic_that_dont_have_like():
    return
