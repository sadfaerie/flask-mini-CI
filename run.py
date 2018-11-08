 # -*- coding: utf-8 -*-

import os
from datetime import datetime
from flask import Flask, redirect, render_template, request



app = Flask(__name__)

messages = []

def add_messages(username, message):
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    #messages.append("({}) {}: {}".format(now, username, message))
    messages.append(messages_dict)

def get_all_messages():
    """ Get all of the messages and separate them by a 'br'"""
    #return "<br>".join(messages)
    return messages

@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    #return "To send a message use /USERNAME/MESSAGE"
    if request.method == "POST":
        #print(request.form)
        with open("data/users.txt", "a") as user_list:
            user_list.writelines(request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route("/<username>")
def user(username):
    """Display chat messages """
    #return "Hi " + username
    #return "<h1>Welcome, {0}</h1> {1}".format(username.upper(), get_all_messages())
    messages = get_all_messages()
    return render_template("chat.html",
                            username=username, chat_messages=messages)


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    #return "{0}: {1}".format(username, message)
    add_messages(username, message)
    return redirect(username)


if __name__ == "__main__":
    app.run(port=5003,debug=True)
