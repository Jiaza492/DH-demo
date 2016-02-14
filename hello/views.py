from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json

# from .forms import SearchForm
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print request.POST.get("search")
        list = request.POST.get("search")
        list = get_data()
        lists = json.dumps(list)
        rendered_response = render(request, 'search_result.html', {"list":lists })
        return rendered_response
         
#          form = SearchForm(request.POST, request.POST.get("search_key"))
         # check whether it's valid:
 
     # if a GET (or any other method) we'll create a blank form
    else:
        list2 = "Should have a result here!"
        return render(request, 'search_result.html', {"list":list2 })
    
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

def get_data2():
    
    list = { "links":[
          {
            "source": "machine-learning", 
            "target": "classification", 
            "value": 76
          }, 
          {
            "source": "machine-learning", 
            "target": "data-mining", 
            "value": 69
          }, 
          {
            "source": "machine-learning", 
            "target": "r", 
            "value": 48
          }, 
          {
            "source": "machine-learning", 
            "target": "python", 
            "value": 34
          }, 
          {
            "source": "machine-learning", 
            "target": "neuralnetwork", 
            "value": 34
          }, 
          {
            "source": "machine-learning", 
            "target": "statistics", 
            "value": 30
          }, 
          {
            "source": "machine-learning", 
            "target": "algorithms", 
            "value": 27
          }, 
          {
            "source": "bigdata", 
            "target": "data-mining", 
            "value": 26
          }, 
          {
            "source": "machine-learning", 
            "target": "bigdata", 
            "value": 26
          }, 
          {
            "source": "machine-learning", 
            "target": "predictive-modeling", 
            "value": 26
          }, 
          {
            "source": "machine-learning", 
            "target": "dataset", 
            "value": 25
          }, 
          {
            "source": "machine-learning", 
            "target": "nlp", 
            "value": 25
          }, 
          {
            "source": "machine-learning", 
            "target": "clustering", 
            "value": 23
          }, 
          {
            "source": "bigdata", 
            "target": "hadoop", 
            "value": 22
          }, 
          {
            "source": "data-mining", 
            "target": "classification", 
            "value": 22
          }, 
          {
            "source": "data-mining", 
            "target": "clustering", 
            "value": 21
          }, 
          {
            "source": "data-mining", 
            "target": "dataset", 
            "value": 21
          }, 
          {
            "source": "nlp", 
            "target": "text-mining", 
            "value": 19
          }, 
          {
            "source": "machine-learning", 
            "target": "svm", 
            "value": 19
          }, 
          {
            "source": "data-mining", 
            "target": "r", 
            "value": 18
          }, 
          {
            "source": "data-mining", 
            "target": "statistics", 
            "value": 17
          }, 
          {
            "source": "machine-learning", 
            "target": "text-mining", 
            "value": 16
          }, 
          {
            "source": "clustering", 
            "target": "k-means", 
            "value": 15
          }, 
          {
            "source": "machine-learning", 
            "target": "recommendation", 
            "value": 15
          }, 
          {
            "source": "r", 
            "target": "python", 
            "value": 14
          }, 
          {
            "source": "machine-learning", 
            "target": "feature-selection", 
            "value": 14
          }, 
          {
            "source": "data-mining", 
            "target": "python", 
            "value": 13
          }, 
          {
            "source": "r", 
            "target": "predictive-modeling", 
            "value": 13
          }, 
          {
            "source": "machine-learning", 
            "target": "deep-learning", 
            "value": 12
          }, 
          {
            "source": "machine-learning", 
            "target": "logistic-regression", 
            "value": 12
          }, 
          {
            "source": "classification", 
            "target": "text-mining", 
            "value": 12
          }, 
          {
            "source": "machine-learning", 
            "target": "regression", 
            "value": 12
          }, 
          {
            "source": "python", 
            "target": "classification", 
            "value": 12
          }, 
          {
            "source": "svm", 
            "target": "classification", 
            "value": 12
          }, 
          {
            "source": "r", 
            "target": "classification", 
            "value": 12
          }, 
          {
            "source": "data-mining", 
            "target": "nlp", 
            "value": 11
          }, 
          {
            "source": "data-mining", 
            "target": "algorithms", 
            "value": 11
          }, 
          {
            "source": "clustering", 
            "target": "classification", 
            "value": 11
          }, 
          {
            "source": "python", 
            "target": "nlp", 
            "value": 11
          }, 
          {
            "source": "machine-learning", 
            "target": "random-forest", 
            "value": 10
          }, 
          {
            "source": "data-cleaning", 
            "target": "dataset", 
            "value": 10
          }, 
          {
            "source": "data-mining", 
            "target": "predictive-modeling", 
            "value": 10
          }, 
          {
            "source": "r", 
            "target": "logistic-regression", 
            "value": 9
          }, 
          {
            "source": "nlp", 
            "target": "classification", 
            "value": 9
          }, 
          {
            "source": "python", 
            "target": "scikit", 
            "value": 9
          }, 
          {
            "source": "machine-learning", 
            "target": "dimensionality-reduction", 
            "value": 9
          }, 
          {
            "source": "machine-learning", 
            "target": "time-series", 
            "value": 9
          }, 
          {
            "source": "bigdata", 
            "target": "efficiency", 
            "value": 9
          }, 
          {
            "source": "bigdata", 
            "target": "statistics", 
            "value": 9
          }, 
          {
            "source": "clustering", 
            "target": "algorithms", 
            "value": 8
          }, 
          {
            "source": "clustering", 
            "target": "text-mining", 
            "value": 8
          }, 
          {
            "source": "bigdata", 
            "target": "dataset", 
            "value": 8
          }, 
          {
            "source": "machine-learning", 
            "target": "search", 
            "value": 8
          }, 
          {
            "source": "classification", 
            "target": "logistic-regression", 
            "value": 8
          }, 
          {
            "source": "statistics", 
            "target": "dataset", 
            "value": 8
          }, 
          {
            "source": "machine-learning", 
            "target": "feature-extraction", 
            "value": 8
          }, 
          {
            "source": "bigdata", 
            "target": "scalability", 
            "value": 8
          }, 
          {
            "source": "data-mining", 
            "target": "text-mining", 
            "value": 7
          }, 
          {
            "source": "machine-learning", 
            "target": "optimization", 
            "value": 7
          }, 
          {
            "source": "classification", 
            "target": "unbalanced-classes", 
            "value": 7
          }, 
          {
            "source": "hadoop", 
            "target": "map-reduce", 
            "value": 7
          }, 
          {
            "source": "machine-learning", 
            "target": "apache-spark", 
            "value": 7
          }, 
          {
            "source": "data-mining", 
            "target": "data-cleaning", 
            "value": 7
          }, 
          {
            "source": "r", 
            "target": "random-forest", 
            "value": 7
          }, 
          {
            "source": "efficiency", 
            "target": "performance", 
            "value": 7
          }, 
          {
            "source": "visualization", 
            "target": "data-visualization", 
            "value": 6
          }, 
          {
            "source": "statistics", 
            "target": "predictive-modeling", 
            "value": 6
          }, 
          {
            "source": "bigdata", 
            "target": "databases", 
            "value": 6
          }, 
          {
            "source": "python", 
            "target": "neuralnetwork", 
            "value": 6
          }, 
          {
            "source": "classification", 
            "target": "random-forest", 
            "value": 6
          }, 
          {
            "source": "data-mining", 
            "target": "time-series", 
            "value": 6
          }, 
          {
            "source": "scalability", 
            "target": "efficiency", 
            "value": 6
          }, 
          {
            "source": "python", 
            "target": "pandas", 
            "value": 6
          }, 
          {
            "source": "r", 
            "target": "optimization", 
            "value": 6
          }, 
          {
            "source": "clustering", 
            "target": "r", 
            "value": 6
          }, 
          {
            "source": "machine-learning", 
            "target": "correlation", 
            "value": 6
          }, 
          {
            "source": "r", 
            "target": "statistics", 
            "value": 6
          }, 
          {
            "source": "neuralnetwork", 
            "target": "deep-learning", 
            "value": 6
          }, 
          {
            "source": "topic-model", 
            "target": "lda", 
            "value": 6
          }, 
          {
            "source": "clustering", 
            "target": "similarity", 
            "value": 6
          }, 
          {
            "source": "bigdata", 
            "target": "python", 
            "value": 6
          }, 
          {
            "source": "feature-selection", 
            "target": "classification", 
            "value": 6
          }, 
          {
            "source": "data-mining", 
            "target": "recommendation", 
            "value": 6
          }, 
          {
            "source": "r", 
            "target": "visualization", 
            "value": 6
          }, 
          {
            "source": "machine-learning", 
            "target": "scikit", 
            "value": 6
          }, 
          {
            "source": "hadoop", 
            "target": "r", 
            "value": 5
          }, 
          {
            "source": "bigdata", 
            "target": "performance", 
            "value": 5
          }, 
          {
            "source": "regression", 
            "target": "predictive-modeling", 
            "value": 5
          }, 
          {
            "source": "python", 
            "target": "svm", 
            "value": 5
          }, 
          {
            "source": "algorithms", 
            "target": "classification", 
            "value": 5
          }, 
          {
            "source": "recommendation", 
            "target": "dataset", 
            "value": 5
          }, 
          {
            "source": "feature-selection", 
            "target": "feature-extraction", 
            "value": 5
          }, 
          {
            "source": "r", 
            "target": "beginner", 
            "value": 5
          }, 
          {
            "source": "clustering", 
            "target": "clusters", 
            "value": 5
          }, 
          {
            "source": "bigdata", 
            "target": "clustering", 
            "value": 5
          }, 
          {
            "source": "visualization", 
            "target": "tableau", 
            "value": 5
          }, 
          {
            "source": "random-forest", 
            "target": "scikit", 
            "value": 5
          }, 
          {
            "source": "clustering", 
            "target": "time-series", 
            "value": 5
          }, 
          {
            "source": "bigdata", 
            "target": "algorithms", 
            "value": 5
          }, 
          {
            "source": "clustering", 
            "target": "python", 
            "value": 5
          }, 
          {
            "source": "bigdata", 
            "target": "classification", 
            "value": 5
          }, 
          {
            "source": "statistics", 
            "target": "classification", 
            "value": 5
          }, 
          {
            "source": "machine-learning", 
            "target": "beginner", 
            "value": 5
          }, 
          {
            "source": "bigdata", 
            "target": "distributed", 
            "value": 5
          }, 
          {
            "source": "classification", 
            "target": "accuracy", 
            "value": 5
          }, 
          {
            "source": "classification", 
            "target": "regression", 
            "value": 5
          }, 
          {
            "source": "machine-learning", 
            "target": "sklearn", 
            "value": 5
          }, 
          {
            "source": "machine-learning", 
            "target": "hadoop", 
            "value": 5
          }, 
          {
            "source": "machine-learning", 
            "target": "k-means", 
            "value": 5
          }, 
          {
            "source": "classification", 
            "target": "predictive-modeling", 
            "value": 5
          }, 
          {
            "source": "algorithms", 
            "target": "statistics", 
            "value": 5
          }, 
          {
            "source": "statistics", 
            "target": "python", 
            "value": 5
          }, 
          {
            "source": "data-mining", 
            "target": "social-network-analysis", 
            "value": 5
          }, 
          {
            "source": "dataset", 
            "target": "classification", 
            "value": 5
          }, 
          {
            "source": "python", 
            "target": "regression", 
            "value": 5
          }, 
          {
            "source": "r", 
            "target": "dataset", 
            "value": 5
          }, 
          {
            "source": "python", 
            "target": "sklearn", 
            "value": 5
          }, 
          {
            "source": "data-mining", 
            "target": "categorical-data", 
            "value": 5
          }, 
          {
            "source": "feature-selection", 
            "target": "time-series", 
            "value": 4
          }, 
          {
            "source": "open-source", 
            "target": "dataset", 
            "value": 4
          }, 
          {
            "source": "algorithms", 
            "target": "dataset", 
            "value": 4
          }, 
          {
            "source": "machine-learning", 
            "target": "topic-model", 
            "value": 4
          }, 
          {
            "source": "visualization", 
            "target": "graphs", 
            "value": 4
          }, 
          {
            "source": "machine-learning", 
            "target": "decision-trees", 
            "value": 4
          }, 
          {
            "source": "machine-learning", 
            "target": "java", 
            "value": 4
          }, 
          {
            "source": "data-mining", 
            "target": "random-forest", 
            "value": 4
          }, 
          {
            "source": "classification", 
            "target": "categorical-data", 
            "value": 4
          }, 
          {
            "source": "dataset", 
            "target": "beginner", 
            "value": 4
          }, 
          {
            "source": "machine-learning", 
            "target": "feature-scaling", 
            "value": 4
          }, 
          {
            "source": "logistic-regression", 
            "target": "scikit", 
            "value": 4
          }, 
          {
            "source": "databases", 
            "target": "nosql", 
            "value": 4
          }, 
          {
            "source": "algorithms", 
            "target": "r", 
            "value": 4
          }, 
          {
            "source": "bigdata", 
            "target": "recommendation", 
            "value": 4
          }, 
          {
            "source": "r", 
            "target": "data-visualization", 
            "value": 4
          }, 
          {
            "source": "data-mining", 
            "target": "beginner", 
            "value": 4
          }, 
          {
            "source": "information-retrieval", 
            "target": "text-mining", 
            "value": 4
          }, 
          {
            "source": "bigdata", 
            "target": "r", 
            "value": 4
          }, 
          {
            "source": "efficiency", 
            "target": "distributed", 
            "value": 4
          }, 
          {
            "source": "hadoop", 
            "target": "apache-pig", 
            "value": 4
          }, 
          {
            "source": "r", 
            "target": "forecast", 
            "value": 4
          }, 
          {
            "source": "dataset", 
            "target": "graphs", 
            "value": 4
          }, 
          {
            "source": "scalability", 
            "target": "distributed", 
            "value": 4
          }, 
          {
            "source": "data-cleaning", 
            "target": "text-mining", 
            "value": 4
          }, 
          {
            "source": "regression", 
            "target": "linear-regression", 
            "value": 4
          }, 
          {
            "source": "time-series", 
            "target": "neuralnetwork", 
            "value": 4
          }, 
          {
            "source": "feature-selection", 
            "target": "scikit", 
            "value": 4
          }, 
          {
            "source": "nlp", 
            "target": "feature-extraction", 
            "value": 4
          }, 
          {
            "source": "nlp", 
            "target": "word-embeddings", 
            "value": 4
          }, 
          {
            "source": "machine-learning", 
            "target": "libsvm", 
            "value": 4
          }, 
          {
            "source": "classification", 
            "target": "sampling", 
            "value": 4
          }, 
          {
            "source": "data-mining", 
            "target": "databases", 
            "value": 4
          }, 
          {
            "source": "machine-learning", 
            "target": "data", 
            "value": 4
          }, 
          {
            "source": "r", 
            "target": "data-cleaning", 
            "value": 4
          }, 
          {
            "source": "machine-learning", 
            "target": "data-cleaning", 
            "value": 4
          }, 
          {
            "source": "nlp", 
            "target": "neuralnetwork", 
            "value": 4
          }, 
          {
            "source": "education", 
            "target": "career", 
            "value": 4
          }, 
          {
            "source": "statistics", 
            "target": "regression", 
            "value": 4
          }, 
          {
            "source": "statistics", 
            "target": "correlation", 
            "value": 4
          }, 
          {
            "source": "neuralnetwork", 
            "target": "matlab", 
            "value": 4
          }, 
          {
            "source": "dataset", 
            "target": "text-mining", 
            "value": 4
          }, 
          {
            "source": "bigdata", 
            "target": "scala", 
            "value": 4
          }, 
          {
            "source": "bigdata", 
            "target": "map-reduce", 
            "value": 4
          }, 
          {
            "source": "neuralnetwork", 
            "target": "convnet", 
            "value": 4
          }, 
          {
            "source": "social-network-analysis", 
            "target": "graphs", 
            "value": 4
          }, 
          {
            "source": "clustering", 
            "target": "hierarchical-data-format", 
            "value": 3
          }, 
          {
            "source": "bigdata", 
            "target": "social-network-analysis", 
            "value": 3
          }, 
          {
            "source": "r", 
            "target": "text-mining", 
            "value": 3
          }, 
          {
            "source": "google", 
            "target": "search", 
            "value": 3
          }, 
          {
            "source": "scalability", 
            "target": "performance", 
            "value": 3
          }, 
          {
            "source": "dataset", 
            "target": "time-series", 
            "value": 3
          }, 
          {
            "source": "classification", 
            "target": "decision-trees", 
            "value": 3
          }, 
          {
            "source": "clustering", 
            "target": "data-cleaning", 
            "value": 3
          }, 
          {
            "source": "similarity", 
            "target": "correlation", 
            "value": 3
          }, 
          {
            "source": "definitions", 
            "target": "knowledge-base", 
            "value": 3
          }, 
          {
            "source": "bigdata", 
            "target": "finance", 
            "value": 3
          }, 
          {
            "source": "neuralnetwork", 
            "target": "regression", 
            "value": 3
          }, 
          {
            "source": "time-series", 
            "target": "classification", 
            "value": 3
          }, 
          {
            "source": "topic-model", 
            "target": "classification", 
            "value": 3
          }, 
          {
            "source": "scala", 
            "target": "apache-spark", 
            "value": 3
          }, 
          {
            "source": "hadoop", 
            "target": "distributed", 
            "value": 3
          }, 
          {
            "source": "clustering", 
            "target": "categorical-data", 
            "value": 3
          }, 
          {
            "source": "clustering", 
            "target": "dataset", 
            "value": 3
          }, 
          {
            "source": "r", 
            "target": "time-series", 
            "value": 3
          }, 
          {
            "source": "neuralnetwork", 
            "target": "predictive-modeling", 
            "value": 3
          }, 
          {
            "source": "k-means", 
            "target": "python", 
            "value": 3
          }, 
          {
            "source": "nlp", 
            "target": "java", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "matlab", 
            "value": 3
          }, 
          {
            "source": "classification", 
            "target": "binary", 
            "value": 3
          }, 
          {
            "source": "statistics", 
            "target": "recommendation", 
            "value": 3
          }, 
          {
            "source": "python", 
            "target": "data", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "kaggle", 
            "value": 3
          }, 
          {
            "source": "hadoop", 
            "target": "aws", 
            "value": 3
          }, 
          {
            "source": "definitions", 
            "target": "education", 
            "value": 3
          }, 
          {
            "source": "education", 
            "target": "beginner", 
            "value": 3
          }, 
          {
            "source": "time-series", 
            "target": "regression", 
            "value": 3
          }, 
          {
            "source": "predictive-modeling", 
            "target": "ranking", 
            "value": 3
          }, 
          {
            "source": "r", 
            "target": "correlation", 
            "value": 3
          }, 
          {
            "source": "nlp", 
            "target": "parsing", 
            "value": 3
          }, 
          {
            "source": "r", 
            "target": "regression", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "online-learning", 
            "value": 3
          }, 
          {
            "source": "bigdata", 
            "target": "text-mining", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "distributed", 
            "value": 3
          }, 
          {
            "source": "recommendation", 
            "target": "python", 
            "value": 3
          }, 
          {
            "source": "tools", 
            "target": "r", 
            "value": 3
          }, 
          {
            "source": "data-mining", 
            "target": "data-visualization", 
            "value": 3
          }, 
          {
            "source": "text-mining", 
            "target": "feature-extraction", 
            "value": 3
          }, 
          {
            "source": "python", 
            "target": "dataset", 
            "value": 3
          }, 
          {
            "source": "r", 
            "target": "sampling", 
            "value": 3
          }, 
          {
            "source": "python", 
            "target": "visualization", 
            "value": 3
          }, 
          {
            "source": "data-mining", 
            "target": "hadoop", 
            "value": 3
          }, 
          {
            "source": "r", 
            "target": "svm", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "gradient-descent", 
            "value": 3
          }, 
          {
            "source": "python", 
            "target": "text-mining", 
            "value": 3
          }, 
          {
            "source": "databases", 
            "target": "sql", 
            "value": 3
          }, 
          {
            "source": "r", 
            "target": "graphs", 
            "value": 3
          }, 
          {
            "source": "sklearn", 
            "target": "scikit", 
            "value": 3
          }, 
          {
            "source": "r", 
            "target": "neuralnetwork", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "accuracy", 
            "value": 3
          }, 
          {
            "source": "bigdata", 
            "target": "optimization", 
            "value": 3
          }, 
          {
            "source": "data-mining", 
            "target": "neuralnetwork", 
            "value": 3
          }, 
          {
            "source": "data-mining", 
            "target": "graphs", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "ranking", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "cross-validation", 
            "value": 3
          }, 
          {
            "source": "recommendation", 
            "target": "similarity", 
            "value": 3
          }, 
          {
            "source": "classification", 
            "target": "object-recognition", 
            "value": 3
          }, 
          {
            "source": "statistics", 
            "target": "time-series", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "anomaly-detection", 
            "value": 3
          }, 
          {
            "source": "statistics", 
            "target": "education", 
            "value": 3
          }, 
          {
            "source": "correlation", 
            "target": "regression", 
            "value": 3
          }, 
          {
            "source": "algorithms", 
            "target": "graphs", 
            "value": 3
          }, 
          {
            "source": "data-mining", 
            "target": "data", 
            "value": 3
          }, 
          {
            "source": "bigdata", 
            "target": "apache-spark", 
            "value": 3
          }, 
          {
            "source": "javascript", 
            "target": "visualization", 
            "value": 3
          }, 
          {
            "source": "algorithms", 
            "target": "neuralnetwork", 
            "value": 3
          }, 
          {
            "source": "similarity", 
            "target": "dataset", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "scalability", 
            "value": 3
          }, 
          {
            "source": "performance", 
            "target": "r", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "map-reduce", 
            "value": 3
          }, 
          {
            "source": "algorithms", 
            "target": "social-network-analysis", 
            "value": 3
          }, 
          {
            "source": "python", 
            "target": "predictive-modeling", 
            "value": 3
          }, 
          {
            "source": "classification", 
            "target": "graphs", 
            "value": 3
          }, 
          {
            "source": "data-mining", 
            "target": "feature-selection", 
            "value": 3
          }, 
          {
            "source": "data-mining", 
            "target": "decision-trees", 
            "value": 3
          }, 
          {
            "source": "bigdata", 
            "target": "nosql", 
            "value": 3
          }, 
          {
            "source": "performance", 
            "target": "python", 
            "value": 3
          }, 
          {
            "source": "pandas", 
            "target": "sklearn", 
            "value": 3
          }, 
          {
            "source": "scalability", 
            "target": "hadoop", 
            "value": 3
          }, 
          {
            "source": "nlp", 
            "target": "language-model", 
            "value": 3
          }, 
          {
            "source": "python", 
            "target": "correlation", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "performance", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "social-network-analysis", 
            "value": 3
          }, 
          {
            "source": "python", 
            "target": "apache-spark", 
            "value": 3
          }, 
          {
            "source": "logistic-regression", 
            "target": "predictive-modeling", 
            "value": 3
          }, 
          {
            "source": "scikit", 
            "target": "kaggle", 
            "value": 3
          }, 
          {
            "source": "k-means", 
            "target": "categorical-data", 
            "value": 3
          }, 
          {
            "source": "machine-learning", 
            "target": "databases", 
            "value": 3
          }, 
          {
            "source": "classification", 
            "target": "scikit", 
            "value": 3
          }, 
          {
            "source": "nlp", 
            "target": "social-network-analysis", 
            "value": 3
          }, 
          {
            "source": "clustering", 
            "target": "bioinformatics", 
            "value": 2
          }, 
          {
            "source": "open-source", 
            "target": "freebase", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "gbm", 
            "value": 2
          }, 
          {
            "source": "dataset", 
            "target": "data-formats", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "feature-scaling", 
            "value": 2
          }, 
          {
            "source": "time-series", 
            "target": "text-mining", 
            "value": 2
          }, 
          {
            "source": "topic-model", 
            "target": "text-mining", 
            "value": 2
          }, 
          {
            "source": "algorithms", 
            "target": "feature-selection", 
            "value": 2
          }, 
          {
            "source": "algorithms", 
            "target": "decision-trees", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "lda", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "linear-regression", 
            "value": 2
          }, 
          {
            "source": "random-forest", 
            "target": "predictive-modeling", 
            "value": 2
          }, 
          {
            "source": "recommendation", 
            "target": "nlp", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "sampling", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "anomaly-detection", 
            "value": 2
          }, 
          {
            "source": "indexing", 
            "target": "data-indexing-techniques", 
            "value": 2
          }, 
          {
            "source": "libsvm", 
            "target": "svm", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "tools", 
            "value": 2
          }, 
          {
            "source": "classification", 
            "target": "deep-learning", 
            "value": 2
          }, 
          {
            "source": "classification", 
            "target": "parameter", 
            "value": 2
          }, 
          {
            "source": "neuralnetwork", 
            "target": "gradient-descent", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "data-stream-mining", 
            "value": 2
          }, 
          {
            "source": "scalability", 
            "target": "feature-selection", 
            "value": 2
          }, 
          {
            "source": "svm", 
            "target": "scikit", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "knowledge-base", 
            "value": 2
          }, 
          {
            "source": "k-means", 
            "target": "text-mining", 
            "value": 2
          }, 
          {
            "source": "feature-selection", 
            "target": "logistic-regression", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "rstudio", 
            "value": 2
          }, 
          {
            "source": "data-cleaning", 
            "target": "statistics", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "markov-process", 
            "value": 2
          }, 
          {
            "source": "nlp", 
            "target": "topic-model", 
            "value": 2
          }, 
          {
            "source": "efficiency", 
            "target": "tools", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "graphs", 
            "value": 2
          }, 
          {
            "source": "predictive-modeling", 
            "target": "scoring", 
            "value": 2
          }, 
          {
            "source": "classification", 
            "target": "java", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "unbalanced-classes", 
            "value": 2
          }, 
          {
            "source": "beginner", 
            "target": "career", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "search", 
            "value": 2
          }, 
          {
            "source": "text-mining", 
            "target": "random-forest", 
            "value": 2
          }, 
          {
            "source": "algorithms", 
            "target": "nlp", 
            "value": 2
          }, 
          {
            "source": "search", 
            "target": "classification", 
            "value": 2
          }, 
          {
            "source": "performance", 
            "target": "neuralnetwork", 
            "value": 2
          }, 
          {
            "source": "feature-selection", 
            "target": "optimization", 
            "value": 2
          }, 
          {
            "source": "tools", 
            "target": "data-stream-mining", 
            "value": 2
          }, 
          {
            "source": "k-means", 
            "target": "dimensionality-reduction", 
            "value": 2
          }, 
          {
            "source": "bigdata", 
            "target": "data-cleaning", 
            "value": 2
          }, 
          {
            "source": "clustering", 
            "target": "nlp", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "visualization", 
            "value": 2
          }, 
          {
            "source": "bigdata", 
            "target": "career", 
            "value": 2
          }, 
          {
            "source": "tableau", 
            "target": "data-visualization", 
            "value": 2
          }, 
          {
            "source": "correlation", 
            "target": "linear-regression", 
            "value": 2
          }, 
          {
            "source": "nlp", 
            "target": "data-formats", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "evaluation", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "social-network-analysis", 
            "value": 2
          }, 
          {
            "source": "algorithms", 
            "target": "genetic", 
            "value": 2
          }, 
          {
            "source": "distributed", 
            "target": "map-reduce", 
            "value": 2
          }, 
          {
            "source": "scalability", 
            "target": "algorithms", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "data", 
            "value": 2
          }, 
          {
            "source": "recommendation", 
            "target": "apache-mahout", 
            "value": 2
          }, 
          {
            "source": "dataset", 
            "target": "regression", 
            "value": 2
          }, 
          {
            "source": "dataset", 
            "target": "correlation", 
            "value": 2
          }, 
          {
            "source": "random-forest", 
            "target": "ensemble-modeling", 
            "value": 2
          }, 
          {
            "source": "cross-validation", 
            "target": "sampling", 
            "value": 2
          }, 
          {
            "source": "hadoop", 
            "target": "correlation", 
            "value": 2
          }, 
          {
            "source": "tools", 
            "target": "visualization", 
            "value": 2
          }, 
          {
            "source": "dataset", 
            "target": "data-visualization", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "logistic-regression", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "parsing", 
            "value": 2
          }, 
          {
            "source": "data-cleaning", 
            "target": "recommendation", 
            "value": 2
          }, 
          {
            "source": "neuralnetwork", 
            "target": "feature-extraction", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "confusion-matrix", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "image-classification", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "glm", 
            "value": 2
          }, 
          {
            "source": "performance", 
            "target": "map-reduce", 
            "value": 2
          }, 
          {
            "source": "classification", 
            "target": "confusion-matrix", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "linear-regression", 
            "value": 2
          }, 
          {
            "source": "algorithms", 
            "target": "python", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "gradient-descent", 
            "value": 2
          }, 
          {
            "source": "bigdata", 
            "target": "mongodb", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "unbalanced-classes", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "deep-learning", 
            "value": 2
          }, 
          {
            "source": "predictive-modeling", 
            "target": "forecast", 
            "value": 2
          }, 
          {
            "source": "unbalanced-classes", 
            "target": "predictive-modeling", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "feature-extraction", 
            "value": 2
          }, 
          {
            "source": "neuralnetwork", 
            "target": "forecast", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "open-source", 
            "value": 2
          }, 
          {
            "source": "k-means", 
            "target": "feature-extraction", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "feature-selection", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "topic-model", 
            "value": 2
          }, 
          {
            "source": "information-retrieval", 
            "target": "nlp", 
            "value": 2
          }, 
          {
            "source": "accuracy", 
            "target": "random-forest", 
            "value": 2
          }, 
          {
            "source": "random-forest", 
            "target": "decision-trees", 
            "value": 2
          }, 
          {
            "source": "data-stream-mining", 
            "target": "apache-spark", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "correlation", 
            "value": 2
          }, 
          {
            "source": "feature-selection", 
            "target": "neuralnetwork", 
            "value": 2
          }, 
          {
            "source": "time-series", 
            "target": "predictive-modeling", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "random-forest", 
            "value": 2
          }, 
          {
            "source": "algorithms", 
            "target": "beginner", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "education", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "similarity", 
            "value": 2
          }, 
          {
            "source": "svm", 
            "target": "random-forest", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "java", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "cross-validation", 
            "value": 2
          }, 
          {
            "source": "recommendation", 
            "target": "predictive-modeling", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "similarity", 
            "value": 2
          }, 
          {
            "source": "dataset", 
            "target": "neuralnetwork", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "k-means", 
            "value": 2
          }, 
          {
            "source": "clustering", 
            "target": "beginner", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "library", 
            "value": 2
          }, 
          {
            "source": "recommendation", 
            "target": "beginner", 
            "value": 2
          }, 
          {
            "source": "logistic-regression", 
            "target": "kaggle", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "nlp", 
            "value": 2
          }, 
          {
            "source": "nosql", 
            "target": "hadoop", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "computer-vision", 
            "value": 2
          }, 
          {
            "source": "hadoop", 
            "target": "scala", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "information-retrieval", 
            "value": 2
          }, 
          {
            "source": "information-retrieval", 
            "target": "search", 
            "value": 2
          }, 
          {
            "source": "data-cleaning", 
            "target": "nlp", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "parsing", 
            "value": 2
          }, 
          {
            "source": "svm", 
            "target": "binary", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "clusters", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "glm", 
            "value": 2
          }, 
          {
            "source": "tools", 
            "target": "processing", 
            "value": 2
          }, 
          {
            "source": "databases", 
            "target": "mongodb", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "text-mining", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "knowledge-base", 
            "value": 2
          }, 
          {
            "source": "tools", 
            "target": "beginner", 
            "value": 2
          }, 
          {
            "source": "classification", 
            "target": "feature-extraction", 
            "value": 2
          }, 
          {
            "source": "clustering", 
            "target": "data-visualization", 
            "value": 2
          }, 
          {
            "source": "svm", 
            "target": "logistic-regression", 
            "value": 2
          }, 
          {
            "source": "optimization", 
            "target": "predictive-modeling", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "map-reduce", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "svm", 
            "value": 2
          }, 
          {
            "source": "library", 
            "target": "deep-learning", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "optimization", 
            "value": 2
          }, 
          {
            "source": "neuralnetwork", 
            "target": "java", 
            "value": 2
          }, 
          {
            "source": "visualization", 
            "target": "marketing", 
            "value": 2
          }, 
          {
            "source": "classification", 
            "target": "apache-spark", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "dimensionality-reduction", 
            "value": 2
          }, 
          {
            "source": "algorithms", 
            "target": "similarity", 
            "value": 2
          }, 
          {
            "source": "dimensionality-reduction", 
            "target": "python", 
            "value": 2
          }, 
          {
            "source": "databases", 
            "target": "dataset", 
            "value": 2
          }, 
          {
            "source": "bigdata", 
            "target": "beginner", 
            "value": 2
          }, 
          {
            "source": "dataset", 
            "target": "data", 
            "value": 2
          }, 
          {
            "source": "recommendation", 
            "target": "graphs", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "graphs", 
            "value": 2
          }, 
          {
            "source": "dataset", 
            "target": "pandas", 
            "value": 2
          }, 
          {
            "source": "time-series", 
            "target": "forecast", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "scala", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "similarity", 
            "value": 2
          }, 
          {
            "source": "svm", 
            "target": "regression", 
            "value": 2
          }, 
          {
            "source": "neuralnetwork", 
            "target": "image-classification", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "information-retrieval", 
            "value": 2
          }, 
          {
            "source": "bigdata", 
            "target": "aws", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "data", 
            "value": 2
          }, 
          {
            "source": "recommendation", 
            "target": "information-retrieval", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "sampling", 
            "value": 2
          }, 
          {
            "source": "classification", 
            "target": "computer-vision", 
            "value": 2
          }, 
          {
            "source": "clustering", 
            "target": "predictive-modeling", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "lda", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "recommendation", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "object-recognition", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "anomaly-detection", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "state-of-the-art", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "logistic-regression", 
            "value": 2
          }, 
          {
            "source": "accuracy", 
            "target": "sampling", 
            "value": 2
          }, 
          {
            "source": "dataset", 
            "target": "freebase", 
            "value": 2
          }, 
          {
            "source": "neuralnetwork", 
            "target": "text-mining", 
            "value": 2
          }, 
          {
            "source": "processing", 
            "target": "data-cleaning", 
            "value": 2
          }, 
          {
            "source": "efficiency", 
            "target": "hadoop", 
            "value": 2
          }, 
          {
            "source": "random-forest", 
            "target": "logistic-regression", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "bioinformatics", 
            "value": 2
          }, 
          {
            "source": "hadoop", 
            "target": "dataset", 
            "value": 2
          }, 
          {
            "source": "databases", 
            "target": "r", 
            "value": 2
          }, 
          {
            "source": "logistic-regression", 
            "target": "gradient-descent", 
            "value": 2
          }, 
          {
            "source": "scalability", 
            "target": "map-reduce", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "feature-selection", 
            "value": 2
          }, 
          {
            "source": "map-reduce", 
            "target": "aws", 
            "value": 2
          }, 
          {
            "source": "processing", 
            "target": "dataset", 
            "value": 2
          }, 
          {
            "source": "logistic-regression", 
            "target": "regression", 
            "value": 2
          }, 
          {
            "source": "machine-learning", 
            "target": "hierarchical-data-format", 
            "value": 2
          }, 
          {
            "source": "classification", 
            "target": "neuralnetwork", 
            "value": 2
          }, 
          {
            "source": "bigdata", 
            "target": "predictive-modeling", 
            "value": 2
          }, 
          {
            "source": "data-cleaning", 
            "target": "predictive-modeling", 
            "value": 2
          }, 
          {
            "source": "efficiency", 
            "target": "statistics", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "accuracy", 
            "value": 2
          }, 
          {
            "source": "information-retrieval", 
            "target": "similarity", 
            "value": 2
          }, 
          {
            "source": "k-means", 
            "target": "algorithms", 
            "value": 2
          }, 
          {
            "source": "dataset", 
            "target": "feature-scaling", 
            "value": 2
          }, 
          {
            "source": "data-cleaning", 
            "target": "data-visualization", 
            "value": 2
          }, 
          {
            "source": "data-stream-mining", 
            "target": "classification", 
            "value": 2
          }, 
          {
            "source": "logistic-regression", 
            "target": "apache-spark", 
            "value": 2
          }, 
          {
            "source": "data-mining", 
            "target": "sql", 
            "value": 2
          }, 
          {
            "source": "similarity", 
            "target": "nlp", 
            "value": 2
          }, 
          {
            "source": "mongodb", 
            "target": "sql", 
            "value": 2
          }, 
          {
            "source": "performance", 
            "target": "distributed", 
            "value": 2
          }, 
          {
            "source": "r", 
            "target": "categorical-data", 
            "value": 2
          }, 
          {
            "source": "hadoop", 
            "target": "hive", 
            "value": 2
          }, 
          {
            "source": "algorithms", 
            "target": "recommendation", 
            "value": 2
          }, 
          {
            "source": "statistics", 
            "target": "glm", 
            "value": 2
          }, 
          {
            "source": "python", 
            "target": "gradient-descent", 
            "value": 2
          }, 
          {
            "source": "clustering", 
            "target": "scikit", 
            "value": 2
          }, 
          {
            "source": "search", 
            "target": "dataset", 
            "value": 2
          }, 
          {
            "source": "hadoop", 
            "target": "mongodb", 
            "value": 2
          }, 
          {
            "source": "svm", 
            "target": "neuralnetwork", 
            "value": 2
          }, 
          {
            "source": "clustering", 
            "target": "anomaly-detection", 
            "value": 2
          }, 
          {
            "source": "text-mining", 
            "target": "categorical-data", 
            "value": 2
          }, 
          {
            "source": "algorithms", 
            "target": "hierarchical-data-format", 
            "value": 2
          }, 
          {
            "source": "processing", 
            "target": "r", 
            "value": 1
          }, 
          {
            "source": "data-mining", 
            "target": "sports", 
            "value": 1
          }, 
          {
            "source": "gbm", 
            "target": "ensemble-modeling", 
            "value": 1
          }, 
          {
            "source": "clusters", 
            "target": "hierarchical-data-format", 
            "value": 1
          }, 
          {
            "source": "nosql", 
            "target": "data-indexing-techniques", 
            "value": 1
          }, 
          {
            "source": "nlp", 
            "target": "ensemble-modeling", 
            "value": 1
          }, 
          {
            "source": "classification", 
            "target": "image-classification", 
            "value": 1
          }, 
          {
            "source": "usecase", 
            "target": "consumerweb", 
            "value": 1
          }, 
          {
            "source": "machine-learning", 
            "target": "image-classification", 
            "value": 1
          }, 
          {
            "source": "error-handling", 
            "target": "matlab", 
            "value": 1
          }, 
          {
            "source": "accuracy", 
            "target": "ensemble-modeling", 
            "value": 1
          }, 
          {
            "source": "research", 
            "target": "deep-learning", 
            "value": 1
          }, 
          {
            "source": "topic-model", 
            "target": "parameter", 
            "value": 1
          }, 
          {
            "source": "hadoop", 
            "target": "random-forest", 
            "value": 1
          }, 
          {
            "source": "information-retrieval", 
            "target": "language-model", 
            "value": 1
          }, 
          {
            "source": "distributed", 
            "target": "python", 
            "value": 1
          }, 
          {
            "source": "dimensionality-reduction", 
            "target": "svm", 
            "value": 1
          }, 
          {
            "source": "categorical-data", 
            "target": "logistic-regression", 
            "value": 1
          }, 
          {
            "source": "optimization", 
            "target": "scikit", 
            "value": 1
          }, 
          {
            "source": "neuralnetwork", 
            "target": "library", 
            "value": 1
          }, 
          {
            "source": "deep-learning", 
            "target": "multitask-learning", 
            "value": 1
          }, 
          {
            "source": "classification", 
            "target": "bioinformatics", 
            "value": 1
          }, 
          {
            "source": "object-recognition", 
            "target": "hog", 
            "value": 1
          }, 
          {
            "source": "algorithms", 
            "target": "knowledge-base", 
            "value": 1
          }, 
          {
            "source": "machine-learning", 
            "target": "bioinformatics", 
            "value": 1
          }, 
          {
            "source": "beginner", 
            "target": "basket-analysis", 
            "value": 1
          }, 
          {
            "source": "r", 
            "target": "genetic", 
            "value": 1
          }, 
          {
            "source": "bigdata", 
            "target": "lda", 
            "value": 1
          }, 
          {
            "source": "efficiency", 
            "target": "state-of-the-art", 
            "value": 1
          }, 
          {
            "source": "hog", 
            "target": "computer-vision", 
            "value": 1
          }, 
          {
            "source": "genes", 
            "target": "bioinformatics", 
            "value": 1
          }, 
          {
            "source": "python", 
            "target": "forecast", 
            "value": 1
          }, 
          {
            "source": "efficiency", 
            "target": "clustering", 
            "value": 1
          }, 
          {
            "source": "nlp", 
            "target": "gate", 
            "value": 1
          }, 
          {
            "source": "random-forest", 
            "target": "cross-validation", 
            "value": 1
          }, 
          {
            "source": "python", 
            "target": "sampling", 
            "value": 1
          }, 
          {
            "source": "svm", 
            "target": "forecast", 
            "value": 1
          }, 
          {
            "source": "performance", 
            "target": "predictive-modeling", 
            "value": 1
          }, 
          {
            "source": "time-series", 
            "target": "parameter", 
            "value": 1
          }, 
          {
            "source": "regression", 
            "target": "scoring", 
            "value": 1
          }, 
          {
            "source": "neo4j", 
            "target": "csv", 
            "value": 1
          }]
            }
    return list 