
from flask import render_template, flash, redirect, url_for
from app import main
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rafael'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

def get_ebooks_by_author(request):
    """ HTTP Cloud Function
    Prints available ebooks by "author" (optional: "lang")
    Arg: request (flask.Request)
    """
    author = request.args.get('author', 'JRR Tolkien')
    lang = request.args.get('lang', 'en')
    author_books = print_author_books(author, lang)
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    return author_books, headers


def print_author_books(author, lang):
    """ Returns book data in plain text table """
    def sort_by_page_count(book):
        return book['volumeInfo'].get('pageCount', 0)
    books = get_google_books_data(author, lang)
    books.sort(key=sort_by_page_count, reverse=True)

    line_fmt = '{:>4} | {:>5} | {:.65}\n'
    lines = [
        '{sep}{h1}{sep}{h2}'.format(
            h1='{:^80}\n'.format('"%s" ebooks (lang=%s)' % (author, lang)),
            h2=line_fmt.format('#', 'Pages', 'Title'),
            sep='{:=<80}\n'.format('')
        )]
    for idx, book in enumerate(books, 1):
        accessInfo = book['accessInfo']
        if not accessInfo['epub']['isAvailable']:
            continue
        volumeInfo = book['volumeInfo']
        title = volumeInfo['title']
        subtitle = volumeInfo.get('subtitle')
        if subtitle is not None:
            title += ' / ' + subtitle
        count = volumeInfo.get('pageCount')
        pages = '{:,}'.format(count) if count is not None else ''
        lines.append(line_fmt.format(idx, pages, title))

    return ''.join(lines)


def get_google_books_data(author, lang):
    """ Fetches data from Google Books API """
    from requests import get

    books = []
    url = 'https://www.googleapis.com/books/v1/volumes'
    book_fields = (
        'items('
        'id'
        ',accessInfo(epub/isAvailable)'
        ',volumeInfo(title,subtitle,language,pageCount)'
        ')'
    )
    req_item_idx = 0  # Response is paginated
    req_item_cnt = 40  # Default=10, Max=40

    while True:
        params = {
            'q': 'inauthor:%s' % author,
            'startIndex': req_item_idx,
            'maxResults': req_item_cnt,
            'langRestrict': lang,
            'download': 'epub',
            'printType': 'books',
            'showPreorders': 'true',
            'fields': book_fields,
        }
        response = get(url, params=params)
        response.raise_for_status()
        book_items = response.json().get('items', None)
        if book_items is None:
            break
        books += book_items
        if len(book_items) != req_item_cnt:
            break  # Last response page
        req_item_idx += req_item_cnt

    return books
