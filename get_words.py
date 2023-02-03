import lyricsgenius
from collections import Counter

def count_words(s, n):  #necessary for get words
        words = s.split(" ");
        words = Counter(words)
        top_n = words.most_common(n)
        return top_n
def get_words_byArtist(artist_name):   #returns list of tuples
    genius = lyricsgenius.Genius("sxDFwDiAtZBe5Isp8ULM9HRUk6NkLQlRLp7toliPN9yOdboykVqNXc9F0OTqOXFC")
    artist = genius.search_artist(artist_name,max_songs=50,sort="popularity")

    unredacted1=''
    for song in artist.songs:
        unredacted1+=song.lyrics
        unredacted1 +="["

    # remove []
    redactedLyrics = ''
    for i in range(0,len(unredacted1)):
        if unredacted1[i] == "]":
            for j in range(i,len(unredacted1)):
                if unredacted1[j] =="[":
                    redactedLyrics += unredacted1[i+1:j]
                    break

    # remove ()
    unredacted2 = ")" + redactedLyrics + "("
    redactedLyrics = ''
    for i in range(0,len(unredacted2)):
        if unredacted2[i] == ")":
            for j in range(i,len(unredacted2)):
                if unredacted2[j] =="(":
                    redactedLyrics += unredacted2[i+1:j]
                    break

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
    words = count_words(redactedLyrics, 100)
    i=0
    for tpl in words: 
        if tpl[0]=='':
            words.pop(i)
        i+=1
    words.pop(i-1)
    return  words

s = get_words_byArtist("забей лерочка")
with open('words.txt', 'w',encoding="utf-8") as outfile:
    for tpl in s:
        word = tpl[0] + ' ' + '|' + ' '
        word_number = str(tpl[1]) + '\n'
        outfile.write(word)
        outfile.write(word_number)