import lyricsgenius
from collections import Counter

def count_words(s, n):  #necessary for get words
        words = s.split(" ");
        words = Counter(words)
        top_n = words.most_common(n)
        return top_n
def get_words_name_img_byArtist(artist_name):   #returns list of tuples
    genius = lyricsgenius.Genius("sxDFwDiAtZBe5Isp8ULM9HRUk6NkLQlRLp7toliPN9yOdboykVqNXc9F0OTqOXFC")
    try:
        artist = genius.search_artist(artist_name,max_songs=2,sort="popularity")
    except:
        print("network error")
        # return None
    if artist is None:
        print("artist not found")
        return None

    # get artist name and img #
    img=artist.image_url
    nm=artist.name

    # redact the string 1step#
    unredacted1=''
    for song in artist.songs:
        unredacted1+=song.lyrics
        unredacted1 +="["
    # remove [] 2step
    redactedLyrics = ''
    for i in range(0,len(unredacted1)):
        if unredacted1[i] == "]":
            for j in range(i,len(unredacted1)):
                if unredacted1[j] =="[":
                    redactedLyrics += unredacted1[i+1:j]
                    break
    # remove () 3step
    unredacted2 = ")" + redactedLyrics + "("
    redactedLyrics = ''
    for i in range(0,len(unredacted2)):
        if unredacted2[i] == ")":
            for j in range(i,len(unredacted2)):
                if unredacted2[j] =="(":
                    redactedLyrics += unredacted2[i+1:j]
                    break
    # 4step
    redactedLyrics = redactedLyrics.lower()
    redactedLyrics = redactedLyrics.replace("Embed", '  ')
    redactedLyrics = redactedLyrics.replace("embed", '  ')

    patterns = [
    "—", "-", ":", " на ", " не ", " в ", " и ", " под ", " над ", 
    " что ", " это ", " как ", " да ", " я ", " м ", " е ", " с ", 
    " у ", " но ", " от ", " , ", " а ", " то ", " как ", ",", 
    "?", " меня ", " я ", " мне ", " так ", " ты ", " мы ", " то ", 
    " эти ", " это ", " вот ", " со ", " ли ", " из ", " все ", 
    " без ", " мой ", " моё ", " ну ", " бы ", " моя ", " всё ", 
    " он ", " за ", " если ", " по ", " же ", " кто ", " для ", 
    " уже ", " нам ", " до ", " твоя ", " твой ", " твои ", 
    " твоей ", " нас ", " твоё ", " тебя ", " про ", " ни ", 
    " нет ", " i ", " me ", " mine ", " my ", " you ", " your ", 
    " yours ", " he ", " him ", " his ", " she ", " her ", " it ", 
    " its ", " it's ", " i'm ", " you're ", " u ", " a ", " am ", 
    " the ", " an ", " do ", " does ", " and ", " or ", " my ", 
    " in ", " to ", " of ", " was ", " but ", " be ", " so ", 
    " on ", " is ", " if ", " oh ", " no ", " at ", " up ", " are ", 
    " as ", " but ", "!"
    ]

    for pattern, replacement in patterns:
        lyrics = lyrics.replace(pattern, " ")
    lyrics = lyrics.strip()

    # return values
    if redactedLyrics =="":
        return [[],nm,img]

    words = count_words(redactedLyrics, 100)
    i=0
    for tpl in words: 
        if tpl[0]=='':
            words.pop(i)
        i+=1
    res = [words,nm,img]
    return res




from flask import Flask, render_template,url_for,request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', words_list=[],artist_name='',artist_img='')

@app.route("/artist")
def artist():
    user_artist_name = request.args.get('input_artist')
    res = get_words_name_img_byArtist(user_artist_name)
    if res is None:
        exit()
    words_list,artist_name,artist_img = res
    return render_template('index.html', words_list=words_list,artist_name=artist_name,artist_img=artist_img)

if __name__=='__main__':
    app.run(debug=False, host="0.0.0.0")
