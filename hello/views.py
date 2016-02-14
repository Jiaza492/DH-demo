from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
import nltk

# from .forms import SearchForm
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def getwords(sentence):
    splitWords = nltk.word_tokenize(sentence.decode('utf-8'))
    tagger = nltk.tag.perceptron.PerceptronTagger()
    tagset = None
    adjDict = []
    for words,pos in nltk.tag._pos_tag(splitWords,tagset,tagger):
            if pos in ['JJ','PRP']:
                adjDict.append(words)
    stem = nltk.stem.lancaster.LancasterStemmer()    
    stemWords = []
    for word in adjDict:
        stemWords.append(stem.stem(word))
    stopwords = nltk.corpus.stopwords.words('english')
    result = [word for word in stemWords if word not in stopwords]
    db = MySQLdb.connect("localhost","root","","SephoraReview")
    cursor = db.cursor()
    sql = "SELECT word from keywords"
    cursor.execute(sql)
    results = cursor.fetchall()
    dictionary = [row[0] for row in results]
    request = set()
    for word in result:
        if word in dictionary:
            request.add(word)
    return list(request)


def get_key_word(search):
    res = {}
    
    return res

def get_match(search):
    res = {}
    
    return res

def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        des = request.POST.get("search")
        keys = getwords(des)
        # get key words list here
        list = get_data() # this is your customize function
        lists = json.dumps(list)
        # get product result here
        product = get_match(des) # this is your customize function
        products = json.dumps(product)
        products = [
                    {"productId":1, "sku_number": "ziang_jia", "product_url": "http://www.columbia.edu/~zj2170","productName":"hahaha"},
                    {"productId":2, "sku_number": "zhen_liang", "product_url": "","productName":"hehehe"}
                    ]
        # render to the result page
        rendered_response = render(request, 'search_result.html', {"list":lists, "products":products, "keys":keys })
        return rendered_response
         
#          form = SearchForm(request.POST, request.POST.get("search_key"))
         # check whether it's valid:
 
     # if a GET (or any other method) we'll create a blank form
    else:
        lists = "Should have a result here!"
        products = "No Products found!"
        return render(request, 'search_result.html', {"list":lists, "products": products })
    
