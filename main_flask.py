from apiFlask import app, ApiFlask

if __name__ == "__main__":
    api_flask = ApiFlask()
    api_flask.get_list_users()
    api_flask.create_user()
    app.run(debug=True)
