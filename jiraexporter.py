#!/usr/bin/env python
""" Export tool for extracting all jira issues from a given project

"""

import json

from jira import JIRA


JIRA_URL = 'https://jira.mongodb.org'
PROJECT = 'SERVER'
OUTPUT_FILE = 'issues.json'


class IssueExporter(object):

    def __init__(self, jira_url=JIRA_URL, project=PROJECT):
        self.jira_url = JIRA_URL
        self.project = project
        self.all_issues = []
        self.jira = JIRA(jira_url)
        self.raw_issues = []

    def fetch_issues(self, startAt=0, maxResults=1000):

        jqlStr = 'project=%s ORDER BY key ASC' % self.project

        while True:
            issues = self.jira.search_issues(jqlStr, startAt=startAt,
                                             maxResults=maxResults)
            if len(issues) == 0:
                print 'no new issues..'
                break

            print 'fetched results: %s' % issues[-1].key
            startAt += maxResults
            self.all_issues.extend(issues)

        self.__store_raw_issues()

    def __store_raw_issues(self):
        if self.raw_issues != []:
            raise Exception('raw issues already exist')
        for issue in self.all_issues:
            self.raw_issues.append(issue.raw)

    def dump_json(self, output_file=OUTPUT_FILE):

        with open(output_file, 'w') as fp:
            json.dump(self.raw_issues, fp)
