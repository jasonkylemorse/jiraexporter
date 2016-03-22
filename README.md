# jiraexporter

Simple python program to import issues from JIRA.

Example use:

'''
    >>> from jiraexporter import JiraIssueExporter
    >>> exporter = JiraIssueExporter(basic_auth=('userid', 'password'))
    >>> exporter.fetch_issues()
'''
