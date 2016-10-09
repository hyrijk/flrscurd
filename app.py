from flask import Flask, jsonify, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy()


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.TEXT(), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'content': self.content,
            'link': url_for('get_article', id=self.id, _external=True)
        }

    @staticmethod
    def from_json(json):
        author = json.get('author')
        title = json.get('title')
        content = json.get('content')
        return Article(author=author, title=title, content=content)

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    articles_json = [article.to_json() for article in articles]
    return jsonify(articles=articles_json)


@app.route('/article/<int:id>', methods=['GET'])
def get_article(id):
    article = Article.query.get_or_404(id)
    return jsonify(article.to_json())


@app.route('/article/<int:id>', methods=['DELETE'])
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return jsonify(message="删除成功")


@app.route('/article/<int:id>', methods=['PUT'])
def update_article(id):
    article = Article.query.get_or_404(id)
    update_attr = request.json
    for k, v in update_attr.items():
        setattr(article, k, v)
    db.session.add(article)
    db.session.commit()
    return jsonify(article.to_json())


@app.route('/articles', methods=['POST'])
def add_article():
    article = Article.from_json(request.json)
    db.session.add(article)
    db.session.commit()
    return jsonify(article.to_json())


@app.after_request
def allow_cross_domain(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    app.run(debug=True)
