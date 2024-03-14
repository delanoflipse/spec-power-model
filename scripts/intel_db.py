import json
import urllib.request, json

def get_db():
    with urllib.request.urlopen("https://github.com/divinity76/intel-cpu-database/raw/master/databases/intel_cpu_database.json") as url:
        data = json.load(url)
        return data

if __name__ == "__main__":
    db = get_db()
    output = {}
    for key in db:
        try:
            tdp_str = db[key]['Performance']['TDP']
            tdp = int(tdp_str.split(' ')[0]) if tdp_str else None
            if tdp > 0:
                output[key] = tdp
        except:
            pass
    json.dump(output, open('tdp.json', 'w'))