from pymongo import MongoClient
client = MongoClient("mongodb+srv://amarnath:scrap3142@cluster0.ipuz3gi.mongodb.net/")
db = client.linkedin
collection = db.linkedinProfile
from linkedin_api import Linkedin

def fetchLinkedInData(username):
    # api = Linkedin('kumarfarzi08@gmail.com','3142farzi@Linkedin')
    api = Linkedin('pobali2245@irnini.com','pobali2245@Linkedin')
    profile_data = api.get_profile(username)
    post_id = collection.insert_one(profile_data).inserted_id
    print("fasdfafasfaf",post_id)


# fetchLinkedInData("vinaygupta3218")
# fetchLinkedInData("fourbrick")
# fetchLinkedInData("microsoft")
# fetchLinkedInData("sandeep-kumar-32365624a")

