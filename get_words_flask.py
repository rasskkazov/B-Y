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
    redactedLyrics = redactedLyrics.replace('\n'," ")
    redactedLyrics = redactedLyrics.lower()
    redactedLyrics = redactedLyrics.replace("Embed", '  ')
    redactedLyrics = redactedLyrics.replace("embed", '  ')
    redactedLyrics = redactedLyrics.replace("—", ' ')
    redactedLyrics = redactedLyrics.replace("-", ' ')
    redactedLyrics = redactedLyrics.replace(":", ' ')
    redactedLyrics = redactedLyrics.replace(" на ", ' ')
    redactedLyrics = redactedLyrics.replace(" не ", ' ')
    redactedLyrics = redactedLyrics.replace(" в ", ' ')
    redactedLyrics = redactedLyrics.replace(" и ", ' ')
    redactedLyrics = redactedLyrics.replace(" под ", ' ')
    redactedLyrics = redactedLyrics.replace(" над ", ' ')
    redactedLyrics = redactedLyrics.replace(" что ", ' ')
    redactedLyrics = redactedLyrics.replace(" это ", ' ')
    redactedLyrics = redactedLyrics.replace(" как ", ' ')
    redactedLyrics = redactedLyrics.replace(" да ", ' ')
    redactedLyrics = redactedLyrics.replace(" я ", ' ')
    redactedLyrics = redactedLyrics.replace(" м ", ' ')
    redactedLyrics = redactedLyrics.replace(" е ", ' ')
    redactedLyrics = redactedLyrics.replace(" с ", ' ')
    redactedLyrics = redactedLyrics.replace(" у ", ' ')
    redactedLyrics = redactedLyrics.replace(" но ", ' ')
    redactedLyrics = redactedLyrics.replace(" от ", ' ')
    redactedLyrics = redactedLyrics.replace(" , ", ' ')
    redactedLyrics = redactedLyrics.replace(" а ", ' ')
    redactedLyrics = redactedLyrics.replace(" то ", ' ')
    redactedLyrics = redactedLyrics.replace(" как ", ' ')
    redactedLyrics = redactedLyrics.replace(",", '')
    redactedLyrics = redactedLyrics.replace("?", '')
    redactedLyrics = redactedLyrics.replace(" меня ", ' ')
    redactedLyrics = redactedLyrics.replace(" я ", ' ')
    redactedLyrics = redactedLyrics.replace(" мне ", ' ')
    redactedLyrics = redactedLyrics.replace(" так ", ' ')
    redactedLyrics = redactedLyrics.replace(" ты ", ' ')
    redactedLyrics = redactedLyrics.replace(" мы ", ' ')
    redactedLyrics = redactedLyrics.replace(" то ", ' ')
    redactedLyrics = redactedLyrics.replace(" эти ", ' ')
    redactedLyrics = redactedLyrics.replace(" это ", ' ')
    redactedLyrics = redactedLyrics.replace(" вот ", ' ')
    redactedLyrics = redactedLyrics.replace(" со ", ' ')
    redactedLyrics = redactedLyrics.replace(" ли ", ' ')
    redactedLyrics = redactedLyrics.replace(" из ", ' ')
    redactedLyrics = redactedLyrics.replace(" все ", ' ')
    redactedLyrics = redactedLyrics.replace(" без ", ' ')
    redactedLyrics = redactedLyrics.replace(" мой ", ' ')
    redactedLyrics = redactedLyrics.replace(" моё ", ' ')
    redactedLyrics = redactedLyrics.replace(" моей ", ' ')
    redactedLyrics = redactedLyrics.replace(" моём ", ' ')
    redactedLyrics = redactedLyrics.replace(" мои ", ' ')
    redactedLyrics = redactedLyrics.replace(" ну ", ' ')
    redactedLyrics = redactedLyrics.replace(" бы ", ' ')
    redactedLyrics = redactedLyrics.replace(" моя ", ' ')
    redactedLyrics = redactedLyrics.replace(" всё ", ' ')
    redactedLyrics = redactedLyrics.replace(" он ", ' ')
    redactedLyrics = redactedLyrics.replace(" за ", ' ')
    redactedLyrics = redactedLyrics.replace(" если ", ' ')
    redactedLyrics = redactedLyrics.replace(" по ", ' ')
    redactedLyrics = redactedLyrics.replace(" же ", ' ')
    redactedLyrics = redactedLyrics.replace(" кто ", ' ')
    redactedLyrics = redactedLyrics.replace(" для ", ' ')
    redactedLyrics = redactedLyrics.replace(" уже ", ' ')
    redactedLyrics = redactedLyrics.replace(" нам ", ' ')
    redactedLyrics = redactedLyrics.replace(" до ", ' ')
    redactedLyrics = redactedLyrics.replace(" твоя ", ' ')
    redactedLyrics = redactedLyrics.replace(" твой ", ' ')
    redactedLyrics = redactedLyrics.replace(" твои ", ' ')
    redactedLyrics = redactedLyrics.replace(" твоей ", ' ')
    redactedLyrics = redactedLyrics.replace(" нас ", ' ')
    redactedLyrics = redactedLyrics.replace(" твоё ", ' ')
    redactedLyrics = redactedLyrics.replace(" тебя ", ' ')
    redactedLyrics = redactedLyrics.replace(" про ", ' ')
    redactedLyrics = redactedLyrics.replace(" ни ", ' ')
    redactedLyrics = redactedLyrics.replace(" нет ", ' ')
    redactedLyrics = redactedLyrics.replace(" i ", ' ')
    redactedLyrics = redactedLyrics.replace(" me ", ' ')
    redactedLyrics = redactedLyrics.replace(" mine ", ' ')
    redactedLyrics = redactedLyrics.replace(" my ", ' ')
    redactedLyrics = redactedLyrics.replace(" you ", ' ')
    redactedLyrics = redactedLyrics.replace(" your ", ' ')
    redactedLyrics = redactedLyrics.replace(" yours ", ' ')
    redactedLyrics = redactedLyrics.replace(" he ", ' ')
    redactedLyrics = redactedLyrics.replace(" him ", ' ')
    redactedLyrics = redactedLyrics.replace(" his ", ' ')
    redactedLyrics = redactedLyrics.replace(" she ", ' ')
    redactedLyrics = redactedLyrics.replace(" her ", ' ')
    redactedLyrics = redactedLyrics.replace(" it ", ' ')
    redactedLyrics = redactedLyrics.replace(" its ", ' ')
    redactedLyrics = redactedLyrics.replace(" it's ", ' ')
    redactedLyrics = redactedLyrics.replace(" i'm ", ' ')
    redactedLyrics = redactedLyrics.replace(" you're ", ' ')
    redactedLyrics = redactedLyrics.replace(" u ", ' ')
    redactedLyrics = redactedLyrics.replace(" a ", ' ')
    redactedLyrics = redactedLyrics.replace(" am ", ' ')
    redactedLyrics = redactedLyrics.replace(" the ", ' ')
    redactedLyrics = redactedLyrics.replace(" an ", ' ')
    redactedLyrics = redactedLyrics.replace(" do ", ' ')
    redactedLyrics = redactedLyrics.replace(" does ", ' ')
    redactedLyrics = redactedLyrics.replace(" and ", ' ')
    redactedLyrics = redactedLyrics.replace(" or ", ' ')
    redactedLyrics = redactedLyrics.replace(" my ", ' ')
    redactedLyrics = redactedLyrics.replace(" in ", ' ')
    redactedLyrics = redactedLyrics.replace(" to ", ' ')
    redactedLyrics = redactedLyrics.replace(" of ", ' ')
    redactedLyrics = redactedLyrics.replace(" was ", ' ')
    redactedLyrics = redactedLyrics.replace(" but ", ' ')
    redactedLyrics = redactedLyrics.replace(" be ", ' ')
    redactedLyrics = redactedLyrics.replace(" so ", ' ')
    redactedLyrics = redactedLyrics.replace(" on ", ' ')
    redactedLyrics = redactedLyrics.replace(" is ", ' ')
    redactedLyrics = redactedLyrics.replace(" if ", ' ')
    redactedLyrics = redactedLyrics.replace(" oh ", ' ')
    redactedLyrics = redactedLyrics.replace(" no ", ' ')
    redactedLyrics = redactedLyrics.replace(" at ", ' ')
    redactedLyrics = redactedLyrics.replace(" up ", ' ')
    redactedLyrics = redactedLyrics.replace(" are ", ' ')
    redactedLyrics = redactedLyrics.replace(" as ", ' ')
    redactedLyrics = redactedLyrics.replace(" but ", ' ')
    redactedLyrics = redactedLyrics.replace("!", ' ')
    redactedLyrics = redactedLyrics.replace(" 2] ", ' ')
    redactedLyrics = redactedLyrics.replace("  ", " ")
    redactedLyrics = redactedLyrics.replace("   ", " ")
    redactedLyrics = redactedLyrics.replace("    ", " ")

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
