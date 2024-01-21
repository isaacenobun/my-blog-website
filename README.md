# my-blog-website

I built a blog platform that allows me or any other authorized individual add/edit posts that can be read by the public. I'm using the django framework for the backend, Sqlite database and bootswatch(bootstrap) for the frontend.

## Table of Contents

- [Project Title](#project-title)
- [Description](#description)
- [Implementation](#Implementation)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Acknowledgements](#acknowledgements)

## Description

Provide a more detailed description of your project. Explain its purpose, features, and any other relevant information.

## Implementation
<ul>
  <li>I used a virtual environment in this project - 'python3 -m venv ...'</li>
  <li>Installed django with pip3</li>
  <li>I used the default SQlite database for this project</li>
  <li>The data models migrated include a 'Post' class which has a title, author, created_on, updated_on, content and status field. Author is designed as a foreign key linked to django's native User model for user authentication.</li>
  <li>Post additions and edits will be done from the django admin dashboard and so some code was written in admin.py to organise and filter the dashboard.</li>
  <li>I used class based views in this project</li>
  <li></li>
</ul>

## Getting Started

To run this blog locally on your machine.
<ul>
  <li>Save the file locally.</li>
  <li>Open the folder my-blog-website, and type the following commands one after the other in your terminal<br>
  - source 'Env/bin/activate'<br>
  - cd blogProject<br>
  - python3 manage.py runserver</li>
</ul>

### Prerequisites

You need [python](www.python.org) installed on your system to run this successfully on your local machine.

## Acknowledgements

My sincere thanks to [Bek Brace](https://www.youtube.com/@BekBrace) for his insights that helped in building this project.