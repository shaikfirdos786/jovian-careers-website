from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Security Engineer',
        'location': 'Remote',
        'salary': 'Rs. 1,00,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientis',
        'location': 'Bangalore, INDIA',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Hyderabad, INDIA',
        'salary': 'Rs. 7,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'San Francisco, USA',
    },
]


@app.route('/')
def hello_jovian():
    return render_template('home.html', jobs=JOBS, company_name='Wipro')


@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
