from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def time_now():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)

@app.route('/blog/')
def blog():
        return render_template('blog.html')

@app.route('/blog/')
def home():
    posts = [
        {
            'title': 'Первый пост',
            'author': 'Автор 1',
            'date': '2024-06-01',
            'content': 'Это содержимое первого поста.'
        },
        {
            'title': 'Второй пост',
            'author': 'Автор 2',
            'date': '2024-06-15',
            'content': 'Это содержимое второго поста.'
        }
    ]
    archives = ['Июнь 2024', 'Май 2024', 'Апрель 2024']
    return render_template('index.html', posts=posts, archives=archives)

@app.route('/contacts/')
def contacts():
        return render_template('contacts.html')


if __name__ == "__main__":
    app.run()
