
from flask import Blueprint, jsonify, request
from .post import Post

post_blueprint = Blueprint('posts', __name__)


@post_blueprint.route('/', methods=['GET'])
def get_posts():
    p = Post()
    posts = p.get_posts()
    return jsonify(posts)


@post_blueprint.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    print('Hello from get_post the post_id is ', post_id)
    p = Post()
    posts = p.get_post(post_id)
    return jsonify(posts)


@post_blueprint.route('/', methods=['POST'])
def create_post():
    print('hello from create_post')
    json_data = request.json
    p = Post(json_data)
    print(p)

    p.create_post()
    # this is an extra database operation
    # it ensures it's really in there at least?
    post_data = p.get_post(p.post_id)

    if post_data:
        return jsonify(post_data[0]), 201
    else:
        return jsonify({}), 409


@post_blueprint.route('/<int:post_id>', methods=['PUT'])
def edit_post(post_id):
    """
    Update the specified post.
    """
    json_data = request.json

    if json_data:
        json_data['post_id'] = post_id
        try:
            p = Post(json_data)
            post_data = p.get_post(post_id)

            # check that the post already exists
            if post_data:
                # then merge the two
                for key in json_data.keys():
                    if key in post_data[0]:
                        post_data[0][key] = json_data[key]

            # save to the db
            p.update_post(p.post_id)

            return jsonify(post_data), 201

        except Exception as e:
            print('Problem making object ', e)

    return jsonify({}), 404


@post_blueprint.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    p = Post()
    # check post exists
    post_data = p.get_post(post_id)
    if post_data:
        # method return true is the post no longer exists
        if p.remove_post(post_id):
            return jsonify({}), 200
    else:
        return jsonify({}), 404
