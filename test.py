from lingcorpora import Corpus
rus_corp = Corpus('zho')
rus_results = rus_corp.search('fgjkfdjkg', numResults = 10)
for result in rus_results:
    for i,target in enumerate(result):
        print(i+1,'\t'.join(target.kwic(left=5,right=5)))
