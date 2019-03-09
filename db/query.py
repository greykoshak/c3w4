from db.models import User, Blog, Topic


def create():
    u1 = User.objects.create(first_name='u1', last_name='u1')
    u1.save()
    u2 = User.objects.create(first_name='u2', last_name='u2')
    u2.save()
    u3 = User.objects.create(first_name='u3', last_name='u3')
    u3.save()

    blog1 = Blog.objects.create(title='blog1', author='u1')
    blog1.save()
    blog2 = Blog.objects.create(title='blog2', author='u1')
    blog2.save()

    blog1.subscribers.add(u1, u2)
    blog2.subscribers.add(u2)
    blog1.save()
    blog2.save()

    topic1 = Topic.objects.create(title='topic2_content', blog=blog1, author=u3, created='2017-01-01')
    topic1.save()

    topic1.likes.add(u1, u2, u3)
    topic1.save()


def edit_all():
    pass


def edit_u1_u2():
    pass


def delete_u1():
    pass


def unsubscribe_u2_from_blogs():
    pass


def get_topic_created_grated():
    pass


def get_topic_title_ended():
    pass


def get_u_with_limit():
    pass


def get_topic_count():
    pass


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_u_that_dont_have_blog():
    pass


def get_topic_that_like_all_us():
    pass


def get_topic_that_dont_have_like():
    pass
