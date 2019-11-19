# Created by Benjamin Alterman, Emilia Garcia-Saravia, and Pravina Pidikiti

from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
