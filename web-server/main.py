import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
            <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Pagina Web</title>
                </head>
                <body>
                    <h1>Esta es una Pagina</h1>
                    <h2>Retornada por un Web Service</h2>
                    <br>
                    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quis eveniet, ab temporibus minima tempore autem dolorum quo quidem iure nam quam aliquid molestiae in sed excepturi explicabo, sapiente sunt culpa.</p>
                </body>
                </html>
"""



def run():
    store.get_categories()


if __name__ == '__main__':
    run()