def get_data():
    list = { "nodes":[
                    {"name":"Myriel","group":1},
                    {"name":"Napoleon","group":1},
                    {"name":"Mlle.Baptistine","group":1},
                    {"name":"Mme.Magloire","group":1},
                    {"name":"CountessdeLo","group":1},
                    {"name":"Geborand","group":1},
                    {"name":"Champtercier","group":1},
                    {"name":"Cravatte","group":1},
                    {"name":"Count","group":1},
                    {"name":"OldMan","group":1},
                    {"name":"Labarre","group":2},
                    {"name":"Valjean","group":2},
                    {"name":"Marguerite","group":3},
                    {"name":"Mme.deR","group":2},
                    {"name":"Isabeau","group":2},
                    {"name":"Gervais","group":2},
                    {"name":"Tholomyes","group":3},
                    {"name":"Listolier","group":3},
                    {"name":"Fameuil","group":3},
                    {"name":"Blacheville","group":3},
                    {"name":"Favourite","group":3},
                    {"name":"Dahlia","group":3},
                    {"name":"Zephine","group":3},
                    {"name":"Fantine","group":3},
                    {"name":"Mme.Thenardier","group":4},
                    {"name":"Thenardier","group":4},
                    {"name":"Cosette","group":5},
                    {"name":"Javert","group":4},
                    {"name":"Fauchelevent","group":0},
                    {"name":"Bamatabois","group":2},
                    {"name":"Perpetue","group":3},
                    {"name":"Simplice","group":2},
                    {"name":"Scaufflaire","group":2},
                    {"name":"Woman1","group":2},
                    {"name":"Judge","group":2},
                    {"name":"Champmathieu","group":2},
                    {"name":"Brevet","group":2},
                    {"name":"Chenildieu","group":2},
                    {"name":"Cochepaille","group":2},
                    {"name":"Pontmercy","group":4},
                    {"name":"Boulatruelle","group":6},
                    {"name":"Eponine","group":4},
                    {"name":"Anzelma","group":4},
                    {"name":"Woman2","group":5},
                    {"name":"MotherInnocent","group":0},
                    {"name":"Gribier","group":0},
                    {"name":"Jondrette","group":7},
                    {"name":"Mme.Burgon","group":7},
                    {"name":"Gavroche","group":8},
                    {"name":"Gillenormand","group":5},
                    {"name":"Magnon","group":5},
                    {"name":"Mlle.Gillenormand","group":5},
                    {"name":"Mme.Pontmercy","group":5},
                    {"name":"Mlle.Vaubois","group":5},
                    {"name":"Lt.Gillenormand","group":5},
                    {"name":"Marius","group":8},
                    {"name":"BaronessT","group":5},
                    {"name":"Mabeuf","group":8},
                    {"name":"Enjolras","group":8},
                    {"name":"Combeferre","group":8},
                    {"name":"Prouvaire","group":8},
                    {"name":"Feuilly","group":8},
                    {"name":"Courfeyrac","group":8},
                    {"name":"Bahorel","group":8},
                    {"name":"Bossuet","group":8},
                    {"name":"Joly","group":8},
                    {"name":"Grantaire","group":8},
                    {"name":"MotherPlutarch","group":9},
                    {"name":"Gueulemer","group":4},
                    {"name":"Babet","group":4},
                    {"name":"Claquesous","group":4},
                    {"name":"Montparnasse","group":4},
                    {"name":"Toussaint","group":5},
                    {"name":"Child1","group":10},
                    {"name":"Child2","group":10},
                    {"name":"Brujon","group":4},
                    {"name":"Mme.Hucheloup","group":8}
                  ],
                  "links":[
                    {"source":1,"target":0,"value":1},
                    {"source":2,"target":0,"value":8},
                    {"source":3,"target":0,"value":10},
                    {"source":3,"target":2,"value":6},
                    {"source":4,"target":0,"value":1},
                    {"source":5,"target":0,"value":1},
                    {"source":6,"target":0,"value":1},
                    {"source":7,"target":0,"value":1},
                    {"source":8,"target":0,"value":2},
                    {"source":9,"target":0,"value":1},
                    {"source":11,"target":10,"value":1},
                    {"source":11,"target":3,"value":3},
                    {"source":11,"target":2,"value":3},
                    {"source":11,"target":0,"value":5},
                    {"source":12,"target":11,"value":1},
                    {"source":13,"target":11,"value":1},
                    {"source":14,"target":11,"value":1},
                    {"source":15,"target":11,"value":1},
                    {"source":17,"target":16,"value":4},
                    {"source":18,"target":16,"value":4},
                    {"source":18,"target":17,"value":4},
                    {"source":19,"target":16,"value":4},
                    {"source":19,"target":17,"value":4},
                    {"source":19,"target":18,"value":4},
                    {"source":20,"target":16,"value":3},
                    {"source":20,"target":17,"value":3},
                    {"source":20,"target":18,"value":3},
                    {"source":20,"target":19,"value":4},
                    {"source":21,"target":16,"value":3},
                    {"source":21,"target":17,"value":3},
                    {"source":21,"target":18,"value":3},
                    {"source":21,"target":19,"value":3},
                    {"source":21,"target":20,"value":5},
                    {"source":22,"target":16,"value":3},
                    {"source":22,"target":17,"value":3},
                    {"source":22,"target":18,"value":3},
                    {"source":22,"target":19,"value":3},
                    {"source":22,"target":20,"value":4},
                    {"source":22,"target":21,"value":4},
                    {"source":23,"target":16,"value":3},
                    {"source":23,"target":17,"value":3},
                    {"source":23,"target":18,"value":3},
                    {"source":23,"target":19,"value":3},
                    {"source":23,"target":20,"value":4},
                    {"source":23,"target":21,"value":4},
                    {"source":23,"target":22,"value":4},
                    {"source":23,"target":12,"value":2},
                    {"source":23,"target":11,"value":9},
                    {"source":24,"target":23,"value":2},
                    {"source":24,"target":11,"value":7},
                    {"source":25,"target":24,"value":13},
                    {"source":25,"target":23,"value":1},
                    {"source":25,"target":11,"value":12},
                    {"source":26,"target":24,"value":4},
                    {"source":26,"target":11,"value":31},
                    {"source":26,"target":16,"value":1},
                    {"source":26,"target":25,"value":1},
                    {"source":27,"target":11,"value":17},
                    {"source":27,"target":23,"value":5},
                    {"source":27,"target":25,"value":5},
                    {"source":27,"target":24,"value":1},
                    {"source":27,"target":26,"value":1},
                    {"source":28,"target":11,"value":8},
                    {"source":28,"target":27,"value":1},
                    {"source":29,"target":23,"value":1},
                    {"source":29,"target":27,"value":1},
                    {"source":29,"target":11,"value":2},
                    {"source":30,"target":23,"value":1},
                    {"source":31,"target":30,"value":2},
                    {"source":31,"target":11,"value":3},
                    {"source":31,"target":23,"value":2},
                    {"source":31,"target":27,"value":1},
                    {"source":32,"target":11,"value":1},
                    {"source":33,"target":11,"value":2},
                    {"source":33,"target":27,"value":1},
                    {"source":34,"target":11,"value":3},
                    {"source":34,"target":29,"value":2},
                    {"source":35,"target":11,"value":3},
                    {"source":35,"target":34,"value":3},
                    {"source":35,"target":29,"value":2},
                    {"source":36,"target":34,"value":2},
                    {"source":36,"target":35,"value":2},
                    {"source":36,"target":11,"value":2},
                    {"source":36,"target":29,"value":1},
                    {"source":37,"target":34,"value":2},
                    {"source":37,"target":35,"value":2},
                    {"source":37,"target":36,"value":2},
                    {"source":37,"target":11,"value":2},
                    {"source":37,"target":29,"value":1},
                    {"source":38,"target":34,"value":2},
                    {"source":38,"target":35,"value":2},
                    {"source":38,"target":36,"value":2},
                    {"source":38,"target":37,"value":2},
                    {"source":38,"target":11,"value":2},
                    {"source":38,"target":29,"value":1},
                    {"source":39,"target":25,"value":1},
                    {"source":40,"target":25,"value":1},
                    {"source":41,"target":24,"value":2},
                    {"source":41,"target":25,"value":3},
                    {"source":42,"target":41,"value":2},
                    {"source":42,"target":25,"value":2},
                    {"source":42,"target":24,"value":1},
                    {"source":43,"target":11,"value":3},
                    {"source":43,"target":26,"value":1},
                    {"source":43,"target":27,"value":1},
                    {"source":44,"target":28,"value":3},
                    {"source":44,"target":11,"value":1},
                    {"source":45,"target":28,"value":2},
                    {"source":47,"target":46,"value":1},
                    {"source":48,"target":47,"value":2},
                    {"source":48,"target":25,"value":1},
                    {"source":48,"target":27,"value":1},
                    {"source":48,"target":11,"value":1},
                    {"source":49,"target":26,"value":3},
                    {"source":49,"target":11,"value":2},
                    {"source":50,"target":49,"value":1},
                    {"source":50,"target":24,"value":1},
                    {"source":51,"target":49,"value":9},
                    {"source":51,"target":26,"value":2},
                    {"source":51,"target":11,"value":2},
                    {"source":52,"target":51,"value":1},
                    {"source":52,"target":39,"value":1},
                    {"source":53,"target":51,"value":1},
                    {"source":54,"target":51,"value":2},
                    {"source":54,"target":49,"value":1},
                    {"source":54,"target":26,"value":1},
                    {"source":55,"target":51,"value":6},
                    {"source":55,"target":49,"value":12},
                    {"source":55,"target":39,"value":1},
                    {"source":55,"target":54,"value":1},
                    {"source":55,"target":26,"value":21},
                    {"source":55,"target":11,"value":19},
                    {"source":55,"target":16,"value":1},
                    {"source":55,"target":25,"value":2},
                    {"source":55,"target":41,"value":5},
                    {"source":55,"target":48,"value":4},
                    {"source":56,"target":49,"value":1},
                    {"source":56,"target":55,"value":1},
                    {"source":57,"target":55,"value":1},
                    {"source":57,"target":41,"value":1},
                    {"source":57,"target":48,"value":1},
                    {"source":58,"target":55,"value":7},
                    {"source":58,"target":48,"value":7},
                    {"source":58,"target":27,"value":6},
                    {"source":58,"target":57,"value":1},
                    {"source":58,"target":11,"value":4},
                    {"source":59,"target":58,"value":15},
                    {"source":59,"target":55,"value":5},
                    {"source":59,"target":48,"value":6},
                    {"source":59,"target":57,"value":2},
                    {"source":60,"target":48,"value":1},
                    {"source":60,"target":58,"value":4},
                    {"source":60,"target":59,"value":2},
                    {"source":61,"target":48,"value":2},
                    {"source":61,"target":58,"value":6},
                    {"source":61,"target":60,"value":2},
                    {"source":61,"target":59,"value":5},
                    {"source":61,"target":57,"value":1},
                    {"source":61,"target":55,"value":1},
                    {"source":62,"target":55,"value":9},
                    {"source":62,"target":58,"value":17},
                    {"source":62,"target":59,"value":13},
                    {"source":62,"target":48,"value":7},
                    {"source":62,"target":57,"value":2},
                    {"source":62,"target":41,"value":1},
                    {"source":62,"target":61,"value":6},
                    {"source":62,"target":60,"value":3},
                    {"source":63,"target":59,"value":5},
                    {"source":63,"target":48,"value":5},
                    {"source":63,"target":62,"value":6},
                    {"source":63,"target":57,"value":2},
                    {"source":63,"target":58,"value":4},
                    {"source":63,"target":61,"value":3},
                    {"source":63,"target":60,"value":2},
                    {"source":63,"target":55,"value":1},
                    {"source":64,"target":55,"value":5},
                    {"source":64,"target":62,"value":12},
                    {"source":64,"target":48,"value":5},
                    {"source":64,"target":63,"value":4},
                    {"source":64,"target":58,"value":10},
                    {"source":64,"target":61,"value":6},
                    {"source":64,"target":60,"value":2},
                    {"source":64,"target":59,"value":9},
                    {"source":64,"target":57,"value":1},
                    {"source":64,"target":11,"value":1},
                    {"source":65,"target":63,"value":5},
                    {"source":65,"target":64,"value":7},
                    {"source":65,"target":48,"value":3},
                    {"source":65,"target":62,"value":5},
                    {"source":65,"target":58,"value":5},
                    {"source":65,"target":61,"value":5},
                    {"source":65,"target":60,"value":2},
                    {"source":65,"target":59,"value":5},
                    {"source":65,"target":57,"value":1},
                    {"source":65,"target":55,"value":2},
                    {"source":66,"target":64,"value":3},
                    {"source":66,"target":58,"value":3},
                    {"source":66,"target":59,"value":1},
                    {"source":66,"target":62,"value":2},
                    {"source":66,"target":65,"value":2},
                    {"source":66,"target":48,"value":1},
                    {"source":66,"target":63,"value":1},
                    {"source":66,"target":61,"value":1},
                    {"source":66,"target":60,"value":1},
                    {"source":67,"target":57,"value":3},
                    {"source":68,"target":25,"value":5},
                    {"source":68,"target":11,"value":1},
                    {"source":68,"target":24,"value":1},
                    {"source":68,"target":27,"value":1},
                    {"source":68,"target":48,"value":1},
                    {"source":68,"target":41,"value":1},
                    {"source":69,"target":25,"value":6},
                    {"source":69,"target":68,"value":6},
                    {"source":69,"target":11,"value":1},
                    {"source":69,"target":24,"value":1},
                    {"source":69,"target":27,"value":2},
                    {"source":69,"target":48,"value":1},
                    {"source":69,"target":41,"value":1},
                    {"source":70,"target":25,"value":4},
                    {"source":70,"target":69,"value":4},
                    {"source":70,"target":68,"value":4},
                    {"source":70,"target":11,"value":1},
                    {"source":70,"target":24,"value":1},
                    {"source":70,"target":27,"value":1},
                    {"source":70,"target":41,"value":1},
                    {"source":70,"target":58,"value":1},
                    {"source":71,"target":27,"value":1},
                    {"source":71,"target":69,"value":2},
                    {"source":71,"target":68,"value":2},
                    {"source":71,"target":70,"value":2},
                    {"source":71,"target":11,"value":1},
                    {"source":71,"target":48,"value":1},
                    {"source":71,"target":41,"value":1},
                    {"source":71,"target":25,"value":1},
                    {"source":72,"target":26,"value":2},
                    {"source":72,"target":27,"value":1},
                    {"source":72,"target":11,"value":1},
                    {"source":73,"target":48,"value":2},
                    {"source":74,"target":48,"value":2},
                    {"source":74,"target":73,"value":3},
                    {"source":75,"target":69,"value":3},
                    {"source":75,"target":68,"value":3},
                    {"source":75,"target":25,"value":3},
                    {"source":75,"target":48,"value":1},
                    {"source":75,"target":41,"value":1},
                    {"source":75,"target":70,"value":1},
                    {"source":75,"target":71,"value":1},
                    {"source":76,"target":64,"value":1},
                    {"source":76,"target":65,"value":1},
                    {"source":76,"target":66,"value":1},
                    {"source":76,"target":63,"value":1},
                    {"source":76,"target":62,"value":1},
                    {"source":76,"target":48,"value":1},
                    {"source":76,"target":58,"value":1}
                  ]
                 }
    return list   
