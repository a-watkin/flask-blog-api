
from flask import Blueprint, jsonify, request
from .post import Post


post_blueprint = Blueprint('post', __name__)


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


@post_blueprint.route('/<int:post_id>', methods=['POST'])
def create_post(post_id):
    pass


@post_blueprint.route('/api/post/<int:id>', methods=['PUT'])
def edit_post(id):
    """
    Update the specified post.
    """
    print('getting here?')
    print('post_id is ', post_id)
    args = request.args.to_dict()
    print('args is: ', args)
    p = Post()
    post_data = p.get_post(post_id)

    if post_data:
        print('what is post data here?', post_data)
        # for key, value in args:
        #     setattr(p, key, args[key])

        # if args has a key that is also in p then
        # update the value of p to be that of args
        print('args values are ', args)
        for key in args.keys():
            if key in post_data[0]:
                post_data[0][key] = args[key]
            print(key)

        # make new instance of Post with the data from the db
        p = Post(post_data[0])

        import inspect
        print(inspect.getmembers(p, lambda a: not(inspect.isroutine(a))))

        return jsonify(post_data), 201
    else:
        print('resource does not exist')
    return jsonify({}), 404
