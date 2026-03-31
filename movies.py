"""
Приложение за управление на филми с рейтинг.
Демонстрира: Flask REST API, SQLAlchemy ORM, SQLite, CORS, CRUD операции.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# SQLite — не изисква инсталация на MySQL, базата е файл
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# --- Модели (ORM) ---

class Movie(db.Model):
    """Модел за филм."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, default=0.0)       # Средна оценка
    rating_count = db.Column(db.Integer, default=0)  # Брой гласове
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "year": self.year,
            "rating": round(self.rating, 1),
            "rating_count": self.rating_count,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M")
        }


# Създаване на таблиците
with app.app_context():
    db.create_all()


# --- API Маршрути (Routes) ---

@app.route('/movies', methods=['GET'])
def get_movies():
    """Връща всички филми. Поддържа търсене по заглавие и жанр."""
    search = request.args.get('search', '').strip()
    genre = request.args.get('genre', '').strip()

    query = Movie.query
    if search:
        query = query.filter(Movie.title.ilike(f'%{search}%'))
    if genre:
        query = query.filter(Movie.genre == genre)

    movies = query.order_by(Movie.rating.desc()).all()
    return jsonify([m.to_dict() for m in movies])


@app.route('/movies', methods=['POST'])
def add_movie():
    """Добавяне на нов филм."""
    data = request.json
    if not data.get('title') or not data.get('genre') or not data.get('year'):
        return jsonify({"error": "Всички полета са задължителни"}), 400

    movie = Movie(
        title=data['title'],
        genre=data['genre'],
        year=int(data['year'])
    )
    db.session.add(movie)
    db.session.commit()
    return jsonify(movie.to_dict()), 201


@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    """Редактиране на филм."""
    movie = Movie.query.get_or_404(movie_id)
    data = request.json
    movie.title = data.get('title', movie.title)
    movie.genre = data.get('genre', movie.genre)
    movie.year = data.get('year', movie.year)
    db.session.commit()
    return jsonify(movie.to_dict())


@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    """Изтриване на филм."""
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message": f"Филмът '{movie.title}' е изтрит"}), 200


@app.route('/movies/<int:movie_id>/rate', methods=['POST'])
def rate_movie(movie_id):
    """Гласуване за филм (оценка от 1 до 5)."""
    movie = Movie.query.get_or_404(movie_id)
    data = request.json
    new_rating = data.get('rating', 0)

    if not (1 <= new_rating <= 5):
        return jsonify({"error": "Оценката трябва да е между 1 и 5"}), 400

    # Изчисляване на новата средна оценка
    total = movie.rating * movie.rating_count + new_rating
    movie.rating_count += 1
    movie.rating = total / movie.rating_count
    db.session.commit()
    return jsonify(movie.to_dict())


@app.route('/movies/stats', methods=['GET'])
def get_stats():
    """Статистика — брой филми, средна оценка, жанрове."""
    total = Movie.query.count()
    avg_rating = db.session.query(db.func.avg(Movie.rating)).scalar() or 0
    genres = db.session.query(Movie.genre, db.func.count(Movie.id)).group_by(Movie.genre).all()

    return jsonify({
        "total_movies": total,
        "average_rating": round(float(avg_rating), 1),
        "genres": {g: c for g, c in genres}
    })


if __name__ == '__main__':
    app.run(debug=True, port=5001)
