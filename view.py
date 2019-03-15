from app import app
from flask import render_template, request
from models import Post

@app.route('/')
def index():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
        page = request.args.get('page')
        if page and page.isdigit():
            page = int(page)
        else:
            page = 1
        pages = posts.paginate(page=page, per_page=5)
        return render_template('posts/index.html', pages=pages)
    else:
        return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
