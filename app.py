import requests 
from flask import Flask, request, render_template
from default_settings import PER_PAGE, URL

app = Flask(__name__)
app.config.from_object('default_settings')
issues = requests.get(url = URL).json()

total_pages = len(issues)/10
if len(issues)%10 != 0:
    total_pages = total_pages + 1

page_urls = {}
for i in range(1, int(total_pages) + 1):
    page_urls[ f"{str(i)}" ] = (f"/issues?page={i}")


@app.route('/issues')
def list_issues():
    page = request.args.get('page', default = 1, type = int)
    start_index = PER_PAGE*(page-1)
    
    print(issues[0])
    current_issues = []
    for i in range(start_index, min(start_index + PER_PAGE - 1, len(issues) - 1)):
        current_issue = {"title": issues[i]["title"], "number": issues[i]["number"], "state": issues[i]["state"], "id": i}
        current_issues.append(current_issue)

    return render_template( "issues_list.html", current_issues=current_issues, page_urls=page_urls)


@app.route('/issues/<int:id>')
def inspect_issue(id: int):
    return render_template("inspect_issue.html", issue=issues[id])