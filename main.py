from app import create_app


stat_app = create_app()

if __name__ == '__main__':
    stat_app.run(host='0.0.0.0', port=80, debug=True)
