# ICTENSW 2026 Architecture of a basic Flask app

Flask can be better for beginner web developers because it starts with a small, simple core—routing, requests, and responses—without a lot of built-in “magic.” Since less is pre-built, you can learn the fundamentals of how a web app works (URLs → view functions → templates/JSON → database) step by step, adding only what you need (like a database layer or authentication) when you’re ready. That simplicity makes early projects feel less overwhelming and helps you understand what each piece does instead of learning a large framework all at once.

## Flask versus Django

Flask and Django are both popular Python web frameworks: Flask is a lightweight “microframework” that gives you the basics and lets you add what you need, while Django is a “batteries-included” framework that provides many built-in features for building full web applications.

| Category                   | Flask                                                                | Django                                                                                         |
| -------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Type / philosophy          | Microframework; minimal core, extensions for extra features          | Full-stack; many features included by default                                                  |
| Learning curve             | Generally easier to start small                                      | More to learn up front, especially with larger feature set                                     |
| Project structure          | Flexible; you choose patterns and layout                             | More opinionated; encourages a standard app/project structure                                  |
| Built-in admin             | Not included (commonly added via extensions)                         | Included (powerful auto-generated admin interface)                                             |
| ORM / database             | No built-in ORM (often use SQLAlchemy)                               | Built-in ORM included                                                                          |
| Routing                    | Simple and explicit                                                  | Robust, with a broader set of built-in conventions                                             |
| Templating                 | Jinja2 (commonly used)                                               | Django Templates (built-in), can also use Jinja2                                               |
| Use cases                  | Small-to-medium apps, APIs, prototypes, services needing flexibility | Content-heavy sites, CRUD apps, larger apps needing built-in components                        |
| Customization              | High flexibility; assemble what you want                             | Highly customizable too, but within a more structured framework                                |
| Performance considerations | Often very lean by default; depends on chosen extensions             | Very capable; may have more overhead due to included components (often negligible in practice) |

## Flask file folder structure

In Flask, the templates/ folder is the conventional place where you put your HTML template files (usually Jinja2 templates) that Flask will render to build the pages sent to the browser. Alongside that, Flask also expects a static/ folder by default, which is where you store files the browser downloads directly—like CSS stylesheets, JavaScript files, images, and icons.

Everything else in a Flask app’s layout is flexible: you can organize Python modules, blueprints, and configuration in many different ways, but templates/ is the standard default location Flask uses for server-rendered HTML, and static/ is the standard default location it uses for front-end assets (typically accessed via URLs like /static/style.css).

```text
├── static
│ └── #Static files & folders
├── templates #titly typed
│ ├── partials
│ │ ├── login_form.html
│ │ └── menu.html
│ ├── index.html
│ └── layout.html
└── main.py
```

## Bootstrap CSS class library

Bootstrap is a simple, intuitive CSS class framework to use with Flask because it lets you style pages mostly by adding pre-named classes directly in your HTML templates (Jinja templates in Flask), instead of writing lots of custom CSS from scratch. That means you can go from a plain Flask route + template to a clean-looking, responsive page quickly.

Why it works well for rapid prototyping with Flask:

- Class-based building blocks: Common UI pieces (buttons, forms, navbars, alerts, cards) are ready-made—add classes like btn btn-primary or form-control and you immediately get consistent styling.
- Responsive by default: The grid system and responsive utilities make layouts adapt to mobile/desktop with minimal effort.
- Consistent design without design work: Bootstrap provides a coherent look-and-feel so your prototype looks “real” early on.
- Easy to drop into templates: You can include Bootstrap via a CDN in base.html, then all Flask pages that extend that base inherit the styling.
- Speeds up iteration: You spend more time on Flask logic (routes, data, forms) and less time tweaking CSS details.

### Important bootstrap links

- [Bootstrap Core](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Bootstrap Navbar](https://getbootstrap.com/docs/5.3/components/navbar/)
- [Bootstrap Forms](https://getbootstrap.com/docs/5.3/forms/overview/)
