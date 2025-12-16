from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    """
    Redirects to the dashboard.
    """
    return redirect(url_for('dashboard'))

@app.route("/dashboard")
def dashboard():
    """Displays the main dashboard."""
    return render_template('dashboard.html')

@app.route("/users")
def users():
    """Displays user management page."""
    return render_template('users.html')


@app.route("/customers")
def customers():
    """Displays user management page."""
    return render_template('customers.html')


@app.route("/logs")
def logs():
    """Displays user management page."""
    return render_template('logs.html')


@app.route("/settings")
def settings():
    """Displays user management page."""
    return render_template('settings.html')


@app.route("/profile")
def profile():
    """Displays user management page."""
    return render_template('profile.html')


if __name__ == "__main__":
    app.run()
