from quiz_card.app import create_app
#if __name__ == '__main__':
app = create_app()

@app.route('/')
def home():
    return 'No entries here so far'
