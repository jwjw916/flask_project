#__init__.py
from flask import Flask

def create_app():
        
    app = Flask(__name__)

    @app.route('/about_me')
    def about_me():
        return f'저는 {__name__}입니다.'

    # 라우팅 주소를 만드실 때는 /경로명 까지만 적어줍니다. 
    # 그 다음에 만들어질 하위 경로도 /경로명 
    @app.route('/hello')
    def hello():
        return f'안녕하세요'

    @app.route('/bye')
    def bye():
        return f'안녕히 가세요'
        
    return app
