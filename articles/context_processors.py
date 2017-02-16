def categories(request):
    """
    Returns a template variable to access the facebook app id.
    """
    from .models import Category
    return {'categories': Category.with_count.all()}