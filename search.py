import os
import time
print("Indexing...")
posts = []
date = input("Date?>>>")

if date == "":
    try:
        os.listdir("/freescanner/data/"+time.strftime("%Y%m%d"))
        dr = "/freescanner/data/"+time.strftime("%Y%m%d")
    except:
        print("No data for today :(")
        quit()
else:
    dr = "/freescanner/data/"+date

for filename in os.listdir(dr):

    with open(dr+"/"+filename, "r") as f:
        s = f.read()

        ps = s.split("\n")
        for p in ps:
            posts.append(p)
print(str(len(posts))+" posts indexed.")
search = "asdf"
while search != "":
    search = input(">>>")
    terms = search.split(" ")
    res = []
    if search != "":
        n = 0
        for post in posts:
            yes = True
            for term in terms:
                if term.upper() not in post.upper():
                    yes = False
            if yes == True:
                n += 1
                print(post)
                res.append(post)
                
        print("")
        print(str(n))

        print("")
        locs = []
        ns = []
        for r in res:
            loc = r[35:].split("/", 1)[0]
            if loc[-2:] == "UK":
                loc = loc[:-2]

            if loc in locs:
                ns[locs.index(loc)] += 1
            else:
                locs.append(loc)
                ns.append(1)

        for i in range(0, len(locs)):
            print(locs[i] + " - " + str(ns[i]))
