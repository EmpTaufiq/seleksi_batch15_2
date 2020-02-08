import json

def print_biodata_json ():
    biodata = {
        "name" : " M Taufiqurahman",
        "age": 22,
        "address" : "Perum. Pabaton Indah, Jln. Zambrut IV, Blok L/1, RT 004/ RW 007, Kota Bogor, 16161",
        "hobbies" : [ "reading a book" , "photography" , "listening to the music" ],
        "is_married" : False,
        "list_school" : [ { "name" : "Universitas Gadjah Mada", "year_in" : "2014" , "year_out" : "2020" , "major" : "S1 Elektronika dan Instrumentasi" } , { "name" : "SMA Negeri 2 Bogor" , "year_in" : "2011" , "year_out" : "2014" , "major": "IPA" } , { "name" : "SMP Negeri 8 Bogor" , "year_in" : "2008" , "year_out" : "2011" , "major" : None } , { "name" : "SDIT Al-Kautsar Bogor" , "year_in" : "2002" , "year_out" : "2008" , "major" : None } ],
        "skills" : [ { "skill_name" : "C++ Programming Language" , "level" : "beginner" } , { "skill_name" : "Python Programming Language" , "level" : "advanced" } ],
        "interest_in_coding" : True
    }
# convert into JSON:
    biodata_json = json.dumps(biodata)
# the result is a JSON string:
    print(biodata_json)