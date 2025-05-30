from flask import jsonify, request
from backend.api import api_bp
from backend.services.search_service import SearchService
from backend.config import storage

search_service = SearchService(storage)


@api_bp.route('/authors/<string:author>/articles', methods=['GET'])
def get_author_articles(author):
    articles = search_service.get_articles_by_author(author)
    return jsonify({
        'success': True,
        'data': [article.to_dict() for article in articles]
    })


@api_bp.route('/authors/<string:author>/collaborators', methods=['GET'])
def get_author_collaborators(author):
    collaborators = search_service.get_collaborators(author)
    return jsonify({
        'success': True,
        'data': collaborators
    })


@api_bp.route('/authors/<string:author>/coauthor-articles', methods=['GET'])
def get_author_coauthor_articles(author):
    coauthor = request.args.get('coauthor', '')

    if coauthor:
        articles = search_service.get_coauthor_articles(author, coauthor)
        return jsonify({
            'success': True,
            'data': articles
        })
    else:
        return jsonify({
            'success': False,
            'message': 'empty coauthor name'
        })
