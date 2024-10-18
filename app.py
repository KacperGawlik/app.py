from flask import Flask, render_template, request

app = Flask(__name__)

# Przykładowa funkcja filtrowania
def filter_words(word_list, pattern):
    filtered_words = []
    for word in word_list:
        match = True
        for i in range(5):
            if pattern[i] != '_' and pattern[i] != word[i]:
                match = False
                break
        if match:
            filtered_words.append(word)
    return filtered_words

# Przykładowa baza słów
words = ["apple", "grape", "stone", "plane", "snake", "blame"]

@app.route('/', methods=['GET', 'POST'])
def index():
    filtered = []
    pattern = ""
    
    if request.method == 'POST':
        pattern = request.form['pattern']
        filtered = filter_words(words, pattern)
    
    return render_template('index.html', words=filtered, pattern=pattern)

if __name__ == '__main__':
    app.run(debug=True)
