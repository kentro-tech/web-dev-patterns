"""EidosUI MVP Showcase - Semantic Typography & Beautiful Buttons"""
from air import *
from eidos.tags import *
import eidos.styles as styles
from eidos.components.headers import EidosHeaders
from eidos.utils import get_eidos_static_directory

app = Air()

from fastapi.staticfiles import StaticFiles

# Mount static files for CSS
app.mount("/eidos", StaticFiles(directory=get_eidos_static_directory()), name="eidos")

def layout(*content):
    return Html(
        Head(
            *EidosHeaders(),
            Title("EidosUI MVP 🎨"),
        ),
        Body(
            Main(
                Button("🌙", id="theme-toggle", cls="fixed top-4 right-4 p-2 rounded-full bg-gray-200 dark:bg-gray-800"),
            *content,
            cls='p-12'
        ),
        Script("""
            const toggle = document.getElementById('theme-toggle');
            toggle.addEventListener('click', () => {
                const html = document.documentElement;
                const currentTheme = html.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                html.setAttribute('data-theme', newTheme);
                toggle.textContent = newTheme === 'dark' ? '☀️' : '🌙';
            });
        """),
    ))


@app.get("/")
def home():
    return layout(
         H1("EidosUI MVP 🎨"),
         P("Beautiful, semantic HTML components with ", Em("intelligent"), " theming"),

        Hr(cls='border-4 my-4'),
        Div(
            H1("H1"),
            H2("H2"),
            H3("H3"),
        ),
        Hr(cls='border-4 my-4'),
        Div(
            Button("Primary", cls=styles.buttons.primary),
            Button("Secondary", cls=styles.buttons.secondary),
            Button("Success", cls=styles.buttons.success),
            Button("Error", cls=styles.buttons.error),
            Button("CTA", cls=styles.buttons.cta),
            cls='space-x-4'
    ),
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)