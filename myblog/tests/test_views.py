from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from myblog.models import Post, Tag
from myblog.views import PostDetailView


class TestBlogPageListView(TestCase):

    def test_blog_url_shows_links_to_all_posts(self):
        # setup a post
        post1 = Post(
            title="First Post Title",
            pub_date=timezone.now(),
            content="Content for the first post",
        )
        post1.save()

        # setup another post
        post2 = Post(
            title="Second Post Title",
            pub_date=timezone.now(),
            content="content for the second post",
        )
        post2.save()

        response = self.client.get('/blog/')

        # check we used the right template
        self.assertTemplateUsed(response, 'post_list.html')

        # check we passed the posts to the template

        # check that the post titles appear on page
        self.assertIn(post1.title, response.content)
        self.assertIn(post2.title, response.content)

        # check that the page also has links to the individual post pages
        post1_url = reverse('post_detail', args=[post1.pk, ])
        self.assertIn(post1_url, response.content)

        post2_url = reverse('post_detail', args=[post2.pk, ])
        self.assertIn(post2_url, response.content)


#class TestBlogDetailView(TestCase):

#    def test_post_url_slug(self):
        # setup a post first
#        post = Post()
#
