from datetime import datetime

from jira import JIRA

from secret import user, passwd

if __name__ == '__main__':
    jira = JIRA(server='http://sigma:9090', basic_auth=(user, passwd))
    with open('data.txt', 'r') as f:
        for line in f.readlines():
            line_split = line.split('//')
            order, issue = line_split[:2]
            started = datetime.strptime(line_split[2], '%Y-%m-%dT%H:%M:%S.%f%z')
            if order == '+':
                time_spent, comment = line_split[3:]
                jira.add_worklog(issue, time_spent, started=started, comment=comment)
            elif order == '-':
                work_logs = list(filter(lambda x: x.started == line_split[2], jira.worklogs(issue)))
                if len(work_logs) < 1:
                    print("work log to delete not exists")
                elif len(work_logs) > 1:
                    print("work log to delete exists more than 2")
                else:
                    work_logs[0].delete()
            else:
                work_logs = jira.worklogs(issue)
                for work_log in work_logs:
                    print(issue, work_log, work_log.timeSpent, work_log.started, work_log.comment)
