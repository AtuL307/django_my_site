################# PostDetailView ################
# Session
def session_stored_post(post, request):
   
        stored_posts = request.session.get("stored_post")
        if stored_posts is not None:
            is_saved_for_later = post.id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

def data_fetch(post, comment_form, is_saved_for_later):
    context ={
        'post': post,
        'post_tag': post.tag.all(),
        'comment_form': comment_form,
        'comments': post.comments.all().order_by("-id"),
        "saved_for_later" : is_saved_for_later,
    }
    return context
