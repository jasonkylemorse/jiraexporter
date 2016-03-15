"""Import Jira Issues into MongoDB

"""

import json

import pymongo


HOST = '172.17.0.1'
INPUT_FILE = 'issues.json'
DATABASE = 'mongo_issues'


class IssueImporter(object):

    def __init__(self, host=HOST, database=DATABASE):

        self.client = pymongo.MongoClient(host)
        self.db = self.client[database]
        self.issues_raw = []

    def load_issues_json(self, filename=INPUT_FILE):

        if self.issues_raw != []:
            raise Exception("raw input already exists")

        with open(filename, 'r') as fp:
            self.issues_raw = json.load(fp)

    def import_to_mongo(self):

        self.issues = self.db.issues
        self.issues.insert_many(self.issues_raw)
