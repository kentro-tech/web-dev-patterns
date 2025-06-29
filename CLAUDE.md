A FastAPI-powered breath of fresh air in Python web development.

Current Features

Designed to work with FastAPI so you can have your API and web pages server from one app
HTML generation from jinja2 or Python classes. Pick one or both!
⁠Shortcut Response class and fastapi tags
Built from the beginning with ⁠HTMX in mind
⁠Shortcut utility functions galore
Static site generation
⁠Serious documentation powered by material-for-mkdocs
Lots of tests
Planned features

⁠pydantic-powered html forms
⁠Shortcut Response class for jinja2
Installation

pip install air
Basic usage

# main.py
from fastapi import FastAPI
from air.responses import TagResponse
import air

app = FastAPI()


@app.get("/")
async def index():
    return air.Html(air.H1("Hello, world!", style="color: blue;"))
Call with fastapi CLI:


fastapi dev
Generate HTML and API
For when you need FastAPI docs but without the web pages appearing in the docs:


from fastapi import FastAPI
import air

# API app
app = FastAPI()
# HTML page app
html = air.Air()

@app.get("/api")
async def read_root():
    return {"Hello": "World"}


@html.get("/", response_class=air.TagResponse)
async def index():
    return air.H1("Welcome to Air")

# Combine into one app
app.mount("/", html)
URLs to see the results:

http://127.0.0.1:8000/
http://127.0.0.1:8000/api
http://127.0.0.1:8000/docs



uickstart
A Minimal Application
A minimal Air application:


Air Tags
Jinja2
main.py

import air

app = air.Air()

@app.get('/')
async def index():
    return air.H1('Hello, world')
So what does this code do?

First we import the air project.
Next we instantiate the Air app. air.Air is just a conveinance wrapper around fastapi.FastAPI that sets the default_response_class to be air.TagResponse
We define a GET route using @api.get, with comes with a response class of TagResponse. Now, when we return Air Tags, they are automatically rendered as HTML
We return air.H1, which renders as an <h1></h1> tag. The response type is text/html, so browsers display web pages.

Running the Application
To run your FastAPI application with uvicorn:


uvicorn main:app --reload
Where:

main is the name of your Python file (main.py)
app is the name of your FastAPI instance
--reload enables auto-reloading when you make changes to your code (useful for development)
Once the server is running, open your browser and navigate to:

http://localhost:8000 - Your application


Air Tags
Air Tags are a fast, expressive way to generate HTML. Instead of a template language, Air Tags use Python classes to represent HTML elements. This allows leveraging Python's capabilities to generate content..

What are Air Tags?
Air Tags are Python classes that render HTML. They can be combined to render web pages or small components. Air Tags are typed and documented, working well with any code completion tool.

How Air Tags work
Used individually or combined into a greater whole, every Air Tag includes a render() method. When the render method is called, it returns the HTML representation of the Air Tag, as well as all the children of the Air Tag.

This example:


>>> from air import Article, H1, P
>>> content = Article(
...     H1("Air Tags"),
...     P("Air Tags are a fast, expressive way to generate HTML.",
...             cls="subtitle")
... )
>>> content
<air.tags.Article at 0x1052f2cf0>
>>> content.render()
This is the output of the render() method for the example above:


<article>
    <h1>Air Tags</h1>
    <p class="subtitle">Air Tags are a fast, expressive way to generate HTML.</p>
</article>
Works well with SVGs
Unlike HTML, SVG tags are case-sensitive. You can access SVG tags by importing them from the air.svg module. Here's a simple example:


from air import svg

svg.Svg(
    svg.Circle(cx='50', cy='50', r='40', fill='blue'),
    width='100',
    height='100'
)
This will render the following SVG:


<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" fill="blue" />
</svg>
Custom Air Tags
The best way to define your own Air Tags is to subclass the air.Tag class. Here's a simple example:


from air import Tag

class Tasty(Tag):
    pass
Let's instantiate this class and call its render() method:


Tasty('Ice Cream', cls='dessert').render()
This will produce the following HTML:


<awesome class="desert">Ice Cream</awesome>
Functions as Custom Air Tags
Subclasses are not the only way to create custom Air Tags. You can also use functions to create Air Tags. This is particularly useful for putting together components quickly without needing to define a class. Here's an example of a function that creates a custom Air Tag for a picocss card:


def card(*content, header:str, footer:str):
    return air.Article(
        air.Header(header),
        *content,
        air.Footer(footer)
    )
We can use this function to create a card:


card(
    air.P("This is a card with some content."),
    air.P("It can have multiple paragraphs."),
    header="Card Header",
    footer="Card Footer",
).render()
Which produces the following HTML:


<article>
    <header>Card Header</header>
    <p>This is a card with some content.</p>
    <p>It can have multiple paragraphs.</p>
    <footer>Card Footer</footer>
</article>