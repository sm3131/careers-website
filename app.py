from flask import Flask, render_template

app = Flask(__name__)

jobList = {
    1: {
        "id": 1,
        "title": "Junior Front End Developer",
        "location": "Remote",
        "company": "Company X",
        "description": "Junior front end developer working with Laravel Blade, Tailwind CSS, and Javascript",
        "requirements": ["Laravel Blade", "Tailwind CSS", "Javascript"],
        "salary": 70000,
    },
    2: {
        "id": 2,
        "title": "Junior Back End Developer",
        "location": "Remote",
        "company": "Company Y",
        "description": "Junior back end developer working with Laravel, PHP, and MySQL",
        "requirements": ["Laravel", "PHP", "MySQL"],
        "salary": 90000,
    },
    3: {
        "id": 3,
        "title": "Junior Front End Developer",
        "location": "Remote",
        "company": "Company Z",
        "description": "Junior front end developer working with Laravel, PHP, Python, JS, and Blade",
        "requirements": ["Laravel", "PHP", "Python", "JS", "Blade"],
        "salary": 100000,
    }
}

articles = {
    1: {
        "title": "Article One",
        "author": "Cool Dude One",
        "preview": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita. Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita. Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita."
    },
    2: {
        "title": "Article Two",
        "author": "Cool Dude Two",
        "preview": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita. Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita. Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita."
    },
    3: {
        "title": "Article Three",
        "author": "Cool Dude Three",
        "preview": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita. Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita. Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis obcaecati reiciendis totam, voluptate aliquid itaque maiores sit ratione ipsam dolorem quo nihil perspiciatis doloribus! Ducimus magni asperiores dolorum aut expedita."
    },
}

@app.route("/")
def home():
    return render_template("home.html", articles=articles)

@app.route("/article/<int:article_id>")
def article(article_id):
    article = articles[article_id]
    return render_template("article.html", article=article)

@app.route("/jobs")
def jobs():
    return render_template("jobs.html", jobs=jobList)

@app.route("/job/<int:job_id>")
def job(job_id):
    job = jobList[job_id]
    return render_template("job.html", job=job)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
