# jiraexporter

Simple python program to import issues from JIRA.

Example use:

```
    >>> from jiraexporter import JiraIssueExporter
    >>> exporter = JiraIssueExporter(jira_url='https://jira.mongodb.org,
    project='SERVER', basic_auth=('userid', 'password'))
    >>> exporter.fetch_issues()
```
