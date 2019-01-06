
from flask import Blueprint, jsonify
from .post import Post


post_blueprint = Blueprint('post', __name__)


@post_blueprint.route('/', methods=['GET'])
def test():
    p = Post()
    posts = p.get_posts()
    return jsonify(posts)


@post_blueprint.route('/api/posts/', methods=['GET'])
def get_posts():
    p = post.Post()
    posts = p.get_posts()
    return jsonify(posts)


@post_blueprint.route('/api/posts/<int:id>', methods=['GET'])
def get_post(id):
    return {}


@post_blueprint.route('/api/posts/', methods=['POST'])
def create_post():
    return {}


@post_blueprint.route('/api/posts/<int:id>', methods=['PUT'])
def edit_post(id):
    return {}
