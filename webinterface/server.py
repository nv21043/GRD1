from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background-image: url('/static/001.png'); /* Updated to 001.png */
                background-size: cover;
                background-position: center;
            }
            .container {
                width: 80%;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
                margin-bottom: 20px;
            }
            button {
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                cursor: pointer;
                transition: background-color 0.3s ease, box-shadow 0.3s ease, font-weight 0.3s ease;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            button:hover {
                background-color: #0056b3;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                font-weight: bold;
            }
            .dropdown {
                position: relative;
                display: inline-block;
                margin: 0 10px;
            }
            .dropbtn {
                background-color: #007bff;
                color: white;
                padding: 10px 20px;
                font-size: 16px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease, box-shadow 0.3s ease, font-weight 0.3s ease;
            }
            .dropbtn:hover {
                background-color: #0056b3;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                font-weight: bold;
            }
            .dropdown-content {
                display: none;
                position: absolute;
                background-color: #f9f9f9;
                min-width: 160px;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
                border-radius: 5px;
                overflow: hidden;
            }
            .dropdown-content a {
                color: black;
                padding: 12px 16px;
                text-decoration: none;
                display: block;
                text-align: left;
                transition: font-weight 0.3s ease;
            }
            .dropdown-content a:hover {
                background-color: #f1f1f1;
                font-weight: bold;
            }
            .dropdown:hover .dropdown-content {
                display: block;
            }
            .dropdown:hover .dropbtn {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Royal Academy of Police</h1>
            <div class="dropdown">
                <button class="dropbtn">Academic</button>
                <div class="dropdown-content">
                    <a href="/bachelors">Bachelors Degree</a>
                    <a href="/masters">Masters Degree</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">E-learning Training</button>
                <div class="dropdown-content">
                    <a href="/elearning/microsoft">Microsoft</a>
                    <a href="/elearning/icdl">ICDL</a>
                    <a href="/elearning/network">NETWORK (CCNA)</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">Other Trainings</button>
                <div class="dropdown-content">
                    <a href="/other/english">English</a>
                    <a href="/other/ielts">IELTS</a>
                    <a href="/other/office_clerk">Office Clerk Training</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/bachelors')
@app.route('/masters')
@app.route('/elearning/microsoft')
@app.route('/elearning/icdl')
@app.route('/elearning/network')
@app.route('/other/english')
@app.route('/other/ielts')
@app.route('/other/office_clerk')
def show_hi():
    return "<h1>Hi! how can I help you?</h1>"

@app.route('/user/<username>')
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
            }
            .container {
                width: 80%;
                margin: 50px auto;
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
                margin-bottom: 20px;
            }
            button {
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                cursor: pointer;
                transition: background-color 0.3s ease, box-shadow 0.3s ease, font-weight 0.3s ease;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            button:hover {
                background-color: #0056b3;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Show Post</h1>
            <p>Post %d</p>
            <button onclick="window.location.href='/'">Home</button>
        </div>
    </body>
    </html>
    """ % post_id

if __name__ == '__main__':
    app.run(debug=True, port=8000)
