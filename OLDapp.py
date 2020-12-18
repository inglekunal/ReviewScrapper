# git init
# git add .
# git commit -m "initial commit"
# heroku create
# git remote -v
# git push heroku master
import app

if __name__ == "__main__":
    app.run(port=8000, debug=True)  # running the app on the local machine on port 8000