from todo_app.app import create_app, db  # Correct import path

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates the tables in your database
    app.run(debug=True)
