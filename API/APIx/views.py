from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def endpoint_view(request):
    # Accept GET parameters slack_name and track
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track', '')

    # Calculate the current day of the week and UTC time
    current_day = datetime.now().strftime('%A')
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Define GitHub repository information
    github_username = 'username'         github_repo = 'reponame'
    github_file = 'views.py'  # Change this to the filename of your view

    # Construct JSON response
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': f'https://github.com/{github_username}/{github_repo}/blob/main/{github_file}',
        'github_repo_url': f'https://github.com/{github_username}/{github_repo}',
        'status_code': '200',
    }

    return JsonResponse(response)
