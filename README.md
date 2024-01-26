# my-blog-website

I developed a blog platform that enables authorized individuals, including myself, to add/edit posts accessible to the public. The backend is powered by the Django framework, with the data stored in an SQLite database. For the frontend, I integrated Bootswatch, an extension of Bootstrap.

## Table of Contents

- [Description](#description)
- [Implementation](#Implementation)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Acknowledgements](#acknowledgements)

## Description

This project involves the development of a web application using Django. The primary purpose of the application is to manage and display posts, utilizing various Django features and best practices.

## Implementation
<ul>
  <li>Set up a virtual environment for this project using 'python3 -m venv ...'</li>
<li>Installed Django using pip3</li>
<li>Utilized the default SQLite database for this project</li>
<li>Implemented data models, including a 'Post' class featuring fields such as title, author, created_on, updated_on, content, and status. The 'Author' field is designed as a foreign key linked to Django's native User model for user authentication.</li>
<li>Configured post additions and edits through the Django admin dashboard, incorporating custom code in admin.py to enhance organization and filtering.</li>
<li>Utilized class-based views in combination with a function-based view to implement the search functionality. <small>Future plans include implementing real-time search updates with JavaScript.</small></li>
<li>Enabled HTML and CSS styling for post contents entered in the Django admin dashboard, using the 'safe' Django template language (DTL) filter.</li>
</ul>

## Getting Started

To run this blog locally on your machine.
<ul>
  <li>Save the [file](https://github.com/isaacenobun/my-blog-website) locally.</li>
  <li>Open the folder my-blog-website, and type the following commands one after the other in your terminal<br>
  - source 'Env/bin/activate'<br>
  - cd blogProject<br>
  - python3 manage.py runserver</li>
</ul>

### Prerequisites

You need [python](https://www.python.org) installed on your system to run this successfully on your local machine.

## Acknowledgements

My sincere thanks to [Bek Brace](https://www.youtube.com/@BekBrace) for his insights that helped in building this project.